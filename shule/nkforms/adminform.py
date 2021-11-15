from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction 

from shule.models import ShuleUser, Admin, Staff


GENDER = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
    ]


class ShuleAdminSignUpForm(UserCreationForm):
    country = forms.CharField(widget=forms.Select(), required=True)
    state = forms.CharField(widget=forms.Select(), required=True)
    city = forms.CharField(widget=forms.Select(), required=True)

    class Meta(UserCreationForm.Meta):
        model = ShuleUser
        fields = UserCreationForm.Meta.fields + (
                'first_name', 'email',  'phone', 'country', 
                'state', 'city', 'username', 'password1', 'password2',
                )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        admin = Admin.objects.create(user=user, country_id=self.cleaned_data.get('country'), 
                   state_id=self.cleaned_data.get('state'), city_id=self.cleaned_data.get('city'))
        admin.save()
        return user 


# Register cachier.......................................

class RegisterCachierForm(UserCreationForm):
    admin1 = forms.CharField(widget=forms.HiddenInput( attrs={
            'id':'idhidden', 
            'placeholder': 'hidden session...', 
            } 
        ), 
        required=False,
        label='',
    )

    firstname = forms.CharField(widget=forms.TextInput( 
        attrs={
            'placeholder': ''
        }),
        required=False)

    lastname = forms.CharField(widget=forms.TextInput(),required=False)
    nickname = forms.CharField(widget=forms.TextInput(),required=False)
    gender = forms.CharField(max_length=3,widget=forms.Select(choices=GENDER))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}),required=False)
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type': 'text',}))
    address = forms.CharField(max_length=255)
    # username = forms.CharField(widget=forms.TextInput(),required=True)
    # password1 = forms.CharField(widget=forms.PasswordInput(),required=True)
    # password2 = forms.CharField(widget=forms.PasswordInput(),required=True)

    class Meta(UserCreationForm.Meta):
        model = ShuleUser
        fiels = UserCreationForm.Meta.fields + ( 
            'first_name','last_name', 'nick_name', 'email',  'phone', 
            'gender', 'address' 'username', 'password1', 'password2',
        )
    
       

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_cachier = True 
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.email= self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        # user.username =  self.cleaned_data.get('username')
        # user.password = self.cleaned_data.get('password2')
        user.save()
        staff = Staff.objects.create(user=user, admin_id=self.cleaned_data.get('admin1'),
                 nick_name=self.cleaned_data.get('nickname'), gender=self.cleaned_data.get('gender'),
                 address=self.cleaned_data.get('address'))
        staff.save()
        return user 





# Register secretary................

class RegisterSecretaryForm(UserCreationForm):
    admin = forms.CharField(widget=forms.HiddenInput( attrs={
            'id':'idhidden1', 
            'placeholder': 'hidden session...', 
            } 
        ), 
        required=False,
        label='',
    )

    firstname = forms.CharField(widget=forms.TextInput( 
        attrs={
            'placeholder': ''
        }),
        required=False)

    lastname = forms.CharField(widget=forms.TextInput(),required=False)
    nickname = forms.CharField(widget=forms.TextInput(),required=False)
    gender = forms.CharField(max_length=3,widget=forms.Select(choices=GENDER))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}),required=False)
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type': 'text',}))
    address = forms.CharField(max_length=255)

    class Meta(UserCreationForm.Meta):
        model = ShuleUser
        fiels = UserCreationForm.Meta.fields + ( 
            'first_name','last_name', 'nick_name', 'email',  'phone', 
            'gender', 'address' 'username', 'password1', 'password2',
        )
    
       

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_secretary = True 
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.email= self.cleaned_data.get('email')
        user.phone = self.cleaned_data.get('phone')
        
        user.save()
        staff = Staff.objects.create(user=user, admin_id=self.cleaned_data.get('admin'),
                 nick_name=self.cleaned_data.get('nickname'), gender=self.cleaned_data.get('gender'),
                 address=self.cleaned_data.get('address'))
        staff.save()
        return user 


# class RegisterSecretaryForm(UserCreationForm):
#     admin = forms.CharField(widget=forms.HiddenInput( attrs={
#             'id':'idhidden1', 
#             'placeholder': 'hidden session...', 
#             } 
#         ), 
#         required=False,
#         label='',
#     )

#     firstname = forms.CharField(widget=forms.TextInput( 
#         attrs={
#             'placeholder': ''
#         }),
#         required=False)

#     lastname = forms.CharField(widget=forms.TextInput(),required=False)
#     nickname = forms.CharField(widget=forms.TextInput(),required=False)
#     gender = forms.CharField(max_length=3,widget=forms.Select(choices=GENDER))
#     email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}),required=False)
#     phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type': 'text',}))
#     address = forms.CharField(max_length=255)

#     class Meta(UserCreationForm.Meta):
#         model = ShuleUser
#         fiels = UserCreationForm.Meta.fields + ( 
#             'first_name','last_name', 'nick_name', 'email',  'phone', 
#             'gender', 'address' 'username', 'password1', 'password2',
#         )
    
       

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_secretary = True 
#         user.first_name = self.cleaned_data.get('firstname')
#         user.last_name = self.cleaned_data.get('lastname')
#         user.email= self.cleaned_data.get('email')
#         user.phone = self.cleaned_data.get('phone')
#         user.save()
        
#         staff = Staff.objects.create(user=user, admin_id=self.cleaned_data.get('admin'),
#                  nick_name=self.cleaned_data.get('nickname'), gender=self.cleaned_data.get('gender'),
#                  address=self.cleaned_data.get('address'))
#         staff.save()
       
#         return user 




   






   



