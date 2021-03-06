# Generated by Django 3.1.3 on 2020-12-29 15:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('story_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='story_api.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
