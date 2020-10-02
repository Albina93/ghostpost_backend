from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from . import models

class PostrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.BoastRoast
        fields = ['id', 'content', 'is_roast', 'upvote', 'downvote', 'date_created', 'last_update', 'sec_key', 'total_votes' ]

