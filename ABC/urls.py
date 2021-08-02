from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlist/', views.studentlist.as_view()),
    path('studentlist/<int:pk>/', views.studentlist.as_view()),
]
