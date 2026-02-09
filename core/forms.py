from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Ad
class AddAdForm(forms.ModelForm):
    class Meta:
        model=Ad
        fields=['title','description','price','phone','image']
        labels={'title':'عنوان آگهی','description':'توضیحات','price':'قیمت(تومان)',
                'phone':'تلفن تماس',
                'image':'تصویر آگهی'
                }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages={'required':'این فیلد الزامی است'}
            field.widget.attrs['class']='form--control'
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form--control'
