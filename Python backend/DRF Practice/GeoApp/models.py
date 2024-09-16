from django.contrib.gis.db import models


class Building(models.Model):
    geom = models.PointField()
    address = models.CharField()

    def __str__(self):
        return self.geom

    class Meta:
        indexes = [
            models.Index(fields=['geom'])
        ]