from django.shortcuts import render
from rest_framework import generics,permissions,filters
from .serializers import NoteSerializer
from .models import Category,Note,Tag
# Create your views here.

class NoteListCreateView(generics.ListCreateAPIView):
      serializer_class=NoteSerializer
      permission_classes=[permissions.AllowAny]
      filter_backends=[filters.SearchFilter,filters.OrderingFilter]
      search_fields=['title','content']

      def get_queryset(self):
            user=self.request.user
            return Note.objects.filter(
                  user=user,
                  is_trashed=False
            )
      def perform_create(self, serializer):
            serializer.save(user=self.request.user)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
      serializer_class=NoteSerializer
      permission_classes=[permissions.AllowAny]

      def get_queryset(self):
            return Note.objects.filter(user=self.request.user)            

class TrashNoteListView(generics.ListAPIView):
      serializer_class=NoteSerializer
      permission_classes=[permissions.AllowAny] 

      def get_queryset(self):
            return Note.objects.filter(user=self.request.user,is_trashed=True)  