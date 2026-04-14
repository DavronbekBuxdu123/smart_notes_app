from django.urls import path
from .views import NoteDetailView,NoteListCreateView,TrashNoteListView,RegisterView
urlpatterns=[
     path('notes/',NoteListCreateView.as_view()),
     path('notes/<int:pk>/',NoteDetailView.as_view()),
     path('notes/trash/',TrashNoteListView.as_view()),
     path('register/',RegisterView.as_view())
]