import pdb
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from django.core.mail import send_mail
from validate_email import validate_email
from django.conf import settings

# Create your views here.
def index(request):

    page_data = {}
    if request.method == 'POST':
        message = 'Appointment Request' + "\n"
        message += 'Name: ' + request.POST.get('name') + "\n"
        message += 'Phone: ' + request.POST.get('phone') + "\n"
        message += 'Email: ' + request.POST.get('email') + "\n"
        message += 'Time: ' + request.POST.get('time') + "\n"
        message += 'Message: ' + request.POST.get('message') + "\n\n"
        message += settings.EMAIL_SIGNATURE
        send_mail(settings.EMAIL_APPOINTMENT_SUBJECT, message,  request.POST.get('email'), [settings.EMAIL_TO], fail_silently=False)
        return JsonResponse({})

    page_data.update(csrf(request))
    return render_to_response('home.html', page_data)

def about(request):
    return render_to_response('pages/about.html')
    
def sendmessage(request):

    if request.method == 'POST':
        message = 'Message Details' + "\n"
        message += 'Name: ' + request.POST.get('fullname') + "\n"
        message += 'Phone: ' + request.POST.get('phone') + "\n"
        message += 'Email: ' + request.POST.get('email') + "\n"
        message += 'Message: ' + request.POST.get('message') + "\n\n"
        message += settings.EMAIL_SIGNATURE
        send_mail(settings.EMAIL_CONTACTUS_SUBJECT, message,  request.POST.get('email'), [settings.EMAIL_TO], fail_silently=False)
    return JsonResponse({})

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
