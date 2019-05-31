from django.contrib import admin
from django.urls import path
from Library import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/<int:pk>/',views.author_detail.as_view()),
    path('author/<int:pk>/',views.author_list.as_view()),
    path('books/<int:pk>/',views.book_detail.as_view()),
    path('book/<int:pk>/',views.book_list.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)