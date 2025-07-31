from sqlalchemy.orm import Session, aliased
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


async def get_subjects(db: Session):

    query = db.query(models.Subjects)

    subjects_all = query.all()
    subjects_all = (
        [new_data.to_dict() for new_data in subjects_all]
        if subjects_all
        else subjects_all
    )
    res = {
        "subjects_all": subjects_all,
    }
    return res


async def get_subjects_subject_id(db: Session, subject_id: int):

    query = db.query(models.Subjects)
    query = query.filter(and_(models.Subjects.subject_id == subject_id))

    subjects_one = query.first()

    subjects_one = (
        (
            subjects_one.to_dict()
            if hasattr(subjects_one, "to_dict")
            else vars(subjects_one)
        )
        if subjects_one
        else subjects_one
    )

    res = {
        "subjects_one": subjects_one,
    }
    return res


async def post_subjects(db: Session, raw_data: schemas.PostSubjects):
    name: str = raw_data.name

    record_to_be_added = {"name": name}
    new_subjects = models.Subjects(**record_to_be_added)
    db.add(new_subjects)
    db.commit()
    db.refresh(new_subjects)
    subjects_inserted_record = new_subjects.to_dict()

    res = {
        "subjects_inserted_record": subjects_inserted_record,
    }
    return res


async def put_subjects_subject_id(db: Session, raw_data: schemas.PutSubjectsSubjectId):
    subject_id: int = raw_data.subject_id
    name: str = raw_data.name

    query = db.query(models.Subjects)
    query = query.filter(and_(models.Subjects.subject_id == subject_id))
    subjects_edited_record = query.first()

    if subjects_edited_record:
        for key, value in {"name": name, "subject_id": subject_id}.items():
            setattr(subjects_edited_record, key, value)

        db.commit()
        db.refresh(subjects_edited_record)

        subjects_edited_record = (
            subjects_edited_record.to_dict()
            if hasattr(subjects_edited_record, "to_dict")
            else vars(subjects_edited_record)
        )
    res = {
        "subjects_edited_record": subjects_edited_record,
    }
    return res


async def delete_subjects_subject_id(db: Session, subject_id: int):

    query = db.query(models.Subjects)
    query = query.filter(and_(models.Subjects.subject_id == subject_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        subjects_deleted = record_to_delete.to_dict()
    else:
        subjects_deleted = record_to_delete
    res = {
        "subjects_deleted": subjects_deleted,
    }
    return res


async def get_classes(db: Session):

    query = db.query(models.Classes)

    classes_all = query.all()
    classes_all = (
        [new_data.to_dict() for new_data in classes_all] if classes_all else classes_all
    )
    res = {
        "classes_all": classes_all,
    }
    return res


async def get_enrollments(db: Session):

    query = db.query(models.Enrollments)

    enrollments_all = query.all()
    enrollments_all = (
        [new_data.to_dict() for new_data in enrollments_all]
        if enrollments_all
        else enrollments_all
    )
    res = {
        "enrollments_all": enrollments_all,
    }
    return res


async def get_enrollments_enrollment_id(db: Session, enrollment_id: int):

    query = db.query(models.Enrollments)
    query = query.filter(and_(models.Enrollments.enrollment_id == enrollment_id))

    enrollments_one = query.first()

    enrollments_one = (
        (
            enrollments_one.to_dict()
            if hasattr(enrollments_one, "to_dict")
            else vars(enrollments_one)
        )
        if enrollments_one
        else enrollments_one
    )

    res = {
        "enrollments_one": enrollments_one,
    }
    return res


async def get_students(db: Session):

    query = db.query(models.Students)

    students_all = query.all()
    students_all = (
        [new_data.to_dict() for new_data in students_all]
        if students_all
        else students_all
    )
    res = {
        "students_all": students_all,
    }
    return res


async def get_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))

    students_one = query.first()

    students_one = (
        (
            students_one.to_dict()
            if hasattr(students_one, "to_dict")
            else vars(students_one)
        )
        if students_one
        else students_one
    )

    res = {
        "students_one": students_one,
    }
    return res


async def put_students_student_id(db: Session, raw_data: schemas.PutStudentsStudentId):
    student_id: int = raw_data.student_id
    name: str = raw_data.name
    contact_info: str = raw_data.contact_info
    date_of_birth: datetime.date = raw_data.date_of_birth

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))
    students_edited_record = query.first()

    if students_edited_record:
        for key, value in {
            "name": name,
            "student_id": student_id,
            "contact_info": contact_info,
            "date_of_birth": date_of_birth,
        }.items():
            setattr(students_edited_record, key, value)

        db.commit()
        db.refresh(students_edited_record)

        students_edited_record = (
            students_edited_record.to_dict()
            if hasattr(students_edited_record, "to_dict")
            else vars(students_edited_record)
        )
    res = {
        "students_edited_record": students_edited_record,
    }
    return res


async def delete_students_student_id(db: Session, student_id: int):

    query = db.query(models.Students)
    query = query.filter(and_(models.Students.student_id == student_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        students_deleted = record_to_delete.to_dict()
    else:
        students_deleted = record_to_delete
    res = {
        "students_deleted": students_deleted,
    }
    return res


async def get_grades(db: Session):

    query = db.query(models.Grades)

    grades_all = query.all()
    grades_all = (
        [new_data.to_dict() for new_data in grades_all] if grades_all else grades_all
    )
    res = {
        "grades_all": grades_all,
    }
    return res


async def get_teachers(db: Session):

    query = db.query(models.Teachers)

    teachers_all = query.all()
    teachers_all = (
        [new_data.to_dict() for new_data in teachers_all]
        if teachers_all
        else teachers_all
    )
    res = {
        "teachers_all": teachers_all,
    }
    return res


async def get_teachers_teacher_id(db: Session, teacher_id: int):

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.teacher_id == teacher_id))

    teachers_one = query.first()

    teachers_one = (
        (
            teachers_one.to_dict()
            if hasattr(teachers_one, "to_dict")
            else vars(teachers_one)
        )
        if teachers_one
        else teachers_one
    )

    res = {
        "teachers_one": teachers_one,
    }
    return res


async def post_teachers(db: Session, raw_data: schemas.PostTeachers):
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    record_to_be_added = {"name": name, "contact_details": contact_details}
    new_teachers = models.Teachers(**record_to_be_added)
    db.add(new_teachers)
    db.commit()
    db.refresh(new_teachers)
    teachers_inserted_record = new_teachers.to_dict()

    res = {
        "teachers_inserted_record": teachers_inserted_record,
    }
    return res


async def put_teachers_teacher_id(db: Session, raw_data: schemas.PutTeachersTeacherId):
    teacher_id: int = raw_data.teacher_id
    name: str = raw_data.name
    contact_details: str = raw_data.contact_details

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.teacher_id == teacher_id))
    teachers_edited_record = query.first()

    if teachers_edited_record:
        for key, value in {
            "name": name,
            "teacher_id": teacher_id,
            "contact_details": contact_details,
        }.items():
            setattr(teachers_edited_record, key, value)

        db.commit()
        db.refresh(teachers_edited_record)

        teachers_edited_record = (
            teachers_edited_record.to_dict()
            if hasattr(teachers_edited_record, "to_dict")
            else vars(teachers_edited_record)
        )
    res = {
        "teachers_edited_record": teachers_edited_record,
    }
    return res


async def delete_teachers_teacher_id(db: Session, teacher_id: int):

    query = db.query(models.Teachers)
    query = query.filter(and_(models.Teachers.teacher_id == teacher_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        teachers_deleted = record_to_delete.to_dict()
    else:
        teachers_deleted = record_to_delete
    res = {
        "teachers_deleted": teachers_deleted,
    }
    return res


async def get_classes_class_id(db: Session, class_id: int):

    query = db.query(models.Classes)
    query = query.filter(and_(models.Classes.class_id == class_id))

    classes_one = query.first()

    classes_one = (
        (
            classes_one.to_dict()
            if hasattr(classes_one, "to_dict")
            else vars(classes_one)
        )
        if classes_one
        else classes_one
    )

    res = {
        "classes_one": classes_one,
    }
    return res


async def post_classes(db: Session, raw_data: schemas.PostClasses):
    subject_id: int = raw_data.subject_id
    teacher_id: int = raw_data.teacher_id
    time: str = raw_data.time
    location: str = raw_data.location

    record_to_be_added = {
        "time": time,
        "location": location,
        "subject_id": subject_id,
        "teacher_id": teacher_id,
    }
    new_classes = models.Classes(**record_to_be_added)
    db.add(new_classes)
    db.commit()
    db.refresh(new_classes)
    classes_inserted_record = new_classes.to_dict()

    res = {
        "classes_inserted_record": classes_inserted_record,
    }
    return res


async def put_classes_class_id(db: Session, raw_data: schemas.PutClassesClassId):
    class_id: int = raw_data.class_id
    subject_id: int = raw_data.subject_id
    teacher_id: int = raw_data.teacher_id
    time: str = raw_data.time
    location: str = raw_data.location

    query = db.query(models.Classes)
    query = query.filter(and_(models.Classes.class_id == class_id))
    classes_edited_record = query.first()

    if classes_edited_record:
        for key, value in {
            "time": time,
            "class_id": class_id,
            "location": location,
            "subject_id": subject_id,
            "teacher_id": teacher_id,
        }.items():
            setattr(classes_edited_record, key, value)

        db.commit()
        db.refresh(classes_edited_record)

        classes_edited_record = (
            classes_edited_record.to_dict()
            if hasattr(classes_edited_record, "to_dict")
            else vars(classes_edited_record)
        )
    res = {
        "classes_edited_record": classes_edited_record,
    }
    return res


async def delete_classes_class_id(db: Session, class_id: int):

    query = db.query(models.Classes)
    query = query.filter(and_(models.Classes.class_id == class_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        classes_deleted = record_to_delete.to_dict()
    else:
        classes_deleted = record_to_delete
    res = {
        "classes_deleted": classes_deleted,
    }
    return res


async def post_enrollments(db: Session, raw_data: schemas.PostEnrollments):
    student_id: int = raw_data.student_id
    class_id: int = raw_data.class_id

    record_to_be_added = {"class_id": class_id, "student_id": student_id}
    new_enrollments = models.Enrollments(**record_to_be_added)
    db.add(new_enrollments)
    db.commit()
    db.refresh(new_enrollments)
    enrollments_inserted_record = new_enrollments.to_dict()

    res = {
        "enrollments_inserted_record": enrollments_inserted_record,
    }
    return res


async def put_enrollments_enrollment_id(
    db: Session, raw_data: schemas.PutEnrollmentsEnrollmentId
):
    enrollment_id: int = raw_data.enrollment_id
    student_id: int = raw_data.student_id
    class_id: int = raw_data.class_id

    query = db.query(models.Enrollments)
    query = query.filter(and_(models.Enrollments.enrollment_id == enrollment_id))
    enrollments_edited_record = query.first()

    if enrollments_edited_record:
        for key, value in {
            "class_id": class_id,
            "student_id": student_id,
            "enrollment_id": enrollment_id,
        }.items():
            setattr(enrollments_edited_record, key, value)

        db.commit()
        db.refresh(enrollments_edited_record)

        enrollments_edited_record = (
            enrollments_edited_record.to_dict()
            if hasattr(enrollments_edited_record, "to_dict")
            else vars(enrollments_edited_record)
        )
    res = {
        "enrollments_edited_record": enrollments_edited_record,
    }
    return res


async def delete_enrollments_enrollment_id(db: Session, enrollment_id: int):

    query = db.query(models.Enrollments)
    query = query.filter(and_(models.Enrollments.enrollment_id == enrollment_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        enrollments_deleted = record_to_delete.to_dict()
    else:
        enrollments_deleted = record_to_delete
    res = {
        "enrollments_deleted": enrollments_deleted,
    }
    return res


async def get_grades_grade_id(db: Session, grade_id: int):

    query = db.query(models.Grades)
    query = query.filter(and_(models.Grades.grade_id == grade_id))

    grades_one = query.first()

    grades_one = (
        (grades_one.to_dict() if hasattr(grades_one, "to_dict") else vars(grades_one))
        if grades_one
        else grades_one
    )

    res = {
        "grades_one": grades_one,
    }
    return res


async def post_grades(db: Session, raw_data: schemas.PostGrades):
    student_id: int = raw_data.student_id
    class_id: int = raw_data.class_id
    grade: str = raw_data.grade

    record_to_be_added = {
        "grade": grade,
        "class_id": class_id,
        "student_id": student_id,
    }
    new_grades = models.Grades(**record_to_be_added)
    db.add(new_grades)
    db.commit()
    db.refresh(new_grades)
    grades_inserted_record = new_grades.to_dict()

    res = {
        "grades_inserted_record": grades_inserted_record,
    }
    return res


async def put_grades_grade_id(db: Session, raw_data: schemas.PutGradesGradeId):
    grade_id: int = raw_data.grade_id
    student_id: int = raw_data.student_id
    class_id: int = raw_data.class_id
    grade: str = raw_data.grade

    query = db.query(models.Grades)
    query = query.filter(and_(models.Grades.grade_id == grade_id))
    grades_edited_record = query.first()

    if grades_edited_record:
        for key, value in {
            "grade": grade,
            "class_id": class_id,
            "grade_id": grade_id,
            "student_id": student_id,
        }.items():
            setattr(grades_edited_record, key, value)

        db.commit()
        db.refresh(grades_edited_record)

        grades_edited_record = (
            grades_edited_record.to_dict()
            if hasattr(grades_edited_record, "to_dict")
            else vars(grades_edited_record)
        )
    res = {
        "grades_edited_record": grades_edited_record,
    }
    return res


async def delete_grades_grade_id(db: Session, grade_id: int):

    query = db.query(models.Grades)
    query = query.filter(and_(models.Grades.grade_id == grade_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        grades_deleted = record_to_delete.to_dict()
    else:
        grades_deleted = record_to_delete
    res = {
        "grades_deleted": grades_deleted,
    }
    return res


async def get_attendance(db: Session):

    query = db.query(models.Attendance)

    attendance_all = query.all()
    attendance_all = (
        [new_data.to_dict() for new_data in attendance_all]
        if attendance_all
        else attendance_all
    )
    res = {
        "attendance_all": attendance_all,
    }
    return res


async def get_attendance_attendance_id(db: Session, attendance_id: int):

    query = db.query(models.Attendance)
    query = query.filter(and_(models.Attendance.attendance_id == attendance_id))

    attendance_one = query.first()

    attendance_one = (
        (
            attendance_one.to_dict()
            if hasattr(attendance_one, "to_dict")
            else vars(attendance_one)
        )
        if attendance_one
        else attendance_one
    )

    res = {
        "attendance_one": attendance_one,
    }
    return res


async def post_attendance(db: Session, raw_data: schemas.PostAttendance):
    student_id: int = raw_data.student_id
    class_id: int = raw_data.class_id
    date: datetime.date = raw_data.date
    status: str = raw_data.status

    record_to_be_added = {
        "date": date,
        "status": status,
        "class_id": class_id,
        "student_id": student_id,
    }
    new_attendance = models.Attendance(**record_to_be_added)
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    attendance_inserted_record = new_attendance.to_dict()

    res = {
        "attendance_inserted_record": attendance_inserted_record,
    }
    return res


async def put_attendance_attendance_id(
    db: Session, raw_data: schemas.PutAttendanceAttendanceId
):
    attendance_id: int = raw_data.attendance_id
    student_id: int = raw_data.student_id
    class_id: int = raw_data.class_id
    date: datetime.date = raw_data.date
    status: str = raw_data.status

    query = db.query(models.Attendance)
    query = query.filter(and_(models.Attendance.attendance_id == attendance_id))
    attendance_edited_record = query.first()

    if attendance_edited_record:
        for key, value in {
            "date": date,
            "status": status,
            "class_id": class_id,
            "student_id": student_id,
            "attendance_id": attendance_id,
        }.items():
            setattr(attendance_edited_record, key, value)

        db.commit()
        db.refresh(attendance_edited_record)

        attendance_edited_record = (
            attendance_edited_record.to_dict()
            if hasattr(attendance_edited_record, "to_dict")
            else vars(attendance_edited_record)
        )
    res = {
        "attendance_edited_record": attendance_edited_record,
    }
    return res


async def delete_attendance_attendance_id(db: Session, attendance_id: int):

    query = db.query(models.Attendance)
    query = query.filter(and_(models.Attendance.attendance_id == attendance_id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        attendance_deleted = record_to_delete.to_dict()
    else:
        attendance_deleted = record_to_delete
    res = {
        "attendance_deleted": attendance_deleted,
    }
    return res


async def post_students(db: Session, raw_data: schemas.PostStudents):
    name: str = raw_data.name
    contact_info: str = raw_data.contact_info
    date_of_birth: str = raw_data.date_of_birth
    password: str = raw_data.password
    email: str = raw_data.email

    record_to_be_added = {
        "name": name,
        "contact_info": contact_info,
        "date_of_birth": date_of_birth,
    }
    new_students = models.Students(**record_to_be_added)
    db.add(new_students)
    db.commit()
    db.refresh(new_students)
    students_inserted_record = new_students.to_dict()

    res = {
        "students_inserted_record": students_inserted_record,
    }
    return res


async def post_login(db: Session, raw_data: schemas.PostLogin):
    email: str = raw_data.email
    password: str = raw_data.password

    query = db.query(models.Students)
    query = query.filter(
        and_(models.Students.email == email, models.Students.password == password)
    )

    fdghj = query.first()

    fdghj = (
        (fdghj.to_dict() if hasattr(fdghj, "to_dict") else vars(fdghj))
        if fdghj
        else fdghj
    )

    res = {
        "dsf": fdghj,
    }
    return res
