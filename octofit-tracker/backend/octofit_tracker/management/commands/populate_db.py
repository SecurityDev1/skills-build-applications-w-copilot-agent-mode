from django.core.management.base import BaseCommand
from django.db import connection
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections if they exist
        db = connection.cursor().db_conn.client['octofit_db']
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create collections and insert test data
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
            {"name": "Batman", "email": "batman@dc.com", "team": "dc"}
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        teams = [
            {"name": "marvel", "members": ["ironman@marvel.com", "cap@marvel.com"]},
            {"name": "dc", "members": ["wonderwoman@dc.com", "batman@dc.com"]}
        ]
        db.teams.insert_many(teams)

        activities = [
            {"user_email": "ironman@marvel.com", "activity": "running", "duration": 30},
            {"user_email": "batman@dc.com", "activity": "cycling", "duration": 45}
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {"team": "marvel", "points": 100},
            {"team": "dc", "points": 90}
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"user_email": "cap@marvel.com", "workout": "pushups", "reps": 50},
            {"user_email": "wonderwoman@dc.com", "workout": "squats", "reps": 60}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
