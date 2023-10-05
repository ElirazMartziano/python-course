1. Create a venv folder: <br /> ```py -m venv venv```

2. Activate the venv: <br /> ```.\.venv\Scripts\activate```

3. Install the requirements: <br /> ```pip install -r requirements.txt```

* When running server.py this will create a server on localhost:8000

# How to create a live server on render.com
1. upload the files to git
2. go to render.com and create a new web service
3. choose the git repo and press connect
4. enter name, choose run time enviorment.
5. in the build command enter: ```pip install -U pip && pip install -r requirements.txt```
6. in the start command enter: ```python3 server.py```
7. In the advanced settings add enviorment variable for API_KEYS and PYTHON_VERSION for which version of python to use.
8. create web service and wait for it to build.
