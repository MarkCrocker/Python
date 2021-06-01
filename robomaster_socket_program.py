import traceback

def default_EventfulKeyValueStore_callback(*args, **kwargs):
    pass

class EventfulKeyValueStore:
    def __init__(self, on_get = default_EventfulKeyValueStore_callback, on_set = default_EventfulKeyValueStore_callback, on_receive = default_EventfulKeyValueStore_callback):
        self._d = dict()
        self.on_get = on_get
        self.on_set = on_set
        self.on_receive = on_receive

    def __contains__(self, key):
        return self._d.__contains__(key)

    def __getitem__(self, key):
        ret = self._d[key]
        self.on_get(key, ret, self)
        return ret
    
    def __setitem__(self, key, value):
        self._d[key] = value
        self.on_set(key, value, self)
    
    def receive(self, key, value):
        self._d[key] = value
        self.on_receive(key, value, self)

class RobotmasterRemoteVariableStore(EventfulKeyValueStore):
    def __init__(self, on_get=default_EventfulKeyValueStore_callback, on_set=default_EventfulKeyValueStore_callback, on_receive = default_EventfulKeyValueStore_callback):
        super().__init__(on_get=on_get, on_set=on_set, on_receive=on_receive)

remote_variables = dict()

def remote_setup():
    global remote_variables
    MY_IP = '0.0.0.0' #"192.168.10.3"
    PORT = 44558
    socket = traceback.__builtins__['__import__']('socket')
    #json = traceback.__builtins__['__import__']('json')
    pickle = traceback.__builtins__['__import__']('pickle')
    threading = traceback.__builtins__['__import__']('threading')
    exec = traceback.__builtins__['exec']

    def socket_handler():
        def process_packet(packet):
            global remote_variables
            if packet[-1] != b'.' and packet[-2] != b'u':
                packet = packet + b'u.'
            j_dict = pickle.loads(packet)
            print("Raw data: {}".format(packet))
            print("Got: {}".format(j_dict))
            if j_dict['type'] == 'header':
                num_bytes = j_dict['bytes']
                next_bytes = 4096 if 4096 > num_bytes else num_bytes 
            if j_dict['type'] == 'python_exec_string':
                print("executing...")
                print(exec)
                print(exec(j_dict['value']))
                print("done executing...")
                next_bytes = 4096
            elif j_dict['type'] == 'variable_dict_update':
                print("updating variable...")
                key = j_dict['key']
                value = j_dict['value']
                #name = pickle.loads(j_dict['remote_name'])
                remote_variables.receive(key, value)
                next_bytes = 4096
            else:
                next_bytes = 4096
            return next_bytes
        global remote_variables
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((MY_IP, PORT))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    print("Connected by", addr)                
                    def variables_on_set_handler(key, value, _obj):
                        data = {
                            "type" : 'variable_dict_update',
                            "key" : key,
                            "value" : value,
                            "name" : 'variables'
                        }
                        print("Sending update....")
                        conn.send(pickle.dumps(data))
                    remote_variables = RobotmasterRemoteVariableStore(on_set=variables_on_set_handler)
                    next_bytes = 4096
                    leftover = b''
                    while True:
                        data = b''
                        print("Residual Data: {}".format(data))
                        while next_bytes > 0:
                            packet = conn.recv(4096)
                            if not packet:
                                break
                            next_bytes -= 4096
                            data += packet
                        if not data:
                            break
                        data = leftover + data
                        try:
                            c = 0
                            packets = data.split(b"u.")
                            for packet in packets[0:-1]:
                                if len(packet) == 0:
                                    continue
                                next_bytes = process_packet(packet)
                                c += 1
                            #print("Leftover?")
                            #print(packets[-1])
                            if len(packets[-1]) > 0 and packets[-1][-1] == b"." and packets[-1][-2] == b"u":
                                next_bytes = process_packet(packets[-1])
                                leftover = b''
                            else:
                                #print("Leftover...")
                                leftover = packets[-1] 
                        except Exception as e:
                            pass
                            #print("WARNING: An error occured {}".format(e))
                            #print(c)
                            #print(packets[c])
                            #print(packets)
                        if next_bytes > 1:
                            next_bytes = 4096
                    print("Connection closed...")
    t = threading.Thread(target=socket_handler)
    return t

def start():
    global remote_variables
    time = traceback.__builtins__['__import__']('time')
    print("Starting up...")
    remote_thread = remote_setup()
    remote_thread.start()
    print("Server started...")
    while "tello_marker_1" not in remote_variables:
        pass

    print("Got tello marker 1 as : {}".format(remote_variables['tello_marker_1']))

    while "tello_marker_2" not in remote_variables:
        pass

    print("Got tello marker 2 as : {}".format(remote_variables['tello_marker_2']))


    while "tello_marker_3" not in remote_variables:
        pass

    print("Got tello marker 3 as : {}".format(remote_variables['tello_marker_3']))

    while "tello_marker_4" not in remote_variables:
        pass

    print("Got tello marker 4 as : {}".format(remote_variables['tello_marker_4']))


    remote_thread.join()

if __name__ == "__main__":
    start()