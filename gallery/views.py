from django.shortcuts import render
from django.views import View
# import uuid
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery
from django.views.generic.edit import CreateView
from django.views.generic import ListView


# Create your views here.


class ListGalleryView(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'


class CreateGalleryView(CreateView):
    model = Gallery
    fields = '__all__'
    template_name = 'gallery/load_file.html'
    success_url = '/load_image'

# def storage_file(file):
#     with open(f"gallery_tmp/{uuid.uuid4()}_{file.name}", 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)


# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm()
#         return render(request, 'gallery/load_file.html', context={'form': form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # storage_file(form.cleaned_data['image'])
#             new_image = Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/load_file.html', context={'form': form})
