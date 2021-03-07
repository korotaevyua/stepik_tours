from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound

tours = []


def MainView(request):
    context = {
        "tours": tours
    }
    return render(request, "index.html", context=context)


def TourView(request, id):
    context = {
        "tours": tours
    }
    return render(request, "tour.html", context=context)


def DepartureView(request, departure):
    context = {
        "tours": tours
    }
    return render(request, "departure.html", context=context)


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка 404')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка 500')
