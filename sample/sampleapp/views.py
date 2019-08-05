from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
#from django.shortcuts import render
#def hello(request):
  #    return render(request,'sampleapp/hello.html',{'page_title':'Welcome'} )


#ef login(request):
#      return render(request, 'sampleapp/login.html', {'page_title': 'login'})


#def departments(request):
 #     data={
  #          'notes':['CSE','ECE','IT'],
   #         'page_title': 'Departments'
    #  }
     # return render(request, 'sampleapp/departments.html',data)
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'sampleapp/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'sampleapp/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content','contact']
    def form_valid(self,form):
      form.instance.author = self.request.user
      form.save()
      return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','contact']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'sampleapp/about.html', {'title': 'About'})

def sendSimpleEmail(request,emailto):
   res = send_mail("hello paul", "comment tu vas?", "paul@polo.com", [emailto])
   return HttpResponse('%s'%res)