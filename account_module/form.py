from  django import forms



class registerform(forms.Form):
    username=forms.CharField(
        label='',
        widget=forms.TextInput(attrs={"type":"text",
                                      "class":"form-control",
                                      "placeholder":"نام کاربری خود را وارد کنید "})
    )

    email = forms.CharField(
        label="",
        widget=forms.EmailInput(attrs={
                                      "class": "form-control",
                                      "placeholder": "ایمیل خود را وارد کنید"})
    )



    desc = forms.CharField(
        label="" ,
        widget=forms.PasswordInput(attrs={
                                      "type":"textwrap",
                                      "placeholder":"پیام خود را وارد کنید:",
                                      "id":"پیام شما",
                                      "class":"form-control" ,
                                      "required data-error":"لطفا پیام را وارد کنید"})
    )

