from Library.models import Author,Book
from Library.serializers import AuthorSerializer,BookSerializer
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics




class author_list(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Author.objects.filter(id=self.kwargs['pk'])
        return queryset



class author_detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    def get_queryset(self, *args, **kwargs):
        queryset = Author.objects.filter(id=self.kwargs['pk'])
        return queryset
    
        



class book_list(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Book.objects.filter(id=self.kwargs['pk'])
        return queryset

   


class book_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

   
    

        

