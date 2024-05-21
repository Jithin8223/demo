from django.urls import path
from.import views
urlpatterns=[
    path('',views.Wp),
    path('add',views.web1,name='add')
]