from django import forms

from inWhite.models import Property


class CreateNewProperty(forms.Form):
    name = forms.CharField(label="Property Name:", max_length=46)
    PROPERTY_TYPE_CHOICES = Property.PROPERTY_TYPE_CHOICES
    property_type = forms.ChoiceField(choices=PROPERTY_TYPE_CHOICES)
    area = forms.IntegerField(label="| Area:", help_text='M sq')
    address = forms.CharField(label="Address:", max_length=200)
    description = forms.CharField(label="Description:", max_length=400)
    photo = forms.ImageField(required=False)

    def clean_property(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data.get('name')
        return name
