from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import logout,login
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[

    url(r'acceuil/$', views.acceuil, name='acceuil'),
    url(r'login/$',login,{'template_name':'accounts\login.html'},name='login'),
    url(r'home/$',views.home,name='home'),
    url(r'logout/$', logout, {'template_name': 'accounts\logout.html'},name='logout'),
    url(r'profile/$', views.view_profile, name='profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^scolarite/$', views.Scolarite, name='scolarite'),
    url(r'^mark-as-read/$', views.mark_all_as_read, name='mark_as_read'),
    url(r'^service_secretariat/$',views.service_secretariat,name="service_secretariat"),
    url(r'^notify_chef/$',views.notify_chef,name="notify_chef"),
    url(r'^notify_Adjoint/$',views.notify_Adjoint,name="notify_Adjoint"),
    url(r'^notify_scolarite/$', views.notify_scolarite, name="notify_scolarite"),
    url(r'^notify_res/$',views.notify_responsable,name="notify_responsable"),
    url(r'^afficher_note/$', views.affiche_note, name="afficher_note"),
    url(r'^emploi_du_temp_et/$', views.emploi_etude, name="emploi_du_temp_et"),
    url(r'^emploi_du_temp_en/$', views.emploi_ens, name="emp_ens"),
    url(r'^emploi_du_temp_et_ex/$', views.emploi_exam_etude, name="emploi_du_temp_et_ex"),
    url(r'^emploi_du_temp_en_ex/$', views.emploi_exam_en, name="emploi_du_temp_en_ex"),
    url(r'^consulter_pv/$', views.pv_cpc, name="pv_cpc"),
    url(r'^pv_filiere/$', views.pv_filiere, name="pv_filiere"),
    url(r'^pv_l1/$', views.pv_l1, name="pv_l1"),
    url(r'^pv_l2/$', views.pv_l2, name="pv_l2"),
    url(r'^pv_l3/$', views.pv_l3, name="pv_l3"),
    url(r'^pv_m1/$', views.pv_m1, name="pv_m1"),
    url(r'^pv_m2/$', views.pv_m2, name="pv_m2"),
    url(r'^liste_l1/$', views.liste_l1, name="liste_l1"),
    url(r'^liste_l2/$', views.liste_l2, name="liste_l2"),
    url(r'^liste_l3/$', views.liste_l3, name="liste_l3"),
    url(r'^liste_m1/$', views.liste_m1, name="liste_m1"),
    url(r'^liste_m2/$', views.liste_m2, name="liste_m2"),
    url(r'^liste_parcour/$',views.liste_parcour,name="liste_parcour"),
    url(r'^Ajouter_etudiant/$', views.save_e, name="ajouter_et"),
    url(r'^Upload_cpc/$', views.upload_cpc, name="upload_cpc"),
    url(r'^document_filiere/$', views.document_F, name="document_f"),
    url(r'^document_scol/$', views.document_scolarite, name="document_scol"),
    url(r'^document_PG/$', views.document_pg, name="document_pg"),
    url(r'^document_chef/$', views.document_chef, name="document_chef"),
    url(r'^document_peda/$', views.document_peda, name="document_peda"),
    url(r'^document_et/$', views.document_et, name="document_et"),
    url(r'^traiter_dossier/$', views.traiter_dossier_chef, name="traiter_dossier_chef"),
    url(r'^traiter_dossier_pg/$', views.traiter_dossier_pg, name="traiter_dossier_pg"),
    url(r'^traiter_dossier_scol/$', views.traiter_dossier_scol, name="traiter_dossier_scol"),
    url(r'^traiter_dossier_f/$', views.traiter_dossier_f, name="traiter_dossier_f"),
    url(r'^traiter_dossier_peda/$', views.traiter_dossier_peda, name="traiter_dossier_peda"),
    url(r'^delete/$', views.delete, name="delete"),
    url(r'^upload_document/$', views.upload_document, name="upload_document"),
    url(r'^dossier_traiter/$', views.dossier_traiter, name="dossier_traiter"),
    url(r'^delete_secretaire/$', views.delete_secretariat, name="delete_secretaire"),
    url(r'^demande_etudiant/$', views.demande_etudiant, name="demande_etudiant"),
    url(r'^suivi_demande/$', views.suivi_de_demande, name="suivi_demande"),
    url(r'^matiere/$', views.matiere_en, name="matiere_en"),
    url(r'^consulter/$', views.consulter, name="consulter"),
    url(r'^liste_doctorat/$',views.liste_doctorat,name='liste_doctorat'),
    url(r'^user/$', views.create_user, name='create_user'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)