from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.db.models import Count
from .authentify import *
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import F
from django.contrib.auth.decorators import user_passes_test


def my_page(request, menu):
    user = request.user
    context = dict()
    context['my_info'] = user
    context['is_teacher'] = is_teacher(user)
    if menu == "info":
        return render(request, 'app/my_page_info.html', context)
    elif menu == "stati":
        teacher = Teacher.objects.filter(user_id=user.id).first()
        times = Teach.objects.filter(teacher_id=teacher).count()

        student_count = Take.objects.filter(section_id__teach__teacher_id=teacher).count()
        print(student_count)

        students = Take.objects.filter(section_id__teach__teacher_id=teacher).values('user_id__username').distinct()
        print("내 수업 들은 애들")
        print(students.query)
        students_list = []
        for s in students:
            students_list.append(s['user_id__username'])
        print(students_list)

        top_people_list = []
        top_people = Take.objects.filter(section_id__teach__teacher_id=teacher).values('user_id__username').annotate(user_take_count=Count('user_id')).order_by('-user_take_count')
        print("top_people")
        print(top_people.query)
        for p in top_people:
            temp_dict = dict()
            temp_dict['username'] = p['user_id__username']
            temp_dict['count'] = p['user_take_count']
            top_people_list.append(temp_dict)

        temp = str(times) + "/" + str(student_count)
        print(str(temp))

        context = {}
        context['times'] = times
        context['student_count'] = student_count
        context['students_list'] = students_list
        context['top_person'] = top_people_list[0]
        context['top_people_list'] = top_people_list
        return render(request, 'app/my_page_stati.html', context)
    elif menu == "history":
        print("history")
        user = request.user
        section_history = Section.objects.filter(teach__teacher_id__user_id=user, end_date__lt=datetime.today())
        print(section_history.query)
        section_list = []
        for section in section_history:
            temp_dict = dict()
            temp_dict['course_title'] = section.course_id.title
            temp_dict['section_id'] = section.id
            temp_dict['start_date'] = section.start_date
            temp_dict['end_date'] = section.end_date
            temp_dict['times'] = section.times
            temp_dict['price'] = section.price
            temp_dict['start_time'] = section.start_time
            temp_dict['end_time'] = section.end_time
            temp_dict['location'] = section.location
            student_count = Take.objects.filter(section_id=section).count()
            temp_dict['student_count'] = student_count
            section_list.append(temp_dict)
        context['section_history_list'] = section_list
        return render(request, 'app/my_page_course_history.html', context)
    elif menu == "ongoing":
        user = request.user
        section_ongoing = Section.objects.filter(teach__teacher_id__user_id=user, end_date__gte=datetime.today())
        print("ongoing")
        print(section_ongoing.query)
        section_list = []
        for section in section_ongoing:
            temp_dict = dict()
            temp_dict['course_title'] = section.course_id.title
            temp_dict['section_id'] = section.id
            temp_dict['start_date'] = section.start_date
            temp_dict['end_date'] = section.end_date
            temp_dict['times'] = section.times
            temp_dict['price'] = section.price
            temp_dict['start_time'] = section.start_time
            temp_dict['end_time'] = section.end_time
            temp_dict['location'] = section.location
            student_count = Take.objects.filter(section_id=section).count()
            temp_dict['student_count'] = student_count
            section_list.append(temp_dict)
        context['section_ongoing_list'] = section_list
        return render(request, 'app/my_page_section_ongoing.html', context)
    elif menu == "friend":
        if request.method == "POST":
            action = request.GET.get('action')
            if action == "search":
                option = request.GET.get('option')[:-1]
                if option == "findbyall":
                    data = request.POST.get("search-friend-by-all")
                    friend_search_list = User.objects.filter(Q(username=data) | Q(first_name=data) | Q(last_name=data))
                    print(friend_search_list.query)
                    if friend_search_list.count() != 0:
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
                    print(maybe_friend_search_list.query)
                    if maybe_friend_search_list.count() != 0:
                        search_list_sub = []
                        for a in maybe_friend_search_list:
                            temp_dict = dict()
                            temp_dict['friend_search_id'] = a.username
                            temp_dict['friend_search_name'] = a.last_name
                            temp_dict['friend_search_nickname'] = a.first_name
                            search_list_sub.append(temp_dict)
                        context['friend_search_list_sub'] = search_list_sub
            elif action == "befriend":
                friend_id = request.GET.get('data')[:-1]
                friend = User.objects.filter(username=friend_id).exclude(username=request.user).first()
                is_friend = Friend.objects.filter(sender_id=request.user, receiver_id=friend).count()
                if is_friend == 0:
                    new_relationship = Friend.objects.create(sender_id=user, receiver_id=friend)
                    new_relationship.save()
            elif action == "approve":
                friend_id = request.GET.get('data')[:-1]
                friend = User.objects.filter(username=friend_id)
                Friend.objects.filter(sender_id=friend, receiver_id=request.user).update(approve=True)

        together_friends = Friend.objects.filter(Q(sender_id=user) & Q(approve=True))
        together_friend_list = []
        for friend in together_friends:
            temp_dict = dict()
            temp_dict['friend_id'] = friend.receiver_id
            together_friend_list.append(temp_dict)
        context['together_friend'] = together_friend_list

        only_me_friends = Friend.objects.filter(sender_id=user)
        only_me_friend_list = []
        for friend in only_me_friends:
            temp_dict = dict()
            temp_dict['friend_id'] = friend.receiver_id
            temp_dict['approve'] = friend.approve
            temp_dict['date'] = friend.date
            only_me_friend_list.append(temp_dict)
        context['only_me_friend'] = only_me_friend_list

        only_you_friends = Friend.objects.filter(receiver_id=user)
        only_you_friend_list = []
        for friend in only_you_friends:
            temp_dict = dict()
            temp_dict['friend_id'] = friend.sender_id
            temp_dict['approve'] = friend.approve
            temp_dict['date'] = friend.date
            only_you_friend_list.append(temp_dict)
        context['only_you_friend'] = only_you_friend_list
        return render(request, 'app/my_page_friend.html', context)
    elif menu == "lecture":
        return render(request, 'app/my_page_course_history.html', context)
    elif menu == "take":
        is_friend_take = request.GET.get('friend')
        if is_friend_take is not None:
            friend_id = is_friend_take[:-1]
            friend = User.objects.filter(username=friend_id).first()
            my_take = Take.objects.filter(user_id=friend).all()
            context['friend_id'] = friend_id
        else:
            my_take = Take.objects.filter(user_id=user).all()
        my_take_section_list = []
        for take in my_take:
            temp_dict = dict()
            temp_dict['course_title'] = take.section_id.course_id.title
            temp_dict['section_id'] = take.section_id.id
            temp_dict['start_date'] = take.section_id.start_date
            temp_dict['end_date'] = take.section_id.end_date
            print(take.id)
            my_take_section_list.append(temp_dict)
        context['take'] = my_take_section_list
        return render(request, 'app/my_page_take.html', context)
    elif menu == "save":
        last_name = request.POST.get("user_name")
        first_name = request.POST.get("nickname")

        this_user = request.user
        user = User.objects.filter(username=this_user).first()
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return HttpResponse("OK")
    return render(request, 'app/my_page_info.html', {})


def my_page_option(request, option):
    if option == "save":
        last_name = request.POST.get("user_name")
        first_name = request.POST.get("nickname")

        this_user = request.user
        this_user.first_name = first_name
        this_user.last_name = last_name
        this_user.save()

        user = User.objects.filter(user_id=this_user).first()
        user.first_name = first_name
        user.last_name = last_name

        # user.save()

    return HttpResponse("OK")


