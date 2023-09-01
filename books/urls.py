from django.urls import path, include
from .views import BookListApiView, book_list_view,BookDetailApiView


urlpatterns = [
    path('', BookListApiView.as_view(), name='booklistapi'),
    path('<int:pk>',BookDetailApiView.as_view(),name='bookdetailapi'),
    path('books', book_list_view)
]
