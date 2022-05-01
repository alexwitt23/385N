# 385N Final Project


# Install

Install the python requirements:

```
python3 -m pip install -r requirements.txt
```

# Running

```
export FLASK_APP=src/flask_api
PYTHONPATH=. flask run
```

# API

```
curl http://127.0.0.1:5000/calculate-reward?archive=rlm_20220426.tar.zst
```

# Deploying Smart Contract

`cd deployContract`
`echo "AURORA_PRIVATE_KEY=<PRIVATE_KEY>" >> .env`
`yarn install`
`make deploy NETWORK=testnet_aurora`

