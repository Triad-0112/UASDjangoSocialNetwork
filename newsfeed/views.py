from django.shortcuts import render

# Create your views here.
import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer # type: ignore
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from friends.models import CustomNotification
from friends.serializers import NotificationSerializer
from .forms import PostCreateForm
from .models import *



class PostCreateView(CreateView):
    model = Post
    http_method_names = ['post']
    form_class = PostCreateForm
    template_name = 'home.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print(form.errors)
        return redirect(reverse_lazy('core:home'))

    def post(self, *args, **kwargs):
        form = self.get_form()
        self.object = None
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def create_comment(request, post_id=None):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        comment = post.comments.create(user=request.user, content=request.POST.get('content'))
        notification = CustomNotification.objects.create(type="comment", recipient=post.user, actor=request.user, verb="commented on your post")
        channel_layer = get_channel_layer()
        channel = "comment_like_notifications_{}".format(post.user.username)
        print(json.dumps(NotificationSerializer(notification).data))
        async_to_sync(channel_layer.group_send)(
            channel, {
                "type": "notify",
                "command": "new_like_comment_notification",
                "notification": json.dumps(NotificationSerializer(notification).data)
            }
        )
        return redirect(reverse_lazy('core:home'))
    else:
        return redirect(reverse_lazy('core:home'))


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        post.dislikes.remove(request.user)  
    print(f"Post {post_id} likes: {post.likes_count}, dislikes: {post.dislikes_count}")
    return JsonResponse({'likes_count': post.likes_count, 'dislikes_count': post.dislikes_count})

def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.dislikes.all():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        post.likes.remove(request.user) 
    return JsonResponse({'likes_count': post.likes_count, 'dislikes_count': post.dislikes_count})