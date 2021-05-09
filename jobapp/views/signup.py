from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from jobapp.forms import SignForm
from jobapp.models import UserInfo
from django.contrib.auth.hashers import make_password
from django.contrib import messages


class SignView(View):
    def get(self, request):
        if not 'myemail' in request.session:
            fm = SignForm()
            return render(request, 'signup.html', {'form': fm})
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        fm = SignForm(request.POST,  request.FILES)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            gender = fm.cleaned_data['gender']
            address = fm.cleaned_data['address']
            password = fm.cleaned_data['password']
            re_password = fm.cleaned_data['re_password']

            contact = UserInfo(name=name, email=email, gender=gender,
                               address=address, password=password, re_password=re_password)
            contact.password = make_password(contact.password)
            contact.re_password = make_password(contact.re_password)
            contact.save()
            messages.success(request, 'Successfully Added')

        return render(request, 'signup.html', {'form': fm})
