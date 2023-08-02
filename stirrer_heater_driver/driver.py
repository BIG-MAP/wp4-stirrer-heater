import serial
import time
import os
import logging

if os.name == "nt":
    comPort = "COM32"  # COM depends on computer, only for debugging
else:
    comPort = "/dev/ttyACM0"

weightMixer = serial.Serial(port=comPort, baudrate=9600, timeout=10, parity=serial.PARITY_EVEN, xonxoff=False)
time.sleep(1)


def get_Name() -> int:
    weightMixer.write(bytes("IN_NAME \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)

    return 0


def set_Speed(speed: int) -> int:
    weightMixer.write(bytes("OUT_SP_4 " + str(speed) + " \r \n", "utf-8"))
    print("Setting speed to " + str(speed))

    return 0


def get_Speed() -> int:
    weightMixer.write(bytes("IN_PV_4 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_Speed_Set_Point() -> int:
    weightMixer.write(bytes("IN_SP_4 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_Viscosity_Trend() -> int:
    weightMixer.write(bytes("IN_PV_5 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    viscosity = data[0 : data.find(" ")]

    return viscosity


def start_Mixer() -> int:
    weightMixer.write(bytes("START_4 \r \n", "utf-8"))
    print("Starting Mixer")

    return 0


def stop_Mixer() -> int:
    weightMixer.write(bytes("STOP_4 \r \n", "utf-8"))
    print("Stopping Mixer")

    return 0


def reset() -> int:
    weightMixer.write(bytes("RESET \r \n", "utf-8"))
    print("Resetting Mixer...")
    time.sleep(30)

    return 0


def start_Weight() -> int:
    weightMixer.write(bytes("START_90 \r \n", "utf-8"))
    print("Starting Weight")

    return 0


def stop_Weight() -> int:
    weightMixer.write(bytes("STOP_90 \r \n", "utf-8"))
    print("Stopping Weight")

    return 0


def get_Weight_Value() -> int:
    weightMixer.write(bytes("IN_PV_90 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    weight = data[0 : data.find(" ")]

    return weight


def get_Weight_Status() -> int:
    tare = False
    scale_on = False
    scale_stable = False
    scale_overload = False
    scale_power_on = False

    weightMixer.write(bytes("STATUS_90 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    value = data[0 : data.find(" ")]
    value = int(value)
    print(bin(value))

    if value & 0b1:
        print("Scale stable")
        scale_stable = True
    else:
        print("Scale not stable")

    if value & 0b1000:
        print("Tare completed")
        tare = True
    else:
        print("Tare not completed")

    if value & 0b10000:
        print("Scale on")
        scale_on = True
    else:
        print("Scale not on")

    if value & 0b1000000000:
        print("Scale overload")
        scale_overload = True

    if value & 0b10000000000:
        print("Scale power on")
        scale_power_on = True

    return tare, scale_on, scale_stable, scale_power_on, scale_overload


def get_hot_plate_temperature() -> int:
    weightMixer.write(bytes("IN_PV_2 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_hot_plate_temperature_set_point() -> int:
    weightMixer.write(bytes("IN_SP_2 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_hot_plate_safety_temperature() -> int:
    weightMixer.write(bytes("IN_PV_3 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_hot_plate_safety_temperature_set_point() -> int:
    weightMixer.write(bytes("IN_SP_3 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_heat_transfer_medium_temperature() -> int:
    weightMixer.write(bytes("IN_PV_7 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_heat_transfer_medium_temperature_set_point() -> int:
    weightMixer.write(bytes("IN_SP_7 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_external_sensor_temperature() -> int:
    weightMixer.write(bytes("IN_PV_1 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def get_external_sensor_temperature_set_point() -> int:
    weightMixer.write(bytes("IN_SP_1 \r \n", "utf-8"))

    getData = weightMixer.readline()
    data = getData.decode("utf-8").rstrip()
    print(data)
    speed = data[0 : data.find(" ")]

    return speed


def set_hot_plate_temperature(temperature: int) -> int:
    weightMixer.write(bytes("OUT_SP_2 " + str(temperature) + " \r \n", "utf-8"))
    print("Setting hot plate temperature to " + str(temperature))

    return 0


def set_heat_transfer_medium_temperature(temperature: int) -> int:
    weightMixer.write(bytes("OUT_SP_7 " + str(temperature) + " \r \n", "utf-8"))
    print("Setting heat transfer medium temperature to " + str(temperature))

    return 0


def set_external_sensor_temperature(temperature: int) -> int:
    weightMixer.write(bytes("OUT_SP_1 " + str(temperature) + " \r \n", "utf-8"))
    print("Setting external sensor temperature to " + str(temperature))

    return 0


def start_hot_plate() -> int:
    weightMixer.write(bytes("START_2 \r \n", "utf-8"))
    print("Starting Hot plate")

    return 0


def stop_hot_plate() -> int:
    weightMixer.write(bytes("STOP_2 \r \n", "utf-8"))
    print("Stopping Hot plate")

    return 0