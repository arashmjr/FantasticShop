from django.db.models.manager import Manager
from Src.Domain.models.ShoppingCartDomainModel import ShoppingCartDomainModel


class ShoppingCartRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: ShoppingCartDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_user_id(self, user_id: int):
        result = self.collection.objects.filter(user_id=user_id)
        return result

    def find_record_by_email(self, email: str):
        return self.collection.objects.get(email=email)

    def find_record_by_email_signup(self, email: str):
        return self.collection.objects.filter(email=email)

    def get_all(self):
        arr = []
        items = self.collection.objects.filter()
        print(items)
        for item in items:
            arr.append(item)
        return arr

    def remove_record(self, shoppingcart_id:  int):
        return self.collection.objects.filter(shoppingCart_id=shoppingcart_id).delete()

    def remove_all(self):
        delete_all = self.collection.all().delete()
        return delete_all
