from Src.repository.SaveUserRepository import SaveUserRepository
import re
import hashlib
from Src.services.Manager.AuthorizationManager import make_token_for_user_id


class LoginUserService:
    repository: SaveUserRepository

    regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    def __init__(self, repository: SaveUserRepository):
        self.repository = repository

    def login_user(self, json: str) -> str:

        if re.search(self.regex, json['email']):
            record = self.repository.find_record_by_email(json['email'])

            if record is not None:
                hashed_password = hashlib.md5(json['password'].encode('utf-8')).hexdigest()
                if record.password == hashed_password:
                    user_id = record.user_id
                    token = make_token_for_user_id(user_id)
                    token_utf = token.decode('utf-8')
                    return token_utf

                raise Exception("Sorry, your password was incorrect. Please double-check your password.")

            raise Exception("The email you entered doesn't belong to an account.Please check your email and try again.")

        raise ValueError
