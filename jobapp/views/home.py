from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from jobapp.models import JobInfo


class HomeView(View):
    def get(self, request):
        myjob = JobInfo.objects.all()
        return render(request, 'home.html', {'job': myjob})
