# encoding: utf-8
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import TeacherTrainingForm

def index(request):
    if request.method == 'POST':
        form = TeacherTrainingForm(request.POST)
        if form.is_valid():
            # process form here
            return HttpResponseRedirect('/thanks/')
    else:
        form = TeacherTrainingForm()

    return render(request, 'hello_world/index.html', {'form': form})

#def get_teacher_training_form(request):
