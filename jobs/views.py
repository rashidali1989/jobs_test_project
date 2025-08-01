from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from .models import Job, Property, Product, TeamMember, Contact
from .serializers import JobSerializer


# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def create(self, request, *args, **kwargs):
        """
        Custom create method for creating a new job.
        Handles property existence check and association of related objects.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            with transaction.atomic():
                job = serializer.save()
                
                # Return response with IDs only for nested resources
                response_data = {
                    'id': job.id,
                    'type': job.type,
                    'status': job.status,
                    'method_of_access': job.method_of_access,
                    'access_details': job.access_details,
                    'listing_agent': job.listing_agent,
                    'occupant_name': job.occupant_name,
                    'occupant_mobile': job.occupant_mobile,
                    'access_other': job.access_other,
                    'package': job.package,
                    'requested_datetime': job.requested_datetime,
                    'property_id': job.property.id,
                    'product_ids': list(job.products.values_list('id', flat=True)),
                    'assigned_team_member_ids': list(job.assigned_team_members.values_list('id', flat=True)),
                    'contact_ids': list(job.contacts.values_list('id', flat=True)),
                }
                
                return Response(response_data, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response(
                {'error': f'Failed to create job: {str(e)}'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def list(self, request, *args, **kwargs):
        """
        Override list method to return IDs only for nested resources.
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        Override retrieve method to return IDs only for nested resources.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
