from django.db import models


class Contact(models.Model):
    CONTACT_TYPE_CHOICES = [
        ('Missing Person', 'Missing Person'),
        ('Undefined Missing Person', 'Undefined Missing Person'),
        ('Undefined Body', 'Undefined Body'),
        ('Volunteer', 'Volunteer'),
        
    ]

    CONTACT_SUBTYPE_CHOICES = [
        ('Personal', 'Personal'),
        ('Business', 'Business'),
        ('Emergency', 'Emergency'),
        
    ]

    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=CONTACT_TYPE_CHOICES)
    subtype = models.CharField(max_length=50, choices=CONTACT_SUBTYPE_CHOICES)
    subtype_detail = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    job_title = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    social_media_handles = models.CharField(max_length=255, null=True, blank=True)
    is_primary = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    notes = models.TextField(null=True, blank=True)
    # volunteer = models.ForeignKey(Volunteer, related_name='addresses', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.phone_number} ({self.type})" 

class Address(models.Model):
    ADDRESS_TYPE_CHOICES = [
        ('Missing Person', 'Missing Person'),
        ('Undefined Missing Person', 'Undefined Missing Person'),
        ('Undefined Body', 'Undefined Body'),
        ('Volunteer', 'Volunteer'),
        
    ]

    ADDRESS_SUBTYPE_CHOICES = [
        ('Permanent Address', 'Permanent Address'),
        ('Current Address', 'Current Address'),
        ('Emergency', 'Emergency'),
       
    ]

    street = models.CharField(max_length=255)
    village = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=ADDRESS_TYPE_CHOICES)
    subtype = models.CharField(max_length=50, choices=ADDRESS_SUBTYPE_CHOICES)
    landmark = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    address_type = models.CharField(max_length=255, null=True, blank=True)
    apartment_number = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    country_code = models.CharField(max_length=10)
    # volunteer = models.ForeignKey(Volunteer, related_name='contacts', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} - {self.postal_code}"


class MissingPerson(models.Model):
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    ]
    
    COMPLEXION_CHOICES = [
        ('Fair', 'Fair'),
        ('Dusky', 'Dusky'),
        ('Wheatish', 'Wheatish'),
        ('Dark', 'Dark'),
    ]
    
    HAIR_COLOR_CHOICES = [
        ('Black', 'Black'),
        ('Brown', 'Brown'),
        ('Grey', 'Grey'),
    ]
    
    HAIR_TYPE_CHOICES = [
        ('Straight', 'Straight'),
        ('Wavy', 'Wavy'),
        ('Curly', 'Curly'),
        ('Bald', 'Bald'),
    ]
    
    EYE_COLOR_CHOICES = [
        ('Dark Brown', 'Dark Brown'),
        ('Light Brown', 'Light Brown'),
        ('Hazel', 'Hazel'),
        ('Amber', 'Amber'),
        ('Green', 'Green'),
        ('Gray', 'Gray'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    
    
    CASTE_CHOICES = [
        ('Open', 'Open'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
       
    ]
    
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
       
    ]
    
    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Sikh', 'Sikh'),
        ('Christian', 'Christian'),
        
    ]
    
    LANGUAGE_CHOICES = [
        ('Hindi', 'Hindi'),
        ('English', 'English'),
        ('Marathi', 'Marathi'),
        
    ]

    IDENTIFICATION_CHOICES = [
        ('Aadhar Card', 'Aadhar Card'),
        ('Pan Card', 'Pan Card'),
        ('Driving License', 'Driving License'),
        ('Passport', 'Passport'),
        
    ]
    
    RELATIONSHIP_CHOICES = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Friend', 'Friend'),
        
    ]
    
    Condition_GROUP_CHOICES=[
        ('Memory loss', 'Memory loss'),
        ('Shock', 'Shock'),
    ]

    # missing person 
    full_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    time_of_birth = models.TimeField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=255, null=True, blank=True)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    complexion = models.CharField(max_length=20, choices=COMPLEXION_CHOICES)
    hair_color = models.CharField(max_length=20, choices=HAIR_COLOR_CHOICES)
    hair_type = models.CharField(max_length=20, choices=HAIR_TYPE_CHOICES)
    eye_color = models.CharField(max_length=20, choices=EYE_COLOR_CHOICES)
    birth_mark = models.TextField(null=True, blank=True)
    distinctive_mark = models.TextField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    photo_upload = models.ImageField(upload_to='Missingperson_photos/', null=True, blank=True)
    
    
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='missing_person', null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='missing_person', null=True)
    Condition = models.CharField(max_length=20, choices=Condition_GROUP_CHOICES, null=True, blank=True)
    
    # additional information
    caste = models.CharField(max_length=50, choices=CASTE_CHOICES)
    sub_caste = models.CharField(max_length=100, null=True, blank=True)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS_CHOICES)
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES)
    mother_tongue = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    other_known_languages = models.CharField(max_length=255, null=True, blank=True, help_text="Comma-separated list of languages")
    educational_details = models.TextField(null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    identification_details = models.CharField(max_length=50, choices=IDENTIFICATION_CHOICES)
    identification_card_no = models.PositiveIntegerField()
    
    # missing details
    missing_time = models.TimeField()
    missing_date = models.DateField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_details = models.TextField(null=True, blank=True)
    last_seen_location = models.TextField(null=True, blank=True)
    
    # police and legal info
    fir_number = models.PositiveIntegerField()
    fir_photo = models.BinaryField(null=True, blank=True)
    police_station_name_address = models.TextField()
    investigating_officer_name = models.CharField(max_length=255)
    investigating_officer_contact_number = models.CharField(max_length=15) 
    
    # reporting person
    reportingperson_name = models.CharField(max_length=255)
    relationship_with_victim = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES)
    contact_numbers = models.CharField(max_length=20, help_text="Contact number(s) of the reporting person",null=True, blank=True)
    email_address = models.EmailField(max_length=255, help_text="Email address of the reporting person",null=True, blank=True)
    willing_to_volunteer = models.BooleanField()
    # areas_regions_willing = models.TextField(null=True, blank=True)
    # availability = models.BooleanField()
    # preferred_mode_of_search = models.CharField(max_length=255, null=True, blank=True)
    # access_to_vehicle = models.BooleanField()
    # specialized_skills = models.TextField(null=True, blank=True)
    # volunteered_in_similar_cases_before = models.BooleanField()
    # details_of_previous_experience = models.TextField(null=True, blank=True)
    # track_live_location = models.BooleanField()
    # method_of_reporting_progress = models.TextField(null=True, blank=True)
    # uploaded_evidence = models.BinaryField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)


    # def save(self, *args, **kwargs):
    #         super().save(*args, **kwargs)
    #         if self.willing_to_volunteer:
    #             contact_instance = Contact.objects.create(
    #                 phone_number=self.contact_numbers, 
    #                 email=self.email_address, 
    #                 type='Volunteer', 
    #                 subtype='Personal', 
    #             )

    #             address_instance = Address.objects.create(
    #                 street="Your Street",  
    #                 city="Your City",
    #                 state="Your State", 
    #                 postal_code="Your Postal Code",  
    #                 country="Your Country", 
    #                 type='Volunteer', 
    #                 subtype='Permanent Address',  
    #             )
    #             self.contact = contact_instance
    #             self.address = address_instance
    #             super().save(*args, **kwargs)
    
    def __str__(self):
        return self.full_name


class UnidentifiedBody(models.Model):
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    ]
    
    COMPLEXION_CHOICES = [
        ('Fair', 'Fair'),
        ('Dusky', 'Dusky'),
        ('Wheatish', 'Wheatish'),
        ('Dark', 'Dark'),
    ]
    
    HAIR_COLOR_CHOICES = [
        ('Black', 'Black'),
        ('Brown', 'Brown'),
        ('Grey', 'Grey'),
    ]
    
    HAIR_TYPE_CHOICES = [
        ('Straight', 'Straight'),
        ('Wavy', 'Wavy'),
        ('Curly', 'Curly'),
        ('Bald', 'Bald'),
    ]
    
    EYE_COLOR_CHOICES = [
        ('Dark Brown', 'Dark Brown'),
        ('Light Brown', 'Light Brown'),
        ('Hazel', 'Hazel'),
        ('Amber', 'Amber'),
        ('Green', 'Green'),
        ('Gray', 'Gray'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    
    # Personal Details
    full_name = models.CharField(max_length=255, blank=True, null=True)
    estimated_age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    date_found = models.DateField()
    estimated_time_of_death = models.TimeField(blank=True, null=True)
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    complexion = models.CharField(max_length=50, choices=COMPLEXION_CHOICES)
    hair_color = models.CharField(max_length=50, choices=HAIR_COLOR_CHOICES)
    hair_type = models.CharField(max_length=50, choices=HAIR_TYPE_CHOICES)
    eye_color = models.CharField(max_length=50, choices=EYE_COLOR_CHOICES)
    birth_mark = models.TextField(max_length=100, blank=True, null=True)
    other_distinctive_mark = models.TextField(max_length=100, blank=True, null=True)
    blood_group = models.CharField(max_length=20, choices=BLOOD_GROUP_CHOICES)
    # Use FileField/ImageField for file uploads
    body_photo_upload = models.FileField(upload_to='body_photos/', blank=True, null=True)
    clothing_description = models.TextField(max_length=100, blank=True, null=True)
    last_seen_details=models.TextField(max_length=100, blank=True, null=True)
    # Connect with Contact and Address models using ForeignKey
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='unidentified_bodies', null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='unidentified_bodies', null=True)

    # Legal and Police Info
    fir_number = models.IntegerField(help_text="FIR Number assigned for the case")
    fir_photo = models.FileField(upload_to='fir_photos/', blank=True, null=True, help_text="Upload the FIR document")
    police_station_name_and_address = models.CharField(max_length=255, help_text="Name and address of the police station")
    investigating_officer_name = models.CharField(max_length=50, help_text="Name of the investigating police officer")
    investigating_officer_contact_number = models.CharField(max_length=15, help_text="Contact number of the investigating officer")

    # Identification
    fingerprints_collected = models.FileField(upload_to='fingerprints/', blank=True, null=True, help_text="Upload fingerprints collected")
    dna_sample_collected = models.FileField(upload_to='dna_samples/', blank=True, null=True, help_text="Upload DNA samples collected")
    post_mortem_report_upload = models.FileField(upload_to='post_mortem_reports/', blank=True, null=True, help_text="Upload the post-mortem report")
    
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"Unidentified Body: {self.full_name or 'Unknown'}"

class Volunteer(models.Model):
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    SEARCH_GROUP_CHOICES = [
        ('Group A', 'Group A'),
        ('Group B', 'Group B'),
        ('Group C', 'Group C'),
        
    ]
    
    MODE_OF_SEARCH_CHOICES = [
        ('On Foot', 'On Foot'),
        ('Vehicle', 'Vehicle'),
        ('Drone', 'Drone'),
    ]
    
    # Personal Details
    full_name = models.CharField(max_length=255)
    dob = models.DateField(help_text="Date of Birth")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    
    # Relationships
    # contacts = models.ManyToManyField('Contact', related_name='volunteers_contacts')
    # addresses = models.ManyToManyField('Address', related_name='volunteers_addresses')
    
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='volunteers')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='volunteers')
    
    # Assignment Info
    volunteer_group = models.CharField(max_length=50, choices=SEARCH_GROUP_CHOICES)
    assigned_region = models.CharField(max_length=100, help_text="Region assigned to the volunteer")
    search_start_date = models.DateField()
    search_end_date = models.DateField(blank=True, null=True)
    search_timing = models.TimeField(help_text="Timing for the volunteer's search")
    gps_tracker_enabled = models.BooleanField(default=False, help_text="Does the volunteer have GPS tracking?")
    mode_of_search = models.CharField(max_length=50, choices=MODE_OF_SEARCH_CHOICES)
    other_equipment_issued = models.TextField(max_length=100, blank=True, null=True)
    
    # Health and Emergency Details
    blood_group = models.CharField(max_length=20, choices=BLOOD_GROUP_CHOICES)
    known_allergies = models.TextField(max_length=100, blank=True, null=True)
    pre_existing_medical_conditions = models.TextField(max_length=200, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=50)
    emergency_contact_number = models.CharField(max_length=15)
    relationship_with_volunteer = models.CharField(max_length=50, help_text="Relationship with the volunteer (e.g., Father, Mother, Spouse)")
    
    # Feedback
    feedback_after_search = models.TextField(max_length=200, blank=True, null=True)
    issues_faced_during_search = models.TextField(max_length=200, blank=True, null=True)
    additional_suggestions = models.TextField(max_length=200, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.full_name 

class UndefinedMissingPerson(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender'),
    ]

    COMPLEXION_CHOICES = [
        ('Fair', 'Fair'),
        ('Dusky', 'Dusky'),
        ('Wheatish', 'Wheatish'),
        ('Dark', 'Dark'),
    ]

    HAIR_COLOR_CHOICES = [
        ('Black', 'Black'),
        ('Brown', 'Brown'),
        ('Grey', 'Grey'),
    ]

    HAIR_TYPE_CHOICES = [
        ('Straight', 'Straight'),
        ('Wavy', 'Wavy'),
        ('Curly', 'Curly'),
        ('Bald', 'Bald'),
    ]

    EYE_COLOR_CHOICES = [
        ('Dark brown', 'Dark brown'),
        ('Light Brown', 'Light Brown'),
        ('Hazel', 'Hazel'),
        ('Amber', 'Amber'),
        ('Green', 'Green'),
        ('Gray', 'Gray'),
    ]

    CASTE_CHOICES = [
        ('Open', 'Open'),
        ('SC', 'Scheduled Caste'),
        ('ST', 'Scheduled Tribe'),
        # Add more options as needed
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        # Add more options as needed
    ]

    RELIGION_CHOICES = [
        ('Hindu', 'Hindu'),
        ('Muslim', 'Muslim'),
        ('Sikh', 'Sikh'),
        # Add more options as needed
    ]

    LANGUAGE_CHOICES = [
        ('Hindi', 'Hindi'),
        ('Marathi', 'Marathi'),
        ('Bengali', 'Bengali'),
        # Add other languages as needed
    ]

    CONDITION_CHOICES = [
        ('Memory loss', 'Memory loss'),
        ('Shock', 'Shock'),
        ('Injured', 'Injured'),
        ('Other', 'Other'),
    ]
    Condition_GROUP_CHOICES=[
        ('Memory loss', 'Memory loss'),
        ('Shock', 'Shock'),
    ]
    

    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    estimated_age = models.PositiveIntegerField(blank=True, null=True,)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True, null=True, verbose_name="Gender")
    height = models.FloatField(blank=True, null=True, verbose_name="Height (cm)")
    weight = models.FloatField(blank=True, null=True, verbose_name="Weight (kg)")
    birth_mark =models.TextField(max_length=255,blank=True, null=True)
    complexion = models.CharField(max_length=50, choices=COMPLEXION_CHOICES, blank=True, null=True, verbose_name="Complexion")
    hair_color = models.CharField(max_length=50, choices=HAIR_COLOR_CHOICES, blank=True, null=True, verbose_name="Hair Color")
    hair_type = models.CharField(max_length=50, choices=HAIR_TYPE_CHOICES, blank=True, null=True, verbose_name="Hair Type")
    eye_color = models.CharField(max_length=50, choices=EYE_COLOR_CHOICES, blank=True, null=True, verbose_name="Eye Color")
    other_distinctive_mark = models.TextField(blank=True, null=True,)
    photo_upload = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo Upload")
    caste = models.CharField(max_length=50, choices=CASTE_CHOICES, blank=True, null=True, verbose_name="Caste")
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES, blank=True, null=True, verbose_name="Marital Status")
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, blank=True, null=True, verbose_name="Religion")
    other_known_languages = models.CharField(max_length=255, choices=LANGUAGE_CHOICES, blank=True, null=True, verbose_name="Other Known Languages")
    identification_details = models.TextField(blank=True, null=True, verbose_name="Identification Details")
    last_location = models.TextField(blank=True, null=True, verbose_name="Last Location of Missing Person")
    last_seen_details = models.TextField(blank=True, null=True, verbose_name="Last Seen Details/Sighting Details")
    condition_at_discovery = models.CharField(max_length=50, choices=CONDITION_CHOICES, blank=True, null=True, verbose_name="Condition at Discovery")
    reporting_person_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Name of Reporting Person")
    reporting_person_contact_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Contact Number(s)")
    reporting_person_email = models.EmailField(blank=True, null=True, verbose_name="Email Address")
    relationship_with_victim = models.CharField(max_length=255, blank=True, null=True, verbose_name="Relationship with Victim")
    availability_for_search_operations = models.CharField(max_length=50, blank=True, null=True, verbose_name="Availability for Search Operations")
    preferred_mode_of_communication = models.CharField(max_length=50, blank=True, null=True, verbose_name="Preferred Mode of Communication")
    access_to_vehicle = models.BooleanField(default=False, verbose_name="Access to Vehicle for Search Operations")
    special_skills = models.TextField(blank=True, null=True, verbose_name="Special Skills")
    previous_search_experience = models.TextField(blank=True, null=True, verbose_name="Details of Previous Search Experience")
    upload_evidence = models.FileField(upload_to='evidence/', blank=True, null=True, verbose_name="Upload Evidence (e.g., photos, notes)")
    Condition = models.CharField(max_length=20, choices=Condition_GROUP_CHOICES, null=True, blank=True)

    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Undefined_missing_person', null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='Undefined_missing_person', null=True)
    is_deleted = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.full_name or 'Unknown'}"

class Match(models.Model):
    missing_person = models.ForeignKey(MissingPerson, on_delete=models.CASCADE)
    undefined_missing_person = models.ForeignKey(UndefinedMissingPerson, null=True, blank=True, on_delete=models.CASCADE)
    unidentified_body = models.ForeignKey(UnidentifiedBody, null=True, blank=True, on_delete=models.CASCADE)
    match_percentage = models.FloatField()

    def __str__(self):
        if self.undefined_missing_person:
            return f"Match: {self.missing_person} - {self.undefined_missing_person} - {self.match_percentage}%"
        if self.unidentified_body:
            return f"Match: {self.missing_person} - {self.unidentified_body} - {self.match_percentage}%"
        return "No Match"






























































# Zone model
class Zone(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Division model (one-to-many relationship with Zone)
class Division(models.Model):
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, related_name='divisions', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.zone.name})"

# Sub-Division model (belongs to a Division)
class SubDivision(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey(Division, related_name='sub_divisions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Police Station model (belongs to a Division)
class PoliceStation(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey(Division, related_name='police_stations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Chowki (Outpost) model (belongs to a Police Station)
class Chowki(models.Model):
    name = models.CharField(max_length=255)
    police_station = models.ForeignKey(PoliceStation, related_name='chowkis', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Hospital model (belongs to a Division)
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey(Division, related_name='hospitals', on_delete=models.CASCADE)
    entity_type = models.CharField(max_length=255, choices=[('Government', 'Government'), ('Private', 'Private')])

    def __str__(self):
        return f"{self.name} ({self.entity_type})"

