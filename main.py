import time
import tello
import tello_vision as tv
import robomaster_remote

# print("Connecting...")
# rm = robomaster_remote.RobomasterRemote('127.0.0.1')
# rm.connect()

t = tello.Tello()
t.connect_and_initialize()

t.enable_video()
tvw = tv.TelloVisionMarkerWatcher(t)
tvw.start()
time.sleep(1)
t.send_command('takeoff')
#t.send_command('right 200')
print(tvw.get_last_detected_id())
rm.variables['tello_marker_1'] = tvw.get_last_detected_id()
'''
# fly to room 1
t.send_command('right 725')
print(tvw.get_last_detected_id())
# fly to room 2
t.send_command('right 860')
t.send_command('cw 90')
t.send_command('right 710')
print(tvw.get_last_detected_id())
# fly to room 3
t.send_command('right 880')
print(tvw.get_last_detected_id())
# fly to room 4
t.send_command('right 1025')
print(tvw.get_last_detected_id())


# return to start
t.send_command('left 2615')
t.send_command('forward 1585')
'''