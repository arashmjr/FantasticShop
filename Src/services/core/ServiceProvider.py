# from repository.core.RepositoryProvider import RepositoryProvider
# from seviceLayer.SaveUserService import SaveUserService
# from seviceLayer.SuggestionService import SuggestionService
# from seviceLayer.SaveOrderService import SaveOrderService
# from seviceLayer.UserFollowService import UserFollowService
# from seviceLayer.Managers.AuthorizationManager import AuthorizationManager
# from seviceLayer.PackagesService import PackagesService
# from seviceLayer.RegisterService import RegisterService
# from seviceLayer.LoginService import LoginService
# from seviceLayer.ResetPasswordService import ResetPasswordService
from Src.repository.core.RepositoryProvider import RepositoryProvider
from Src.services.Manager.AuthorizationManager import AuthorizationManager
from Src.services.SignupUserService import SignupUserService


class ServiceProvider:
    repository_provider: RepositoryProvider
    auth: AuthorizationManager

    def __init__(self):
        self.repository_provider = RepositoryProvider()
        self.auth = AuthorizationManager()

    def make_signup_user_service(self):
        return SignupUserService(self.repository_provider.make_user_profile(),  self.auth)
    #
    # def make_get_suggestions_service(self):
    #     return SuggestionService(self.repository_provider.submit_orders(), self.repository_provider.make_user_follows(),
    #                              self.repository_provider.make_user_profile(), self.auth)
    #
    # def make_save_orders_service(self):
    #     return SaveOrderService(self.repository_provider.submit_orders(), self.repository_provider.make_user_profile(),
    #                             self.auth)
    #
    # def make_user_follow_service(self):
    #     return UserFollowService(self.repository_provider.make_user_follows(), self.repository_provider.make_user_profile(),
    #                              self.auth)
    #
    # def make_get_packages_service(self):
    #     return PackagesService(self.repository_provider.make_user_profile(), self.repository_provider.make_packages(),
    #                            self.auth)
    #
    #

