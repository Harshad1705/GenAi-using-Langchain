from pydantic import BaseModel,Field
from typing import Optional

class Student(BaseModel):
    name : str = "default_value"
    age : Optional[int] = None
    cgpa : float = Field(gt=0 , lt=10 , default=5 , description="Decimal value representing cgpa of student")


new_student = { "name" : "harshad" , "cgpa" : 8.2  }

student = Student(**new_student)

print(student)

student_dict = dict(student)
print(student_dict)

student_json = student.model_dump_json()
print(student_json)