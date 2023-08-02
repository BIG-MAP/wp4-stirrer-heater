import time

from stirrer_heater_driver.serial_driver import SerialDriver


class StirrerHeater:
    def __init__(self, port: str):
        self._serial = SerialDriver(port)
        self._locked = False

    def stirr_at_rpm_for_minutes(self, rpm: int, minutes: int):
        if self._locked:
            raise RuntimeError("Device is locked")

        self._locked = True
        try:
            self._set_stirrer_safety_speed(rpm * 1.1)
            self._set_stirrer_speed(rpm)
            self._start_stirrer()
            time.sleep(minutes * 60)
            self._stop_stirrer()
        except Exception as e:
            raise e
        finally:
            self._locked = False

    def stirr_and_heat_at_rpm_and_temperature_for_minutes(self, rpm: int, temperature: int, minutes: int):
        if self._locked:
            raise RuntimeError("Device is locked")

        self._locked = True
        try:
            self._set_stirrer_safety_speed(rpm * 1.1)
            self._set_stirrer_speed(rpm)
            self._set_hot_plate_safety_temperature(temperature * 1.1)
            self._set_hot_plate_temperature(temperature)
            self._start_stirrer()
            self._start_hot_plate()
            time.sleep(minutes * 60)
            self._stop_stirrer()
            self._stop_hot_plate()
        except Exception as e:
            raise e
        finally:
            self._locked = False

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
