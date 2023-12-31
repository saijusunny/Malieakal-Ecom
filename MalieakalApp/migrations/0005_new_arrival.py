# Generated by Django 4.0.2 on 2023-11-07 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0004_profile_user_banner_access_profile_user_cat_access_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='static/images/logo/noimage.jpg', upload_to='images/items')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('price', models.FloatField(default=0)),
                ('offer_price', models.FloatField(default=0)),
                ('offer', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MalieakalApp.user_registration')),
            ],
        ),
    ]
