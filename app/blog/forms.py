from django import forms
from blog.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "body",
            "status",
        )
        exclude = ("author",)

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author')
        super().__init__(*args, **kwargs)

    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(author=self.author, title=title).exists():
            raise forms.ValidationError("You have already created a post with same title.")
        return title