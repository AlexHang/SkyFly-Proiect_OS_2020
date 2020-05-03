from django.urls import path
from . import views


urlpatterns = [
    path('/flights', views.showFlights, name='Flights'),
    path('/offers',views.showOffers, name='Offers'),
    path('/getFlights', views.getFlights, name='getFlights'),    #http://127.0.0.1:8000/SkyFly/getFlights
    path('/getOffers', views.getOffers, name='getOffers'),
    path('/getMeetings', views.getMeetings, name='getMeetings'),
    path('/getClients', views.getClients, name='getClients'),
    path('/getEmployees', views.getEmployees, name='getEmployees'),
    path('/addFlight', views.addFlight, name='addFlight'),
    path('/addOffer',views.addOffer, name='addOffer'),
    path('/addMeeting',views.addMeeting, name='addMeeting'),
    path('/addCompany',views.addCompany, name='addCompany'),
    path('/addMeeting',views.addPerson, name='addMeeting'),
    path('/addEmployee',views.addEmployee, name='addEmployee'),

]