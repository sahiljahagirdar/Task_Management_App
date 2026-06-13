from fastapi import FastAPI
from src.utils.db import Base,engine
from src.tasks.router import task_routes
from src.users.router import user_router

Base.metadata.create_all(engine)

app = FastAPI(title='This is my Task management Application')
app.include_router(task_routes)
app.include_router(user_router)



@app.get('/')
def home():
    return 'TASK_MANAGEMENT_APP'


