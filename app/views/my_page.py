from django.shortcuts import render


def my_page(request, menu):
    if menu == "info":
        return render(request, 'app/my_page_info.html', {})
    elif menu == "friend":
        return render(request, 'app/my_page_friend.html', {})
    elif menu == "lecture":
        return render(request, 'app/my_page_lecture.html', {})
    return render(request, 'app/my_page_info.html', {})
