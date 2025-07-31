from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Students(BaseModel):
    name: Optional[str]=None
    contact_info: Optional[str]=None
    date_of_birth: Optional[datetime.date]=None
    email: Optional[str]=None
    password: Optional[str]=None


class ReadStudents(BaseModel):
    name: Optional[str]=None
    contact_info: Optional[str]=None
    date_of_birth: Optional[datetime.date]=None
    email: Optional[str]=None
    password: Optional[str]=None
    class Config:
        from_attributes = True


class Teachers(BaseModel):
    name: Optional[str]=None
    contact_details: Optional[str]=None


class ReadTeachers(BaseModel):
    name: Optional[str]=None
    contact_details: Optional[str]=None
    class Config:
        from_attributes = True


class Subjects(BaseModel):
    name: Optional[str]=None


class ReadSubjects(BaseModel):
    name: Optional[str]=None
    class Config:
        from_attributes = True


class Classes(BaseModel):
    subject_id: Optional[int]=None
    teacher_id: Optional[int]=None
    time: Optional[str]=None
    location: Optional[str]=None


class ReadClasses(BaseModel):
    subject_id: Optional[int]=None
    teacher_id: Optional[int]=None
    time: Optional[str]=None
    location: Optional[str]=None
    class Config:
        from_attributes = True


class Enrollments(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None


class ReadEnrollments(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    class Config:
        from_attributes = True


class Grades(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    grade: Optional[float]=None


class ReadGrades(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    grade: Optional[float]=None
    class Config:
        from_attributes = True


class Attendance(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    date: Optional[datetime.date]=None
    status: Optional[str]=None


class ReadAttendance(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    date: Optional[datetime.date]=None
    status: Optional[str]=None
    class Config:
        from_attributes = True




class PostSubjects(BaseModel):
    name: Optional[str]=None

    class Config:
        from_attributes = True



class PutSubjectsSubjectId(BaseModel):
    subject_id: Optional[int]=None
    name: Optional[str]=None

    class Config:
        from_attributes = True



class PutStudentsStudentId(BaseModel):
    student_id: Optional[int]=None
    name: Optional[str]=None
    contact_info: Optional[str]=None
    date_of_birth: Optional[Any]=None

    class Config:
        from_attributes = True



class PostTeachers(BaseModel):
    name: Optional[str]=None
    contact_details: Optional[str]=None

    class Config:
        from_attributes = True



class PutTeachersTeacherId(BaseModel):
    teacher_id: Optional[int]=None
    name: Optional[str]=None
    contact_details: Optional[str]=None

    class Config:
        from_attributes = True



class PostClasses(BaseModel):
    subject_id: Optional[int]=None
    teacher_id: Optional[int]=None
    time: Optional[str]=None
    location: Optional[str]=None

    class Config:
        from_attributes = True



class PutClassesClassId(BaseModel):
    class_id: Optional[int]=None
    subject_id: Optional[int]=None
    teacher_id: Optional[int]=None
    time: Optional[str]=None
    location: Optional[str]=None

    class Config:
        from_attributes = True



class PostEnrollments(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None

    class Config:
        from_attributes = True



class PutEnrollmentsEnrollmentId(BaseModel):
    enrollment_id: Optional[int]=None
    student_id: Optional[int]=None
    class_id: Optional[int]=None

    class Config:
        from_attributes = True



class PostGrades(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    grade: Optional[str]=None

    class Config:
        from_attributes = True



class PutGradesGradeId(BaseModel):
    grade_id: Optional[int]=None
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    grade: Optional[str]=None

    class Config:
        from_attributes = True



class PostAttendance(BaseModel):
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    date: Optional[Any]=None
    status: Optional[str]=None

    class Config:
        from_attributes = True



class PutAttendanceAttendanceId(BaseModel):
    attendance_id: Optional[int]=None
    student_id: Optional[int]=None
    class_id: Optional[int]=None
    date: Optional[Any]=None
    status: Optional[str]=None

    class Config:
        from_attributes = True



class PostStudents(BaseModel):
    name: Optional[str]=None
    contact_info: Optional[str]=None
    date_of_birth: Optional[str]=None
    password: str = Field(..., max_length=100)
    email: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True

