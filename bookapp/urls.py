

from django.urls import path
from . import views

urlpatterns=[
    path("create-book/",views.createBook,name='createbook'),

    path("author/",views.Create_Author,name='author'),

    path('',views.listBook,name='booklist'),

    path('detailsview/<int:book_id>/',views.detailsView,name='details'),

    path('updateview/<int:book_id>/',views.updateBook,name='update'),

    path('deleteview/<int:book_id>/',views.deleteView,name='delete'),

    path('index/',views.index,name='index'),

    path('deleteAuthorView/<int:book_id>/',views.deleteAuthorView,name='deleteAuthorView'),
    path('updateAuthor/<int:book_id>/',views.updateAuthor,name="updateAuthor"),
    path('search/',views.Search_Book,name='search')



]

