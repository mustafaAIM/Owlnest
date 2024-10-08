#DRF
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
#models 
from system.models.Course import Course

#serializer
from system.serializers.DraftAdditionalResourcesSerializer import DraftAdditionalResourcesSerializer

#django 
from django.shortcuts import get_object_or_404

class AddAdditionalResourcesToCourse(ListCreateAPIView):
      serializer_class = DraftAdditionalResourcesSerializer
      permission_classes = [IsAuthenticated]
      def get_queryset(self): 
           return get_object_or_404(Course ,id= self.kwargs["id"]).draftadditionalresources_set.all() 
      
      def post(self, request, *args, **kwargs):
          
          if not( "text" in request.data.keys()):
              raise ValidationError({"message":"Please Enter the additonal resources as text"})  
          course =get_object_or_404(Course,id =  kwargs["id"])
          resource_data = {
               "text":request.data.get('text')
          }

          serialized_resource = DraftAdditionalResourcesSerializer(data = resource_data)
          serialized_resource.is_valid(raise_exception=True)
          serialized_resource.save(course = course)


          return Response({"message":"additional resources added to the course"})