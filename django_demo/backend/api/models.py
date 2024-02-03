from django.db import models
from django.contrib.auth.models import Group, User
from rest_framework.authtoken.models import Token

# Create your models here.
# API User model inherited from django/contrib/auth/models.py User

# use with:
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
#
# for user in User.objects.all():
#     user.generate_token

# class CustomUser(User):
#     def __str__(self):
#         return self.first_name + " " + self.last_name + "," + self.username
#
#     def generate_token(self):
#         token = Token.objects.get_or_create(user=self)
#         print(token.key)
#
#
# class CustomGroup(Group):
#     def __str__(self):
#         return self.name


# or:
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
#
# user = User.objects.all()[0]:
#     token = Token.objects.get_or_create(user=user)
#     print(token)