from Src.services.Manager.AuthorizationManager import AuthorizationManager
from Src.repository.SaveUserRepository import SaveUserRepository
from Src.Domain.models.SaveUserDomainModel import SaveUserDomainModel
import re
import datetime
import hashlib


class SignupUserService:
    repository: SaveUserRepository
    auth: AuthorizationManager

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository: SaveUserRepository,  auth: AuthorizationManager):
        self.repository = repository
        self.auth = auth

    def sign_up_user(self, json: str) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository.find_record_by_email(json['email'])
            print(record)
            if record.count() == 0:
                if json['password'] == json['confirm_password']:

                    hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                    # creation_date = datetime.datetime.now()
                    model = SaveUserDomainModel(json['user_id'],
                                                    json['name'],
                                                    json['email'],
                                                    hashed_password,
                                                    json['access_level'],
                                                    json['address'],
                                                    json['postal_code'],
                                                    json['phone_number']
                                                )
                    self.repository.insert(model)
                    user_id = model.user_id
                    token = self.auth.make_token_for_user_id(user_id)
                    token_utf = token.decode('utf-8')
                    return token_utf

                raise Exception("Sorry, password & confirm-pass is not equal")

            raise Exception("This email isn't available. Please try another.")

        raise ValueError





