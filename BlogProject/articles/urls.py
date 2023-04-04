from django.urls import path, include
from . import views

#Linking the specified path to a function in views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('search/', views.search.as_view(), name='search_results'),
    path('dashboard/',views.dashboard),
    path('questions/',views.questions),
    path('discussion/<int:question_id>/',views.discussion),
    path('upvote/<int:answer_id>/',views.upvote),
    path('delete_ques/<int:question_id>/', views.delete_ques),
    path('delete_ans/<int:answer_id>/', views.delete_ans),
]