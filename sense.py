pir_pin =16
pir_sensor = machine.Pin(pir_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
if pir_sensor.value():
	print('something going on')
else:
	print('no motion detected')