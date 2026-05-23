import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cross = students.merge(subjects, how='cross')
    exams_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    result = cross.merge(exams_count, on=['student_id', 'subject_name'], how='left').fillna({'attended_exams': 0})
    result['attended_exams'] = result['attended_exams'].astype(int)
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']].sort_values(by=['student_id', 'subject_name'])

    