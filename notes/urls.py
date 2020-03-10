"""Define url patterns for notes app"""
from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.topics, name='topics'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('topic/create/', views.create_topic, name='create_topic'),
    path('topic/<int:topic_id>/delete', views.delete_topic, name='delete_topic'),
    path('note/<int:topic_id>/create', views.create_note, name='create_note'),
    path('note/edit/<int:note_id>', views.edit_note, name='edit_note'),
    path('note/delete/<int:note_id>', views.delete_note, name='delete_note')
]