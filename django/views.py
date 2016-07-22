from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader, RequestContext
from net_system.models import NetworkDevice


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def test(request):
    c = RequestContext(request, {})
    t = loader.get_template("./test.html")
    page_body_id = 'blog'
    c.update({'page_body_id': page_body_id})

    device_names = []
    my_devices = NetworkDevice.objects.all()
    device_names = [a_device.device_name for a_device in my_devices]
    c.update({'device_names': device_names})

    if request.method == 'GET':
        return HttpResponse(t.render(c))

