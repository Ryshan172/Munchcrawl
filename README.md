# MunchCrawl 

MunchCrawl is a search engine for cravings. 
Connecting you to the dishes your heart (stomach) desires


## Backend 

### Set-up and Running  

Create and activate virtual environment

```
cd backend 

python3 -m venv code_env

source code_env/bin/activate
```

Install required packages in environment

```
pip install -r requirements.txt
```


**Run API**

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be accessible locally at http://localhost:8000/docs#/


TODO: 
- Add docker container 