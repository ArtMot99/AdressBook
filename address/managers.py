from django.db import models


class OwnContactQs(models.QuerySet):
    def personal_contacts(self, user):
        return super(OwnContactQs, self).filter(is_active=False, user=user)


class AllContactManager(models.Manager):
    def get_queryset(self):
        return super(AllContactManager, self).get_queryset().filter(is_active=True)
