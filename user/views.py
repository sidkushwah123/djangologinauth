from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from .forms import my



def index(request):
    return render(request,'user/index.html')

def logout_user(request):
    logout(request)
    return redirect('index')

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username,password=password)
#             login(request,user)
#             return redirect('index')

#     else:
#         form = UserCreationForm()

#     context = {'form':form}
#     return render(request,'registration/register.html',context)

class registerclass(View):
    
    def get(self,request):
        form = my()
        context = {'form':form}
        return render(request,'registration/register.html',context)
        

    def post(self,request):
        form = my(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')

        context = {'form':form}
        return render(request,'registration/register.html',context)
        







