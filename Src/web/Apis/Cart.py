from urllib.request import Request

from Src.services.core.ServiceProvider import ServiceProvider
from Src.web.dtos.BaseResponse import BaseResponse, BaseError
from Src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib.request


class Cart:

    @csrf_exempt
    def add_item(self, request):
        json_data = json.loads(request.body)

        try:
            service = ServiceProvider().make_cart_service()
            service.add_item(json_data, request)
            response = BaseResponse({}, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

        except ValueError:
            response = BaseError(MessageIds.ERROR_BAD_JSON)
            return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def get_items(self, request):

        try:
            service = ServiceProvider().make_cart_service()
            products = service.get_carts()
            response = BaseResponse(products, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

        except ValueError:
            response = BaseError(MessageIds.ERROR_BAD_JSON)
            return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def remove_item(self, request):
        json_data = json.loads(request.body)

        try:
            service = ServiceProvider().make_cart_service()
            products = service.remove_item(json_data)
            response = BaseResponse(products, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

        except ValueError:
            response = BaseError(MessageIds.ERROR_BAD_JSON)
            return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)

