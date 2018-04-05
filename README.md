# Django Language Demo
This app is a simple demo of Django's multi-language support capabilities using forms and templates. 

This app was created using Python 2.7.14 and Django 1.11.11

## App structure
The app follows a typical Django app structure. There is one main difference, however. The locale folder is the location where the translation files are stored. 

```
├── hello_world
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── hello_world
│   │       └── index.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── locale
│   ├── es
│   │   └── LC_MESSAGES
│   │       ├── django.mo
│   │       └── django.po
│   └── zh
│       └── LC_MESSAGES
│           ├── django.mo
│           └── django.po
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
``` 

## Requirements
In order to use Django's translation capabilities, it is necessary to have a couple of things set up in the settings.py file. 

Have USE_I18N = True and include django.middleware.locale.LocaleMiddleware in MIDLEWARE. Because of the way Django handles middlewares, LocaleMiddleware must be after django.contrib.sessions.middleware.SessionMiddleware and before django.middleware.common.CommonMiddleware. Finally, add

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale/'),
]

and the languages your application will support

LANGUAGES = [
    ('zh-hans', ('Chinese')),
    ('en'', ('English')),
    ('es', ('Spanish')),
]

For a list of languages supported by Django and their codes see https://github.com/django/django/blob/master/django/conf/locale/__init__.py

## Specifying translation strings
### Views
To specify a string marked for translation, use the function ugettext(). For example, in views.py do
from django.utils.translation import ugettext as _
Suppose we want to translate "Hello World". We would simply have to wrap "Hello World" in _(). For example:
from django.utils.translation import ugettext as _
from django.http import HttpResponse

def my_view(request):
    output = _("Hello World.")
    return HttpResponse(output)

This applies to any content within a view, including messages.
### Forms and models
Forms and models use a similar logic but use ugettext_lazy(). For example:
from django import forms
from django.utils.translation import ugettext_lazy as _

class TeacherTrainingForm(forms.Form):
    first_name = forms.CharField(label=_("First name"), max_length=100)

### Templates
To use translations in templates insert {% load i18n %} at the beginning of each template file. Then wrap strings to be translated with {% trans ... %}. For example:
 
{% load i18n %} 

<h1>{% trans "Hello World" %}</h1>

<p>{% trans "Welcome to my site." %}</p>

## Make translation files
Once you have done the initial setup and marked strings for translation, create the translation message files by running django-admin makemessages -l ln for each language, where ln is the locale name for the language. For example, to create the message file for Chinese (zh) run django-admin makemessages -l zh. This command creates a file with a .po extension in locale/ln/LC_MESSAGES/django.po . 
To add a new translation, open the django.po file and add the corresponding translation for each string. For example:
msgid "Hello World"
msgstr "你好, 世界从模"

The next step is to compile the translation files by running django-admin compilemessages.


## Language prefix in URL patterns
So far, Django uses the user's browser preferences to set the display language. Django provides a tool that adds a language prefix in URLs in order to specify the language. 

Begin by importing i18n_patterns to your site's urls.py
from django.conf.urls.i18n import i18n_patterns

Then add url(r'^i18n/', include('django.conf.urls.i18n')) to your urlpatterns.
urlpatterns = 
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

Finally, use the i18n_patterns function to add your previous url patterns.
urlpatterns += i18n_patterns(
    url(r'^hello_world/', include('hello_world.urls')),
    url(r'^admin/', admin.site.urls),
)

## Toggling between translations
Django comes with the set_language view that allows users to explicitly set a language preference. This is activated by including url(r'^i18n/', include('django.conf.urls.i18n')), in the URLconf, which was done in the previous step. The view is to be called with a POST method, the language being sent in the request.

An example form is included in the template. 

