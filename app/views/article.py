from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from app.models import *
import datetime
import json


def article(request, option):
    if option == 'total':

        if request.method == "POST":

            data = request.POST
            text = data['search']
            option = data.get('option',None)
            if option == 'title' :
                article_list = Article.objects.filter(title__contains=text)

            elif option == 'user' :
                user_list = User.objects.filter(Q(username__contains=text))
                article_list = Article.objects.filter(user_id__in = user_list)

            elif option == 'content':
                article_list = Article.objects.filter(contents__contains=text)

            else :
                article_list = Article.objects.all()

            for article in article_list:
                temp_dict = dict()
                temp_dict['article_id'] = article.id
                temp_dict['article_user'] = article.user_id
                temp_dict['article_title'] = article.title
                temp_dict['article_date'] = article.date
            context = {}
            context['article_list'] = article_list

            return render(request, 'app/total_article.html', context)

        else :

            article_list = Article.objects.all()
            for article in article_list:
                temp_dict = dict()
                temp_dict['article_id'] = article.id
                temp_dict['article_user'] = article.user_id
                temp_dict['article_title'] = article.title
                temp_dict['article_date'] = article.date
            context = {}
            context['article_list'] = article_list
            return render(request, 'app/total_article.html', context)

    elif option == 'write':
        if request.method == "GET":
            category_list = Category.objects.all()
            for category in category_list:
                temp_dict = dict()
                temp_dict['category_id'] = category.id
                temp_dict['category_name'] = category.category_name
            context = {}
            context['category_list'] = category_list
            return render(request, 'app/write_article.html', context)
        elif request.method == "POST":
            data = request.POST
            c_user_id = request.user
            c_title = data['title']

            c_content = data['content']
            c_date = datetime.datetime.now(),
            article = Article.objects.create(user_id=c_user_id, title=c_title, contents=c_content,
                                             date=c_date, notice=False)
            article.save()
            return render(request, 'app/write_article.html', {})


def info_article(request, pk):
    context = Article.objects.get(id=pk)
    if request.method == "GET":
        return render(request, 'app/info_article.html', {'article': context, })

    else:

        d_id = pk
        Article.objects.filter(id=pk).delete()

        category_list = Category.objects.all()
        for category in category_list:
            temp_dict = dict()
            temp_dict['category_id'] = category.id
            temp_dict['category_name'] = category.category_name
        context = {}
        context['category_list'] = category_list
        return render(request, 'app/info_article.html', context)
