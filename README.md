# GPSPhotoSorter
Use Google Maps KML files to automatically sort photos in to subfolders.

WORK-IN-PROGRESS. Initial code was created by ChatGPT.

```
usage: sortphotosbygps.py [-h] [--kml KML] [--input INPUT] [--output OUTPUT] [--nogpsdir NOGPSDIR]

Sort photos based on GPS data.

optional arguments:
  -h, --help           show this help message and exit
  --kml KML            Path to KML file containing GPS areas (default: GPS Areas.kml)
  --input INPUT        Path to directory containing photos (default: photos)
  --output OUTPUT      Path to directory where sorted photos will be moved (default: sorted_photos)
  --nogpsdir NOGPSDIR  Path to directory where photos without GPS data be moved (default: photos_no_gps)
  ```
  
