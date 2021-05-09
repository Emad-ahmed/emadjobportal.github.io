from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views import View
from jobapp.forms import SignForm
from jobapp.models import UserInfo
from django.contrib.auth.hashers import check_password
from django.contrib import messages


class LoginView(View):
    def get(self, request):
        if not 'myemail' in request.session:
            return render(request, 'login.html')
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = UserInfo.objects.get(email=email)

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['myemail'] = email
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Email Or Password Invalid")

        else:
            return HttpResponse("Email Or Password Invalid")

        return render(request, 'login.html')


def logout(request):
    if 'myemail' in request.session:
        request.session.flush()
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/login')
