#
# GPS Photo Sorter
# Created (mostly) by chat.chatgpt.com
# With updates to make it actually work by Allen C. Huffman
# www.subethasoftware.com
#
import os
import shutil
import xml.etree.ElementTree as ET
import exifread
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# Parse the KML file and extract the coordinates of the Placemarks
tree = ET.parse('GPS Areas.kml')
root = tree.getroot()
placemarks = {}
for pm in root.iter('{http://www.opengis.net/kml/2.2}Placemark'):
    name = pm.find('{http://www.opengis.net/kml/2.2}name').text
    coords_str = pm.find('{http://www.opengis.net/kml/2.2}Polygon/{http://www.opengis.net/kml/2.2}outerBoundaryIs/{http://www.opengis.net/kml/2.2}LinearRing/{http://www.opengis.net/kml/2.2}coordinates').text
    coords = [(float(c.split(',')[0]), float(c.split(',')[1])) for c in coords_str.split()]
    placemarks[name] = Polygon(coords)
    print('  Checking Placemark:', name)
    print('    Placemark coordinates:', coords)

# Loop through each photo and move it to the appropriate folder
for filename in os.listdir('photos'):
    if filename.endswith('.jpg'):
        with open(os.path.join('photos', filename), 'rb') as f:
            tags = exifread.process_file(f)
            # for tag in tags.keys():
            #     if 'GPS' in tag:
            #         print(tag, tags[tag])
            try:
                lat = float(tags['GPS GPSLatitude'].values[0].num) / float(tags['GPS GPSLatitude'].values[0].den) + \
                    (float(tags['GPS GPSLatitude'].values[1].num) / float(tags['GPS GPSLatitude'].values[1].den))/60 + \
                    (float(tags['GPS GPSLatitude'].values[2].num) / float(tags['GPS GPSLatitude'].values[2].den))/3600
                
                if (tags['GPS GPSLatitudeRef'].values == 'S'):
                    lat = -lat

                lon = float(tags['GPS GPSLongitude'].values[0].num) / float(tags['GPS GPSLongitude'].values[0].den) + \
                    (float(tags['GPS GPSLongitude'].values[1].num) / float(tags['GPS GPSLongitude'].values[1].den)/60) + \
                    (float(tags['GPS GPSLongitude'].values[2].num) / float(tags['GPS GPSLongitude'].values[2].den)/3600)

                if (tags['GPS GPSLongitudeRef'].values == 'W'):
                    lon = -lon

                print('  Photo coordinates:', lat, lon)
                point = Point(lon, lat)
                for name, polygon in placemarks.items():
                    if polygon.contains(point):
                        dest_dir = os.path.join('photos', name)
                        if not os.path.exists(dest_dir):
                            os.makedirs(dest_dir)
                        shutil.move(os.path.join('photos', filename), os.path.join(dest_dir, filename))
                        break
            except:
                dest_dir = os.path.join('photos', 'NoGPS')
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(os.path.join('photos', filename), os.path.join(dest_dir, filename))
                pass # ignore photos without GPS data or with invalid GPS data
