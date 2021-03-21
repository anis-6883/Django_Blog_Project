from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    author       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    title        = models.CharField(max_length=264, verbose_name='Put a title')
    slug         = models.SlugField(max_length=264, unique=True)
    content      = models.TextField(verbose_name="What's on your mind?")
    blog_image   = models.ImageField(upload_to='blog_images', verbose_name='Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']

class Comment(models.Model):
    blog         = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment      = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:30] + "..."

    class Meta:
        ordering = ['-comment_date']
        

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_user')

    def __str__(self):
        return self.user.username + " Likes " + self.blog.title


