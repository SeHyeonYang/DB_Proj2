from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta

# Create your models here.

#
#class User(models.Model):
#    user_id = models.CharField(max_length=45, primary_key=True)
#    password = models.CharField(max_length=45)
#    name = models.CharField(max_length=45)
#    nickname = models.CharField(max_length=45)
#    last_login = models.DateTimeField(blank=True, null=True)
#


class AppUser(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=45)
    nickname = models.CharField(max_length=45)


def default_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)


class Teacher(models.Model):
    # teacher_id is auto serial key. 1,2,3,4,...
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=45)
    email_addr = models.EmailField()
    level = models.IntegerField(default=1)


class Category(models.Model):
    # category_id is auto serial key. 1,2,3,4,...
    category_name = models.CharField(max_length=45)


class TeacherCategory(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Course(models.Model):
    # course_id is auto serial key. 1,2,3,4,...
    title = models.CharField(max_length=80)
    category_id = models.ForeignKey(Category)
    comments = models.TextField(null=False)


class Section(models.Model):
    # section_id is auto serial key. 1,2,3,4,...
    course_id = models.ForeignKey(Course, related_name="section")  # not cascade
    start_date = models.DateField()
    end_date = models.DateField()
    times = models.IntegerField()
    location = models.CharField(max_length=80)
    price = models.IntegerField()
    due_date = models.DateField()
    max_capacity = models.IntegerField()
    min_capacity = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()


class TimeSlot(models.Model):
    # time_slot_id is auto serial key. 1,2,3,4,...
    day = models.IntegerField()  # mon~sun : 1~7
    start_time = models.TimeField()
    end_time = models.TimeField()


class Teach(models.Model):
    teacher_id = models.ForeignKey(Teacher)
    section_id = models.ForeignKey(Section)


class Take(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    section_id = models.ForeignKey(Section)


class Friend(models.Model):
    sender_id = models.ForeignKey(User, related_name='sender_id')
    receiver_id = models.ForeignKey(User, related_name='receiver_id')
    approve = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)  # approve 변경시 date 갱신


class Group(models.Model):
    # group_id is auto serial key. 1,2,3,4,...
    group_name = models.CharField(max_length=80)
    leader = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)  # group 생성시의 date
    comments = models.TextField()
    category = models.ForeignKey(Category)


class Article(models.Model):
    # article_id is auto serial key. 1,2,3,4,...
    user_id = models.ForeignKey(User)
    title = models.CharField(max_length=80)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    notice = models.BooleanField(default=False)


class UserGroup(models.Model):
    user_id = models.ForeignKey(User)
    group_id = models.ForeignKey(Group)


class GroupArticle(models.Model):
    article_id = models.ForeignKey(Article)
    group_id = models.ForeignKey(Group)


class Level(models.Model):
    level = models.IntegerField(primary_key=True)
    times = models.IntegerField(default=0)
    students = models.IntegerField(default=0)
