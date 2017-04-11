# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.cache import cache

class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SiteSettings(SingletonModel):
    support = models.EmailField(default='supprot@example.com')
    sales_department = models.EmailField(blank=True)
    twilio_account_sid = models.CharField(max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99')
    twilio_auth_token = models.CharField(max_length=255, default='abd4d45dd57dd79b86dd51df2e2a6cd5')
    twilio_phone_number = models.CharField(max_length=255, default='+15006660005')
