from django import forms
from project.models import Activity


class ActivityForm(forms.ModelForm):
     class Meta:
    # """ Render and process a form based on the Activity model. """
        model = Activity
        fields = ("title", "content", "author", "image")
