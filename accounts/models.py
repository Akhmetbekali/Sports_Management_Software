from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_save


# Create your models here.

def groups_and_permissions():
    managers = Group.objects.get(name='manager')
    club_leaders = Group.objects.get(name='club_leader')
    students = Group.objects.get(name='student')
    managers.permissions.add(6, 10, 29, 30, 31, 32)
    club_leaders.permissions.add(30, 32)
    students.permissions.add(32)


class ClubProfile(models.Model):
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='leader')
    club_name = models.CharField(max_length=100)
    club_description = models.CharField(max_length=1000)
    club_schedule = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, blank=True, related_name='participants')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(ClubProfile, self).save()
