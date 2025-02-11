from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import asyncmy  
from typing import Optional


app = FastAPI()

DB_HOST = "mysql" 
DB_USER = "user"
DB_PASSWORD = "userpassword"
DB_NAME = "student_db"


class Student(BaseModel):
    name: str
    student_id: str
    gpa: float 

async def get_db_connection():
    return await asyncmy.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        host=DB_HOST,
        port=3306
    )

@app.get("/students", response_model=list[Student])
async def get_students(sortBy: Optional[str] = None,count : Optional[int] = None):
    db = await get_db_connection()
  
    cursor = db.cursor() 
    query = "SELECT * FROM students"

    if sortBy in {"id", "name", "student_id", "gpa"}:
        query += f" ORDER BY {sortBy} DESC"
    
    if count  is not None:
        query += f" LIMIT {count }"

    await cursor.execute(query)
    students = await cursor.fetchall()

    students = [Student(id=row[0], name=row[1], student_id=row[2], gpa=row[3]) for row in students]

    return students
    
    

@app.get("/students/{student_id}", response_model=Student)
async def get_specific_student(student_id: str):
    db = await get_db_connection()

    cursor = db.cursor()
    await cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id))
    student = await cursor.fetchone()

    if not student:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Student with student_id {student_id} not found"
    )
    print("student is: ", student)
    return Student(id=student[0], name=student[1], student_id=student[2], gpa=student[3])



        


@app.post("/students", status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    db = await get_db_connection()

    if not all([student.name, student.student_id, student.gpa]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid data: name, student_id, and gpa are required."
            )
   
    cursor = db.cursor()
    
        
    query = "INSERT INTO students (name, student_id, gpa) VALUES (%s, %s, %s)"
    await cursor.execute(query, (student.name, student.student_id, student.gpa))
    await db.commit()  

    new_id = cursor.lastrowid


    return {
        "message": " POST request completed successfully.",
        "student": {
            "id": new_id,
            "name": student.name,
            "student_id": student.student_id,
            "gpa": student.gpa

        }
    }



@app.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student(student_id: str):
    db = await get_db_connection()
    print("student id is: ", student_id)
    cursor = db.cursor() 

    # Check if student exists
    await cursor.execute("SELECT * FROM students WHERE student_id = %s", (student_id))
    student = await cursor.fetchone()
    
    print("student is: ", student)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with student_id {student_id} not found"
        )

    await cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    await db.commit() 

    return {
        "message": f"Student with student_id {student_id} has been deleted successfully"
    }

 

#To test if server is spinning
@app.get('/yehaw')
def get_all_yeehaws():
    print("comingthrough here?")
    return ["Alice", "Bob", "Charlie"]

