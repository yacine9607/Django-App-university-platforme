from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from accounts.models import *
from django.http import *
from notifications.signals import notify
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import UserCreationForm


def acceuil(request):
    return render(request, 'accounts/home/acceuil.html')


@login_required
def mark_all_as_read(request):
    request.user.notifications.mark_all_as_read()
    _next = request.GET.get('next')

    if _next:
        return redirect(_next)
    return redirect(reverse('home'))




@login_required
def home(request):
   for chef in Chef_Departement.objects.all():
       if chef.User.get_full_name()== request.user.get_full_name():
           return render(request, 'accounts/home/chef departement.html')

   for fil in Responsable_Filière.objects.all():
       if fil.User.get_full_name()==request.user.get_full_name():
           return render(request, 'accounts/home/responsabe filiere.html')

   for pg in Adjoint_PG.objects.all():
       if pg.User.get_full_name()==request.user.get_full_name():
           return render(request, 'accounts/home/responsable pg.html')

   for pg in Adjoint_pédagogie.objects.all():
       if pg.User.get_full_name()==request.user.get_full_name():
           return render(request, 'accounts/home/Responsable_Pedagogie.html')

   for sc in Adjoint_secrétariat.objects.all():
       if sc.User.get_full_name() == request.user.get_full_name():
           return render(request, 'accounts/home/secretaire.html')
   for sc in Adjoint_scolarité.objects.all():
           if sc.User.get_full_name() == request.user.get_full_name():
               return render(request, 'accounts/home/Adjoint_scolarite.html')

   for cpc in Responsable_CPC.objects.all():
       if cpc.enseignant.User.get_full_name() == request.user.get_full_name():
           return render(request, 'accounts/home/President cpc.html')

   for mat in Responsable_Matière.objects.all():
       if mat.enseignant.User.get_full_name() == request.user.get_full_name():
           return render(request, 'accounts/home/responsabe matiere.html')

   for enseignant in Enseignant.objects.all():
       if enseignant.User.get_full_name()== request.user.get_full_name():
           return render(request, 'accounts/home/enseignant.html')


   for etudiant in Etudiant.objects.all():
         if etudiant.User.get_full_name() == request.user.get_full_name():

                   return render(request, 'accounts/home/etudiant.html')


@login_required
def liste_doctorat(request):
    par=parcour.objects.filter(nom='Doctorant')
    etudiant=Etudiant.objects.filter(parcour=par)

    return render(request,'accounts/PV/liste.html',{'etudiant':etudiant})


@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)



@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('home'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)




@login_required
def Scolarite(request, pk=None):
           for etudiant in Etudiant.objects.all():
               if etudiant.User.get_full_name() == "Rahmani Taha":
                     notify.send(request.user, recipient=etudiant.User, verb='scolarite')




           return render(request,'accounts/te_en/scolarité.html')


@login_required
def service_secretariat(request):
    return render(request,'accounts/Service_Secretariat.html')





@login_required
def notify_chef(request):

      for chef in Chef_Departement.objects.all():
           notify.send(request.user, recipient=chef.User, verb='Un dossier doit etre traiter')
           messages.success(request, '"Notification envoyé !."')
           return render(request, 'accounts/Service_Secretariat.html')




@login_required
def notify_responsable(request):
    for res in Responsable_Filière.objects.all():
        notify.send(request.user, recipient=res.User, verb='Un dossier doit etre traiter')
        messages.success(request, '"Notification envoyé !."')
        return render(request, 'accounts/Service_Secretariat.html')


@login_required
def notify_Adjoint(request):
    for adjoint in Adjoint_PG.objects.all():
        notify.send(request.user, recipient=adjoint.User, verb='Un dossier doit etre traiter')
        messages.success(request, '"Notification envoyé !."')
        return render(request, 'accounts/Service_Secretariat.html')

@login_required
def notify_scolarite(request):
    for adjoint in Adjoint_scolarité.objects.all():
        notify.send(request.user, recipient=adjoint.User, verb='Un dossier doit etre traiter')
        messages.success(request, '"Notification envoyé !."')
        return render(request, 'accounts/Service_Secretariat.html')



    for sec in Adjoint_secrétariat.objects.all():
        notify.send(request.user, recipient=sec.User, verb='le dossier a été traiter')
        messages.success(request, '"Notification envoyé !."')
        return redirect(reverse('home'))


notes={}
@login_required
def affiche_note(request):
    for etudiant in Etudiant.objects.all():
        if etudiant.User.get_full_name() == request.user.get_full_name():

            notes=Notes.objects.filter(etudiant=etudiant)
            parcours=parcour.objects.filter(etudiant=etudiant)

            return render(request, 'accounts/afficher_note.html',{'notes':notes,'parcour':parcours})




@login_required
def emploi_etude(request):
    for etudiant in Etudiant.objects.all():
        if etudiant.User.get_full_name() == request.user.get_full_name():
            t = etudiant.parcour


            empli=Emploi_du_temp_etudiant.objects.filter(parcour=t)
            sem1=empli.filter(semestre="semestre1")
            sem2 = empli.filter(semestre="semestre2")
            return render(request,'accounts/emploi_du_temp_et.html',{'sem1':sem1,'sem2':sem2})


@login_required
def emploi_exam_etude(request):
    for etudiant in Etudiant.objects.all():
        if etudiant.User.get_full_name() == request.user.get_full_name():
            t = etudiant.parcour


            empli=Emploi_du_temp_examin_etudiant.objects.filter(parcour=t)
            return render(request,'accounts/emploi_et_ex.html',{'emploi':empli})

@login_required
def emploi_exam_en(request):
    for en in Enseignant.objects.all():
        if en.User.get_full_name() == request.user.get_full_name():
            enseigant=en


            empli=Emploi_du_temp_examin_enseignant.objects.filter(enseignant=enseigant)
            return render(request,'accounts/emploi_exem_en.html',{'emploi':empli})

@login_required
def emploi_ens(request):
    for ens in Enseignant.objects.all():
        if ens.User.get_full_name()==request.user.get_full_name():

            emploi=Emploi_du_temp_enseignant.objects.filter(enseignant=ens)
            sem1=emploi.filter(semestre='semestre1')
            sem2= emploi.filter(semestre='semestre2')
            return render(request, 'accounts/empli_en.html', {'sem1':sem1,'sem2':sem2})


@login_required
def pv_cpc(request):
    for Res in Responsable_CPC.objects.all():
        if Res.enseignant.User.get_full_name() == request.user.get_full_name():
            image_list_1 = Res.images.filter(semestre='semestre1')
            image_list_2 = Res.images.filter(semestre='semestre2')



            return render(request,'accounts/consulter_pv.html',{'semestre1':image_list_1,'semestre2':image_list_2})

@login_required
def pv_filiere(request):
    for fil in Responsable_Filière.objects.all():
        if fil.User.get_full_name() == request.user.get_full_name():
            return render(request, 'accounts/pv_filiere.html')
    for chef in Chef_Departement.objects.all():
        if chef.User.get_full_name() == request.user.get_full_name():
            return render(request, 'accounts/pv_filiere.html')

@login_required
def pv_l1(request):
     pv = Pv_cpc.objects.filter(parcour='L1')
     image_list_1 = pv.objects.filter(semestre='semestre1')
     image_list_2 = pv.objects.filter(semestre='semestre2')
     return render(request, 'accounts/PV/pv_L1.html',{'semestre1':image_list_1,'semestre2':image_list_2})

@login_required
def pv_l2(request):
     pv = Pv_cpc.objects.filter(parcour='L2')
     image_list_1 = pv.objects.filter(semestre='semestre1')
     image_list_2 = pv.objects.filter(semestre='semestre2')
     return render(request, 'accounts/PV/pv_L1.html',{'semestre1':image_list_1,'semestre2':image_list_2})
@login_required
def pv_l3(request):
     pv = Pv_cpc.objects.filter(parcour='L3')
     image_list_1 = pv.filter(semestre='semestre1')
     image_list_2 = pv.filter(semestre='semestre2')
     return render(request, 'accounts/PV/pv_L1.html',{'semestre1':image_list_1,'semestre2':image_list_2})
@login_required
def pv_m1(request):
     pv = Pv_cpc.objects.filter(parcour='M1')
     image_list_1 = pv.objects.filter(semestre='semestre1')
     image_list_2 = pv.objects.filter(semestre='semestre2')
     return render(request, 'accounts/PV/pv_L1.html',{'semestre1':image_list_1,'semestre2':image_list_2})


@login_required
def pv_m2(request):

     pv = Pv_cpc.objects.filter(parcour='M2')
     image_list_1 = pv.objects.filter(semestre='semestre1')
     image_list_2 = pv.objects.filter(semestre='semestre2')
     return render(request, 'accounts/PV/pv_L1.html',{'semestre1':image_list_1,'semestre2':image_list_2})


@login_required
def liste_parcour(request):
    return render(request,'accounts/liste_parcour.html')


@login_required
def liste_l1(request):
    prc = parcour.objects.filter(nom="L1")
    etudiant=Etudiant.objects.filter(parcour=prc)
    return render(request,'accounts/PV/liste.html',{'etudiant':etudiant})

@login_required
def liste_l2(request):
    prc = parcour.objects.filter(nom="L2")
    etudiant=Etudiant.objects.filter(parcour=prc)
    return render(request,'accounts/PV/liste.html',{'etudiant':etudiant})

@login_required
def liste_l3(request):
    prc=parcour.objects.filter(nom="L3")
    etudiant=Etudiant.objects.filter(parcour=prc)

    return render(request,'accounts/PV/liste.html',{'etudiant':etudiant})

@login_required
def liste_m1(request):
    prc = parcour.objects.filter(nom="M1")
    etudiant=Etudiant.objects.filter(parcour=prc)
    return render(request,'accounts/PV/liste.html',{'etudiant':etudiant})

@login_required
def liste_m2(request):
    prc = parcour.objects.filter(nom="M2")
    etudiant=Etudiant.objects.filter(parcour=prc)
    return render(request,'accounts/PV/liste.html',{'etudiant':etudiant})


@login_required
def save_e(request):
    if request.method == 'POST':
        form = ajouter_etudian(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, '"Ajouter avec Succée!."')
            return redirect(reverse('create_user'))
    else:
        form = ajouter_etudian()
    return render(request, 'accounts/ajouter_etudiant.html', {'form': form})



@login_required
def upload_cpc(request):

        if request.method == 'POST':
            form = upload_cp(request.POST, request.FILES)
            if form.is_valid():

                form.save()
                messages.success(request, '"Ajouter avec Succée!."')
                return redirect(reverse('upload_cpc'))
        else:
            form = upload_cp()
        return render(request, 'accounts/upload_cpc.html', {'form': form})

@login_required
def document_F(request):



        if request.method == 'POST':
            form = filiere(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                name = form.cleaned_data['responsable_filiere']
                notify.send(request.user, recipient=name.User, verb='Un dossier Doit etre traiter')
                messages.success(request,name.User, '"Document envoyé avec Succée!."')
                return redirect(reverse('home'))
        else:
            form = filiere()
        return render(request, 'accounts/document_filiere.html', {'form': form})

@login_required
def document_pg(request):


    if request.method == 'POST':
        form = PG(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['responsable_pg']
            notify.send(request.user, recipient=name.User, verb='Un dossier Doit etre traiter')
            messages.success(request, '"Document envoyé avec Succée!."')
            return redirect(reverse('home'))
    else:
        form = PG()
    return render(request, 'accounts/document_pg.html', {'form': form})

@login_required
def document_peda(request):


    if request.method == 'POST':
        form = pedagogie(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['adjoint_pedagogie']
            notify.send(request.user, recipient=name.User, verb='Un dossier Doit etre traiter')
            messages.success(request, '"Document envoyé avec Succée!."')
            return redirect(reverse('home'))
    else:
        form = pedagogie()
    return render(request, 'accounts/document_pedagogie.html', {'form': form})

@login_required
def document_scol(request):
    if request.method == 'POST':
        form = scolarite(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['adjoint_scolarite']
            notify.send(request.user, recipient=name.User, verb='Un dossier Doit etre traiter')
            messages.success(request, '"Document envoyé avec Succée!."')
            return redirect(reverse('home'))
    else:
        form = scolarite()
    return render(request, 'accounts/document_scolarite.html', {'form': form})

@login_required
def document_chef(request):


    if request.method == 'POST':
        form = chef(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['chef_departement']
            notify.send(request.user, recipient=name.User, verb='Un dossier Doit etre traiter')
            messages.success(request, '"Document envoyé avec Succée!."')
            return redirect(reverse('home'))
    else:
        form = chef()
    return render(request, 'accounts/document_chef.html', {'form': form})

@login_required
def document_et(request):


    if request.method == 'POST':
        form = etudiant(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['etudiant']
            notify.send(request.user, recipient=name.User, verb='votre demande a été traiter')
            messages.success(request, '"Document envoyé avec Succée!."')
            return redirect(reverse('home'))
    else:
        form = etudiant()
    return render(request, 'accounts/document_et.html', {'form': form})

@login_required
def traiter_dossier_f(request):
    for fil in Responsable_Filière.objects.all():
        if fil.User.get_full_name() == request.user.get_full_name():
              document=document_filiere.objects.filter(responsable_filiere=fil)
    return render(request,'accounts/PV/traiter.html',{'document':document})
@login_required
def traiter_dossier_chef(request):
    for chef in Chef_Departement.objects.all():
        if chef.User.get_full_name() == request.user.get_full_name():
           document=document_chefDepartement.objects.filter(chef_departement=chef)
    return render(request,'accounts/PV/traiter.html',{'document':document})

@login_required
def traiter_dossier_pg(request):
    for pg in Adjoint_PG.objects.all():
        if pg.User.get_full_name() == request.user.get_full_name():
                 document=document_PG.objects.filter(responsable_pg=pg)
    return render(request,'accounts/PV/traiter.html',{'document':document})

@login_required
def traiter_dossier_scol(request):
    for sc in Adjoint_scolarité.objects.all():
        if sc.User.get_full_name() == request.user.get_full_name():
              document=document_scolarite.objects.filter(adjoint_scolarite=sc)
    return render(request,'accounts/PV/traiter.html',{'document':document})

@login_required
def traiter_dossier_peda(request):
    for pg in Adjoint_pédagogie.objects.all():
        if pg.User.get_full_name() == request.user.get_full_name():
             document=document_pedagogie.objects.filter(adjoint_pedagogie=pg)
    return render(request,'accounts/PV/traiter.html',{'document':document})


@login_required
def delete(request):
    for chef in Chef_Departement.objects.all():
        if chef.User.get_full_name() == request.user.get_full_name():
            dele=document_chefDepartement.objects.filter(chef_departement=chef)
            dele.delete()
            for sec in Adjoint_secrétariat.objects.all():
                notify.send(request.user, recipient=sec.User, verb='le dossier est en cour de traitement')
                messages.success(request, '"Liste Vidé !."')
                return redirect(reverse('home'))


    for fil in Responsable_Filière.objects.all():
        if fil.User.get_full_name() == request.user.get_full_name():
            dele = document_filiere.objects.filter(responsable_filiere=fil)
            dele.delete()
            for sec in Adjoint_secrétariat.objects.all():
                notify.send(request.user, recipient=sec.User, verb='le dossier est en cour de traitement')
                messages.success(request, '"Liste Vidé !."')
                return redirect(reverse('home'))

    for pg in Adjoint_PG.objects.all():
        if pg.User.get_full_name() == request.user.get_full_name():
            dele = document_PG.objects.filter(adjoint_pg=pg)
            dele.delete()
            for sec in Adjoint_secrétariat.objects.all():
                notify.send(request.user, recipient=sec.User, verb='le dossier est en cour de traitement')
                messages.success(request, '"Liste Vidé !."')
                return redirect(reverse('home'))

    for sc in Adjoint_scolarité.objects.all():
        if sc.User.get_full_name() == request.user.get_full_name():
            dele = document_scolarite.objects.filter(adjoint_scolarite=sc)
            dele.delete()
            for sec in Adjoint_secrétariat.objects.all():
                notify.send(request.user, recipient=sec.User, verb='le dossier est en cour de traitement')
                messages.success(request, '"Liste Vidé !."')
                return redirect(reverse('home'))

    for pg in Adjoint_pédagogie.objects.all():
        if pg.User.get_full_name() == request.user.get_full_name():
            dele = document_PG.objects.filter(adjoint_pedagogie=pg)
            dele.delete()
            for sec in Adjoint_secrétariat.objects.all():
                notify.send(request.user, recipient=sec.User, verb='le dossier est en cour de traitement')
                messages.success(request, '"Liste Vidé !."')
                return redirect(reverse('home'))
    for pg in Etudiant.objects.all():
        if pg.User.get_full_name() == request.user.get_full_name():
            dele = document_etudiant.objects.filter(etudiant=pg)
            dele.delete()
            return redirect(reverse('home'))


@login_required
def upload_document(request):


    if request.method == 'POST':
        form = secretariat(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name =form.cleaned_data['adjoint_secretariat']
            notify.send(request.user, recipient=name.User, verb='le dossier a été traiter')
            messages.success(request, '"Document envoyé avec Succée!."')
            return redirect(reverse('home'))
    else:
        form = secretariat()
    return render(request, 'accounts/upload_document.html', {'form': form})


@login_required
def dossier_traiter(request):
    document=document_secretariat.objects.all()
    return render(request,'accounts/PV/dossier_traiter.html',{'document':document})


@login_required
def delete_secretariat(request):
    for sc in Adjoint_secrétariat.objects.all():
        if sc.User.get_full_name() == request.user.get_full_name():
            dele = document_secretariat.objects.filter(adjoint_secretariat=sc)
            dele.delete()
            messages.success(request, '"Liste Vidé !."')
            return redirect(reverse('home'))



@login_required
def demande_etudiant(request):
    responsable = Adjoint_secrétariat.objects.all()

    if request.method == 'POST':
        form = secretariat(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            for res in responsable:
                notify.send(request.user, recipient=res.User, verb='une demande Etudiant a traité')
            messages.success(request, '"Document envoyé avec Succée!."')

            return redirect(reverse('home'))
    else:
        form = secretariat()
    return render(request, 'accounts/upload_document.html', {'form': form})

@login_required
def suivi_de_demande(request):
    for et in Etudiant.objects.all():
        if et.User.get_full_name() == request.user.get_full_name():
            document=document_etudiant.objects.filter(etudiant=et)

            return render(request, 'accounts/suivi_de_demande.html', {'document': document})


@login_required
def matiere_en(request):
    if request.method == 'POST':
        form = note(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, '"Document Enregistrer avec Succée!."')
            return redirect(reverse('matiere_en'))
    else:
        form = note()
    return render(request, 'accounts/matiere_en.html', {'form': form})


@login_required
def consulter(request):
    note = []
    tall=[]
    i=0
    for en in Enseignant.objects.all():
        if en.User.get_full_name()==request.user.get_full_name():
            enseignant=en

    matiere=Matière.objects.filter(enseignat=enseignant)
    for mat in matiere.all():
        nt=Notes.objects.filter(matière=mat)
        note.append(nt)
        i=i+1
        tall.append(i)


    return render(request, 'accounts/consulter_note.html', {'note':note,'range':tall})



@login_required
def create_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '"utilisateur crée avec Succée!."')
            return redirect (reverse('ajouter_et'))
    else:
        form = RegistrationForm()
        return render(request, 'accounts/create_user.html', {'form': form})


