from src.tasks.dtos import Task_schema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException,status
from src.users.models import UserModel

def create_task(body:Task_schema,db:Session,user:UserModel):
    data = body.model_dump()
    new_task = TaskModel(title = data['title'],
                         description = data['description'],
                         is_completed = data['is_completed'],
                         user_id = user.id
                         )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks(db:Session,user:UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return tasks


def get_specific_task(task_id:int,db:Session,user:UserModel):

    one_task:TaskModel = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(
            404,
            detail="Task Id is incorrect"
        )
    
    if one_task.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task Not found'
        )
    
    return one_task


def update_task(body:Task_schema,task_id:int,db:Session,user:UserModel):
    one_task:TaskModel = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = 'Task Id is Incorrect'
        )
    
    if one_task.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='NOT ALLOWED TO MAKE CHANGES'
        )
    
    body = body.model_dump()
    for field,value in body.items():
        setattr(one_task,field,value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)

    return one_task
    
    


def delete_specific_task(task_id:int,db:Session,user:UserModel):
    one_task:TaskModel = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(
            404,
            detail='Task Id not found'
        )
    
    if one_task.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Not authorized to perform this task'
        )
    
    db.delete(one_task)
    db.commit()

    return None

