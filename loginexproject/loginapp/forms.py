from django import forms
from .models import Login

class Login(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['trinity_id', 'trinity_password']
        widgets = {
            'trinity_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '아이디'
                }
            ),
            'trinity_password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '비밀번호'
                }
            )
        }