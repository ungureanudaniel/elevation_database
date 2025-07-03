from django.contrib.gis.db import models

class RasterDownload(models.Model):
    url = models.URLField()
    downloaded_file = models.FileField(upload_to='rasters/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
