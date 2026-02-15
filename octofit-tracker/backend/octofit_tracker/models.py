from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    members = models.JSONField()

    def __str__(self):
        return self.name

class Activity(models.Model):
    user_email = models.EmailField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()

class Workout(models.Model):
    user_email = models.EmailField()
    workout = models.CharField(max_length=100)
    reps = models.IntegerField()
