from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from app.models import *




def lecture_all(request):
    return render(request, 'app/lecture_all.html', {})

class LectureAdd(View):  # 강좌 개설
    def get(self, request):
        category_list = Category.objects.all()

        for category in category_list:
            temp_dict = dict()
            temp_dict['category_id'] = category.id
            temp_dict['category_name'] = category.category_name
        context = {}
        context['category_list'] = category_list
        return render(request, 'app/lecture_add.html', context)

    def post(self, request):
        data = request.POST
        lecture_select = data['lecture_select']
        lecture_name = data['lecture_name']
        lecture_sum = data['lecture_sum']
        lecture_min_pnum = data['lecture_min_pnum']
        lecture_max_pnum = data['lecture_max_pnum']
        lecture_place = data['lecture_place']
        monday_button = data['monday_button']
        tuesday_button = data['tuesday_button']
        wednesday_button = data['wednesday_button']
        thursday_button = data['thursday_button']
        friday_button = data['friday_button']
        saturday_button = data['saturday_button']
        sunday_button = data['sunday_button']
        lecture_start_time = data['lecture_start_time']
        lecture_finish_time = data['lecture_finish_time']
        lecture_describe = data['lecture_describe']


        return HttpResponseRedirect('/app/lecture/all')