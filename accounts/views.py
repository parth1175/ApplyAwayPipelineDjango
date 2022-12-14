from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from django.contrib.auth.models import User, auth
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect("/")
#         else:
#             messages.info(request, 'Invalid Credentials')
#             return redirect('login')

#     else:
#         return render(request, 'Login/login.html')

# def register(request):

#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Taken')
#                 return redirect('register')
#             else:
#                 user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email,password=password1)
#                 user.save();
#                 messages.info(request, 'User Created')

#         else:
#             messages.info(request, 'Passwords Not Matching')
#             return redirect('register')
#         return redirect('/')

#     else:
#         return render(request, 'Register/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')