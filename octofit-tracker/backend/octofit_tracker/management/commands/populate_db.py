from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True),
            User(email='captain@marvel.com', name='Captain America', team='Marvel', is_superhero=True),
            User(email='batman@dc.com', name='Batman', team='DC', is_superhero=True),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', is_superhero=True),
        ]
        for user in users:
            user.save()

        # Add users to teams
        marvel.members = [users[0], users[1]]
        dc.members = [users[2], users[3]]
        marvel.save()
        dc.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2026-02-20')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2026-02-19')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2026-02-18')
        Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2026-02-17')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=175)
        Leaderboard.objects.create(team='DC', points=110)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='Marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
