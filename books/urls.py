from django.urls import path, include
from .views import BookListApiView, BookDetailApiView, BookDeleteApiView,BookUpdateView


urlpatterns = [
    path('', BookListApiView.as_view(), name='booklistapi'),
    path('<int:pk>',BookDetailApiView.as_view(),name='bookdetailapi'),
    path('<int:pk>',BookDeleteApiView.as_view(),name='bookdeleteapi'),
    path('<int:pk>',BookUpdateView.as_view(),name='bookupdateapi'),
]
