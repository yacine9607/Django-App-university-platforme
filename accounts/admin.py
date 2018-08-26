from django.contrib import admin
from accounts.models import *


class PropertyImageInline(admin.TabularInline):
    model = Pv_cpc
    extra = 1

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]


class PropertyImageInlin(admin.TabularInline):
    model = Notes
    extra = 1



class PropertyAdm(admin.ModelAdmin):
    inlines = [ PropertyImageInlin, ]




admin.site.register(Enseignant)
admin.site.register(Etudiant,PropertyAdm)
admin.site.register(Matière,PropertyAdm)
admin.site.register(Responsable_CPC, PropertyAdmin)
admin.site.register(Chef_Departement)
admin.site.register(Responsable_Filière)
admin.site.register(Responsable_Matière)
admin.site.register(Adjoint_scolarité)
admin.site.register(Adjoint_secrétariat)
admin.site.register(Adjoint_pédagogie)
admin.site.register(Adjoint_PG)
admin.site.register(Emploi_du_temp_examin_enseignant)
admin.site.register(Emploi_du_temp_examin_etudiant)
admin.site.register(Emploi_du_temp_enseignant)
admin.site.register(Emploi_du_temp_etudiant)
admin.site.register(Notes)
admin.site.register(Pv_cpc)
admin.site.register(parcour)
admin.site.register(document_scolarite)
admin.site.register(document_PG)
admin.site.register(document_chefDepartement)
admin.site.register(document_filiere)
admin.site.register(document_secretariat)
admin.site.register(document_pedagogie)
admin.site.register(fichier_note)