from django.db import models
from datetime import datetime

# Create your models here.


class BoastRoast(models.Model):
    content = models.CharField(max_length=255)
    is_roast = models.BooleanField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.now)
    last_update = models.DateTimeField(default=datetime.now)
    sec_key = models.CharField(max_length=8)

    

    @property
    def total_votes(self):
        return self.upvote + self.downvote
