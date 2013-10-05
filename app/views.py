from django.views.generic import TemplateView, View
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return HttpResponse("This is a get view")
