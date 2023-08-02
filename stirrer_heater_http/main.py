import logging
import os
from dataclasses import dataclass
from typing import Any, Optional

from fastapi import FastAPI

from stirrer_heater_driver.driver import StirrerHeater

serial_port: Optional[str] = os.environ.get("IKA_SERIAL_PORT")
if serial_port is None:
    raise RuntimeError("IKA_SERIAL_PORT environment variable is not set")

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lifespan(app: FastAPI):
    yield
    app.state.logger.info("Shutting down the stirrer-heater")
    app.state.ika.close()


app = FastAPI(lifespan=lifespan)
app.state.ika = StirrerHeater(serial_port)
app.state.logger = logger


@dataclass
class APIResponse:
    data: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None

    def json(self):
        return self.__dict__


@app.post("/stirr")
async def stirr(rpm: int):
    app.state.ika.stirr(rpm=rpm)
    return APIResponse(message=f"Stirring at {rpm} rpm")


@app.post("/stop_stirring")
async def stop_stirring():
    app.state.ika.stop_stirring()
    return APIResponse(message="Stopped stirring")


@app.post("/heat")
async def heat(temperature: int):
    app.state.ika.heat(temperature=temperature)
    return APIResponse(message=f"Heating to {temperature} °C")


@app.post("/stop_heating")
async def stop_heating():
    app.state.ika.stop_heating()
    return APIResponse(message="Stopped heating")


@app.post("/stirr_and_heat")
async def stirr_and_heat(rpm: int, temperature: int):
    app.state.ika.stirr_and_heat(rpm=rpm, temperature=temperature)
    return APIResponse(message=f"Stirring at {rpm} rpm and heating to {temperature} °C")


@app.post("/stop_stirring_and_heating")
async def stop_stirring_and_heating():
    app.state.ika.stop_stirring_and_heating()
    return APIResponse(message="Stopped stirring and heating")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
