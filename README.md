# WP4 Magnetic Stirrer and Hotplate IKA

This repository contains:

- The [driver](./stirrer_heater_driver/) for the IKA magnetic stirrer and hotplate.
- The [HTTP server](./stirrer_heater_http/) that provides a REST API to control the stirrer and hotplate.

## Getting Started

We use the obsolete way of installing Python packages using `setup.py` to avoid issues with the missing Rust compiler for the cryptography package [[1](https://github.com/pyca/cryptography/issues/5771#issuecomment-775016788), [2](https://cryptography.io/en/latest/faq/#why-does-cryptography-require-rust)].

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install the packages
pip install -r requirements.txt
python setup.py install

# Run the manual test
python tests/manual_driver_test.py
```

To start an HTTP server, run:

```bash
IKA_SERIAL_PORT=/dev/ttyACM0 uvicorn stirrer_heater_http.main:app --host "0.0.0.0" --port 8080
```

To stirr at 100 RPM, run:

```bash
curl -X POST "localhost:8080/stirr?rpm=100"
```

To stop stirring, run:

```bash
curl -X POST "localhost:8080/stop_stirring"
```

To heat and stirr at the same time, run:

```bash
curl -X POST "localhost:8080/stirr_and_heat?rpm=100&temperature=50"
# after some time
curl -X POST "localhost:8080/stop_stirring_and_heating"
```

## Possible workflows

### Workflow 1

- Set RPM: 250-800 rpm
- Mix 5-20 minutes

### Workflow 2

- Set RPM: 250-800 rpm
- Mix 2 hours

### Workflow 3

- Set RPM: 250-800 rpm
- Mix 12 hours

### Workflow 4

- Set RPM: 250-800 rpm
- Set max hot plate temperature about 100 C
- Mix 120 hours (?) and heat till 50 C at the same time

### Workflow 5

- Set RPM: 250-800 rpm
- Mix 15 min
