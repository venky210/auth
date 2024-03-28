from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager,Permission,Group
class UserManager(BaseUserManager):
    def create_user(self,email,username,password):
        if not email:
            raise ValueError('Email Must Be Provide...')
        
        user=self.model(email=email,username=username)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        user.is_activate=True
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user

class NewUser(AbstractUser):
    email=models.EmailField(max_length=100,primary_key=True)
    username=models.CharField(max_length=100)

    user_permissions = models.ManyToManyField (
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='user_permissions_set'  # Change this to a unique related_name
    )
    

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='user_groups'  # Change this to a unique related_name
    )
   


    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username','password']



    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['username','password']



    objects=UserManager()
