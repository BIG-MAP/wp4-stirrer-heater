import time

from stirrer_heater_driver.serial_driver import SerialDriver


class StirrerHeater:
    def __init__(self, port: str):
        self._serial = SerialDriver(port)
        self._locked = False

    @staticmethod
    def respect_lock(func):
        """
        Decorator to respect the lock of the device by raising an exception if the device is locked.
        """

        def wrapper(self, *args, **kwargs):
            if self._locked:
                raise RuntimeError("Device is locked")
            self._locked = True
            try:
                return func(self, *args, **kwargs)
            finally:
                self._locked = False

        return wrapper

    @respect_lock
    def stirr_at_rpm(self, rpm: int):
        self._set_stirrer_safety_speed(rpm * 1.1)
        self._set_stirrer_speed(rpm)
        self._start_stirrer()

    @respect_lock
    def stop_stirring(self):
        self._stop_stirrer()

    @respect_lock
    def heat_to_temperature(self, temperature: int):
        self._set_hot_plate_safety_temperature(temperature * 1.1)
        self._set_hot_plate_temperature(temperature)
        self._start_hot_plate()

    @respect_lock
    def stop_heating(self):
        self._stop_hot_plate()

    @respect_lock
    def stirr_and_heat(self, rpm: int, temperature: int):
        self.stirr_at_rpm(rpm)
        self.heat_to_temperature(temperature)

    @respect_lock
    def stop_stirring_and_heating(self):
        self.stop_stirring()
        self.stop_heating()

    @respect_lock
    def stirr_at_rpm_for_minutes_blocking(self, rpm: int, minutes: int):
        self.stirr_at_rpm(rpm)
        time.sleep(minutes * 60)
        self.stop_stirring()

    @respect_lock
    def stirr_and_heat_at_rpm_and_temperature_for_minutes_blocking(self, rpm: int, temperature: int, minutes: int):
        self.stirr_at_rpm(rpm)
        self.heat_to_temperature(temperature)
        time.sleep(minutes * 60)
        self.stop_stirring()
        self.stop_heating()

    def close(self):
        self._serial.close()

    def _get_stirrer_speed(self) -> int:
        self._serial.send_command("IN_PV_4")
        return int(self._serial.read_last_line().split()[0])

    def _set_stirrer_speed(self, rpm: int):
        self._serial.send_command(f"OUT_SP_4 {rpm}")

    def _get_stirrer_speed_set_point(self) -> int:
        self._serial.send_command("IN_SP_4")
        return int(self._serial.read_last_line().split()[0])

    def _set_stirrer_safety_speed(self, rpm: int):
        self._serial.send_command(f"OUT_SP_42@{rpm}")

    def _start_stirrer(self):
        self._serial.send_command("START_4")

    def _stop_stirrer(self):
        self._serial.send_command("STOP_4")

    def _get_hot_plate_temperature(self) -> int:
        self._serial.send_command("IN_PV_2")
        return int(self._serial.read_last_line().split()[0])

    def _set_hot_plate_temperature(self, temperature: int):
        self._serial.send_command(f"OUT_SP_2 {temperature}")

    def _get_hot_plate_temperature_set_point(self) -> int:
        self._serial.send_command("IN_SP_2")
        return int(self._serial.read_last_line().split()[0])

    def _set_hot_plate_safety_temperature(self, temperature: int):
        self._serial.send_command(f"OUT_SP_12@{temperature}")

    def _start_hot_plate(self):
        self._serial.send_command("START_2")

    def _stop_hot_plate(self):
        self._serial.send_command("STOP_2")
