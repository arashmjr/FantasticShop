from django.db.models.manager import Manager
from Src.Domain.models.SaveUserDomainModel import SaveUserDomainModel
from Src.Domain.Entities.User import User


class SaveUserRepository:
    collection: Manager

    def __init__(self, collection: Manager):
        self.collection = collection
        # self.objects = User()

    def insert(self, model: SaveUserDomainModel):
        result = self.collection.objects.create(**model.to_dict())
        return result

    def find_record_by_user_id(self, user_id: int):
        result = self.collection.objects.filter(user_id=user_id)
        return result

    def find_record_by_email(self, email: str):
        return self.collection.objects.filter(email=email)

    def get_all(self):
        arr = []
        for x in self.collection.filter():
            arr.append(x)
        return arr

    def remove_record(self, user_id:  int):
        return self.collection.objects.filter(user_id=user_id).delete()

    def remove_all(self):
        delete_all = self.collection.all().delete()
        return delete_all
