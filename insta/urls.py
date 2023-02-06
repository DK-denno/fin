from django.urls import re_path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    re_path(r'^$',views.index,name="index"),
    re_path(r'auth/',include('django.contrib.auth.urls')),
    re_path(r'auth/',include('django_registration.backends.activation.urls')),
    re_path(r'^sign/$',views.signup, name='signup'),
    re_path(r'^profile/$',views.profile, name='profile'),
    re_path(r'^prof/(\d+)',views.profiles,name='prof'),
    re_path(r'^search',views.search_results,name='search_results'),
    re_path(r'^one/(\d+)',views.classes,name="classes"),
    re_path(r'^students/(\d+)',views.students,name="students")

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)