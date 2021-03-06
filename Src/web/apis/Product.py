from Src.services.core.ServiceProvider import ServiceProvider
from Src.web.dtos.BaseResponse import BaseResponse, BaseError
from Src.web.utils.Localizations import MessageIds
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Src.services.Manager.AuthorizationManager import is_admin_only
import json


class Product:
    @csrf_exempt
    @is_admin_only
    def add_product(self, request):
        json_data = json.loads(request.body)
        try:
            service = ServiceProvider().make_product_service()
            service.add_product(json_data)
            response = BaseResponse({}, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

        except ValueError:
            response = BaseError(MessageIds.ERROR_BAD_JSON)
            return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def get_products(self, request):
        try:
            service = ServiceProvider().make_product_service()
            products = service.get_products()
            response = BaseResponse(products, True, MessageIds.SUCCESS)
            return JsonResponse(response.serialize(), safe=False, status=status.HTTP_201_CREATED)

        except ValueError:
            response = BaseError(MessageIds.ERROR_BAD_JSON)
            return JsonResponse(response.serialize(), status=status.HTTP_400_BAD_REQUEST)


