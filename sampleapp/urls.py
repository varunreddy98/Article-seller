from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from sampleapp import views
#for more apps from sampleapp2 import views as views1
#urlpatterns = [
  #  url(r'^admin/', admin.site.urls),
   # url(r'hello/',views.hello,name='hello'),
    #url(r'login/', views.login,name='login'),
#url(r'departments/', views.departments,name='departments')
#]
from django.urls import path
from sampleapp.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from sampleapp import views

urlpatterns = [
    path('', PostListView.as_view(), name='sampleapp-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path(r'home/',views.home,name='home'),
    path('about/', views.about, name='sampleapp-about'),
    #url(r'post_form/', views.profile,name='post_form'),
]