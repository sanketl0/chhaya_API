
from django.contrib import admin
from django.urls import path
from MissingPersonApp.views import  MissingPersonAPIView, SearchAllMatches, UndefinedMissingPersonAPIView, UnidentifiedBodyAPIView, VolunteerAPIView
from MissingPersonApp.views import ZoneView, DivisionView, SubDivisionView, PoliceStationView, ChowkiView, HospitalView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('volunteer/', VolunteerAPIView.as_view(), name='volunteer-list'),
    path('volunteer/<int:volunteer_id>/', VolunteerAPIView.as_view(), name='volunteer-detail'),
    path('unidentified-bodies/', UnidentifiedBodyAPIView.as_view(), name='unidentified-body-list'),
    path('unidentified-bodies/<int:unidentified_body_id>/', UnidentifiedBodyAPIView.as_view(), name='unidentified-body-detail'),
    path('missing-person/', MissingPersonAPIView.as_view(), name='missing_person_list'),
    path('missing-person/<int:missing_person_id>/', MissingPersonAPIView.as_view(), name='missing_person_detail'),
    path('undefined-missing-persons/', UndefinedMissingPersonAPIView.as_view(), name='undefined_missing_persons'),  # List and create
    path('undefined-missing-persons/<int:undefined_missing_person_id>/', UndefinedMissingPersonAPIView.as_view(), name='undefined_missing_person_detail'),  # Retrieve, update, delete
    path('search-all-matches/', SearchAllMatches.as_view(), name='search_all_matches'),

    
    path('api/zones/', ZoneView.as_view(), name='zone_list_create'),
    path('api/divisions/', DivisionView.as_view(), name='division_list_create'),
    path('api/sub-divisions/', SubDivisionView.as_view(), name='subdivision_list_create'),
    path('api/police-stations/', PoliceStationView.as_view(), name='policestation_list_create'),
    path('api/chowkis/', ChowkiView.as_view(), name='chowki_list_create'),
    path('api/hospitals/', HospitalView.as_view(), name='hospital_list_create'),
    
]



