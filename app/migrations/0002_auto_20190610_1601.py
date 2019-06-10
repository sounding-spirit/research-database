# Generated by Django 2.1.8 on 2019-06-10 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='page_placement',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('b', 'b')], help_text='Only has a value if it is one of two songs that begin on a page. Use "A" for top, "B" for bottom.', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='printingrelationship',
            name='text_unit',
            field=models.ForeignKey(blank=True, help_text='Section - Page - Sequence', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.TextUnit'),
        ),
        migrations.AlterField(
            model_name='sourcerelationship',
            name='text_unit',
            field=models.ForeignKey(blank=True, help_text='Section - Page - Sequence', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.TextUnit'),
        ),
        migrations.AlterField(
            model_name='textunit',
            name='section',
            field=models.CharField(choices=[('Front Cover', 'Front Cover'), ('Frontispiece', 'Frontispiece'), ('Title Page', 'Title Page'), ('Summary Statement', 'Summary Statement'), ('Preface', 'Preface'), ('Report', 'Report'), ('Introductory', 'Introductory'), ('Rudiments of Music', 'Rudiments of Music'), ('Part II', 'Part II'), ('Part III', 'Part III'), ('Appendix 1850', 'Appendix 1850'), ('Appendix 1859', 'Appendix 1859'), ('Appendix 1869', 'Appendix 1869'), ('Appendix 1911', 'Appendix 1911'), ('Index', 'Index'), ('Back Cover', 'Back Cover')], help_text='Name of the section of the book', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='textunit',
            name='subsection',
            field=models.CharField(blank=True, choices=[('Sub-committee', 'Sub-committee'), ('Committee', 'Committee'), ('Introduction', 'Introduction'), ('Lesson I', 'Lesson I'), ('Lesson II', 'Lesson II'), ('Lesson III', 'Lesson III'), ('Lesson IV', 'Lesson IV'), ('Lesson V', 'Lesson V'), ('Lesson VI', 'Lesson VI'), ('Lesson VII', 'Lesson VII'), ('Lesson VIII', 'Lesson VIII'), ('Lesson IX', 'Lesson IX'), ('Lesson X', 'Lesson X'), ('Dynamics', 'Dynamics'), ('Solmization-Greek Notation', 'Solmization-Greek Notation'), ('The Voice in Singing', 'The Voice in Singing'), ('Intervals', 'Intervals'), ('Miscellaneous', 'Miscellaneous'), ('Metre', 'Metre'), ('Signs Used in Music', 'Signs Used in Music'), ('Additional Index', 'Additional Index')], help_text='Name of a subsection of the book, e.g. a section of the Rudiments', max_length=255, null=True),
        ),
    ]
