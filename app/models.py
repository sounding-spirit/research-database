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

    SUBSECTION_CHOICES = (
    ('Sub-committee', 'Sub-committee'),
    ('Committee', 'Committee'),
    ('Introduction', 'Introduction'),
    ('Lesson I', 'Lesson I'),
    ('Lesson II', 'Lesson II'),
    ('Lesson III', 'Lesson III'),
    ('Lesson IV', 'Lesson IV'),
    ('Lesson V', 'Lesson V'),
    ('Lesson VI', 'Lesson VI'),
    ('Lesson VII', 'Lesson VII'),
    ('Lesson VIII', 'Lesson VIII'),
    ('Lesson IX', 'Lesson IX'),
    ('Lesson X', 'Lesson X'),
    ('Dynamics', 'Dynamics'),
    ('Solmization-Greek Notation', 'Solmization-Greek Notation'),
    ('The Voice in Singing', 'The Voice in Singing'),
    ('Intervals', 'Intervals'),
    ('Miscellaneous', 'Miscellaneous'),
    ('Metre', 'Metre'),
    ('Signs Used in Music', 'Signs Used in Music'),
    ('Additional Index', 'Additional Index'),
    )

    page = models.ForeignKey('Page', blank=False, null=True, on_delete=models.CASCADE, help_text='Relevant page from Pages table')
    seq = models.PositiveIntegerField(blank=False, null=True, help_text='Number indicating where on the page this text unit falls')
    value = models.TextField(blank=False, null=True, help_text='The content of the unit, or a description of it')
    section = models.CharField(max_length=255, blank=False, null=True, help_text='Name of the section of the book', choices=SECTION_CHOICES)
    subsection = models.CharField(max_length=255, blank=True, null=True, help_text='Name of a subsection of the book, e.g. a section of the Rudiments', choices=SUBSECTION_CHOICES)

    def __str__(self):
        return "%s - %s - %s" % (self.section, self.page, self.seq)


class Song(models.Model):
    LINES_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    PAGE_PLACEMENT_CHOICES = (
        ('a', 'a'),
        ('b', 'b'),
    )

    KEY_CHOICES = (
        ('A', 'A'),
        ('Aflat', 'A♭'),
        ('Asharp', 'A♯'),
        ('B', 'B'),
        ('Bflat', 'B♭'),
        ('C', 'C'),
        ('Csharp', 'C♯'),
        ('D', 'D'),
        ('Dflat', 'D♭'),
        ('Dsharp', 'D♯'),
        ('Eflat', 'E♭'),
        ('E', 'E'),
        ('F', 'F'),
        ('Fsharp', 'F♯'),
        ('G', 'G'),
        ('Gflat', 'G♭'),
        ('Gsharp', 'G♯'),
    )

    MODE_CHOICES = (
        ('major', 'major'),
        ('minor', 'minor'),
        ('multiple', 'multiple'),
    )

    page_start = models.ForeignKey('Page', blank=False, null=True, related_name='page_start', help_text='Starting page of song from Pages', on_delete=models.CASCADE)
    page_end = models.ForeignKey('Page', blank=False, null=True, related_name = 'page_end', help_text='Last page of song from Pages; should be same as the page start if a half-page or one-page song', on_delete=models.CASCADE)
    page_placement = models.CharField(max_length=1, blank=True, null=True, choices=PAGE_PLACEMENT_CHOICES, help_text='Only has a value if it is one of two songs that begin on a page. Use "A" for top, "B" for bottom.')
    title = models.CharField(max_length=255, blank=False, null=True)
    lines = models.PositiveIntegerField(blank=False, null=True, choices=LINES_CHOICES)
    key = models.CharField(max_length=255, blank=True, null=True, choices=KEY_CHOICES)
    mode = models.CharField(max_length=255, blank=True, null=True, choices=MODE_CHOICES)
    attributed_person_text = models.ForeignKey('Person', blank=True, null=True, related_name='attributed_person_text', on_delete=models.CASCADE)
    attributed_person_music = models.ForeignKey('Person', blank=True, null=True, related_name='attributed_person_music', on_delete=models.CASCADE)
    attribution_text = models.CharField(max_length=255, blank=True, null=True)
    attribution_music = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s - %s " % (self.title, self.page_start.number)



class Person(models.Model):
    last_name = models.CharField(max_length=255, blank=False, null=True)
    first_middle_name = models.CharField(max_length=255, blank=True, null=True)
    female = models.BooleanField(max_length=255, blank=False, null=True, default=False)
    alternate_spellings = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.first_middle_name, self.last_name)

    class Meta:
        verbose_name_plural = 'People'


class Book(models.Model):
    YEAR_CERTAINTY_CHOICES = (
        ('circa', 'circa'),
    )

    title = models.CharField(max_length=255, blank=False, null=True)
    abbreviated_title = models.CharField(max_length=255, blank=False, null=True)
    year_range_start = models.PositiveIntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2000)], help_text='Year of publication if known or first possible year of publication otherwise', blank=True, null=True)
    year_certainty = models.CharField(max_length=255, help_text='If year of publication is uncertain, use circa.', blank=True, null=True, choices=YEAR_CERTAINTY_CHOICES)
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
    birth_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    birth_lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    birth_location = models.CharField(max_length=255, blank=True, null=True, help_text="Name of place of residence when born")
    book_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    book_lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    book_location = models.CharField(max_length=255, blank=True, null=True, help_text="Name of place of residence when contributed to SH edition")
    death_year = models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2050)], blank=True, null=True)
    death_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    death_lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    death_location = models.CharField(max_length=255, blank=True, null=True)
    committee = models.BooleanField(max_length=255, blank=False, null=True)
    subcommittee = models.BooleanField(max_length=255, blank=False, null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class TextSourceRelationship(models.Model):
    CATEGORY_CHOICES = (
        ('scriptural citation', 'scriptural citation'),
        ('attribution', 'attribution'),
        ('hymn', 'hymn'),
        ('historical note', 'historical note'),
        ('other content', 'other content'),
    )

    TYPE_CHOICES = (
        ('identical', 'identical'),
        ('near identical', 'near identical'),
        ('adapted', 'adapted'),
        ('direct citation', 'direct citation'),
    )

    song = models.ForeignKey('Song', blank=True, null=True, on_delete=models.CASCADE)
    text_unit = models.ForeignKey('TextUnit', blank=True, null=True, on_delete=models.CASCADE, help_text = "Section - Page - Sequence")
    book = models.ForeignKey('Book', help_text='Book that serves as source for song/text unit', blank=False, null=True, on_delete=models.CASCADE)
    sr_category = models.CharField(max_length=255, help_text='Category of relationship', blank=False, null=True, choices=CATEGORY_CHOICES)
    sr_type = models.CharField(max_length=255, help_text='Type of the relationship', blank=True, null=True, choices=TYPE_CHOICES)


class SongSourceRelationship(models.Model):
    SR_TYPE_CHOICES = (
        ('identical', 'identical'),
        ('near identical', 'near identical'),
        ('adapted', 'adapted'),
    )

    KEY_IN_SOURCE_CHOICES = (
        ('A', 'A'),
        ('Aflat', 'A♭'),
        ('Asharp', 'A♯'),
        ('B', 'B'),
        ('Bflat', 'B♭'),
        ('C', 'C'),
        ('Csharp', 'C♯'),
        ('D', 'D'),
        ('Dflat', 'D♭'),
        ('Dsharp', 'D♯'),
        ('Eflat', 'E♭'),
        ('E', 'E'),
        ('F', 'F'),
        ('Fsharp', 'F♯'),
        ('G', 'G'),
        ('Gflat', 'G♭'),
        ('Gsharp', 'G♯'),
    )

    LINES_IN_SOURCE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    song = models.ForeignKey('Song', blank=False, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', help_text='Book that serves as source for song', blank=False, null=True, on_delete=models.CASCADE)
    sr_type = models.CharField(max_length=255, blank=True, null=True, help_text='Type of relationship', choices=SR_TYPE_CHOICES)
    title_in_source = models.CharField(max_length=255, blank=True, null=True)
    page_in_source = models.CharField(max_length=255, blank=True, null=True)
    key_in_source = models.CharField(max_length=255, blank=True, null=True, choices=KEY_IN_SOURCE_CHOICES)
    lines_in_source = models.CharField(max_length=255, blank=True, null=True, choices=LINES_IN_SOURCE_CHOICES)
    attritbuted_person_text_in_source = models.ForeignKey('Person', blank=True, null=True, related_name='attritbuted_person_text_in_source', on_delete=models.CASCADE)
    attritbuted_person_music_in_source = models.ForeignKey('Person', blank=True, null=True, related_name='attritbuted_person_music_in_source', on_delete=models.CASCADE)
    attribution_text_in_source = models.CharField(max_length=255, blank=True, null=True)
    attribution_music_in_source = models.CharField(max_length=255, blank=True, null=True)


class OSHPrintingSequence(models.Model):
    sequence_name = models.CharField(max_length=255, blank=False, null=True)
    book_1 = models.ForeignKey('Book', help_text='ID of a printing unless first printing', blank=True, null=True, related_name = 'book_1', on_delete=models.CASCADE)
    book_2 = models.ForeignKey('Book', help_text='ID of a printing unless last printing', blank=True, null=True, related_name = 'book_2', on_delete=models.CASCADE)

    def __str__(self):
        return self.sequence_name

class PrintingRelationship(models.Model):
    CATEGORY_CHOICES = (
    ('scriptural citation', 'scriptural citation'),
    ('attribution', 'attribution'),
    ('song', 'song'),
    ('hymn', 'hymn'),
    ('alto', 'alto'),
    ('historical note', 'historical note'),
    ('other content', 'other content'),
    )
    TYPE_CHOICES = (
    ('correction', 'correction'),
    ('addition', 'addition'),
    ('alteration', 'alteration'),
    )

    osh_printing_sequence = models.ForeignKey('OSHPrintingSequence', blank=False, null=True, on_delete=models.CASCADE, help_text="Printing where change introduced")
    page = models.ForeignKey('Page', blank=True, null=True, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', blank=True, null=True, on_delete=models.CASCADE)
    text_unit = models.ForeignKey('TextUnit', blank=True, null=True, on_delete=models.CASCADE, help_text = "Section - Page - Sequence")
    pr_category = models.CharField(max_length=255, blank=False, null=True, choices=CATEGORY_CHOICES)
    pr_type = models.CharField(max_length=255, blank=True, null=True, choices=TYPE_CHOICES)

class Contribution(models.Model):
    CONTRIBUTION_CHOICES = (
        ('composer', 'composer'),
        ('arranger', 'arranger'),
        ('hymnwriter', 'hymnwriter'),
        ('hymn revisor', 'hymn revisor'),
        ('hymn selector', 'hymn selector'),
        ('alto', 'alto'),
        ('treble', 'treble'),

    )

    song = models.ForeignKey('Song', blank=False, null=True, on_delete=models.CASCADE)
    contributor = models.ForeignKey('Contributor', blank=False, null=True, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=False, null=True, choices=CONTRIBUTION_CHOICES)
