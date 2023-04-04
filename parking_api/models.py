from django.db import models

class Parking(models.Model):
    status = models.BooleanField(default = False, blank = True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return 'available' if self.status else 'occupied'




