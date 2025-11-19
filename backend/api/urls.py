from django.urls import path
from .import views

urlpatterns = [
    path('notes/', views.NoteListCreate.as_view(), name='note_list_create'),
    path('notes/<int:pk>/', views.NoteDeleteView.as_view(), name='note_delete'),
]