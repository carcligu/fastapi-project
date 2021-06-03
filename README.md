This repository is a tutorial on how to build a Fast API from scratch: https://fastapi.tiangolo.com/tutorial/

# 1. Installation and Set Up

## Install Pip
Make sure you have pip installed and upgraded to the latest version:
```
python3 -m pip install --upgrade pip
```
or
```
python -m pip install --upgrade pip
```
## Create a virtual enviroment
Create a virtual enviroment
```
virtualenv fast-api
```

## Activate virtual enviroment
### MacOS / Linux
```
source fast-api/bin/activate
```

### Windows
```
fast-api\Scripts\activate
```

## Install dependencies

In order to use fastapi, you need to install:
```
pip install fastapi
pip install uvicorn[standard]
```

or you can install it directly from the requirements.txt file

```
pip install -r requirements.txt
```

# 2. Create a hello world app
In the main.py file: 
```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

In order to run the server, we have to run the following command from terminal
```
uvicorn main:app --reload
```

where:
* main: refers to the python file
* app: refers to the FastAPI instance init in main.py




