# Generated by Django 4.2.2 on 2023-07-17 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gramofonsite', '0011_room_alter_local_describe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='describe',
        ),
        migrations.AddField(
            model_name='local',
            name='note',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gramofonsite.shortdescribe'),
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
