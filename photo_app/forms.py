from django import forms
from .models import PostModel

class AddNewPostForm(forms.ModelForm):

    location = forms.CharField(
        widget= forms.TextInput(
            attrs={
            'class':"edit-profile__input"
            }
        )
    )

    class Meta:
        model = PostModel
        fields = (
            'location',
            'image',
        )