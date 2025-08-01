from rest_framework import serializers
from .models import Job, Property, Product, TeamMember, Contact


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'id', 'unit', 'street_number', 'street_name', 'suburb', 
            'state', 'postcode', 'country', 'bedrooms', 'bathrooms', 
            'levels', 'land_size', 'house_size'
        ]


class JobSerializer(serializers.ModelSerializer):
    property = PropertySerializer()
    products = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )
    assigned_team_members = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )
    contacts = serializers.ListField(
        child=serializers.CharField(),
        write_only=True
    )
    
    # Read-only fields for response
    property_id = serializers.IntegerField(read_only=True)
    product_ids = serializers.ListField(
        child=serializers.CharField(),
        read_only=True
    )
    assigned_team_member_ids = serializers.ListField(
        child=serializers.CharField(),
        read_only=True
    )
    contact_ids = serializers.ListField(
        child=serializers.CharField(),
        read_only=True
    )

    class Meta:
        model = Job
        fields = [
            'id', 'type', 'status', 'method_of_access', 'access_details',
            'listing_agent', 'occupant_name', 'occupant_mobile', 'access_other',
            'package', 'property', 'products', 'assigned_team_members', 'contacts',
            'requested_datetime', 'property_id', 'product_ids', 
            'assigned_team_member_ids', 'contact_ids'
        ]

    def create(self, validated_data):
        property_data = validated_data.pop('property')
        product_ids = validated_data.pop('products')
        team_member_ids = validated_data.pop('assigned_team_members')
        contact_ids = validated_data.pop('contacts')

        # Check if property already exists
        try:
            property_obj = Property.objects.get(
                street_number=property_data['street_number'],
                street_name=property_data['street_name'],
                suburb=property_data['suburb'],
                postcode=property_data['postcode']
            )
        except Property.DoesNotExist:
            property_obj = Property.objects.create(**property_data)

        # Create the job
        job = Job.objects.create(property=property_obj, **validated_data)

        # Associate products
        products = Product.objects.filter(id__in=product_ids)
        job.products.set(products)

        # Associate team members
        team_members = TeamMember.objects.filter(id__in=team_member_ids)
        job.assigned_team_members.set(team_members)

        # Associate contacts
        contacts = Contact.objects.filter(id__in=contact_ids)
        job.contacts.set(contacts)

        return job

    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Add IDs for nested resources
        data['property_id'] = instance.property.id
        data['product_ids'] = list(instance.products.values_list('id', flat=True))
        data['assigned_team_member_ids'] = list(instance.assigned_team_members.values_list('id', flat=True))
        data['contact_ids'] = list(instance.contacts.values_list('id', flat=True))
        
        # Remove the nested property data from response
        data.pop('property', None)
        
        return data 