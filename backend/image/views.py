from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer

# Create your views here.
class RetrieveImageView(APIView):
    def get(self, request, format = None):
        try:
            if Image.objects.all().exists():
                image = Image.objects.all()
                serializer = ImageSerializer(image, many=True)
                return Response({'images':serializer.data},
                                status=status.HTTP_200_OK)
            else:
                return Response(
                {'error': 'No images found'},
                status = status.HTTP_400_BAD_REQUEST)
        except Image.DoesNotExist:
            return Response(
                {'error': 'Image does not exist'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class UploadImageView(APIView):
    def post(self, request, format = None):
        try:
            data = request.data
            print(data)
            
            image = data['image']
            alt_text = data['alt_text']

            print(image)
            print(alt_text)

            Image.objects.create(image=image, alt_text=alt_text)
            
            return Response({'sucess': 'Image uploaded succesfullt'}, 
                            status=status.HTTP_201_CREATED)

        except Image.DoesNotExist:
            return Response(
                {'error': 'Error Uplaoding Image'}, 
                status = status.HTTP_500_INTERNAL_SERVER_ERROR)