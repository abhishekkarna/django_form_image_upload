from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .helpers import convertToOpencvImage
from .myscript import proc_image
from PIL import Image as im
import io, base64
from django.http import HttpResponse
from .custom_renderer import JPEGRenderer, PNGRenderer
from wsgiref.util import FileWrapper

def image_to_byte_array(image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


class ImageUpload(APIView):
    renderer_classes = [JPEGRenderer, PNGRenderer]
    def post(self, request):
        source_image = request.FILES.get("sourceImage")
        checkprint_image = request.FILES.get("checkprintImage")
        content_type = None
        if None in (source_image, checkprint_image):
            return Response({
                "success": False,
                "message": "Source and checkprint image is mandatory"
            })
        else:
            content_type = source_image.content_type
            print('content_type',content_type)
            source_image_converted = convertToOpencvImage(stream=source_image)
            checkprint_image_converted = convertToOpencvImage(
                stream=checkprint_image)
            final_image_arr = proc_image(
                source_image_converted, checkprint_image_converted)
            final_image = im.fromarray(final_image_arr)
            file_name = "result.png"
            final_image.save(file_name)
            return Response(FileWrapper(open(file_name,'rb')))
