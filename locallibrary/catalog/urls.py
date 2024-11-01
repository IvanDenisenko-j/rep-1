from django.urls import path
from . import views
from django.urls import re_path as url
from .views import BorrowedBooksListView



urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('borrowed/', BorrowedBooksListView.as_view(), name='borrowed_books'),
    path('create/', views.create_book, name='create_book'),
    path('update/<pk>/', views.update_book, name='update_book'),
    path('delete/', views.delete_book, name='delete_book'),
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]

