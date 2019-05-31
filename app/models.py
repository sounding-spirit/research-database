from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Page(models.Model):
    # Note: OSH1 must be entered first when database is initiated
    DEFAULT_BOOK_ID = 1

    TYPOGRAPHY_CHOICES = (
    ('OSH1', 'OSH1'),
    ('OSH2', 'OSH2'),
    ('OSH3', 'OSH3'),
    ('UHHS', 'UHHS'),
    )

    seq = models.PositiveIntegerField(blank=False, null=True, help_text='Page order')
    number = models.CharField(max_length=255, blank=False, null=True, help_text='Page number in book')
    book = models.ForeignKey("Book", blank=False, default=DEFAULT_BOOK_ID, help_text='Book in which page appears', on_delete=models.CASCADE)
    typography = models.CharField(max_length=255, blank=True, null=True, choices=TYPOGRAPHY_CHOICES)

    def __str__(self):
        return self.number


class TextUnit(models.Model):
    SECTION_CHOICES = (
    ('Front Cover', 'Front Cover'),
    ('Frontispiece', 'Frontispiece'),
    ('Title Page', 'Title Page'),
    ('Summary Statement', 'Summary Statement'),
    ('Preface', 'Preface'),
    ('Report', 'Report'),
    ('Introductory', 'Introductory'),
    ('Rudiments of Music', 'Rudiments of Music'),
    ('Part II', 'Part II'),
    ('Part III', 'Part III'),
    ('Appendix 1850', 'Appendix 1850'),
    ('Appendix 1859', 'Appendix 1859'),
    ('Appendix 1869', 'Appendix 1869'),
    ('Appendix 1911', 'Appendix 1911'),
    ('Index', 'Index'),
    ('Back Cover', 'Back Cover'),
    )


    page = models.ForeignKey('Page', blank=False, null=True, on_delete=models.CASCADE, help_text='Relevant page from Pages table')
    seq = models.PositiveIntegerField(blank=False, null=True, help_text='Number indicating where on the page this text unit falls')
    value = models.TextField(blank=False, null=True, help_text='The content of the unit, or a description of it')
    section = models.CharField(max_length=255, blank=False, null=True, help_text='Name of the section of the book', choices=SECTION_CHOICES)
    subsection = models.CharField(max_length=255, blank=True, null=True, help_text='Name of a subsection of the book, e.g. a section of the Rudiments')

    def __str__(self):
        return "%s - %s - %s" % (self.section, self.page, self.seq)


class Song(models.Model):
    LINES_CHOICES = (
        (3, '3'),
        (4, '4'),
    )

    page_start = models.ForeignKey('Page', blank=False, null=True, related_name='page_start', help_text='Starting page of song from Pages', on_delete=models.CASCADE)
    page_end = models.ForeignKey('Page', blank=False, null=True, related_name = 'page_end', help_text='Last page of song from Pages; should be same as the page start if a half-page or one-page song', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=True)
    lines = models.PositiveIntegerField(blank=False, null=True, choices=LINES_CHOICES)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    abbreviated_title = models.CharField(max_length=10, blank=False, null=True)
    year_range_start = models.PositiveIntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2000)], help_text='Year of publication if known or first possible year of publication otherwise', blank=True, null=True)
    year_certainty = models.CharField(max_length=255, help_text='Way of indicating “circa” or the like', blank=True, null=True)
    year_range_end = models.PositiveIntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2000)], help_text='Last possible year of publication if precise date not known', blank=True, null=True)
    place = models.CharField(max_length=255, help_text='Place of publication', blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    author_editor = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.abbreviated_title

class Contributor(models.Model):
    last_name = models.CharField(max_length=255, help_text='Must be identical across entries for the same person involved in multiple books', blank=False, null=True)
    first_name = models.CharField(max_length=255, help_text='Must be identical across entries for the same person involved in multiple books', blank=False, null=True)
    book = models.ForeignKey('Book', help_text='The book corresponding with the SH edition this contributor worked on', blank=False, null=True, on_delete=models.CASCADE)
    birth_year = models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2000)], blank=True, null=True)
    birth_lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    birth_lon = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    birth_location = models.CharField(max_length=255, blank=True, null=True, help_text="Name of place of residence when born")
    book_lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    book_lon = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    book_location = models.CharField(max_length=255, blank=True, null=True, help_text="Name of place of residence when contributed to SH edition")
    death_year = models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2050)], blank=True, null=True)
    death_lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    death_lon = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    death_location = models.CharField(max_length=255, blank=True, null=True)
    committee = models.BooleanField(max_length=255, blank=False, null=True)
    subcommittee = models.BooleanField(max_length=255, blank=False, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class SourceRelationship(models.Model):
    CATEGORY_CHOICES = (
        ('scriptural citation', 'scriptural citation'),
        ('attribution', 'attribution'),
        ('song', 'song'),
        ('hymn text', 'hymn text'),
        ('alto', 'alto'),
        ('historical note', 'historical note'),
        ('rudiments', 'rudiments'),
    )

    TYPE_CHOICES = (
        ('identical', 'identical'),
        ('near identical', 'near identical'),
        ('adapted', 'adapted'),
        ('direct citation', 'direct citation'),
    )

    song = models.ForeignKey('Song', blank=True, null=True, on_delete=models.CASCADE)
    text_unit = models.ForeignKey('TextUnit', blank=True, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', help_text='Book that serves as source for song/text unit', blank=False, null=True, on_delete=models.CASCADE)
    sr_category = models.CharField(max_length=255, help_text='Category of relationship', blank=False, null=True, choices=CATEGORY_CHOICES)
    sr_type = models.CharField(max_length=255, help_text='Type of the relationship', blank=True, null=True, choices=TYPE_CHOICES)

class OSHPrintingSequence(models.Model):
    sequence_name = models.CharField(max_length=255, blank=False, null=True)
    book_1 = models.ForeignKey('Book', help_text='ID of a printing unless first printing', blank=True, null=True, related_name = 'book_1', on_delete=models.CASCADE)
    book_2 = models.ForeignKey('Book', help_text='ID of a printing unless last printing', blank=True, null=True, related_name = 'book_2', on_delete=models.CASCADE)

    def __str__(self):
        return self.sequence_name

class PrintingRelationship(models.Model):
    CATEGORY_CHOICES = (
    #placeholder for values
    )
    TYPE_CHOICES = (
    #placeholder for values
    )

    osh_printing_sequence = models.ForeignKey('OSHPrintingSequence', blank=False, null=True, on_delete=models.CASCADE, help_text="Printing where change introduced")
    page = models.ForeignKey('Page', blank=True, null=True, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', blank=True, null=True, on_delete=models.CASCADE)
    text_unit = models.ForeignKey('TextUnit', blank=True, null=True, on_delete=models.CASCADE)
    pr_category = models.CharField(max_length=255, blank=False, null=True) # add choices="CATEGORY_CHOICES"
    pr_type = models.CharField(max_length=255, blank=True, null=True) # add choices="TYPE_CHOICES"

class Contribution(models.Model):
    CONTRIBUTION_CHOICES = (
        ('composer', 'composer'),
        ('arranger', 'arranger'),
        ('hymnwriter', 'hymnwriter'),
    )

    song = models.ForeignKey('Song', blank=False, null=True, on_delete=models.CASCADE)
    contributor = models.ForeignKey('Contributor', blank=False, null=True, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=False, null=True, choices=CONTRIBUTION_CHOICES)
