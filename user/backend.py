"""
import logging


class MyAuthBackend(object):
    def authenticate(self, email, password):    
        try:
            user = UserInfo.objects.get(email=email)
            print( user.email )
            if user.check_password(password):
                return user
            else:
                return None
        except UserInfo.DoesNotExist:
            return None
        except Exception as e:
            return None
    def get_user(self, user_id):
        try:
            user = UserInfo.objects.get(sys_id=user_id)
            if user.is_active:
                return user
            return None
        except UserInfo.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None
"""