from django.http import JsonResponse
from api.models import Event
from django.forms.models import model_to_dict
from django.db.models import Q
# Create your views here.
def hello_world(request):
    return JsonResponse({"Bread":"wheat"})
def list_events(request):
    q=request.GET.get('q',None)
    if q is None:
        eventset=Event.objects.all()
    else:
        eventset=Event.objects.filter(Q(title__contains=q)|Q(description__contains=q))
    my_models=[model_to_dict(m) for m in eventset]

    return JsonResponse({"Events":my_models})
def get_event(request,id):
    my_model=model_to_dict(Event.objects.get(pk=id))

    return JsonResponse({"Events":my_model})
