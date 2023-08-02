from stirrer_heater_driver.driver import StirrerHeater

serial_port = "/dev/ttyACM0"

ika = StirrerHeater(serial_port)

ika.stirr_at_rpm_for_minutes(100, 1)
