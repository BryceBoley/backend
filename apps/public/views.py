from rest_framework import generics
from serializers import *


class DinnerList(generics.ListAPIView):
    serializer_class = DinnerSerializer
    queryset = Dinner.objects.all()



class NewDinner(generics.CreateAPIView):
    serializer_class = DinnerSerializer
    queryset = Dinner.objects.all()


class EditDinner(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DinnerSerializer
    queryset = Dinner.objects.all()




