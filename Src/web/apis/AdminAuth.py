from Src.services.core.ServiceProvider import ServiceProvider
from Src.web.dtos.BaseResponse import BaseResponse, BaseError
from Src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def sign_up_admin(request):
    json_data = json.loads(request.body)

    try:
        service = ServiceProvider().make_signup_admin_service()
        token = service.sign_up_admin(json_data)
        response = BaseResponse({"access token": token}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def login_admin(request):
    json_data = json.loads(request.body)
    try:
        service = ServiceProvider().make_login_admin_service()
        token = service.login_admin(json_data)
        response = BaseResponse({"access token": token}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)
