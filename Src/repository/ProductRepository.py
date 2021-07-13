from django.db.models.manager import Manager
from Src.Domain.models.ProductDomainModel import ProductDomainModel


class ProductRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection

    def insert(self, model: ProductDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_user_id(self, user_id: int):
        result = self.collection.objects.filter(user_id=user_id)
        return result

    def find_record_by_product_id(self, product_id: int):
        return self.collection.objects.get(product_id=product_id)

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

    def remove_record(self, user_id:  int):
        return self.collection.objects.filter(user_id=user_id).delete()

    def remove_all(self):
        delete_all = self.collection.all().delete()
        return delete_all

    def update_record_by_product_id(self, product_id: int):
        items = self.collection.objects.filter(product_id=product_id)
        for item in items:
            item.quantity = item.quantity - 1
            item.save()
        return
