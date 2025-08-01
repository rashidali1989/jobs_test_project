from django.core.management.base import BaseCommand
from jobs.models import Product, TeamMember, Contact


class Command(BaseCommand):
    help = 'Populate database with sample data for testing'

    def handle(self, *args, **options):
        # Create sample products
        products_data = [
            {'id': 'sd8eas6d2', 'name': 'Property Inspection', 'description': 'Comprehensive property inspection service'},
            {'id': 'a9d83k2m1', 'name': 'Photography', 'description': 'Professional property photography'},
            {'id': 'x8d72j1k3', 'name': 'Floor Plan', 'description': 'Detailed floor plan creation'},
        ]
        
        for product_data in products_data:
            Product.objects.get_or_create(
                id=product_data['id'],
                defaults=product_data
            )
        
        # Create sample team members
        team_members_data = [
            {'id': 'vx7p3s0d', 'name': 'John Smith', 'email': 'john.smith@example.com', 'phone': '0412345678'},
            {'id': 'fipuhsgb', 'name': 'Jane Doe', 'email': 'jane.doe@example.com', 'phone': '0423456789'},
        ]
        
        for member_data in team_members_data:
            TeamMember.objects.get_or_create(
                id=member_data['id'],
                defaults=member_data
            )
        
        # Create sample contacts
        contacts_data = [
            {'id': 'wtlc111k', 'name': 'Bob Wilson', 'email': 'bob.wilson@example.com', 'phone': '0434567890'},
            {'id': 'u93agwnf', 'name': 'Alice Brown', 'email': 'alice.brown@example.com', 'phone': '0445678901'},
        ]
        
        for contact_data in contacts_data:
            Contact.objects.get_or_create(
                id=contact_data['id'],
                defaults=contact_data
            )
        
        self.stdout.write(
            self.style.SUCCESS('Successfully populated sample data')
        ) 