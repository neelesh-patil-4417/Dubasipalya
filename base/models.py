from django.db import models

# Create your models here.
class schedule(models.Model):
    train_name = models.TextField()
    arrives = models.TimeField()
    departs = models.TextField()
    stop_time = models.TextField()
    mon = models.TextField()
    tue = models.TextField()
    wed = models.TextField()
    thu = models.TextField()
    fri = models.TextField()
    sat = models.TextField()
    sun = models.TextField()

    def __str__(self) -> str:
        return self.train_name
    