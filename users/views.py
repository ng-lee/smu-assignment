from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from . import models, mixins


class ProfileView(DetailView):

    model = models.User
    context_object_name = "user_obj"
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ob = context["object"]
        context["reviews"] = ob.reviews.all().order_by("-created")
        return context


""" 
class FavsView(View):
    pass
 """


def follow(request, pk):
    target_user = models.User.objects.get(pk=pk)

    if request.method == "POST":
        request.user.followings.add(target_user)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def unfollow(request, pk):
    target_user = models.User.objects.get(pk=pk)

    if request.method == "POST":
        request.user.followings.remove(target_user)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class FollowersView(mixins.LoggedInOnlyView, DetailView):

    model = models.User
    context_object_name = "user_obj"
    template_name = "users/followers.html"


class FollowingsView(mixins.LoggedInOnlyView, DetailView):

    model = models.User
    context_object_name = "user_obj"
    template_name = "users/followings.html"
