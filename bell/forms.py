from django import forms
from django.forms import ModelForm
from bell.models import Visitor


TOPIC_CHOICES = (
    ('general', 'General Enquiry'),
    ('bug', 'Bug Report'),
    ('suggestions', 'Suggestions'),
)


class ContactForm (forms.Form):
    subject = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField(widget=forms.Textarea(), initial='Write your feedback here!')
    email = forms.EmailField(required=False)


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = '__all__'


class VisitorEditForm(forms.Form):
    name = forms.CharField(max_length=200)
    surname = forms.CharField(max_length=200)
    welcome = forms.BooleanField()


