from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import TestModel

# Create your views here.
def home(request):
    modelData = TestModel.objects.all().values()
    context = {
        'modelData':modelData,
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def tailwindSample(request):
    context = {
        'test': 1,
    }
    template = loader.get_template('tailwindsample.html')
    return HttpResponse(template.render(context, request))

def save(request):
    if request.method == 'POST':
        testmodel = TestModel(firstname = request.POST.get('fname'), lastname = request.POST.get('lname'))
        testmodel.save()
        return HttpResponseRedirect('/') 
    else:
        return HttpResponse(print('error'))

def delUser(request):
    if request.method == 'POST':
        if TestModel.objects.filter(id = request.POST.get('id')).exists():
            testmodel = TestModel.objects.get(id = request.POST.get('id'))
            testmodel.delete()
            return HttpResponseRedirect('/') 
        else:
            return HttpResponse(print('error'))
    else:
        return HttpResponse(print('error'))

def update(request):
    if request.method == 'POST':
        if TestModel.objects.filter(id = request.POST.get('id')).exists():
            testmodel = TestModel.objects.get(id = request.POST.get('id'))
            testmodel.firstname = request.POST.get('fname')
            testmodel.lastname = request.POST.get('lname')
            testmodel.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(print(request))
    else:
        return HttpResponse(print('error'))