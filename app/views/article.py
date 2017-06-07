from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *
import json

def article(request, option):

    if option == 'total' :
        article_list = Article.objects.all()
        for article in article_list:
            temp_dict = dict()
            temp_dict['article_id'] = article.article_id
            temp_dict['article_user'] = article.user_id
            temp_dict['article_title'] = article.title
            temp_dict['article_date'] = article.date
        context = {}
        context['article_list'] = article_list
        return render(request, 'app/total_article.html', context)

    elif option == 'write' :
        category_list = Category.objects.all()
        for category in category_list:
            temp_dict = dict()
            temp_dict['category_id'] = category.id
            temp_dict['category_name'] = category.category_name
        context = {}
        context['category_list'] = category_list
        return render(request, 'app/write_article.html', context)
