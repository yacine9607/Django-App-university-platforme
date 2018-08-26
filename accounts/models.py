from django.db import models
from django.contrib.auth.models import User



niveau = (('L1', 'L1'), ('L2', 'L2'), ('L3', 'L3'), ('M1', 'M1'), ('M2', 'M2'), ('Doctorant', 'Doctorant'))
semestre = (('semestre1', 'semestre1'), ('semestre2', 'semestre2'))
grade=(('Assistant','Assistant'),('Maitre assistant B','Maitre assistant B'),('Maitre assistant A','Maitre assistant A'),
       ('Maitre conference B','Maitre conference B'),('Maitre conference A','Maitre conference A'),('Professeur','Professeur'))





class Enseignant(models.Model):
    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    grade = models.CharField(max_length=25, choices=grade, default='Assistant')
    phone = models.CharField(max_length=15, default='')


    def __str__(self):
          return self.User.get_full_name()

    class Meta:
        ordering = ('grade',)



class Emploi_du_temp_enseignant(models.Model):
    enseignant = models.OneToOneField(
        Enseignant,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    description = models.CharField(max_length=255, blank=True)
    semestre = models.CharField(max_length=9, choices=semestre, default='semestre1')
    Dimanche_S1 = models.TextField(max_length=255, blank=True)
    Dimanche_S2 = models.TextField(max_length=255, blank=True)
    Dimanche_S3 = models.TextField(max_length=255, blank=True)
    Dimanche_S4 = models.TextField(max_length=255, blank=True)
    Lundi_S1 = models.TextField(max_length=255, blank=True)
    Lundi_S2 = models.TextField(max_length=255, blank=True)
    Lundi_S3 = models.TextField(max_length=255, blank=True)
    Lundi_S4 = models.TextField(max_length=255, blank=True)
    Mardi_S1 = models.TextField(max_length=255, blank=True)
    Mardi_S2 = models.TextField(max_length=255, blank=True)
    Mardi_S3 = models.TextField(max_length=255, blank=True)
    Mardi_S4 = models.TextField(max_length=255, blank=True)
    Mercredi_S1 = models.TextField(max_length=255, blank=True)
    Mercredi_S2 = models.TextField(max_length=255, blank=True)
    Mercredi_S3 = models.TextField(max_length=255, blank=True)
    Mercredi_S4 = models.TextField(max_length=255, blank=True)
    Jeudi_S1 = models.TextField(max_length=255, blank=True)
    Jeudi_S2 = models.TextField(max_length=255, blank=True)
    Jeudi_S3 = models.TextField(max_length=255, blank=True)
    Jeudi_S4 = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return "Emploi du temp "+self.enseignant.User.get_full_name()






class Emploi_du_temp_examin_enseignant(models.Model):
    enseignant = models.OneToOneField(
        Enseignant,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    description = models.CharField(max_length=255, blank=True)

    Dimanche=models.TextField(max_length=255,blank=True)
    Lundi = models.TextField(max_length=255, blank=True)
    Mardi = models.TextField(max_length=255, blank=True)
    Mercredi = models.TextField(max_length=255, blank=True)
    Jeudi = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return "Emploi du temp " + self.enseignant.User.get_full_name()



class parcour(models.Model):

    nom=models.CharField(max_length=10,choices=niveau)

    def __str__(self):
        return self.nom

class Etudiant(models.Model):

    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    filiere = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=15, default='')
    parcour = models.ForeignKey(parcour, on_delete=models.CASCADE)



    def __str__(self):
          return self.User.get_full_name()





class Matière(models.Model):

    enseignat = models.ManyToManyField(Enseignant,)
    Nom_Mat = models.CharField(max_length=100, default='')
    Parcour =models.ForeignKey(parcour, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=9, choices=semestre, default='semestre1')



    def __str__(self):
          return self.Nom_Mat+' '+self.Parcour.nom

    class Meta:
        ordering = ('Nom_Mat',)

class Emploi_du_temp_etudiant(models.Model):
    description = models.CharField(max_length=255, blank=True)
    parcour=models.ForeignKey(parcour, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=9, choices=semestre, default='semestre1')
    Dimanche_S1 = models.TextField(max_length=255, blank=True)
    Dimanche_S2 = models.TextField(max_length=255, blank=True)
    Dimanche_S3 = models.TextField(max_length=255, blank=True)
    Dimanche_S4 = models.TextField(max_length=255, blank=True)
    Lundi_S1 = models.TextField(max_length=255, blank=True)
    Lundi_S2 = models.TextField(max_length=255, blank=True)
    Lundi_S3 = models.TextField(max_length=255, blank=True)
    Lundi_S4 = models.TextField(max_length=255, blank=True)
    Mardi_S1 = models.TextField(max_length=255, blank=True)
    Mardi_S2 = models.TextField(max_length=255, blank=True)
    Mardi_S3 = models.TextField(max_length=255, blank=True)
    Mardi_S4 = models.TextField(max_length=255, blank=True)
    Mercredi_S1 = models.TextField(max_length=255, blank=True)
    Mercredi_S2 = models.TextField(max_length=255, blank=True)
    Mercredi_S3 = models.TextField(max_length=255, blank=True)
    Mercredi_S4 = models.TextField(max_length=255, blank=True)
    Jeudi_S1 = models.TextField(max_length=255, blank=True)
    Jeudi_S2 = models.TextField(max_length=255, blank=True)
    Jeudi_S3 = models.TextField(max_length=255, blank=True)
    Jeudi_S4 = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return "Emploi_du_temp_etudiant "+self.parcour.nom


class Emploi_du_temp_examin_etudiant(models.Model):
    description = models.CharField(max_length=255, blank=True)
    parcour = models.ForeignKey(parcour, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=9, choices=semestre, default='semestre1')
    Dimanche = models.TextField(max_length=255, blank=True)
    Lundi = models.TextField(max_length=255, blank=True)
    Mardi = models.TextField(max_length=255, blank=True)
    Mercredi = models.TextField(max_length=255, blank=True)
    Jeudi = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return "Emploi_du_temp_examin_etudiant "+self.parcour.nom



class Notes(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE,related_name='notes')
    matière = models.ForeignKey(Matière, on_delete=models.CASCADE,related_name='Notes')
    semestre = models.CharField(max_length=9, choices=semestre, default='semestre1')
    note_CC= models.FloatField( default=0.0)
    note_examin= models.FloatField( default=0.0)
    note_ratrappage= models.FloatField(default=0.0)


    def __str__(self):
         return self.etudiant.User.get_full_name()+'      '+self.matière.Nom_Mat+'      '+self.matière.Parcour.nom


    class Meta:
        ordering = ('note_CC',)

class Responsable_CPC(models.Model):
    enseignant= models.OneToOneField(
        Enseignant,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    parcour = models.ForeignKey(parcour, on_delete=models.CASCADE)

    def __str__(self):
        return self.enseignant.User.get_full_name()+' '+self.parcour.nom




class Pv_cpc(models.Model):
    responsable_cpc = models.ForeignKey(Responsable_CPC, on_delete=models.CASCADE,related_name='images')
    file=models.FileField(upload_to='pv_cpc/')
    semestre = models.CharField(max_length=9, choices=semestre, default='semestre1')
    description = models.CharField(max_length=50, default='')
    parcour = models.CharField(max_length=9, choices=niveau, default='semestre1')

    def __str__(self):
        return self.description+' '+self.semestre+' '+ self.responsable_cpc.parcour.nom

class Responsable_Matière(models.Model):
    enseignant = models.ForeignKey(
        Enseignant, on_delete=models.CASCADE)

    matière = models.ForeignKey( Matière, on_delete=models.CASCADE)



    def __str__(self):
        return self.enseignant.User.get_full_name()+' '+self.matière.Nom_Mat


class Responsable_Filière(models.Model):
    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.User.get_full_name()

class Chef_Departement(models.Model):
    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.User.get_full_name()

class Adjoint_secrétariat(models.Model):
    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.User.get_full_name()

class Adjoint_PG(models.Model):
    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.User.get_full_name()

class Adjoint_pédagogie(models.Model):
    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.User.get_full_name()

class Adjoint_scolarité(models.Model):
    User = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.User.get_full_name()

class document_filiere(models.Model):
    responsable_filiere= models.ForeignKey( Responsable_Filière, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    file=models.FileField(upload_to='document_filiere/')

class document_PG(models.Model):
    responsable_pg= models.ForeignKey( Adjoint_PG, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    file=models.FileField(upload_to='document_PG/')

class document_scolarite(models.Model):
    adjoint_scolarite= models.ForeignKey( Adjoint_scolarité, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    file=models.FileField(upload_to='document_scol/')

class document_chefDepartement(models.Model):
    chef_departement= models.ForeignKey( Chef_Departement, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    file=models.FileField(upload_to='document_chef/')

class document_pedagogie(models.Model):
    adjoint_pedagogie= models.ForeignKey( Adjoint_pédagogie, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    file=models.FileField(upload_to='document_pedagogie/')

class document_etudiant(models.Model):
    etudiant= models.ForeignKey( Etudiant, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    file=models.FileField(upload_to='document_Etudiant/')

class document_secretariat(models.Model):
    adjoint_secretariat= models.ForeignKey(Adjoint_secrétariat, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    file=models.FileField(upload_to='document_secretariat/')

class fichier_note(models.Model):
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    matière= models.ForeignKey(Matière, on_delete=models.CASCADE)
    description = models.CharField(max_length=50, default='')
    file = models.FileField(upload_to='document_secretariat/')

    def __str__(self):
        return self.matière.Nom_Mat+' '+self.enseignant.User.get_full_name()










def save(self, *args, **kwargs):
    if not self.pk:
        try:
            s=Enseignant.objects.get(user=self.user)
            e = Etudiant.objects.get(user=self.user)
            self.pk = s.pk
            self.pk=e.pk
        except Etudiant.DoesNotExist | Enseignant.DoesNotExist :
            pass
