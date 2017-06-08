from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
import time
import json
from django.db.models import Q

def group_home(request):
    _group_list = Group.objects.all()
    group_list = []
    article_list =[]

    for group in _group_list:
        temp = GroupArticle.objects.filter(group_id=group).count()
        temp_dict = dict()
        temp_dict['group_id'] = group.id
        temp_dict['group_name'] = group.group_name
        temp_dict['leader'] = group.leader
        temp_dict['date'] = group.date
        temp_dict['comments'] = group.comments
        temp_dict['category'] = group.category
        group_list.append(temp_dict)
    context = {}
    context['group_list'] = group_list

    _my_group_list = Group.objects.filter(usergroup__user_id=request.user)
    my_group_list = []
    for group in _my_group_list:
        temp_dict = dict()
        temp_dict['group_id'] = group.id
        temp_dict['group_name'] = group.group_name
        temp_dict['leader'] = group.leader
        temp_dict['date'] = group.date
        temp_dict['comments'] = group.comments
        temp_dict['category'] = group.category
        try:
            _garticle = GroupArticle.objects.filter(group_id=group).last()
            _article = _garticle.article_id
            temp_dict['article_id'] = str(_article.id)
            temp_dict['article_title'] = str(_article.title)
        except:
            pass
        my_group_list.append(temp_dict)
    context['my_group_list'] = my_group_list

    if request.method == "GET":
        return render(request, 'app/group_home.html', context)

    else:
        post_group_list =[]
        if request.method == "POST":
            data = request.POST

            if request.GET.get('option') == 'join':
                print("OK2")
                group_id = request.GET.get('data')[:-1]
                group = Group.objects.filter(id=group_id).first()
                user_group = UserGroup.objects.create(group_id=group, user_id=request.user)
                user_group.save()
                return HttpResponse("OK")

            else :
                data = request.POST
                text = data['search']
                option = data.get('option', None)
                if option == 'title':
                    _group_list = Group.objects.filter(group_name__contains=text)

                elif option == 'user':
                    user_list = User.objects.filter(Q(username__contains=text))
                    _group_list = Group.objects.filter(leader__in=user_list)

                elif option == 'category':
                    category_list = Category.objects.filter(category_name__contains=text)
                    _group_list = Group.objects.filter(category__in = category_list)

                else:
                    _group_list = Group.objects.all()

                for group in _group_list:
                    # temp = GroupArticle.objects.filter(group_id=group).count()
                    temp_dict = dict()
                    temp_dict['group_id'] = group.id
                    temp_dict['group_name'] = group.group_name
                    temp_dict['leader'] = group.leader
                    temp_dict['date'] = group.date
                    temp_dict['comments'] = group.comments
                    temp_dict['category'] = group.category
                    post_group_list.append(temp_dict)
                context = {}
                context['group_list'] = post_group_list
                _my_group_list = Group.objects.filter(usergroup__user_id=request.user)
                my_group_list = []

                for group in _my_group_list:
                    temp_dict = dict()
                    temp_dict['group_id'] = group.id
                    temp_dict['group_name'] = group.group_name
                    temp_dict['leader'] = group.leader
                    temp_dict['date'] = group.date
                    temp_dict['comments'] = group.comments
                    temp_dict['category'] = group.category
                    try:
                        _garticle = GroupArticle.objects.filter(group_id=group).last()
                        _article = _garticle.article_id
                        temp_dict['article_id'] = str(_article.id)
                        temp_dict['article_title'] = str(_article.title)
                    except:
                        pass
                    my_group_list.append(temp_dict)
                context['my_group_list'] = my_group_list
                return render(request, 'app/group_home.html', context)


def group_create(request):
    _category_list = Category.objects.all()
    category_list = []
    for category in _category_list:
        temp_dict = dict()
        temp_dict['category_id'] = category.id
        temp_dict['category_name'] = category.category_name
        category_list.append(temp_dict)
    context = {}
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


def group_private(request,group_id, option):
    group_member = UserGroup.objects.filter(group_id=group_id)
    member_list = []
    for member in group_member:
        temp_dict = dict()
        temp_dict['member_id'] = member.user_id
        print(member.user_id)
        # temp_dict['member_nickname'] = User.objects.filter(username=member.user_id).first().fi
        member_list.append(temp_dict)
    context = {}
    context['member_list'] = member_list
    context['group_id'] = Group.objects.get(id=group_id)
    if option == 'write':
        if request.method == "GET":
            category_list = Category.objects.all()
            for category in category_list:
                temp_dict = dict()
                temp_dict['category_id'] = category.id
                temp_dict['category_name'] = category.category_name
            context['category_list'] = category_list
            return render(request, 'app/group_write.html', context)
        elif request.method == "POST":
            data = request.POST
            c_user_id = request.user
            c_title = data['title']

            c_content = data['content']
            c_date = time.ctime()

            group = Group.objects.filter(id=group_id).first()
            article = Article( user_id=c_user_id, title=c_title, contents=c_content,
                            date=c_date, notice=False)
            article.save()
            article2 = Article.objects.all().order_by('id').last()
            group_article = GroupArticle(article_id = article2, group_id = group)
            group_article.save()
            return render(request,'app/group_write.html', context)
    else :
        # context = Group.objects.get(id=group_id)
        article_list = GroupArticle.objects.filter(group_id = group_id)
        for article in article_list:
            temp_dict = dict()
            temp_dict['article_id'] = article.article_id.id
            temp_dict['article_user'] = article.article_id.user_id
            temp_dict['article_title'] = article.article_id.title
            temp_dict['article_date'] = article.article_id.date
        context['article_list'] = article_list
        return render(request, 'app/group_private.html', context)


def group_write(request,group_id):

    return render(request, 'app/group_private.html',{})