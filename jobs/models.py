from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    unit = models.CharField(max_length=50, null=True, blank=True)
    street_number = models.CharField(max_length=20)
    street_name = models.CharField(max_length=200)
    suburb = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=100, default="Australia")
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    levels = models.IntegerField()
    land_size = models.DecimalField(max_digits=10, decimal_places=2)
    house_size = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['street_number', 'street_name', 'suburb', 'postcode']
        verbose_name_plural = "Properties"

    def __str__(self):
        return f"{self.street_number} {self.street_name}, {self.suburb}"


class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPES = [
        ('Property', 'Property'),
        ('Commercial', 'Commercial'),
        ('Industrial', 'Industrial'),
    ]
    
    STATUS_CHOICES = [
        (1, 'Pending'),
        (2, 'In Progress'),
        (3, 'Completed'),
        (4, 'Cancelled'),
    ]
    
    ACCESS_METHOD_CHOICES = [
        (1, 'Keysafe'),
        (2, 'Agent'),
        (3, 'Occupant'),
        (4, 'Other'),
    ]

    type = models.CharField(max_length=20, choices=JOB_TYPES)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    method_of_access = models.IntegerField(choices=ACCESS_METHOD_CHOICES)
    access_details = models.TextField(blank=True)
    listing_agent = models.CharField(max_length=50)
    occupant_name = models.CharField(max_length=200, null=True, blank=True)
    occupant_mobile = models.CharField(max_length=20, null=True, blank=True)
    access_other = models.TextField(null=True, blank=True)
    package = models.CharField(max_length=100, null=True, blank=True)
    
    # Relationships
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='jobs')
    products = models.ManyToManyField(Product, related_name='jobs')
    assigned_team_members = models.ManyToManyField(TeamMember, related_name='assigned_jobs')
    contacts = models.ManyToManyField(Contact, related_name='jobs')
    
    # Timestamps
    requested_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Job {self.id} - {self.type} at {self.property}"
