# Generated by Django 4.2.2 on 2023-07-16 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gramofonsite', '0010_alter_local_describe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('describe', models.CharField(choices=[('Dance', 'Sala Taneczna'), ('WC', 'Toaleta'), ('Cook', 'Kuchnia')], default='Dance', max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='local',
            name='describe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gramofonsite.room'),
        ),
    ]