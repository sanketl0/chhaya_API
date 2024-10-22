from rest_framework import serializers
from .models import Address, Contact, MissingPerson, UndefinedMissingPerson, Volunteer ,UnidentifiedBody
from datetime import date

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        

class MissingPersonSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    address = AddressSerializer()

    class Meta:
        model = MissingPerson
        fields = '__all__'

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        address_data = validated_data.pop('address')

        # Create nested objects
        contact = Contact.objects.create(**contact_data)
        address = Address.objects.create(**address_data)

        # Create the MissingPerson instance
        missing_person = MissingPerson.objects.create(
            contact=contact,
            address=address,
            **validated_data
        )
        return missing_person

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact', None)
        address_data = validated_data.pop('address', None)

        # Update contact and address if provided
        if contact_data:
            for attr, value in contact_data.items():
                setattr(instance.contact, attr, value)
            instance.contact.save()

        if address_data:
            for attr, value in address_data.items():
                setattr(instance.address, attr, value)
            instance.address.save()

        # Update the MissingPerson instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class UnidentifiedBodySerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    address = AddressSerializer()

    class Meta:
        model = UnidentifiedBody
        fields = '__all__'

    def create(self, validated_data):
        contact_data = validated_data.pop('contact')
        address_data = validated_data.pop('address')

        # Create the nested Contact and Address instances
        contact = Contact.objects.create(**contact_data)
        address = Address.objects.create(**address_data)

        # Create the UnidentifiedBody instance with the newly created Contact and Address
        unidentified_body = UnidentifiedBody.objects.create(
            contact=contact,
            address=address,
            **validated_data
        )

        return unidentified_body

    def update(self, instance, validated_data):
        contact_data = validated_data.pop('contact', None)
        address_data = validated_data.pop('address', None)

        # Update the nested Contact instance
        if contact_data:
            for attr, value in contact_data.items():
                setattr(instance.contact, attr, value)
            instance.contact.save()

        # Update the nested Address instance
        if address_data:
            for attr, value in address_data.items():
                setattr(instance.address, attr, value)
            instance.address.save()

        # Update the UnidentifiedBody instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    
class VolunteerSerializer(serializers.ModelSerializer):
    # Nested serializers for contacts and addresses
    contact = ContactSerializer()
    address = AddressSerializer()

    class Meta:
        model = Volunteer
        fields = '__all__'

    def create(self, validated_data):
        # Extract nested data
        contact_data = validated_data.pop('contact')
        address_data = validated_data.pop('address')

        # Create the contact and address first
        contact = Contact.objects.create(**contact_data)
        address = Address.objects.create(**address_data)

        # Create the volunteer with the contact and address
        volunteer = Volunteer.objects.create(contact=contact, address=address, **validated_data)
        return volunteer

    def update(self, instance, validated_data):
        # Extract nested data
        contact_data = validated_data.pop('contact')
        address_data = validated_data.pop('address')

        # Update or create contact
        contact, created = Contact.objects.update_or_create(
            id=instance.contact.id, defaults=contact_data
        )

        # Update or create address
        address, created = Address.objects.update_or_create(
            id=instance.address.id, defaults=address_data
        )

        # Update volunteer fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    
    
class UndefinedMissingpersonSerializer(serializers.ModelSerializer):
    address = AddressSerializer()  # Nested serializer for Address
    contact = ContactSerializer()  # Nested serializer for Contact

    class Meta:
        model = UndefinedMissingPerson
        fields = '__all__' 

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        contact_data = validated_data.pop('contact')

        # Create Address instance
        address = Address.objects.create(**address_data)
        # Create Contact instance
        contact = Contact.objects.create(**contact_data)

        # Create PersonalDetails instance with the created Address and Contact
        personal_details = UndefinedMissingPerson.objects.create(
            address=address,
            contact=contact,
            **validated_data
        )

        return personal_details

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        contact_data = validated_data.pop('contact', None)

        # Update Address instance if address data is provided
        if address_data:
            for attr, value in address_data.items():
                setattr(instance.address, attr, value)
            instance.address.save()

        # Update Contact instance if contact data is provided
        if contact_data:
            for attr, value in contact_data.items():
                setattr(instance.contact, attr, value)
            instance.contact.save()

        # Update other fields in PersonalDetails
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
from .models import Zone, Division, SubDivision, PoliceStation, Chowki, Hospital

# Chowki Serializer
class ChowkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chowki
        fields = ['id', 'name', 'police_station']

# Police Station Serializer with Nested Chowkis
class PoliceStationSerializer(serializers.ModelSerializer):
    chowkis = ChowkiSerializer(many=True, read_only=True)

    class Meta:
        model = PoliceStation
        fields = ['id', 'name', 'division', 'chowkis']

# Sub-Division Serializer
class SubDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDivision
        fields = ['id', 'name', 'division']

# Hospital Serializer
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'division', 'entity_type']

# Division Serializer with Nested Police Stations, SubDivisions, and Hospitals
class DivisionSerializer(serializers.ModelSerializer):
    police_stations = PoliceStationSerializer(many=True, read_only=True)
    sub_divisions = SubDivisionSerializer(many=True, read_only=True)
    hospitals = HospitalSerializer(many=True, read_only=True)

    class Meta:
        model = Division
        fields = ['id', 'name', 'zone', 'police_stations', 'sub_divisions', 'hospitals']

# Zone Serializer with Nested Divisions
class ZoneSerializer(serializers.ModelSerializer):
    divisions = DivisionSerializer(many=True, read_only=True)

    class Meta:
        model = Zone
        fields = ['id', 'name', 'divisions']

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    