from django.contrib import admin
from app.models import Page, TextUnit, Song, Book, Contributor, TextSourceRelationship, OSHPrintingSequence, PrintingRelationship, Contribution, Person
from app.forms import TextSourceRelationshipAdminForm, PrintingRelationshipAdminForm
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class SongResource(resources.ModelResource):

    class Meta:
        model = Song
        fields = ('id', 'page_start__number', 'page_end__number', 'page_placement', 'title', 'lines')

class PageAdmin(admin.ModelAdmin):
    list_display = ('seq', 'number', 'book', 'typography')

class TextUnitAdmin(admin.ModelAdmin):
    list_display = ('page', 'seq', 'value', 'section', 'subsection')

class SongAdmin(ImportExportModelAdmin):
    resource_class = SongResource
    list_display = ('id', 'page_start', 'page_end', 'title', 'lines')

class BookAdmin(admin.ModelAdmin):
    list_display = ('abbreviated_title', 'year_range_start', 'year_range_end', 'year_certainty', 'place', 'publisher', 'author_editor')

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'book', 'birth_year', 'death_year', 'committee', 'subcommittee')

class TextSourceRelationshipAdmin(admin.ModelAdmin):
    list_display = ('book', 'song', 'text_unit', 'sr_category', 'sr_type')
    form = TextSourceRelationshipAdminForm

class OSHPrintingSequenceAdmin(admin.ModelAdmin):
    list_display = ('sequence_name', 'book_1', 'book_2')

class PrintingRelationshipAdmin(admin.ModelAdmin):
    list_display = ('osh_printing_sequence', 'page', 'song', 'text_unit', 'pr_category', 'pr_type')
    form = PrintingRelationshipAdminForm

class ContributionAdmin(admin.ModelAdmin):
    list_display = ('song', 'contributor', 'contribution')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_middle_name', 'female', 'alternate_spellings')

admin.site.register(Page, PageAdmin)
admin.site.register(TextUnit, TextUnitAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(TextSourceRelationship, TextSourceRelationshipAdmin)
admin.site.register(OSHPrintingSequence, OSHPrintingSequenceAdmin)
admin.site.register(PrintingRelationship, PrintingRelationshipAdmin)
admin.site.register(Contribution, ContributionAdmin)
admin.site.register(Person, PersonAdmin)
