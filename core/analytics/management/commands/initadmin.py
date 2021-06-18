from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model



class Command(BaseCommand):
    help = 'Create Super User, User: admin@admin.com, Password: admin'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if User.objects.count() == 0:
            username = 'admin@admin.com'
            email = 'admin@admin.com'
            password = 'admin'
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
