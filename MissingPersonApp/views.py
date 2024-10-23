from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  MissingPerson, UnidentifiedMissingPerson, UnidentifiedBody, Volunteer ,Match
from .serializers import MissingPersonSerializer, UndefinedMissingpersonSerializer, UnidentifiedBodySerializer, VolunteerSerializer
from django.core.exceptions import ObjectDoesNotExist
# from .models import Zone, Division, SubDivision, PoliceStation, Chowki, Hospital
# from .serializers import ZoneSerializer, DivisionSerializer, SubDivisionSerializer, PoliceStationSerializer, ChowkiSerializer, HospitalSerializer
from django.db.models import Q

class VolunteerAPIView(APIView):

    def get(self, request, volunteer_id=None):
        if volunteer_id is not None:
            try:
                volunteer = Volunteer.objects.get(pk=volunteer_id, is_deleted=False)
                serializer = VolunteerSerializer(volunteer)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({"error": "Volunteer not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        try:
            volunteers = Volunteer.objects.filter(is_deleted=False)
            serializer = VolunteerSerializer(volunteers, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = VolunteerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, volunteer_id):
        try:
            volunteer = Volunteer.objects.get(pk=volunteer_id, is_deleted=False)
            serializer = VolunteerSerializer(volunteer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error": "Volunteer not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, volunteer_id):
        try:
            volunteer = Volunteer.objects.get(pk=volunteer_id, is_deleted=False)
            volunteer.is_deleted = True
            volunteer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "Volunteer not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UnidentifiedBodyAPIView(APIView):

    def get(self, request, unidentified_body_id=None):
        if unidentified_body_id is not None:
            try:
                unidentified_body = UnidentifiedBody.objects.get(pk=unidentified_body_id, is_deleted=False)
                serializer = UnidentifiedBodySerializer(unidentified_body)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({"error": "Unidentified body not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            unidentified_bodies = UnidentifiedBody.objects.filter(is_deleted=False)
            serializer = UnidentifiedBodySerializer(unidentified_bodies, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = UnidentifiedBodySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, unidentified_body_id):
        try:
            unidentified_body = UnidentifiedBody.objects.get(pk=unidentified_body_id, is_deleted=False)
            serializer = UnidentifiedBodySerializer(unidentified_body, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error": "Unidentified body not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, unidentified_body_id):
        try:
            unidentified_body = UnidentifiedBody.objects.get(pk=unidentified_body_id, is_deleted=False)
            unidentified_body.is_deleted = True
            unidentified_body.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": "Unidentified body not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class MissingPersonAPIView(APIView):

    def get(self, request, missing_person_id=None):
        if missing_person_id is not None:
            try:
                missing_person = MissingPerson.objects.get(pk=missing_person_id, is_deleted=False)
                serializer = MissingPersonSerializer(missing_person)
                return Response(serializer.data)
            except MissingPerson.DoesNotExist:
                return Response({"error": "Missing person not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            missing_persons = MissingPerson.objects.filter(is_deleted=False)
            serializer = MissingPersonSerializer(missing_persons, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = MissingPersonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, missing_person_id):
        try:
            missing_person = MissingPerson.objects.get(pk=missing_person_id, is_deleted=False)
            serializer = MissingPersonSerializer(missing_person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MissingPerson.DoesNotExist:
            return Response({"error": "Missing person not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, missing_person_id):
        try:
            missing_person = MissingPerson.objects.get(pk=missing_person_id, is_deleted=False)
            missing_person.is_deleted = True
            missing_person.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except MissingPerson.DoesNotExist:
            return Response({"error": "Missing person not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UnidentifiedMissingPersonMissingPersonAPIView(APIView):

    def get(self, request, undefined_missing_person_id=None):
        if undefined_missing_person_id is not None:
            try:
                undefined_missing_person = UnidentifiedMissingPerson.objects.get(pk=undefined_missing_person_id, is_deleted=False)
                serializer = UndefinedMissingpersonSerializer(undefined_missing_person)
                return Response(serializer.data)
            except UnidentifiedMissingPerson.DoesNotExist:
                return Response({"error": "Undefined missing person not found"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            undefined_missing_persons = UnidentifiedMissingPerson.objects.filter(is_deleted=False)
            serializer = UndefinedMissingpersonSerializer(undefined_missing_persons, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = UndefinedMissingpersonSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, undefined_missing_person_id):
        try:
            undefined_missing_person = UnidentifiedMissingPerson.objects.get(pk=undefined_missing_person_id, is_deleted=False)
            serializer = UndefinedMissingpersonSerializer(undefined_missing_person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UnidentifiedMissingPerson.DoesNotExist:
            return Response({"error": "Undefined missing person not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, undefined_missing_person_id):
        try:
            undefined_missing_person = UnidentifiedMissingPerson.objects.get(pk=undefined_missing_person_id, is_deleted=False)
            undefined_missing_person.is_deleted = True
            undefined_missing_person.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except UnidentifiedMissingPerson.DoesNotExist:
            return Response({"error": "Undefined missing person not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class ZoneView(APIView):
#     def get(self, request):
#         try:
#             zones = Zone.objects.all()
#             serializer = ZoneSerializer(zones, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def post(self, request):
#         try:
#             serializer = ZoneSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # View to handle CRUD operations for Division
# class DivisionView(APIView):
#     def get(self, request):
#         try:
#             divisions = Division.objects.all()
#             serializer = DivisionSerializer(divisions, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def post(self, request):
#         try:
#             serializer = DivisionSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # View to handle CRUD operations for SubDivision
# class SubDivisionView(APIView):
#     def get(self, request):
#         try:
#             sub_divisions = SubDivision.objects.all()
#             serializer = SubDivisionSerializer(sub_divisions, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def post(self, request):
#         try:
#             serializer = SubDivisionSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # View to handle CRUD operations for Police Station
# class PoliceStationView(APIView):
#     def get(self, request):
#         try:
#             police_stations = PoliceStation.objects.all()
#             serializer = PoliceStationSerializer(police_stations, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def post(self, request):
#         try:
#             serializer = PoliceStationSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # View to handle CRUD operations for Chowki (Outpost)
# class ChowkiView(APIView):
#     def get(self, request):
#         try:
#             chowkis = Chowki.objects.all()
#             serializer = ChowkiSerializer(chowkis, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def post(self, request):
#         try:
#             serializer = ChowkiSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# # View to handle CRUD operations for Hospital
# class HospitalView(APIView):
#     def get(self, request):
#         try:
#             hospitals = Hospital.objects.all()
#             serializer = HospitalSerializer(hospitals, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def post(self, request):
#         try:
#             serializer = HospitalSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







class SearchAllMatches(APIView):
    def get(self, request):
        results = []

        # Fetch all records, ensure no null full names
        missing_people = MissingPerson.objects.exclude(full_name=None)
        undefined_missing_people = UnidentifiedMissingPerson.objects.exclude(full_name=None)
        unidentified_bodies = UnidentifiedBody.objects.exclude(full_name=None)

        # Missing Person vs Undefined Missing Person
        for missing_person in missing_people:
            for undefined_missing_person in undefined_missing_people:
                is_match, match_percentage = self.is_match_with_undefined_missing_person(missing_person, undefined_missing_person)
                
                if is_match:
                    results.append({
                        'missing_person_name': missing_person.full_name,
                        'match_type': 'Missing Person vs Undefined Missing Person',
                        'undefined_missing_person_name': undefined_missing_person.full_name if is_match else "No Match",
                        'match_percentage': match_percentage if is_match else 0
                    })
                    # Save match result, ensuring foreign keys are valid
                    Match.objects.create(
                        missing_person=missing_person if is_match else None,
                        undefined_missing_person=undefined_missing_person if is_match else None,
                        match_percentage=match_percentage if is_match else 0
                    )

            # Missing Person vs Unidentified Dead Body
            for unidentified_body in unidentified_bodies:
                is_match, match_percentage = self.is_match_with_unidentified_body(missing_person, unidentified_body)
                
                if is_match:
                    results.append({
                        'missing_person_name': missing_person.full_name,
                        'match_type': 'Missing Person vs Unidentified Dead Body',
                        'unidentified_body_name': unidentified_body.full_name if is_match else "No Match",
                        'match_percentage': match_percentage if is_match else 0
                    })
                    # Save match result
                    Match.objects.create(
                        missing_person=missing_person if is_match else None,
                        unidentified_body=unidentified_body if is_match else None,
                        match_percentage=match_percentage if is_match else 0
                    )

        # Undefined Missing Person vs Unidentified Dead Body
        for undefined_missing_person in undefined_missing_people:
            for unidentified_body in unidentified_bodies:
                is_match, match_percentage = self.is_match_between_undefined_missing_person_and_unidentified_body(undefined_missing_person, unidentified_body)
                
                if is_match:
                    results.append({
                        'undefined_missing_person_name': undefined_missing_person.full_name,
                        'match_type': 'Undefined Missing Person vs Unidentified Dead Body',
                        'unidentified_body_name': unidentified_body.full_name if is_match else "No Match",
                        'match_percentage': match_percentage if is_match else 0
                    })
                    # Save match result
                    Match.objects.create(
                        undefined_missing_person=undefined_missing_person if is_match else None,
                        unidentified_body=unidentified_body if is_match else None,
                        match_percentage=match_percentage if is_match else 0
                    )

        # Response logic
        if not results:
            return JsonResponse({
                'message': 'No matches found',
                'results': results  
            })

        return JsonResponse({
            'message': 'Matches found',
            'results': results
        }, safe=False)

    
    def is_match_with_undefined_missing_person(self, missing_person, UndefinedMissingPerson):
        match_score = 0
        total_checks = 0

        # 1. Full Name - Exact/Partial Match
        if missing_person.full_name and UndefinedMissingPerson.full_name:
            total_checks += 1
            if missing_person.full_name.lower() == UndefinedMissingPerson.full_name.lower():
                match_score += 1  # Exact match
            elif missing_person.full_name.lower() in UndefinedMissingPerson.full_name.lower() or UndefinedMissingPerson.full_name.lower() in missing_person.full_name.lower():
                match_score += 0.5  # Partial match

        # 2. Age - Approximate Match
        if missing_person.age is not None and UndefinedMissingPerson.estimated_age is not None:
            total_checks += 1
            if abs(missing_person.age - UndefinedMissingPerson.estimated_age) <= 5:  # Allow age range ±5
                match_score += 1

        # 3. Gender - Exact Match
        if missing_person.gender and UndefinedMissingPerson.gender:
            total_checks += 1
            if missing_person.gender == UndefinedMissingPerson.gender:
                match_score += 1

        # 4. Height - Approximate Match
        if missing_person.height and UndefinedMissingPerson.height:
            total_checks += 1
            if abs(missing_person.height - UndefinedMissingPerson.height) <= 5:  # Allow height range ±5 cm
                match_score += 1

        # 5. Weight - Approximate Match
        if missing_person.weight and UndefinedMissingPerson.weight:
            total_checks += 1
            if abs(missing_person.weight - UndefinedMissingPerson.weight) <= 5:  # Allow weight range ±5 kg
                match_score += 1

        # 6. Complexion - Exact Match
        if missing_person.complexion and UndefinedMissingPerson.complexion:
            total_checks += 1
            if missing_person.complexion.lower() == UndefinedMissingPerson.complexion.lower():
                match_score += 1

        # 7. Hair Color - Exact Match
        if missing_person.hair_color and UndefinedMissingPerson.hair_color:
            total_checks += 1
            if missing_person.hair_color.lower() == UndefinedMissingPerson.hair_color.lower():
                match_score += 1

        # 8. Hair Type - Exact Match
        if missing_person.hair_type and UndefinedMissingPerson.hair_type:
            total_checks += 1
            if missing_person.hair_type.lower() == UndefinedMissingPerson.hair_type.lower():
                match_score += 1

        # 9. Eye Color - Exact Match
        if missing_person.eye_color and UndefinedMissingPerson.eye_color:
            total_checks += 1
            if missing_person.eye_color.lower() == UndefinedMissingPerson.eye_color.lower():
                match_score += 1

        # 10. Birth Mark - Exact Match
        if missing_person.birth_mark and UndefinedMissingPerson.birth_mark:
            total_checks += 1
            if missing_person.birth_mark.lower() == UndefinedMissingPerson.birth_mark.lower():
                match_score += 1

        # 11. Other Distinctive Marks - Exact Match
        if missing_person.distinctive_mark and UndefinedMissingPerson.other_distinctive_mark:
            total_checks += 1
            if missing_person.distinctive_mark.lower() == UndefinedMissingPerson.other_distinctive_mark.lower():
                match_score += 1

        # 12. Last Location of Missing Person vs Location Found - Geographic Proximity
        if missing_person.last_seen_location and UndefinedMissingPerson.last_seen_details:
            total_checks += 1
            if missing_person.last_seen_location.lower() == UndefinedMissingPerson.last_seen_details.lower():
                match_score += 1

        # 13. Caste - Exact Match
        if missing_person.caste and UndefinedMissingPerson.caste:
            total_checks += 1
            if missing_person.caste.lower() == UndefinedMissingPerson.caste.lower():
                match_score += 1

        # 14. photo Number - Exact Match
        if missing_person.photo_upload and UndefinedMissingPerson.photo_upload:
            total_checks += 1
            if missing_person.photo_upload == UndefinedMissingPerson.photo_upload:
                match_score += 1

        # 15. Identification Details - Direct Verification (e.g., Aadhar, PAN)
        if missing_person.identification_card_no and UndefinedMissingPerson.identification_details:
            total_checks += 1
            if missing_person.identification_card_no == UndefinedMissingPerson.identification_details:
                match_score += 1
        
        if missing_person.Condition and UndefinedMissingPerson.condition_at_discovery:
            total_checks += 1
            if missing_person.Condition == UndefinedMissingPerson.condition_at_discovery:
                match_score += 1

        # Match percentage
        match_percentage = (match_score / total_checks) * 100 if total_checks > 0 else 0
        return match_percentage >= 50, match_percentage

    def is_match_with_unidentified_body(self, missing_person, UnidentifiedBody):
        match_score = 0
        total_checks = 0

        # 1. Full Name - Exact/Partial Match
        if missing_person.full_name and UnidentifiedBody.full_name:
            total_checks += 1
            if missing_person.full_name.lower() == UnidentifiedBody.full_name.lower():
                match_score += 1  # Exact match
            elif missing_person.full_name.lower() in UnidentifiedBody.full_name.lower() or UnidentifiedBody.full_name.lower() in missing_person.full_name.lower():
                match_score += 0.5  # Partial match

        # 2. Age - Approximate Match
        if missing_person.age is not None and UnidentifiedBody.estimated_age is not None:
            total_checks += 1
            if abs(missing_person.age - UnidentifiedBody.estimated_age) <= 5:  # Allow age range ±5
                match_score += 1

        # 3. Gender - Exact Match
        if missing_person.gender and UnidentifiedBody.gender:
            total_checks += 1
            if missing_person.gender == UnidentifiedBody.gender:
                match_score += 1

        # 4. Height - Approximate Match
        if missing_person.height and UnidentifiedBody.height:
            total_checks += 1
            if abs(missing_person.height - UnidentifiedBody.height) <= 5:  # Allow height range ±5 cm
                match_score += 1

        # 5. Weight - Approximate Match
        if missing_person.weight and UnidentifiedBody.weight:
            total_checks += 1
            if abs(missing_person.weight - UnidentifiedBody.weight) <= 5:  # Allow weight range ±5 kg
                match_score += 1

        # 6. Complexion - Exact Match
        if missing_person.complexion and UnidentifiedBody.complexion:
            total_checks += 1
            if missing_person.complexion.lower() == UnidentifiedBody.complexion.lower():
                match_score += 1

        # 7. Hair Color - Exact Match
        if missing_person.hair_color and UnidentifiedBody.hair_color:
            total_checks += 1
            if missing_person.hair_color.lower() == UnidentifiedBody.hair_color.lower():
                match_score += 1

        # 8. Hair Type - Exact Match
        if missing_person.hair_type and UnidentifiedBody.hair_type:
            total_checks += 1
            if missing_person.hair_type.lower() == UnidentifiedBody.hair_type.lower():
                match_score += 1

        # 9. Eye Color - Exact Match
        if missing_person.eye_color and UnidentifiedBody.eye_color:
            total_checks += 1
            if missing_person.eye_color.lower() == UnidentifiedBody.eye_color.lower():
                match_score += 1

        # 10. Birth Mark - Exact Match
        if missing_person.birth_mark and UnidentifiedBody.birth_mark:
            total_checks += 1
            if missing_person.birth_mark.lower() == UnidentifiedBody.birth_mark.lower():
                match_score += 1

        # 11. Other Distinctive Marks - Exact Match
        if missing_person.distinctive_mark and UnidentifiedBody.other_distinctive_mark:
            total_checks += 1
            if missing_person.distinctive_mark.lower() == UnidentifiedBody.other_distinctive_mark.lower():
                match_score += 1

        # 12. Last Location of Missing Person vs Location Found - Geographic Proximity
        if missing_person.last_seen_location and UnidentifiedBody.last_seen_details:
            total_checks += 1
            if missing_person.last_seen_location.lower() == UnidentifiedBody.last_seen_details.lower():
                match_score += 1


        # 14. Photo Upload - Visual Match (optional, requires external visual comparison)
        if missing_person.photo_upload and UnidentifiedBody.body_photo_upload:
            total_checks += 1
            if missing_person.photo_upload == UnidentifiedBody.body_photo_upload:
                match_score += 1

        # # 15. Identification Details - Direct Verification (e.g., Aadhar, PAN, DNA)
        # if missing_person.identification_card_no and UnidentifiedBody.identification_details:
        #     total_checks += 1
        #     if missing_person.identification_card_no == UnidentifiedBody.identification_details:
        #         match_score += 1

        # Match percentage
        match_percentage = (match_score / total_checks) * 100 if total_checks > 0 else 0
        return match_percentage >= 50, match_percentage

    def is_match_between_undefined_missing_person_and_unidentified_body(self, undefined_missing_person, unidentified_body):
        match_score = 0
        total_checks = 0

        if undefined_missing_person.full_name and unidentified_body.full_name:
            total_checks += 1
            if undefined_missing_person.full_name.lower() == unidentified_body.full_name.lower():
                match_score += 1  # Exact match

        

        # Calculate match percentage
        match_percentage = (match_score / total_checks) * 100 if total_checks > 0 else 0
        return match_percentage >= 50, match_percentage  # Return if it's a match and the match percentage


    

