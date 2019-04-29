from django import forms
from app.models import SourceRelationship, PrintingRelationship

class SourceRelationshipAdminForm(forms.ModelForm):
    class Meta:
        model = SourceRelationship
        fields = '__all__'

    def clean(self):
        song = self.cleaned_data.get('song')
        text_unit = self.cleaned_data.get('text_unit')
        if not song and not text_unit:
            raise forms.ValidationError('A value for either song or text_unit is required')
        if song and text_unit:
            raise forms.ValidationError('Enter a value for either song or text_unit but not both')
        return self.cleaned_data


class PrintingRelationshipAdminForm(forms.ModelForm):
    class Meta:
        model = PrintingRelationship
        fields = '__all__'

    def clean(self):
        page = self.cleaned_data.get('page')
        song = self.cleaned_data.get('song')
        text_unit = self.cleaned_data.get('text_unit')
        options = []
        if page:
            options.append(page)
        if song:
            options.append(song)
        if text_unit:
            options.append(text_unit)
        if len(options) != 2:
            raise forms.ValidationError('One and only one of page, song, and text unit should be blank')
        return self.cleaned_data
