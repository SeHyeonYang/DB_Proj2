from app.models import *


def login_required(user):
    if user.is_anonymous():
        return False
    return True


def is_teacher(user):
    if Teacher.objects.filter(user_id=user.id).count() == 1:
        return Teacher.objects.filter(user_id=user.id).first()
    return False
