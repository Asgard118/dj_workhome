from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

