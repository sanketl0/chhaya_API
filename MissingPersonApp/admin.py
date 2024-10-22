from ast import Match
from django.contrib import admin
from .models import MissingPerson, UndefinedMissingPerson, UnidentifiedBody, Volunteer, Contact, Address,Match



# admin dashboard for voluenteer
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'dob','volunteer_group', 'gender' ,'is_active')
    search_fields = ('full_name', 'contact_numbers', 'email_address')
    list_filter = ('gender', 'blood_group', 'is_active')
    ordering = ('full_name',)
    list_editable = ('is_active',)
    

class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'type','phone_number', 'email', 'is_primary')
    search_fields = ('phone_number', 'email', 'company_name')
    list_filter = ('type', 'is_primary')
    ordering = ('phone_number',)

class AddressAdmin(admin.ModelAdmin):
    list_display = ( 'type','street', 'city', 'state', 'postal_code')
    search_fields = ('street', 'city', 'state')
    list_filter = ('type', 'subtype')
    ordering = ('city',)
    

class UnidentifiedBodyAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'gender',
        'estimated_age',
        'date_found',
        'height',
        'weight',
        'blood_group',
        'is_deleted',
    )
    search_fields = ('full_name', 'gender', 'blood_group', 'police_station_name_and_address')
    list_filter = ('gender', 'blood_group', 'is_deleted')
    ordering = ('-date_found',)
    list_editable = ('is_deleted',) 
    

class MissingPersonAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'age',
        'gender',
        'height',
        'weight',
        'missing_date',
        'is_deleted',
    )
    search_fields = ('full_name', 'reportingperson_name', 'fir_number')
    list_filter = ('gender', 'blood_group', 'missing_date', 'is_deleted')
    ordering = ('-missing_date',)
    list_editable = ('is_deleted',)


class UndefinedMissingPersonAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'estimated_age',
        'gender',
        'height',
        'weight',
        'caste',
        'marital_status',
        'religion',
        'is_active',
    )
    search_fields = ('full_name', 'contact_number', 'reporting_person_name')
    list_filter = ('gender', 'caste', 'marital_status', 'is_active')
    ordering = ('-created_date',)

    fieldsets = (
        (None, {
            'fields': ('full_name', 'estimated_age', 'gender', 'height', 'weight', 'complexion', 'hair_color', 'hair_type', 'eye_color', 'other_distinctive_mark', 'photo_upload')
        }),
        ('Address', {
            'fields': ('address',)
        }),
        ('Contact', {
            'fields': ('contact',)
        }),
        ('Additional Information', {
            'fields': ('caste', 'marital_status', 'religion', 'other_known_languages', 'identification_details')
        }),
        ('Missing Data', {
            'fields': ('last_location', 'last_seen_details', 'condition_at_discovery')
        }),
        ('Reporting Person', {
            'fields': ('reporting_person_name', 'reporting_person_contact_number', 'reporting_person_email', 'relationship_with_victim', 'availability_for_search_operations', 'preferred_mode_of_communication', 'access_to_vehicle', 'special_skills')
        }),
        ('Evidence', {
            'fields': ('upload_evidence',)
        }),
    )

# Register the model with the admin site
admin.site.register(UndefinedMissingPerson, UndefinedMissingPersonAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(UnidentifiedBody, UnidentifiedBodyAdmin)
admin.site.register(MissingPerson, MissingPersonAdmin)



class MatchAdmin(admin.ModelAdmin):
    list_display = ('missing_person', 'undefined_missing_person', 'unidentified_body', 'match_percentage')
    list_filter = ('match_percentage',)
    search_fields = ('missing_person__full_name', 'undefined_missing_person__full_name', 'unidentified_body__full_name')

admin.site.register(Match, MatchAdmin)




































from .models import Zone, Division, SubDivision, PoliceStation, Chowki, Hospital

# Admin for Chowki (Outpost)
class ChowkiAdmin(admin.ModelAdmin):
    list_display = ('name', 'police_station')
    search_fields = ('name',)
    list_filter = ('police_station__name',)

# Admin for Police Station
class PoliceStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'division')
    search_fields = ('name',)
    list_filter = ('division__name', 'division__zone__name')

# Admin for SubDivision
class SubDivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'division')
    search_fields = ('name',)
    list_filter = ('division__name', 'division__zone__name')

# Admin for Hospital
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'entity_type')
    search_fields = ('name',)
    list_filter = ('division__name', 'entity_type')

# Admin for Division
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'zone')
    search_fields = ('name',)
    list_filter = ('zone__name',)

# Admin for Zone
class ZoneAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Register the models and their admin views
# admin.site.register(Zone, ZoneAdmin)
# admin.site.register(Division, DivisionAdmin)
# admin.site.register(SubDivision, SubDivisionAdmin)
# admin.site.register(PoliceStation, PoliceStationAdmin)
# admin.site.register(Chowki, ChowkiAdmin)
# admin.site.register(Hospital, HospitalAdmin)