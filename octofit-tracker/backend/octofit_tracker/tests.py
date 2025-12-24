from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team)
        self.assertEqual(str(user), 'U')
    def test_activity_create(self):
        team = Team.objects.create(name='T', description='d')
        user = User.objects.create(name='U', email='u@test.com', team=team)
        activity = Activity.objects.create(user=user, activity_type='A', duration_minutes=10, date='2025-01-01')
        self.assertEqual(str(activity), 'U - A')
    def test_workout_create(self):
        workout = Workout.objects.create(name='W', description='desc')
        self.assertEqual(str(workout), 'W')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='T', description='d')
        leaderboard = Leaderboard.objects.create(team=team, total_points=10, rank=1)
        self.assertEqual(str(leaderboard), 'T - Rank 1')
