
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.imgupload,name='imgupload'),
    path('imgProcessing',views.imgProcessing,name='imgProcessing')

]
