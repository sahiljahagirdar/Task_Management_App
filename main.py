from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.router import task_routes

Base.metadata.create_all(engine)

app = FastAPI(title='This is my Task management Application')
app.include_router(task_routes)


@app.get('/')
def home():
    return 'TASK_MANAGEMENT_APP'


