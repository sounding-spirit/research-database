# Generated by Django 2.1.8 on 2021-02-02 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_songsourcerelationship'),
    ]

    operations = [
        migrations.CreateModel(
            name='OSHAddedAlto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_in_ch', models.PositiveIntegerField(blank=True, null=True)),
                ('attribution_in_ch', models.CharField(blank=True, max_length=255, null=True)),
                ('page_in_cooper_sh', models.PositiveIntegerField(blank=True, null=True)),
                ('attribution_in_cooper_sh', models.CharField(blank=True, max_length=255, null=True)),
                ('page_in_white_sh', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('attribution_in_white_sh', models.CharField(blank=True, max_length=255, null=True)),
                ('page_in_nhc', models.PositiveIntegerField(blank=True, null=True)),
                ('attribution_in_nhc', models.CharField(blank=True, max_length=255, null=True)),
                ('attributed_person_in_ch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attritbuted_person_in_ch', to='app.Person')),
                ('attributed_person_in_cooper_sh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attritbuted_person_in_cooper_sh', to='app.Person')),
                ('attributed_person_in_nhc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributed_person_in_nhc', to='app.Person')),
                ('attributed_person_in_white_sh', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attributed_person_in_white_sh', to='app.Person')),
                ('song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Song')),
            ],
        ),
    ]
