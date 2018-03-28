# use ugettext in views, ugettext_lazy in forms and models
# encoding: utf-8
from django.utils.translation import ugettext as _
from django.http import HttpResponse


def index(request):
    output = _("Hello world. Welcome to my site.")
    return HttpResponse(output)
