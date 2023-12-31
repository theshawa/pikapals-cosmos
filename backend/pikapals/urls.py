from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("port/", views.port_endpoint, name="port_endpoint"),
    path("service_provider/", views.service_provider_endpoint, name="service_provider_endpoint"),
    path("voyage/", views.voyage_endpoint, name="voyage_endpoint"),
    path("book_seat/", views.book_seat_endpoint, name="book_seat_endpoint"),
]
