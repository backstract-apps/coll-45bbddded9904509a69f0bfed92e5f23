from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/subjects/')
async def get_subjects(db: Session = Depends(get_db)):
    try:
        return await service.get_subjects(db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/subjects/subject_id')
async def get_subjects_subject_id(subject_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_subjects_subject_id(db, subject_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/subjects/')
async def post_subjects(raw_data: schemas.PostSubjects, db: Session = Depends(get_db)):
    try:
        return await service.post_subjects(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/subjects/subject_id/')
async def put_subjects_subject_id(raw_data: schemas.PutSubjectsSubjectId, db: Session = Depends(get_db)):
    try:
        return await service.put_subjects_subject_id(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/subjects/subject_id')
async def delete_subjects_subject_id(subject_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_subjects_subject_id(db, subject_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/classes/')
async def get_classes(db: Session = Depends(get_db)):
    try:
        return await service.get_classes(db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/enrollments/')
async def get_enrollments(db: Session = Depends(get_db)):
    try:
        return await service.get_enrollments(db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/enrollments/enrollment_id')
async def get_enrollments_enrollment_id(enrollment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_enrollments_enrollment_id(db, enrollment_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/')
async def get_students(db: Session = Depends(get_db)):
    try:
        return await service.get_students(db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/students/student_id')
async def get_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_students_student_id(db, student_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/students/student_id/')
async def put_students_student_id(raw_data: schemas.PutStudentsStudentId, db: Session = Depends(get_db)):
    try:
        return await service.put_students_student_id(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/students/student_id')
async def delete_students_student_id(student_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_students_student_id(db, student_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/grades/')
async def get_grades(db: Session = Depends(get_db)):
    try:
        return await service.get_grades(db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teachers/')
async def get_teachers(db: Session = Depends(get_db)):
    try:
        return await service.get_teachers(db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teachers/teacher_id')
async def get_teachers_teacher_id(teacher_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_teachers_teacher_id(db, teacher_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/teachers/')
async def post_teachers(raw_data: schemas.PostTeachers, db: Session = Depends(get_db)):
    try:
        return await service.post_teachers(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/teachers/teacher_id/')
async def put_teachers_teacher_id(raw_data: schemas.PutTeachersTeacherId, db: Session = Depends(get_db)):
    try:
        return await service.put_teachers_teacher_id(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/teachers/teacher_id')
async def delete_teachers_teacher_id(teacher_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_teachers_teacher_id(db, teacher_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/classes/class_id')
async def get_classes_class_id(class_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_classes_class_id(db, class_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/classes/')
async def post_classes(raw_data: schemas.PostClasses, db: Session = Depends(get_db)):
    try:
        return await service.post_classes(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/classes/class_id/')
async def put_classes_class_id(raw_data: schemas.PutClassesClassId, db: Session = Depends(get_db)):
    try:
        return await service.put_classes_class_id(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/classes/class_id')
async def delete_classes_class_id(class_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_classes_class_id(db, class_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/enrollments/')
async def post_enrollments(raw_data: schemas.PostEnrollments, db: Session = Depends(get_db)):
    try:
        return await service.post_enrollments(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/enrollments/enrollment_id/')
async def put_enrollments_enrollment_id(raw_data: schemas.PutEnrollmentsEnrollmentId, db: Session = Depends(get_db)):
    try:
        return await service.put_enrollments_enrollment_id(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/enrollments/enrollment_id')
async def delete_enrollments_enrollment_id(enrollment_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_enrollments_enrollment_id(db, enrollment_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/grades/grade_id')
async def get_grades_grade_id(grade_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_grades_grade_id(db, grade_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/grades/')
async def post_grades(raw_data: schemas.PostGrades, db: Session = Depends(get_db)):
    try:
        return await service.post_grades(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/grades/grade_id/')
async def put_grades_grade_id(raw_data: schemas.PutGradesGradeId, db: Session = Depends(get_db)):
    try:
        return await service.put_grades_grade_id(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/grades/grade_id')
async def delete_grades_grade_id(grade_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_grades_grade_id(db, grade_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/attendance/')
async def get_attendance(db: Session = Depends(get_db)):
    try:
        return await service.get_attendance(db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/attendance/attendance_id')
async def get_attendance_attendance_id(attendance_id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_attendance_attendance_id(db, attendance_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/attendance/')
async def post_attendance(raw_data: schemas.PostAttendance, db: Session = Depends(get_db)):
    try:
        return await service.post_attendance(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/attendance/attendance_id/')
async def put_attendance_attendance_id(raw_data: schemas.PutAttendanceAttendanceId, db: Session = Depends(get_db)):
    try:
        return await service.put_attendance_attendance_id(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/attendance/attendance_id')
async def delete_attendance_attendance_id(attendance_id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_attendance_attendance_id(db, attendance_id)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/students/')
async def post_students(raw_data: schemas.PostStudents, db: Session = Depends(get_db)):
    try:
        return await service.post_students(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/login')
async def post_login(raw_data: schemas.PostLogin, db: Session = Depends(get_db)):
    try:
        return await service.post_login(db, raw_data)
    except ValueError as e:
        raise HTTPException(400, str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

