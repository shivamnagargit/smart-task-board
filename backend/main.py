from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from pydantic import BaseModel

# 1. CONNECT TO THE PANTRY (Database Connection)
# We are telling Python where to find the Docker database we made yesterday.
DATABASE_URL = "postgresql://admin:secretpassword@localhost:5432/taskboard"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. PANTRY BLUEPRINT (How data looks in the database)
class TaskDB(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default="todo")

# 3. WAITER BLUEPRINT (How we expect users to send us data)
class TaskCreate(BaseModel):
    title: str
    description: str = None

# 4. TURN ON THE KITCHEN (Start FastAPI)
app = FastAPI(title="Smart Task Board API")

# Helper function to open and close the pantry door
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. OUR RECIPES (The API Endpoints)

# A simple greeting
@app.get("/")
def read_root():
    return {"message": "Welcome to the Kitchen!"}

# Recipe to Create a new task
@app.post("/tasks/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = TaskDB(title=task.title, description=task.description)
    db.add(new_task)  # Put it in the pantry
    db.commit()       # Close the door and save
    db.refresh(new_task)
    return new_task

# Recipe to Read all tasks
@app.get("/tasks/")
def read_tasks(db: Session = Depends(get_db)):
    return db.query(TaskDB).all() # Fetch everything from the tasks table
