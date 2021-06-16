from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .helpers import convertToOpencvImage
from .myscript import proc_image
from PIL import Image as im
import io
from django.shortcuts import render
from django.views.generic.base import TemplateView


def image_to_byte_array(image):
    imgByteArr = io.BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


class ImageUpload(APIView):
    def post(self, request):
        source_image = request.FILES.get("sourceImage")
        checkprint_image = request.FILES.get("checkprintImage")
        if None in (source_image, checkprint_image):
            return Response({
                "success": False,
                "message": "Source and checkprint image is mandatory"
            })
        else:
            source_image_converted = convertToOpencvImage(stream=source_image)
            checkprint_image_converted = convertToOpencvImage(
                stream=checkprint_image)
            final_image_arr = proc_image(
                source_image_converted, checkprint_image_converted)
            final_image = im.fromarray(final_image_arr)
            file_name = "result.png"
            final_image.save(file_name)
            return Response(open(file_name,'rb'))


class ImageUploadtemplate(TemplateView):
    template_name = "upload_image.html"
