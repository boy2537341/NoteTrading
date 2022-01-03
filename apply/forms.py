from django import forms
from .models import Person
from django.core.exceptions import ValidationError


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'  # __all__ 表示要全部呈現中所有欄位

        # widget 用來設定介面的呈現
        widgets = {
            'user_account': forms.Select(attrs = {'class': 'form-control'}),
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.TextInput(attrs = {'class': 'form-control'}),
            'score': forms.NumberInput(attrs = {'class': 'form-control'}),
            'memo': forms.Textarea(attrs = {'class': 'form-control', 'Row':'6'},),
            'suggest_id': forms.Select(attrs = {'class': 'form-control'}),
        }

        labels = {
            'user_account': '帳號',
            'name': '姓名',
            'email': 'Email',
            'score': '分數',
            'memo': '留言內容',
            'suggest_id': '滿意度',
        }

    def clean_score(self):
        data = self.cleaned_data['score']

        if data < 0 or data > 100  :
            raise ValidationError('分數需介於0~100之間')

        return data

    def clean_memo(self):
        data = self.cleaned_data['memo']

        if str(data)[0].isupper() != True :
            raise ValidationError('第一個字母不是大寫')

        if len(data) < 20 :
            raise ValidationError('留言內容不可小於20字')

        return data      