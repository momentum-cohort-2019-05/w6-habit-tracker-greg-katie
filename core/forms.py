from django import forms

class NewHabitForm(forms.Form):
    name = forms.CharField(max_length=200, help_text="Declare your new habit here")
    objective = forms.CharField(max_length=500, help_text="Describe your new habit goals")

