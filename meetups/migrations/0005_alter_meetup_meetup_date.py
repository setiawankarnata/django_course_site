# Generated by Django 4.0 on 2021-12-30 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_meetup_meetup_date_meetup_organizer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetup',
            name='meetup_date',
            field=models.DateField(default=None),
        ),
    ]