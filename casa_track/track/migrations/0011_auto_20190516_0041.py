# Generated by Django 2.0.5 on 2019-05-16 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0010_auto_20190309_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackingform',
            name='signature',
        ),
        migrations.AlterField(
            model_name='trackingform',
            name='supervisor',
            field=models.CharField(choices=[('C', 'Celena Zupko'), ('H', 'Heidi Turbow'), ('G', 'Gail Wechsler'), ('K', 'Katie Robinson'), ('P', 'Pete Skarda'), ('M', 'Melanie Barket'), ('N', 'Nicole Perotti')], max_length=256),
        ),
    ]