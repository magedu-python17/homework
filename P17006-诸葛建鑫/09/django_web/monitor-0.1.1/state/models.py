from django.db import models

# Create your models here.


class AgentBase(models.Model):
    class Meta:
        db_table = 'agentbase'
    id = models.AutoField(primary_key=True)
    host = models.CharField(max_length=48, null=True)
    ip = models.CharField(max_length=15, null=False)
    cpu_count = models.IntegerField(null=False)
    memory_size = models.IntegerField(null=False)
    disk_total_size = models.IntegerField(null=False)

    def __repr__(self):
        return '<AgentBase ip={}, cpu={}, mem={}M, disk={}G>'.format(
            self.ip, self.cpu_count, self.memory_size, self.disk_total_size)

    __str__ = __repr__


class AgentDisk(models.Model):
    class Meta:
        db_table = 'agentdisk'
    id = models.AutoField(primary_key=True)
    agentbase = models.ForeignKey('AgentBase', on_delete=models.CASCADE)
    dp = models.CharField(max_length=20, null=False)
    size = models.IntegerField(null=False)
    is_deleted = models.IntegerField(null=True)

    def __repr__(self):
        return '<AgentDisk agent={} dp={} size={} del={}>'.format(self.agentbase.id, self.dp, self.size, self.is_deleted)

    __str__ = __repr__


class StateBase(models.Model):
    class Meta:
        db_table = 'statebase'
    id = models.AutoField(primary_key=True)
    agentbase = models.ForeignKey('AgentBase', on_delete=models.CASCADE)
    date = models.IntegerField(null=False)
    cpu_percent = models.FloatField(null=False)
    memory_percent = models.FloatField(null=False)

    def __repr__(self):
        return '<StateBase agent={} date={}, cpu={}% mem={}%>'.format(
            self.agentbase.id, self.date, self.cpu_percent, self.memory_percent)

    __str__ = __repr__


class StateDisk(models.Model):
    class Meta:
        db_table = 'statedisk'
    id = models.AutoField(primary_key=True)
    agentdisk = models.ForeignKey('AgentDisk', on_delete=models.CASCADE)
    date = models.IntegerField(null=False)
    disk_percent = models.FloatField(null=False)

    def __repr__(self):
        return '<StateDisk agent={} date={} disk={}%>'.format(self.agentdisk.id, self.date, self.disk_percent)

    __str__ = __repr__
