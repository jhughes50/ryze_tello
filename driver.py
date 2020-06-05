from flight_commander import Commander
import time
tello = Commander()

#tello.send_command('command')
tello.take_off()
time.sleep(5.0)
tello.land()


