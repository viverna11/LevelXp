from django import forms
from .models import Post, Comment

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']




class CreateComent(forms.Form):
    comment = forms.CharField(
        label='Comment',
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Enter your comment here...'
        }),
        max_length=500,
        required=True
    )

    def clean_comment(self):
        comment = self.cleaned_data.get('comment')
        if not comment:
            raise forms.ValidationError("Comment cannot be empty.")
        return comment
    

class FilterPostsForm(forms.Form):
    STATUS = [
        ('Enabled', 'Enabled'),
        ('Disabled', 'Disabled')
    ]
    status = forms.ChoiceField(choices=STATUS, required=False, label='Status')

