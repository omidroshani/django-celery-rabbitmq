from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import sample_task

@api_view(['GET'])
def sample_request(request):
    x = sample_task.delay( 1 , 2)
    return Response({
        'result' : x.id
    })