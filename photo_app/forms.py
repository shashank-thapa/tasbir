from django import forms
from .models import PostModel, CommentModel

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

class AddNewCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = (
            'text',
        )