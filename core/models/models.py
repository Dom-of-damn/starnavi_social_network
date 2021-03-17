from activity_log.models import UserMixin
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.models.managers import CustomUserManager


class User(AbstractUser, UserMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, verbose_name=_('user'))
    title = models.CharField(_('title'), max_length=50, blank=False)
    text = models.TextField(_('text'))
    created = models.DateTimeField(_('created'), auto_now=True)


class PostsFeedBack(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, verbose_name=_('post'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, verbose_name=_('user'))
    like = models.BooleanField(_('like'), default=True)
    created = models.DateTimeField(_('created'), auto_now=True)
