# encoding: utf-8
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import TeacherTrainingForm

def index(request):
    if request.method == 'POST':
        form = TeacherTrainingForm(request.POST)
        if form.is_valid():
            # process form here
	    first_name = form.cleaned_data['first_name']
	    if (len(first_name) < 3):
	        messages.error(request, _("Your first name is too short"))
	    else:
                messages.success(request, _("Thank you for submitting your form"))
            return render(request, 'hello_world/index.html', {'form': form})
        else:
            messages.success(request, _("There was an error while submitting your form"))
    else:
        form = TeacherTrainingForm()

    return render(request, 'hello_world/index.html', {'form': form})

