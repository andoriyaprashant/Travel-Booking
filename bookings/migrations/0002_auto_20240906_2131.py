from django.db import migrations

def create_initial_travel_options(apps, schema_editor):
    TravelOption = apps.get_model('bookings', 'TravelOption')
    TravelOption.objects.create(
        type='Flight',
        source=' York',
        destination='Los Angeles',
        date_time='2024-09-01T15:00:00Z',
        price=299.99,
        available_seats=100
    )
    TravelOption.objects.create(
        type='Train',
        source='Chicago',
        destination='Houston',
        date_time='2024-09-05T08:00:00Z',
        price=89.99,
        available_seats=150
    )
    TravelOption.objects.create(
        type='Bus',
        source='San Francisco',
        destination='Las Vegas',
        date_time='2024-09-10T10:00:00Z',
        price=49.99,
        available_seats=50
    )
    TravelOption.objects.create(
        type='Flight',
        source='Miami',
        destination='New York',
        date_time='2024-09-12T20:00:00Z',
        price=199.99,
        available_seats=200
    )
    TravelOption.objects.create(
        type='Train',
        source='Seattle',
        destination='Portland',
        date_time='2024-09-15T09:00:00Z',
        price=59.99,
        available_seats=75
    )
    TravelOption.objects.create(
        type='Bus',
        source='Denver',
        destination='Phoenix',
        date_time='2024-09-20T14:00:00Z',
        price=69.99,
        available_seats=120
    )

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(create_initial_travel_options),
    ]
