from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerializer

def customers(request):
  data = Customer.objects.all()
  serializer = CustomerSerializer(data, many=True)
  return JsonResponse({'Customers': serializer.data})

def customer(request, id):
  try:
    data = Customer.objects.get(pk=id)
  except Customer.DoesNotExist:
    raise Http404('Customer not found')
  serializer = CustomerSerializer(data)
  return JsonResponse({'Customer': serializer.data})
