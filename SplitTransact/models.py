from __future__ import unicode_literals
from Django.contrib import User
from django.db import models

class Expenses(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    meta = models.CharField(max_length=250)
    created = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.user in self.group.members():
            raise "user does not belongs to group"
        return super(Expenses, self).save(*args, **kwargs)


class Group(models.Model):
    name = models.CharField(max_length=100)
    meta = models.CharField(max_length=250)
    created = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User)

    def members(self):
        return GroupMember.objects.filter(group=self).values("id")

class GroupMember(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)

    class Meta:
        unique_together = ('user', 'group')


