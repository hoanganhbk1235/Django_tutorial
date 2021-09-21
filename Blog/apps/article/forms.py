from django import forms
from .models import Article, Comment, Category, SubCategory
from apps.user.models import UserProf

# way 1: create form don't use model
# class ArticleForm(forms.ModelForm):
#     choice_cate = Category.objects.all()
#     choice_sub_cate = SubCategory.objects.all()
#     users = UserProf.objects.all()
#     title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'title_detail', 'id': 'id_title'}))
#     content =  forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'content-art'}))
#     published =  forms.DateField(widget=forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'date-time'}))
#     id_cate=  forms.ChoiceField(choices=choice_cate)
#     id_sub_cate = forms.ChoiceField(choices=choice_sub_cate)
#     id_user = forms.ChoiceField(choices=users, widget=forms.TextInput(attrs={'class': 'author'}))

# way 2: Aticle Form use model
class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'published', 'id_cate', 'id_sub_cate', 'id_user')

        # add widgets for model form type and create attributes for the each tag to contain data
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title_detail', 'id': 'id_title'}),
            'content': forms.Textarea(attrs={'class': 'content-art'}),
            'published': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'date-time'}),
            'id_user': forms.HiddenInput(attrs={'class': 'user_detail'})
        }

class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'id_cate', 'id_sub_cate')
        # add widgets for model form type and create attributes for the each tag to contain data
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title_detail', 'id': 'id_title'}),
            'content': forms.Textarea(attrs={'class': 'content-art'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('id_article', 'id_user', 'content')
        # add widgets for model form type and create attributes for the each tag to contain data
        widgets = {
            'id_article': forms.HiddenInput(attrs={'class': 'article_'}),
            'id_user': forms.HiddenInput(attrs={'class': 'user_cmt'}),
            'content': forms.TextInput(attrs={'class': 'content-art'})
        }