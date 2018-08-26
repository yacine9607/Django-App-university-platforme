
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class EditProfileForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',

            'password'
        )


class ajouter_etudian(forms.ModelForm):

    class Meta:
       model=Etudiant

       fields=[
         'User',
        'filiere',
         'phone',
         'parcour',

     ]

class upload_cp(forms.ModelForm):
    class Meta:
        model=Pv_cpc
        fields=[
            'responsable_cpc',
            'semestre',
            'description',
            'parcour',
            'file',

        ]


class filiere(forms.ModelForm):
    class Meta:
       model=document_filiere
       fields=[
           'responsable_filiere',
           'description',
           'file'
       ]
class PG(forms.ModelForm):
    class Meta:
       model=document_PG
       fields=[
           'responsable_pg',
           'description',
           'file'
       ]

class scolarite(forms.ModelForm):
    class Meta:
       model=document_scolarite
       fields=[
           'adjoint_scolarite',
           'description',
           'file'
       ]

class chef(forms.ModelForm):
    class Meta:
       model=document_chefDepartement
       fields=[
           'chef_departement',
           'description',
           'file'
       ]

class pedagogie(forms.ModelForm):
    class Meta:
       model=document_pedagogie
       fields=[
           'adjoint_pedagogie',
           'description',
           'file'
       ]

class secretariat(forms.ModelForm):
    class Meta:
       model=document_secretariat
       fields=[
           'adjoint_secretariat',
           'user',
           'description',
           'file'
       ]

class etudiant(forms.ModelForm):
    class Meta:
       model=document_etudiant
       fields=[
           'etudiant',
            'description',
           'file'
       ]

class note(forms.ModelForm):
    class Meta:
       model=fichier_note
       fields=[
           'enseignant',
            'matière',
            'description',
            'file'
       ]



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )



    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user