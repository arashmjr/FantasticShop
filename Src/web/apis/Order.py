from Src.services.Manager.AuthorizationManager import login_required
from Src.services.core.ServiceProvider import ServiceProvider
from Src.web.dtos.BaseResponse import BaseResponse, BaseError
from Src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.handlers.wsgi import WSGIRequest


class Order:

    @csrf_exempt
    @login_required
    def checkout(self, request: WSGIRequest):

        try:
            service = ServiceProvider().make_order_service()
            service.checkout(request)
            response = BaseResponse({}, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

        except ValueError:
            response = BaseError(MessageIds.ERROR_BAD_JSON)
            return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)