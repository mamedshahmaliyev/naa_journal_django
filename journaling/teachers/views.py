from django.shortcuts import render
from django.http import HttpResponse

from .models import Teacher
from django.db.models import Q
from django.shortcuts import get_object_or_404

def index(request):
    # incident = get_object_or_404(Incident, pk=incident_id)

    teachers = Teacher.objects.order_by('name')

    nameFilter = request.GET.get('name')

    if nameFilter:
       teachers = teachers.filter(Q(name__icontains=nameFilter))

    context = {
        'teachers': teachers,
        'page_title': "Müəllimlər",
    }
    return render(request, 'teachers/index.html', context)

def view(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    context = {
        'teacher': teacher,
        'page_title': teacher.name + ' ' + teacher.surname,
    }
    return render(request, 'teachers/view.html', context)

def edit(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    notification = ''
    if request.method == 'POST':
        teacher.name = request.POST.get('name') 
        teacher.surname = request.POST.get('surname') 
        teacher.patronymic = request.POST.get('patronymic')
        teacher.save() 
        notification = 'Müəllim uğurla redaktə edildi.'

    context = {
        'teacher': teacher,
        'notification': notification,
        'page_title': teacher.name + ' ' + teacher.surname,
    }
    return render(request, 'teachers/edit.html', context)

def add(request):
    teacher = Teacher()

    notification = ''
    if request.method == 'POST':
        teacher.name = request.POST.get('name') 
        teacher.surname = request.POST.get('surname') 
        teacher.patronymic = request.POST.get('patronymic')
        teacher.save() 
        notification = 'Müəllim uğurla əlavə edildi.'

    context = {
        'notification': notification,
        'page_title': 'Müəllim əlavə et',
    }
    return render(request, 'teachers/add.html', context)
