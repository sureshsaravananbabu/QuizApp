from django import forms
from Quiz.models import Question,Quiz
class Createform(forms.Form):
    Title = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter the Title'}))

    def clean_Title(self):
        print(type(self.cleaned_data))
        a=Quiz.objects.filter(Title=self.cleaned_data.get('Title'))
        if a:
            raise forms.ValidationError("Title with this Quiz is Already exist")
        else:
            return a