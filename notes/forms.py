from django import forms
from .models import Topic, Note

class TopicForm(forms.ModelForm):
    """A Form to add topics"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class NoteForm(forms.ModelForm):
    """A Form to add Note"""
    class Meta:
        model = Note
        fields = ['text']
        labels = {'text' : ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80, 'id':'text-area'})}