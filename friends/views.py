import json

from accounts.models import User
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer # type: ignore
from django.http import JsonResponse
from django.views.generic import ListView

from .serializers import NotificationSerializer
from .models import *


class FindFriendsListView(ListView):
    model = Friend
    context_object_name = 'users'
    template_name = "friends/find-friends.html"

    def get_queryset(self):
        current_user_friends = self.request.user.friends.values('id')
        sent_request = list(Friend.objects.filter(user=self.request.user).values_list('friend_id', flat=True))
        friends = list(Friend.objects.filter(friend=self.request.user, status= 'friend').values_list('user_id', flat=True))
        users = User.objects.exclude(id__in=current_user_friends).exclude(id__in=sent_request).exclude(id=self.request.user.id).exclude(id__in=friends)
        data = []
        for user in users:
            if Friend.objects.filter(user_id=user.id, friend_id=self.request.user.id):
                user.needAccept = True
            else:
                user.needAccept = False
            data.append(user)
        return data


def send_request(request, username=None):
    if username is not None:
        friend_user = User.objects.get(username=username)
        friend = Friend.objects.create(user=request.user, friend=friend_user)
        notification = CustomNotification.objects.create(type="friend", recipient=friend_user, actor=request.user, verb="sent you friend request")
        channel_layer = get_channel_layer()
        channel = "notifications_{}".format(friend_user.username)
        async_to_sync(channel_layer.group_send)(
            channel, {
                "type": "notify",  # method name
                "command": "new_notification",
                "notification": json.dumps(NotificationSerializer(notification).data)
            }
        )
        data = {
            'status': True,
            'message': "Permintaan dikirim.",
        }
        return JsonResponse(data)
    else:
        pass


def accept_request(request, friend=None):
    if friend is not None:
        friend_user = User.objects.get(username=friend)
        current_user = request.user
        f = Friend.objects.filter(user=friend_user, friend=current_user, status='requested')[0]
        f.status = "friend"
        f.save()
        CustomNotification.objects.filter(recipient=current_user, actor=friend_user).delete()
        data = {
            'status': True,
            'message': "Lo udah terima permintaan teman!",
        }
        return JsonResponse(data)
