from django import forms
from .models import RasterDownload

class RasterDownloadForm(forms.ModelForm):
    class Meta:
        model = RasterDownload
        fields = ['url']