from django.contrib import admin
from app.models import Page, TextUnit, Song, Book, Contributor, SourceRelationship, OSHPrintingSequence, PrintingRelationship, Contribution
from app.forms import SourceRelationshipAdminForm, PrintingRelationshipAdminForm

class PageAdmin(admin.ModelAdmin):
    list_display = ('seq', 'number', 'book', 'typography')

class TextUnitAdmin(admin.ModelAdmin):
    list_display = ('page', 'seq', 'value', 'section', 'subsection')

class SongAdmin(admin.ModelAdmin):
    list_display = ('page_start_id', 'page_end_id', 'title', 'lines')

class BookAdmin(admin.ModelAdmin):
    list_display = ('abbreviated_title', 'year_range_start', 'year_range_end', 'year_certainty', 'place', 'publisher', 'author_editor')

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'book', 'birth_year', 'death_year', 'committee', 'subcommittee')

class SourceRelationshipAdmin(admin.ModelAdmin):
    list_display = ('book', 'song', 'text_unit', 'sr_category', 'sr_type')
    form = SourceRelationshipAdminForm

class OSHPrintingSequenceAdmin(admin.ModelAdmin):
    list_display = ('sequence_name', 'book_1', 'book_2')

class PrintingRelationshipAdmin(admin.ModelAdmin):
    list_display = ('osh_printing_sequence', 'page', 'song', 'text_unit', 'pr_category', 'pr_type')
    form = PrintingRelationshipAdminForm

class ContributionAdmin(admin.ModelAdmin):
    list_display = ('song', 'contributor', 'contribution')

admin.site.register(Page, PageAdmin)
admin.site.register(TextUnit, TextUnitAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(SourceRelationship, SourceRelationshipAdmin)
admin.site.register(OSHPrintingSequence, OSHPrintingSequenceAdmin)
admin.site.register(PrintingRelationship, PrintingRelationshipAdmin)
admin.site.register(Contribution, ContributionAdmin)
