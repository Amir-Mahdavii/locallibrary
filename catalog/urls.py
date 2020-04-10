from django.urls import include, path
from . import views

app_name='catalog'

urlpatterns = [
path('', views.index.as_view(), name='index'),

]


#path('books/', views.BookListView.as_view(), name='books'),
#path('book/(?P<pk>\d+)/', views.BookDetailView.as_view(), name='book-detail'),



#re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


#re_path(r'^books/$', views.BookListView.as_view(), name='books'),
#re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
