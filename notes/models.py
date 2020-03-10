from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic for the note"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string form of model"""
        return self.text

class Note(models.Model):
    """The note written"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string form of model"""
        if len(self.text)>50:
            return self.text[:50] + "..."
        else:
            return self.text