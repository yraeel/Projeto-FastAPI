from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return 'Flamengo campeão'


@app.get('/eu')
def read_root():
    return 'amo alicia'

