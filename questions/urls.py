from django.urls import path
from . import views

urlpatterns = [
    path('ask/', views.ask_view, name='ask'),
    path('', views.index_view, name='index'),
    path('question/<int:question_id>/', views.question_view, name='question'),
    path('tag/<str:tag_name>/', views.tag_view, name='tag'),
    path('hot/', views.hot_view, name='hot'),
]