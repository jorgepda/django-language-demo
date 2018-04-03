from django import forms
from django.utils.translation import ugettext_lazy as _

class TeacherTrainingForm(forms.Form):
    first_name = forms.CharField(label=_("First name"), max_length=100, required=False)
    last_name = forms.CharField(label=_("Last name"), max_length=100, required=False)
    email = forms.EmailField(label=_("Email address"), required=False)
    school_name = forms.CharField(label=_("School name"), max_length=250, required=False)
    school_district = forms.CharField(label=_("School district"), max_length=250, required=False)
    school_choices = (("public", _("Public School")),("private", _("Private or Charter School")),("other", _("Other")),)
    school_type = forms.ChoiceField(label=_("School type"), choices=school_choices)
