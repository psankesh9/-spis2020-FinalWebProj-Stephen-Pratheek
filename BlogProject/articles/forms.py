from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

#The form entry for creating a document
class CreateNewArticle (forms.Form):
    title = forms.CharField(max_length=200, label='Title of Document')
    text = SummernoteTextFormField(label='Document Body')

#The form entry for querying the database for a document that is only created by the user
class SearchForm(forms.Form):
    q = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter the Document Name for Search'}), label='')