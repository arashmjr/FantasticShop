from django.db.models.manager import Manager
from Src.Domain.models.CartDomainModel import CartDomainModel


class CartRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: CartDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_user_id(self, user_id: int):
        result = self.collection.objects.get(user_id=user_id)
        return result

    def find_record_by_email(self, email: str):
        return self.collection.objects.get(email=email)

    def find_record_by_email_signup(self, email: str):
        return self.collection.objects.filter(email=email)

    def get_all(self):
        items = self.collection.objects.filter()
        return items

    def remove_record(self, cart_id:  int):
        return self.collection.objects.filter(cart_id=cart_id).delete()

    def remove_all(self):
        delete_all = self.collection.objects.all().delete()
        return delete_all
