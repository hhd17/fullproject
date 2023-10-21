from django.urls import path
from .views import home, success, fibonacci, edit_book, delete_book

urlpatterns = [
    path('', home, name='home'),
    path('success/<int:book_id>/', success, name='success'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
    path('fibonacci/', fibonacci, name='fibonacci'),
]
