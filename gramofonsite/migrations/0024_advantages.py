# Generated by Django 4.2.2 on 2023-08-21 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gramofonsite', '0023_alter_local_title_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_features', models.CharField(blank=True, max_length=200, null=True, verbose_name='Cechy szczególne - wypunktowanie')),
                ('advantages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gramofonsite.local')),
            ],
        ),
    ]
