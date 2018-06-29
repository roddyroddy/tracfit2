from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index), #this is for display
    url(r'admin$', views.admin),
    url(r'adminlogin$', views.adminlogin),
    url(r'adminloginpage$', views.adminloginpage),
    url(r'createwod$', views.createwod),
    url(r'addscores$', views.addscore),
    url(r'student$', views.student)
]                            
