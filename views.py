from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog/blog_form.html', {'form': form})

def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_list'))
        else:
            return render(request, 'blog/create.html', {'form': form})
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})

# def create_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('blog_list')  # Redirect to a blog list view after saving
#             except IntegrityError as e:
#                 return render(request, 'blog/create.html', {
#                     'form': form,
#                     'error_message': 'There was an error saving your blog. Please ensure all fields are filled out correctly and try again.'
#                 })
#     else:
#         form = BlogForm()
#     return render(request, 'blog/create.html', {'form': form})



