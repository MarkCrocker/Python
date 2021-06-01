import socket
import pickle
import threading
import json
import math

def default_MetaHandleAnyCallable_callback(*args, **kwargs):
    '''
    A function used as the default callback for the MetaHandleAnyCallable class more than anything.
    Does absolutely nothing, just ignores the invocation and anything passed to it.
    The intended use for this is to pass it as the callback to the MetaHandleAnyCallable class
    For example:
    a = MetaHandleAnyCallable(callback=default_MetaHandleAnyCallable_callback)
    '''
    pass

class MetaHandleAnyCallable:
    '''
    MetaHandleAnyCallable
        This is a special type of metaobject, that can handle any attribute chain you throw at it, as long as it ends in a function invocation.
        When the final function is invoked, it provides a callback that contains the entire invocation chain (except the variable name).
        You can pass the variable name as the "current_invocation" if you'd like to include it in the invocation chain.

        Usage:
        a = MetaHandleAnyCallable(callback = print_helper_default_cb, current_invocation='a')
        a.put.whatever.you.want.here.in.this.chain.and.call.it.at.the.end('any','args',you='want',abc=123)
    '''
    def __init__(self, callback = default_MetaHandleAnyCallable_callback, current_invocation = ""):
        '''
        Constructor for the object. Takes in a callback to call on final invocation, as well as an initial current_invocation string.
            callback(inv, *args, **kwargs)
                - Where inv is a string representing the invocation chain, *args is any number of positional arguments passed to it, and **kwargs is any number of named arguments passed to it.
            current_invocation
                - A string that will be prepended to the invocation. You can pass the name of the variable containing this object here to get the full invocation, or you can leave it as an empty string. 
        Note that the default callback (if none is provided to the constructor) is default_MetaHandleAny_callback which simply ignores all arguments passed to it and does nothing at all.
        By default the current_invocation string is simply an empty string.
        '''
        self.cb = callback
        self.current_invocation = current_invocation
    def __call__(self, *args, **kwargs):
        '''
        Calls self as a function. This is part of the meta-programming magic. Handle the final invocation in the chain.
        This __call__ method shouldn't be invoked directly under normal circumstances.
        '''
        self.cb(self.current_invocation, *args, **kwargs)
    def __getattr__(self, name):
        '''
        This is part of the meta-programming magic. Handles undefined attributes as part of the chain, 
        letting us have whatever we want in our chain.
        This __getattr___ shouldn't be invoked directly under normal circumstances.
        '''
        return MetaHandleAnyCallable(callback = self.cb, current_invocation=f"{self.current_invocation}.{name}")

def default_RemoteSyncVariableDictionary_callback(*args, **kwargs):
    pass

class EventfulKeyValueStore:
    def __init__(self, on_get = default_RemoteSyncVariableDictionary_callback, on_set = default_RemoteSyncVariableDictionary_callback, on_receive = default_RemoteSyncVariableDictionary_callback):
        self._d = dict()
        self.on_get = on_get
        self.on_set = on_set
        self.on_receive = on_receive
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
    def __init__(self, on_get=default_RemoteSyncVariableDictionary_callback, on_set=default_RemoteSyncVariableDictionary_callback, on_receive = default_RemoteSyncVariableDictionary_callback):
        super().__init__(on_get=on_get, on_set=on_set, on_receive=on_receive)

def default_thread_stop_callback():
    return False

def generate_default_RobomasterRemoteVariableStore_thread_handler(robomaster_remote_variable_store, conn, stop_cb = default_thread_stop_callback, local_name = None):
    def th():
        while not stop_cb():
            data = conn.recv(4096)
            j = pickle.loads(data)
            if j['type'] == 'variable_dict_update':
                key = j['key']
                value = j['value']
                #TODO: Check if sent name equals local name if local name is provided.
                robomaster_remote_variable_store.receive(key, value)
    return th

def format_setter_parameters_as_string(name, key, value):
    value_fmt = value
    if isinstance(value, str):
        value_fmt = f'''\"{value}\"'''
    return f'''{name}['{key}']={value_fmt}'''

def create_socket_based_robomaster_remote_variable_store(conn, remote_name=""):
    def on_get(key, value, _obj):
        pass
    def on_set(key, value, _obj):
        send_variable_update_over_socket(conn, remote_name, key, value)
    return RobotmasterRemoteVariableStore(on_get=on_get, on_set=on_set)

def create_threaded_socket_based_robomaster_remote_variable_store(conn, remote_name="", stop_cb = default_thread_stop_callback, local_name = None):
    rrm = create_socket_based_robomaster_remote_variable_store(conn, remote_name)
    f = generate_default_RobomasterRemoteVariableStore_thread_handler(rrm, conn, stop_cb, local_name)
    thread = threading.Thread(target=f)
    return rrm, thread

def format_args_list_as_string(args_list):
    return ",".join([ f'''"{i}"''' if isinstance(i,str) else str(i) for i in args_list])

def format_kwargs_dict_as_string(kwargs_dict):
    formatted_kwargs_list = []
    for k,v in kwargs_dict.items():
        v = f'''"{v}"''' if isinstance(v,str) else str(v)
        formatted_kwargs_list.append(f"{k}={v}")
    return ",".join(formatted_kwargs_list)

def format_args_list_and_kwargs_dict_into_function_argument_list(args_list, kwargs_dict):
    args_list = list(args_list) #Copy and ensure list.
    kwargs_dict = dict(kwargs_dict) #Copy and ensure dict.
    arguments_parts = []
    if len(args_list):
        formatted_args = format_args_list_as_string(args_list)
        arguments_parts.append(formatted_args)
    if len(kwargs_dict):
        formatted_kwargs = format_kwargs_dict_as_string(kwargs_dict)
        arguments_parts.append(formatted_kwargs)
    formatted_arguments = ",".join(arguments_parts)
    return formatted_arguments

def get_invocation_string_from_invocation_and_formatted_arguments(invocation, formatted_function_arguments):
    return f"{invocation}({formatted_function_arguments})"

def print_helper_default_cb(inv, *args, **kwargs):
    '''
    A function used for testing the MetaHandleAnyCallable class more than anything.
    Simply prints out the invocation string and any arguments passed into the final invocation.
    The intended use for this is to pass it as the callback to the MetaHandleAnyCallable class
    For example:
    a = MetaHandleAnyCallable(callback=print_helper_default_cb)
    '''
    print(f"Invocation: {inv}")
    print(f"Args: {args}")
    print(f"KWArgs: {kwargs}")
    formatted_arguments = format_args_list_and_kwargs_dict_into_function_argument_list(args, kwargs)
    return get_invocation_string_from_invocation_and_formatted_arguments(inv, formatted_arguments)

def default_robomaster_module_cb(inv, *args, **kwargs):
    print_helper_default_cb(inv, *args, **kwargs)

class RoboMasterModule(MetaHandleAnyCallable):
    def __init__(self, robomaster_module_cb=default_robomaster_module_cb, robomaster_module_prefix=""):
        super().__init__(callback=robomaster_module_cb, current_invocation=robomaster_module_prefix)

DEFAULT_ROBOMASTER_REMOTE_PORT = 44558

class RobomasterRemote():
    def __init__(self, ip, port = DEFAULT_ROBOMASTER_REMOTE_PORT):
        self.conn = socket.socket()
        self.ip = ip
        self.port = port
        def module_callback(inv, *args, **kwargs):
            formatted_arguments = format_args_list_and_kwargs_dict_into_function_argument_list(args, kwargs)
            invocation = get_invocation_string_from_invocation_and_formatted_arguments(inv, formatted_arguments)
            self.send_python_string(invocation)
        
        def general_callback(inv, *args, **kwargs):
            if inv[0] == '.':
                inv = inv[1:]
            module_callback(inv, *args, **kwargs)
        
        self.general = RoboMasterModule(general_callback, "")
        self.robot_ctrl = RoboMasterModule(module_callback, 'robot_ctrl')
        self.gimbal_ctrl = RoboMasterModule(module_callback, 'gimbal_ctrl')
        self.chassis_ctrl = RoboMasterModule(module_callback, 'chassis_ctrl')
        self.gun_ctrl = RoboMasterModule(module_callback, 'gun_ctrl')
        self.vision_ctrl = RoboMasterModule(module_callback, 'vision_ctrl')
        self.media_ctrl = RoboMasterModule(module_callback, 'media_ctrl')
        self.armor_ctrl = RoboMasterModule(module_callback, 'armor_ctrl')
        self.led_ctrl = RoboMasterModule(module_callback, 'led_ctrl')
        self.variables = RobotmasterRemoteVariableStore()
        self.connected = False
    def connect(self, ip = None, port = None):
        ip = ip if ip is not None else self.ip
        port = port if port is not None else self.port 
        self.conn = socket.create_connection((ip, port))
        self.connected = True
        self.variables, self.variables_recv_thread = create_threaded_socket_based_robomaster_remote_variable_store(self.conn, 'variables', stop_cb= lambda : not self.connected)
        self.variables_recv_thread.start()

    def disconnect(self):
        self.connected = False
        self.variables_recv_thread.join()
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()

    def send_python_string(self, s):
        send_python_string_over_socket(self.conn, s)

    def send_function(self, func):
        s = function_source_code_to_formatted_string(func)
        self.send_python_string(s)

def extend_global_enviornment(robomaster_remote_object):
    globals()['robot_ctrl'] = robomaster_remote_object.robot_ctrl
    globals()['gimbal_ctrl'] = robomaster_remote_object.gimbal_ctrl
    globals()['chassis_ctrl'] = robomaster_remote_object.chassis_ctrl
    globals()['gun_ctrl'] = robomaster_remote_object.gun_ctrl
    globals()['vision_ctrl'] = robomaster_remote_object.vision_ctrl
    globals()['media_ctrl'] = robomaster_remote_object.media_ctrl
    globals()['armor_ctrl'] = robomaster_remote_object.armor_ctrl
    globals()['led_ctrl'] = robomaster_remote_object.led_ctrl

def send_dict_over_socket_as_pickle(soc, data_dict):
    data_s = pickle.dumps(data_dict)
    header = {
        'type' : 'header',
        'bytes' : len(data_s) #2 ** math.ceil(math.log2(len(data_s) + 1024))
    }
    header_s = pickle.dumps(header)
    #header_s = str(len(data_s)) + b"|"
    r1 = soc.send(header_s)
    r2 = soc.send(data_s)
    return r1, r2

def send_python_string_over_socket(soc, s):
    data = {
        'type'  : "python_exec_string",
        'value' :  s
    }

    return send_dict_over_socket_as_pickle(soc, data)

def send_variable_update_over_socket(soc, remote_name, key, value):
    #formatted = format_setter_parameters_as_string(remote_name, key, value)
    data = {
        'type' : "variable_dict_update",
        'remote_name' : remote_name,
        'key' : key,
        'value' : value
    }
    return send_dict_over_socket_as_pickle(soc, data)

def remove_source_indentation(source_code_line, num_spaces = None):
    if num_spaces is None:
        c = 0
        rem = []
        while source_code_line[0] == ' ' or source_code_line[0] == '\t':
            rem.append(source_code_line[0])
            source_code_line = source_code_line[1:]
            c = c + 1
        return source_code_line, c, rem
    else:
        c = 0
        rem = []
        while c < num_spaces:
            if source_code_line[0] == ' ' or source_code_line[0] == '\t':
                rem.append(source_code_line[0])
                source_code_line = source_code_line[1:]
                c += 1
            else:
                break
        return (source_code_line, c, rem)

def list_is_homogenous(l):
    if(len(l) < 2):
        return True
    target_element = l[0]
    for i in l[1:]:
        if target_element != i:
            return False
    return True

def format_function_source_lines_for_serialization(func_source_lines):
    formatted_lines = []
    new_line, c, rem = remove_source_indentation(func_source_lines[0])
    rem_error = ValueError("Misformatted source code detected! A mix of tabs and spaces!")
    if(not list_is_homogenous(rem)):
        raise rem_error 
    formatted_lines.append(new_line)
    for line in func_source_lines[1:]:
        new_line, d, _ = remove_source_indentation(line, c)
        if d != c:
            raise ValueError("Invalid function definition detected for serialization. Inconsistent indentation amount!")
        if(not list_is_homogenous(rem)):
            raise rem_error
        formatted_lines.append(new_line)
    return formatted_lines

def function_source_code_to_formatted_string(func):
    func_lines = inspect.getsourcelines(func)[0]
    formatted_lines = format_function_source_lines_for_serialization(func_lines)
    formatted_string = "".join(formatted_lines)
    return formatted_string

''' TEST CODE '''
if __name__ == "__main__":
    import inspect
    a = MetaHandleAnyCallable(print_helper_default_cb)
    a.who.when.where("apple", 1, pink='blue')
    b = RoboMasterModule()
    b.robot_ctrl.whatever('apple')
    a.who()
    b.whatever(kevin="pizza")

    def foo(a, b=1):
        print(a)
        print(b)
        return a + b

    #src = inspect.getsourcelines(foo)[0]
    #print(src)
    #del locals()['foo']
    #print(foo(1,2))
    #src_corr = format_function_source_lines_for_serialization(src)
    #src_corr_str = "".join(src_corr)
    #print(src_corr)
    #print(src_corr_str)
    #exec(src_corr_str)
    #print(foo(1,2))

    #src = function_source_code_to_formatted_string(foo)
    #del locals()['foo']
    #try:
    #    foo(1)
    #except:
    #    print("Foo was successfully undefined!")
    #else:
    #    raise Exception("Foo is still defined!")
    #print("Redefining foo from source string!")
    #exec(src)
    #print(foo(1))
    print("rmr section")
    rmr = RobomasterRemote('127.0.0.1', port=44558)
    rmr.connect()
    print("Sending first...")
    rmr.variables['bapple'] = 2
    
    rmr.send_function(foo)
    extend_global_enviornment(rmr)
    #robot_ctrl.whatever(1)
    print("Sending second...")
    #rmr.variables['apple'] = 1
    rmr.variables['foo'] = 5
    #rmr.send_python_string("print(remote_variables['apple'])")
    #rmr.send_python_string("print(foo)")
    #rmr.send_python_string("print(foo(1))")
    while rmr.variables['bapple'] == 2:
        pass
    print("Done!")
    #rmr.disconnect()
#'''