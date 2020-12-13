from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

# class QuizzManager(BaseUserManager):
#     """
#     A custom user manager to deal with emails as unique identifiers for auth
#     instead of usernames. The default that's used is "UserManager"
#     """
#
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

    # def create_superuser(self, email, password, **extra_fields):
    #     user = self._create_user(email, password, **extra_fields)
    #     user.is_admin = True
    #     user.save(using=self._db)
    #     return user

# class User(AbstractBaseUser):
    # email = models.EmailField(unique=True, null=True, )
    # USERNAME_FIELD = 'email'
    # pass

class User(AbstractUser):
    pass


class Quizz(models.Model):
    name = models.CharField(max_length=250, null=True)


class Questions(models.Model):
    quiz_id = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True)
    options = models.CharField(max_length=250, null=True)
    option = models.CharField(max_length=250, null=True, blank=True)
    answer = models.CharField(max_length=250, null=True)


class Scores(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quizz_id = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, null=False)