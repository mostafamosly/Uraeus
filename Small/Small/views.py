from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

class Home(TemplateView):
    template_name = "index.html"

class Pricing(TemplateView):
    template_name = "pricing.html"

class Services(TemplateView):
    template_name = "services.html"

class About(TemplateView):
    template_name = "about.html"


@login_required
def Profile(request):
    return render(request, 'registration/profile.html')


@login_required
def profile(request):
    user_profile = request.user.get_profile()
    url = user_profile.url
