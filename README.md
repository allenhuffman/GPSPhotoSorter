# GPSPhotoSorter #
Use Google Maps KML files to automatically sort photos in to subfolders.

WORK-IN-PROGRESS. Initial code was created by ChatGPT.

## Description ##
I asked ChatGPT to describe what the script does:

>This script is a Python program for sorting photos based on GPS data. It takes input images from a directory specified by the user using the `--input` argument, reads the GPS coordinates of each image using the `exifread` library, and then checks if the coordinates lie within any of the polygons defined in a KML file specified by the user using the `--kml` argument. If the coordinates are within a polygon, the script moves the image to a directory corresponding to that polygon in another directory specified by the user using the `--output` argument. If the coordinates are not within any polygon or if there is no GPS data for the image, the script moves the image to a directory specified by the user using the `--nogpsdir` argument.
>
>The script uses the `argparse` library to handle command-line arguments. It also uses the `xml.etree.ElementTree` library to parse the KML file, the `shapely.geometry` library to create and manipulate polygons, and the `os` and `shutil` libraries to move files between directories.
>
>Overall, this script provides a useful tool for organizing photos based on their GPS coordinates and the user's desired organization scheme.

## Usage ##
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
  
## Generate the KML file using Google Maps ##
TBA
