from Library.models import Author,Book
from Library.serializers import AuthorSerializer,BookSerializer
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.db.models import Q



class author_list(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            queryset = Author.objects.filter(book__name=query)
            print(queryset)
        
        return queryset



class author_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class book_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            queryset = Book.objects.filter(author__name=query)
        return queryset
    
   


class book_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

        

