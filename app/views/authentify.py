from app.models import *


def login_required(user):
    if user.is_anonymous():
        return False
    return True


def is_teacher(user):
    if Teacher.objects.filter(user_id=user.id).count() == 1:
        teacher = Teacher.objects.filter(user_id=user.id).first()
        times = Teach.objects.filter(teacher_id=teacher).count()
        students = Take.objects.filter(section_id__teach__teacher_id=teacher).count()
        levels = Level.objects.all().order_by('-level')
        for level in levels:
            if (students >= level.students) and (times >= level.times):
                teacher.level = level.level
                teacher.save()
                break
        return teacher
    return False
