from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.project_name


class Log(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.SET_NULL,
        null=True,
    )
    remarks = models.CharField(max_length=400)
    created = models.DateField(auto_now_add=True, null=True, blank=False)
    date = models.DateField(null=True, blank=False)
    time = models.TimeField(null=True, blank=False)

    def __unicode__(self):
        return self.remarks


