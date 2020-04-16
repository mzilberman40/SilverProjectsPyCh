from .config import *


def get_user(user_name):
    """
    :param user_name:
    :return: Existing user-object with user-name or creating new one.
    """

    if UserModel.objects.filter(user=user_name).count() > 0:
        return UserModel.objects.get(user=user_name)

    user_dict = {'user': user_name}
    user_form = UserForm(user_dict)
    if user_form.is_valid():
        return user_form.save()


