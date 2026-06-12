from src.tasks.dtos import Task_schema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(body:Task_schema,db:Session):
    data = body.model_dump()
    new_task = TaskModel(title = data['title'],
                         description = data['description'],
                         is_completed = data['is_completed']
                         )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {'status':"task created sucessfully","Data":new_task}


def get_tasks(db:Session):
    tasks = db.query(TaskModel).all()
    return {"Status":"All tasks","data":tasks}


def get_specific_task(task_id:int,db:Session):

    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(
            404,
            detail="Task Id is incorrect"
        )
    return {"Status":"Task fetched sucessfully","data":one_task}
