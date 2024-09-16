from django import forms

from blog.models import Post, Category


class LeaveMessageForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, label='Ваше имя')
    email = forms.EmailField(label='Почта', required=False)
    need_answer = forms.BooleanField(label='Нужна обратная связь', required=False)
    content = forms.CharField(label='Ваше сообщение', widget=forms.Textarea(attrs=
                                                                            {'cols': 50,
                                                                             'rows': 5}))



class LeaveComment(forms.Form):
    comment = forms.CharField(max_length=255, min_length=5, label='Комментарий', widget=forms.Textarea(
        attrs={'class': 'comment',
               'placeholder': 'Напишите ваш комментарий...',
               'cols': 50, 'rows': 5}))



class AddArticle(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана')
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'status']
        labels = {
            'title': 'Заголовок',
            'content': 'Содержимое',
            'category': 'Категория',
            'status': 'Статус',
        }
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }