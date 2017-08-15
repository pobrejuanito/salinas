from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about.html',TemplateView.as_view(template_name="pages/about.html")),
    url(r'^our-team.html',TemplateView.as_view(template_name="pages/our-team.html")),
    url(r'^our-staff.html',TemplateView.as_view(template_name="pages/our-staff.html")),
    url(r'^welcome.html',TemplateView.as_view(template_name="pages/welcome.html")),
    url(r'^contact.html',TemplateView.as_view(template_name="pages/contact.html")),
    url(r'^invisalign.html', TemplateView.as_view(template_name="pages/invisalign.html")),
    url(r'^services.html', TemplateView.as_view(template_name="pages/bonding.html")),
    url(r'^bonding.html', TemplateView.as_view(template_name="pages/bonding.html")),
    url(r'^bridges.html', TemplateView.as_view(template_name="pages/bridges.html")),
    url(r'^crowns.html', TemplateView.as_view(template_name="pages/crowns.html")),
    url(r'^dentures.html', TemplateView.as_view(template_name="pages/dentures.html")),
    url(r'^extractions.html', TemplateView.as_view(template_name="pages/extractions.html")),
    url(r'^whitening.html', TemplateView.as_view(template_name="pages/whitening.html")),
    url(r'^implants.html', TemplateView.as_view(template_name="pages/implants.html")),
    url(r'^guards.html', TemplateView.as_view(template_name="pages/guards.html")),
    url(r'^veneers.html', TemplateView.as_view(template_name="pages/veneers.html")),
    url(r'^tmj.html', TemplateView.as_view(template_name="pages/tmj.html")),
    url(r'^braces.html', TemplateView.as_view(template_name="pages/braces.html")),
    url(r'^crown-in-one-appointment.html', TemplateView.as_view(template_name="pages/crown-in-one-appointment.html")),
    url(r'^sendmessage/', views.sendmessage, name='home'),
]
