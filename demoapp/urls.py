from django.urls import path
from demoapp import views

urlpatterns = [

    path('', views.BookList.as_view()),
    path('<int:pk>/', views.BookDetail.as_view()),
    path('webEx', views.home, name='home'),
]
