from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('nithin/',nithin,name='nithin'),
    path('jin/',jin,name='jin'),

]