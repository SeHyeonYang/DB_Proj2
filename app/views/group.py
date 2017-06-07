from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
import time
import json


def group_home(request):
    group_list = Group.objects.all()
    for group in group_list:
        temp_dict = dict()
        temp_dict['group_name'] = group.group_name
        temp_dict['leader'] = group.leader
        temp_dict['date'] = group.date
        temp_dict['comments'] = group.comments
        temp_dict['category'] = group.category

        context = {}

        context['group_list'] = group_list
        print("OK1")
        if request.method == "GET":
            return render(request, 'app/group_home.html', context)
        else:
            print("OK2")
            group_id = request.GET.get('data')[:-1]
            group = Group.objects.filter(id=group_id).first()
            user_group = UserGroup.objects.create(group_id=group, user_id=request.user)
            user_group.save()
            return HttpResponse("OK")




def group_create(request):
    category_list = Category.objects.all()
    for category in category_list:
        temp_dict = dict()
        temp_dict['category_id'] = category.id
        temp_dict['category_name'] = category.category_name
    context = []
    context['category_list'] = category_list

    if request.method == "GET":
        return render(request, 'app/group_create.html', context)

    else:
        data = request.POST
        group_name = data['group_name']
        group_comments = data['group_comment']
        this_group_category = data.get('category')
        group_cateogry = Category.objects.filter(category_name=this_group_category).first()
        print(group_cateogry.id)
        group = group_cateogry
        group_creater = request.user
        create_time = time.ctime()
        # print(str(group_catergory))
        group = Group.objects.create(group_name=group_name, leader=group_creater, date=create_time,
                                     comments=group_comments, category=group)
        group.save()
        return render(request, 'app/group_create.html', context)


def group_private(request):
    return render(request, 'app/group_private.html', {})