from Src.services.core.ServiceProvider import ServiceProvider
from Src.web.dtos.BaseResponse import BaseResponse, BaseError
from Src.web.utils.Localizations import MessageIds
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# from flask import request
# from seviceLayer.core.ServiceProvider import ServiceProvider
# from flask import jsonify
# from flask_api import status
import jwt
# from seviceLayer.Managers.AuthorizationManager import AuthorizationManager


@csrf_exempt
def sign_up_user(request):
    json_data = json.loads(request.body)
    # json_data = request.POST.get()
    try:
        service = ServiceProvider().make_signup_user_service()
        token = service.sign_up_user(json_data)
        response = BaseResponse({"access token": token}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False)


    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=400)



