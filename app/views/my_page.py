from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .authentify import *
from django.http import HttpResponseRedirect, HttpResponse


def my_page(request, menu):
    user = request.user
    context = dict()
    context['my_info'] = user
    context['is_teacher'] = is_teacher(user)
    if menu == "info":
        return render(request, 'app/my_page_info.html', context)
    elif menu == "friend":
        if request.method == "POST":
            action = request.GET.get('action')
            if action == "search":
                option = request.GET.get('option')[:-1]
                if option == "findbyall":
                    data = request.POST.get("search-friend-by-all")
                    friend_search_list = User.objects.filter(Q(username=data) | Q(first_name=data) | Q(last_name=data))
                    search_list = []
                    for a in friend_search_list:
                        temp_dict = dict()
                        temp_dict['friend_search_id'] = a.username
                        temp_dict['friend_search_name'] = a.last_name
                        temp_dict['friend_search_nickname'] = a.first_name
                        search_list.append(temp_dict)
                    context['friend_search_list'] = search_list
                    maybe_friend_search_list = User.objects.filter(
                        Q(username__contains=data) | Q(first_name__contains=data) | Q(last_name__contains=data))
                    search_list_sub = []
                    for a in maybe_friend_search_list:
                        temp_dict = dict()
                        temp_dict['friend_search_id'] = a.username
                        temp_dict['friend_search_name'] = a.last_name
                        temp_dict['friend_search_nickname'] = a.first_name
                        search_list_sub.append(temp_dict)
                    context['friend_search_list_sub'] = search_list_sub
            elif action == "befriend":
                friend_id= request.GET.get('data')[:-1]
                friend = User.objects.filter(username=friend_id).first()
                new_relationship = Friend.objects.create(sender_id=user, receiver_id=friend)
                new_relationship.save()

        friends = Friend.objects.filter(Q(sender_id=user) | Q(receiver_id=user))
        friend_list = []
        for friend in friends:
            temp_dict = dict()
            temp_dict['friend_id'] = friend.receiver_id
            friend_list.append(temp_dict)
        context['friends'] = friend_list
        return render(request, 'app/my_page_friend.html', context)
    elif menu == "lecture":
        return render(request, 'app/my_page_lecture.html', {})

    elif menu == "save":
        user_name = request.POST.get("user_name")
        nickname = request.POST.get("nickname")

        this_user = request.user
        user = User.objects.filter(username=this_user).first()
        user.first_name = nickname
        user.last_name = user_name
        user.save()
        return HttpResponse("OK")
    return render(request, 'app/my_page_info.html', {})


def my_page_option(request, option):
    if option == "save":
        user_name = request.POST.get("user_name")
        nickname = request.POST.get("nickname")

        this_user = request.user
        this_user.first_name = nickname
        this_user.last_name = user_name
        this_user.save()

        user = User.objects.filter(user_id=this_user).first()
        user.first_name = nickname
        user.last_name = user_name

        # user.save()

    return HttpResponse("OK")
