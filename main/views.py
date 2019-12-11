from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .forms import MyUserCreationForm


@csrf_exempt
@api_view(['POST'])
def user_register(request):
    form = MyUserCreationForm(request.POST)
    if form.is_valid():
        this_user, this_token = form.save()
        return JsonResponse({
            'username': request.POST['username'],
            'password': request.POST['password1'],
            'token': this_token.key
        }, status=201)
    return JsonResponse({
        'error': form.errors
    }, status=409)
