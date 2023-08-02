from distutils.core import setup

setup(
    name="stirrer-heater-ika",
    version="0.1",
    description="SDK for Magnetic Stirrer and Heater IKA",
    packages=["stirrer_heater_driver", "stirrer_heater_http"],
    install_requires=[
        "pyserial",
        "fastapi",
        "uvicorn",
    ],
)
