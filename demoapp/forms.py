from django import forms

from demoapp.models import task


class dateinput(forms.DateInput):
    input_type = "date"

class taskform(forms.ModelForm):
    Date = forms.DateField(widget=dateinput)
    class Meta:
        model = task
        fields=("__all__")