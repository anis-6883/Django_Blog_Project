from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Blog, Comment, Like
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
    UpdateView
    )
import uuid
from .forms import CommentForm

class BlogList(ListView):
    model               = Blog
    context_object_name = 'blogs'
    template_name       = 'App_Blog/blog_list.html'
    paginate_by         = 2
    # queryset            = Blog.objects.order_by('-publish_date')
  

class CreateBlog(LoginRequiredMixin, CreateView):
    model         = Blog
    template_name = 'App_Blog/blog_create.html'
    fields        = ['title', 'content', 'blog_image']

    def form_valid(self, form):
        blog_obj        = form.save(commit=False)
        blog_obj.author = self.request.user
        title           = blog_obj.title
        blog_obj.slug   = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:blog-home'))

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = CommentForm(request.POST or None)
    already_liked = Like.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.blog = blog
        comment.save()
        messages.success(request, 'Your comment post successfully...🚀')
        return HttpResponseRedirect(reverse('App_Blog:blog-details', kwargs={'slug':slug}))

    context = {
        'blog' : blog,
        'form' : form,
        'liked': liked
    }
    return render(request, 'App_Blog/blog_details.html', context)


@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post = Like(blog=blog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Blog:blog-details', kwargs={'slug': blog.slug})) 


@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('App_Blog:blog-details', kwargs={'slug': blog.slug}))



class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'App_Blog/my_blogs.html'


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model  = Blog
    fields = ['title', 'content', 'blog_image']
    template_name = 'App_Blog/blog_edit.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:blog-details', kwargs={'slug' : self.object.slug}) #not reverse till update


def blog_delete(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    messages.warning(request, 'Your Blog Deleted Successfully!')
    return HttpResponseRedirect(reverse('App_Blog:my-blogs'))


def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    slug = comment.blog.slug
    comment.delete()
    messages.warning(request, 'Your Comment  Deleted Successfully!')
    return HttpResponseRedirect(reverse('App_Blog:blog-details', kwargs={'slug': slug}))


