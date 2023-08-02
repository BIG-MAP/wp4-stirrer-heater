from stirrer_heater_driver.driver import StirrerHeater

serial_port = "/dev/ttyACM0"

ika = StirrerHeater(serial_port)

ika.stirr_for_minutes_blocking(100, 1)
