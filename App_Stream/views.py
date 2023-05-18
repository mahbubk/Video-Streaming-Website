from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from App_Stream.forms import VideoForm, CommentForm, SearchForm


# Importing views
from django.views.generic import ListView, DetailView

# Models
from App_Stream.models import Category, Video

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(ListView):
    model = Video
    template_name = 'home.html'


def search_vedio(request):
    # if request.method == 'GET':
    #     form = SearchForm(request.GET)
    #     if form.is_valid():
    #       search = form.cleaned_data['search_vid']
    #       result = Video.objects.filter(title__icontains=search)
    # form = SearchForm(request.GET)
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
          search = request.GET.get('search', '')
          result = Video.objects.filter(title__icontains=search)
          render(request, 'home.html', context={'title':'Home', 'search':search, 'result':result})
    return render(request, 'home.html', context={'title':'Home', 'search':search, 'result':result})



@login_required
def comments(request, video_id):
    item = Video.objects.get(pk=video_id)
    comment_form = CommentForm()
    # if request.method == 'POST':
    #      comment_form = CommentForm(request.POST)
    #      if comment_form.is_valid():
    #         # comment = comment_form
    #         # comment.user = request.user
    #         # comment.item = video_id
    #         comment_form.save()
    if request.method == 'POST':
         comment_form = CommentForm(request.POST)
         if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.video = item
            comment.save()
            return render(request, 'App_Stream/comments.html', context={'video_id':video_id})
    return render(request, 'App_Stream/comments.html', context={'item':item, 'comment_form':comment_form})

# class comments(ListView, LoginRequiredMixin):
#     model = Video
#     template_name = 'App_Stream/comments.html'
