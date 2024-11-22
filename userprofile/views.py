import os
import re
from django.conf import settings
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from accounts.models import User
from userprofile.models import Profile


class TimelineView(DetailView):
    model = User
    template_name = "profile/user-profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"
    object = None

    def get_object(self, queryset=None):
        return self.model.objects.select_related('profile').prefetch_related("posts").get(username=self.kwargs.get(self.slug_url_kwarg))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ProfileEditView(UpdateView):
    model = Profile
    template_name = "profile/edit-my-profile.html"
    context_object_name = "profile"
    object = None
    fields = "__all__"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def delete_unwanted_images(self):
        media_path = os.path.join(settings.MEDIA_ROOT, 'avatars')
        if os.path.exists(media_path):
            for filename in os.listdir(media_path):
                if filename.endswith('.jpg') and not re.match(r'^\d{4}-\d{2}-\d{2}', filename):
                    if filename not in ['cover.png', 'guest.png']:
                        file_path = os.path.join(media_path, filename)
                        if os.path.exists(file_path):
                            print(f"Deleting unwanted image: {file_path}")
                            os.remove(file_path)
                        else:
                            print(f"File not found: {file_path}")

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile

        if first_name := request.POST.get('first_name'):
            user.first_name = first_name
        if last_name := request.POST.get('last_name'):
            user.last_name = last_name
        if about := request.POST.get('about'):
            user.about = about
        if gender := request.POST.get('gender'):
            user.gender = gender

        user.save()

        if country := request.POST.get('country'):
            profile.country = country
        if city := request.POST.get('city'):
            profile.city = city
        if phone := request.POST.get('phone'):
            profile.phone = phone

        if profile_image := request.FILES.get('profile_image'):
            try:
                if not profile_image.name.endswith(('jpg', 'jpeg', 'png', 'gif')):
                    raise ValidationError("Only image files (jpg, jpeg, png, gif) are allowed.")
                
                if profile.profile_image:
                    old_image_path = os.path.join(settings.MEDIA_ROOT, str(profile.profile_image))
                    if os.path.exists(old_image_path):
                        print(f"Deleting old image: {old_image_path}")
                        os.remove(old_image_path)
                    else:
                        print(f"Old image not found: {old_image_path}")

                profile.profile_image = profile_image
                print(f"New image uploaded: {profile_image.name}")
                self.delete_unwanted_images()

            except ValidationError as e:
                return redirect(reverse_lazy('profile:edit-profile') + f"?error={e}")
        profile.save()
        print(f"Profile saved with image: {profile.profile_image}") 

        return redirect(reverse_lazy('profile:edit-profile'))
    
    
