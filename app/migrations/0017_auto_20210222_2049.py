# Generated by Django 2.1.8 on 2021-02-22 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210222_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songsourcerelationship',
            name='attritbuted_person_music_in_source',
        ),
        migrations.RemoveField(
            model_name='songsourcerelationship',
            name='attritbuted_person_text_in_source',
        ),
        migrations.AddField(
            model_name='songsourcerelationship',
            name='attributed_person_music_in_source',
            field=models.ManyToManyField(blank=True, related_name='attributed_person_music_in_source', to='app.Person'),
        ),
        migrations.AddField(
            model_name='songsourcerelationship',
            name='attributed_person_text_in_source',
            field=models.ManyToManyField(blank=True, related_name='attributed_person_text_in_source', to='app.Person'),
        ),
    ]