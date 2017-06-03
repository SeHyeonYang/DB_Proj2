from django.shortcuts import render


def my_page(request, menu):
    if menu == "info":
        user = request.user
        context = dict()
        context['my_info'] = user
        return render(request, 'app/my_page_info.html', context)
    elif menu == "friend":
        return render(request, 'app/my_page_friend.html', {})
    elif menu == "lecture":
        return render(request, 'app/my_page_lecture.html', {})
    return render(request, 'app/my_page_info.html', {})
