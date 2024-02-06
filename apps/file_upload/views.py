from django.http import HttpResponseRedirect
from django.shortcuts import render

# Imaginary function to handle an uploaded file.
from .handle_file import handle_uploaded_file
from .forms import UploadFileForm
from . import models


def upload_file(request):
    if request.method == "POST":
        # Fetching the form data
        file = request.FILES["file"]

        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     handle_uploaded_file(request.FILES["file"])
        if file:
            # Saving the information in the database
            document = models.UploadedFile(
                uploadedFile=file,
            )
            document.save()

            context = {
                'document': document,
            }

            # return HttpResponseRedirect("/success/url/")
            return render(request, 'upload_success.html', context)
        else:
            # 表单验证失败，获取失败原因
            # errors = form.errors
            # print(errors)
            return render(request, 'upload_fail.html')
    else:
        form = UploadFileForm()
        return render(request, "upload.html", {"form": form})
