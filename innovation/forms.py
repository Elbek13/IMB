from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'video']  # 'video' qo'shildi
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            # 'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'video': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'title': 'Sarlavha',
            'content': 'Matn',
            # 'image': 'Rasm',
            'video': 'Video',
        }
