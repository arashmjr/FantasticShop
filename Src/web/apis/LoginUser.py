from Src.services.core.ServiceProvider import ServiceProvider
from Src.web.dtos.BaseResponse import BaseResponse, BaseError
from Src.web.utils.Localizations import MessageIds
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import status
import json


@csrf_exempt
def login_user(request):
    json_data = json.loads(request.body)
    try:
        service = ServiceProvider().make_login_user_service()
        token = service.login_user(json_data)
        response = BaseResponse({"access token": token}, True, MessageIds.SUCCESS)
        return JsonResponse(response.serialize(), status=status.HTTP_201_CREATED)

    except ValueError:
        response = BaseError(MessageIds.ERROR_BAD_JSON)
        return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


