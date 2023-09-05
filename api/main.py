import sys
from fastapi import FastAPI

from models import Todo

app = FastAPI()

sys.path.append(".")


@app.get("/")
async def root():
    return {"message": "Hello"}


todos = []


# GetAll Todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}


# GetSingle Todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No Todo found"}


# Create a Todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully"}


# Update a Todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_to_update: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_to_update.id
            todo.item = todo_to_update.item
            return {"todo": todo}
    return {"message": "No Todo found to update"}


# Delete a Todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been deleted!"}
    return {"message": "No Todo found"}
