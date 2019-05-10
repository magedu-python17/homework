from django.db import models

# Create your models here.

class Host(models.Model):
    class Meta:
        db_table = 'host'
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=45, null=False)
    ip = models.CharField(max_length=45, null=False, unique=True)
    cpu_num = models.IntegerField(max_length=11, null=False)
    men_size=models.BigIntegerField(max_length=20, null=False)
    disk_size_total = models.BigIntegerField(max_length=20, null=False)

class Disk(models.Model):
    class Meta:
        db_table = 'disk'
    id = models.AutoField(primary_key=True)
    partition = models.CharField(max_length=45, null=False)
    size = models.BigIntegerField(max_length=45, null=False)
    deleted = models.IntegerField(max_length=1, null=False)
    host = models.ForeignKey(Host)

class Disk_state(models.Model):
    class Meta:
        db_table = 'disk_state'

    id = models.AutoField(primary_key=True)
    size_percent = models.IntegerField(max_length=11, null=False)
    date = models.DateTimeField(null=False)
    disk = models.ForeignKey(Disk, to_field='id')

class Cm_state(models.Model):
    class Meta:
        db_table = 'cm_state'
    id = models.AutoField(primary_key=True)
    men_percent = models.IntegerField(max_length=11, null=False)
    cpu_percent = models.IntegerField(max_length=11, null=False)
    date = models.DateTimeField(null=False)
    host = models.ForeignKey(Host)



