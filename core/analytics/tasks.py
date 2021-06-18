# Create your tasks here
from celery import shared_task
from datetime import datetime

@shared_task
def sample_task(a,b):
    return a + b
    


