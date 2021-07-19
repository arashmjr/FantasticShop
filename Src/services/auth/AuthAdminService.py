from Src.repository.UserAdminRepository import UserAdminRepository
from Src.repository.CartRepository import CartRepository
from Src.Domain.models.UserAdminDomainModel import UserAdminDomainModel
from Src.Domain.models.CartDomainModel import CartDomainModel
from Src.services.Manager.AuthorizationManager import make_token_for_admin
import re
import datetime
import hashlib


class AuthAdminService:
    repository_user: UserAdminRepository
    repository_cart: CartRepository

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository_user: UserAdminRepository, repository_cart: CartRepository):

        self.repository_user = repository_user
        self.repository_cart = repository_cart

    def sign_up_admin(self, json: str) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository_user.find_record_by_email_signup(json['email'])
            if record.count() == 0:
                if json['password'] == json['confirm_password']:

                    hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                    creation_date = datetime.datetime.now()
                    model = UserAdminDomainModel(
                                                    json['name'],
                                                    json['email'],
                                                    hashed_password,
                                                    creation_date
                                                )
                    print(model.creation_date)
                    self.repository_user.insert(model)
                    item = self.repository_user.find_record_by_email(json['email'])
                    admin_id = item.admin_id

                    # create token for user
                    token = make_token_for_admin(admin_id)
                    token_utf = token.decode('utf-8')
                    return token_utf

                raise Exception("Sorry, password & confirm-pass is not equal")

            raise Exception("This email isn't available. Please try another.")

        raise ValueError

    def login_admin(self, json: str) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository_user.find_record_by_email(json['email'])

            if record is not None:
                hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                if record.password == hashed_password:
                    admin_id = record.admin_id
                    token = make_token_for_admin(admin_id)
                    token_utf = token.decode('utf-8')
                    return token_utf

                raise Exception("Sorry, your password was incorrect. Please double-check your password.")

            raise Exception("The email you entered doesn't belong to an account.Please check your email and try again.")

        raise ValueError


