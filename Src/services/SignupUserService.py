from Src.repository.SaveUserRepository import SaveUserRepository
from Src.repository.CartRepository import CartRepository
from Src.Domain.models.SaveUserDomainModel import SaveUserDomainModel
from Src.Domain.models.CartDomainModel import CartDomainModel
from Src.services.Manager.AuthorizationManager import make_token_for_user_id
import re
import datetime
import hashlib


class SignupUserService:
    repository_user: SaveUserRepository
    repository_cart: CartRepository

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository_user: SaveUserRepository, repository_cart: CartRepository):

        self.repository_user = repository_user
        self.repository_cart = repository_cart

    def sign_up_user(self, json: str) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository_user.find_record_by_email_signup(json['email'])
            if record.count() == 0:
                if json['password'] == json['confirm_password']:

                    hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                    creation_date = datetime.datetime.now()
                    model = SaveUserDomainModel(
                                                    json['name'],
                                                    json['email'],
                                                    hashed_password,
                                                    json['access_level'],
                                                    json['address'],
                                                    json['postal_code'],
                                                    json['phone_number'],
                                                    creation_date
                                                )
                    self.repository_user.insert(model)
                    item = self.repository_user.find_record_by_email(json['email'])
                    user_id = item.user_id

                    # creat a cart for user
                    model_cart = CartDomainModel(user_id, -1, creation_date)
                    print(model_cart.to_dict())
                    self.repository_cart.insert(model_cart)

                    # create token for user
                    token = make_token_for_user_id(item.user_id)
                    token_utf = token.decode('utf-8')
                    return token_utf

                raise Exception("Sorry, password & confirm-pass is not equal")

            raise Exception("This email isn't available. Please try another.")

        raise ValueError





