# Generated by Django 2.0.4 on 2018-05-05 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_client_dog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dog_for_user', to='accounts.Client'),
        ),
    ]
