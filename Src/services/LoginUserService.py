from Src.repository.SaveUserRepository import SaveUserRepository
from Src.services.Manager.AuthorizationManager import AuthorizationManager
import re
import hashlib


class LoginUserService:
    repository: SaveUserRepository
    auth: AuthorizationManager

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository: SaveUserRepository,  auth: AuthorizationManager):
        self.repository = repository
        self.auth = auth

    def login_user(self, json: str) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository.find_record_by_email(json['email'])
            print(record)
            if record is not None:
                hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                if record.password == hashed_password:
                    user_id = record.user_id
                    token = self.auth.make_token_for_user_id(user_id)
                    token_utf = token.decode('utf-8')
                    return token_utf

                raise Exception("Sorry, your password was incorrect. Please double-check your password.")

            raise Exception("The email you entered doesn't belong to an account.Please check your email and try again.")

        raise ValueError
