from django.db.models.manager import Manager
from Src.Domain.models.CartProductDomainModel import CartProductDomainModel


class CartProductRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: CartProductDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_user_id(self, user_id: int):
        result = self.collection.objects.filter(user_id=user_id)
        return result

    def find_record_by_product_id(self, product_id: int):
        return self.collection.objects.get(product_id=product_id)

    def find_record_by_email(self, email: str):
        return self.collection.objects.get(email=email)

    def find_records_by_cart_id(self, cart_id: int):
        return self.collection.objects.filter(cart_id=cart_id)

    def get_all(self):
        arr = []
        items = self.collection.objects.filter()
        print(items)
        for item in items:
            arr.append(item)
        return arr

    def remove_record(self, user_id:  int):
        return self.collection.objects.filter(user_id=user_id).delete()

    def remove_all(self):
        delete_all = self.collection.all().delete()
        return delete_all

