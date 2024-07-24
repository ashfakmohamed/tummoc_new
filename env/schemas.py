from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    grade: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    teacher_id: Optional[int] = None

    class Config:
        orm_mode = True

class TeacherBase(BaseModel):
    name: str
    subject: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int
    students: List[Student] = []

    class Config:
        orm_mode = True