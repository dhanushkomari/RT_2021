from django.urls import path
from . import views

app_name = 'RTApp'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('', views.StandardView, name = 'standard'),
    path('std/<str:std_id>/sec', views.SectionView, name= 'single-std'),
    path('sec/<str:sec_id>/sub', views.SubjectView, name= 'single-sec'),
    path('sub/<str:sub_id>/top', views.TopicView, name = 'single-sub'),
    path('top/<str:topic_id>/conf', views.ConfigurationView, name = 'single-top'),

    path('api-data/', views.DataView, name = 'api-data')

]


