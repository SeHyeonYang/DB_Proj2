from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
        option = request.GET.get('option')
        data = request.GET.get('data')
        if data is not None :
            temp_string = str(option)+"/"+str(data)
            print(temp_string)

        friends = Friend.objects.filter(sender_id=user)
        friend_list = []
        for friend in friends:
            temp_dict = dict()
            temp_dict['friend_id'] = friend.receiver_id
            friend_list.append(temp_dict)

        temp_dict = dict()
        temp_dict['friend_id'] = "test"
        friend_list.append(temp_dict)
        temp_dict = dict()
        temp_dict['friend_id'] = "test2"
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

        #user.save()

    return HttpResponse("OK")
