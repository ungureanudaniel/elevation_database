import os
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RasterDownloadForm
from .models import RasterDownload

def download_raster(request):
    if request.method == 'POST':
        form = RasterDownloadForm(request.POST)
        if form.is_valid():
            raster = form.save(commit=False)
            url = form.cleaned_data['url']
            filename = os.path.basename(url)

            save_path = os.path.join(settings.MEDIA_ROOT, 'rasters', filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            try:
                r = requests.get(url, stream=True)
                with open(save_path, 'wb') as f:
                    for chunk in r.iter_content(8192):
                        f.write(chunk)
                raster.downloaded_file.name = f'rasters/{filename}'
                raster.save()
                return redirect('raster_success')
            except Exception as e:
                form.add_error('url', f"Download failed: {e}")
    else:
        form = RasterDownloadForm()
    return render(request, 'download_raster.html', {'form': form})
