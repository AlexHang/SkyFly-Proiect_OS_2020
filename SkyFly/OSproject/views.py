from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from OSproject.models import Flight
from OSproject.models import Offer
from OSproject.models import Meeting
from OSproject.models import Client
from OSproject.models import Company
from OSproject.models import Person
from OSproject.models import Employee

from django.core import serializers

def showFlights(request):
    return render(request, 'flights.html', {})
def showOffers(request):
    return render(request, 'offers.html', {})

def getFlights(request):
    dataset = Flight.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def getOffers(request):
    dataset = Offer.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def getMeetings(request):
    dataset = Meeting.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def getClients(request):
    dataset = Client.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def getEmployees(request):
    dataset = Meeting.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def addFlight(request):
    Flight.objects.create(departure = request.GET.get('departure') , landing = request.GET.get('landing') , price = request.GET.get('price'), date = request.GET.get('date'))
    #Flight.objects.filter(landing="Istambul").delete()
    return JsonResponse({"status":"ok"}, safe=False)

def addOffer(request):
    Offer.objects.create(client = request.GET.get('client') , flight = request.GET.get('flight') , discount = request.GET.get('discount'))
    return JsonResponse({"status":"ok"}, safe=False)

def addMeeting(request):
    Meeting.objects.create(date = request.GET.get('date') , hour = request.GET.get('hour') , employees = request.GET.get('employees'))
    return JsonResponse({"status":"ok"}, safe=False)

def addCompany(request):
    Offer.objects.create(email = request.GET.get('email') , phone = request.GET.get('phone') , budget = request.GET.get('budget'), nationality = request.GET.get('nationality'), domainOfActivity = request.GET.get('domainOfActivity') )
    return JsonResponse({"status":"ok"}, safe=False)

def addPerson(request):
    Person.objects.create(email = request.GET.get('email') , phone = request.GET.get('phone') , nationality = request.GET.get('nationality'), age = request.GET.get('age') )
    return JsonResponse({"status":"ok"}, safe=False)

def addEmployee(request):
    Employee.objects.create(firstname = request.GET.get('firstName') , lastName = request.GET.get('lastName') , role = request.GET.get('role'), adress = request.GET.get('adress'), phone = request.GET.get('phone'), availability = request.GET.get('availability') , certifications = request.GET.get('certifications'), contract = request.GET.get('contract') )
    return JsonResponse({"status":"ok"}, safe=False)