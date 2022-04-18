import os.path
from rest_framework.response import Response
from .models import ImageUpload
from .serializers import ProductSerializer
from rest_framework.views import APIView
from .service.Services import Services
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.status import HTTP_200_OK


# Create your views here.

class ImageResponseView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print("valid serializer")
            serializer.save()
        service = Services()

        obj = ImageUpload.objects.create(image=request.FILES['image'])  # let's insert it to db
        image_path = os.path.join("media/"+obj.image.name)
        result = service.getMatches(image_path)
        os.remove(image_path)
        return Response(result, HTTP_200_OK)
