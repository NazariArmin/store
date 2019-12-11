from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField
from .models import User
from rest_framework.authtoken.models import Token


class MyUserCreationForm(UserCreationForm):
    first_name = CharField(required=False)
    last_name = CharField(required=False)
    email = CharField(required=False)
    address = CharField(required=False)
    city = CharField(required=False)

    class Meta:
        model = User
        fields = [
            'password1', 'password2', 'username',
            'first_name', 'last_name', 'email', 'address', 'city',
        ]

    def save(self, commit=True):
        this_user = super(MyUserCreationForm, self).save(commit=False)

        this_user.first_name = self.cleaned_data['first_name'] if 'first_name' in self.cleaned_data \
            else ""
        this_user.last_name = self.cleaned_data['last_name'] if 'last_name' in self.cleaned_data \
            else ""
        this_user.email = self.cleaned_data['email'] if 'email' in self.cleaned_data \
            else ""
        this_user.address = self.cleaned_data['address'] if 'address' in self.cleaned_data \
            else ""
        this_user.city = self.cleaned_data['city'] if 'city' in self.cleaned_data \
            else ""

        if commit:
            this_user.save()
        this_token = Token.objects.create(user=this_user)
        return this_user, this_token
