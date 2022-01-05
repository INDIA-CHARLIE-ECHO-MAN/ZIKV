import GEOparse
import json
import gzip
import shutil
import os

gse_folder = './GSE/'
extension = ".gz"

# reads json file to download GSE files as .soft.gz
with open('GEOnum.json') as f:
	data = json.load(f)
	for num in data['data']:
		geoNum = "GSE" + num
		gse = GEOparse.get_GEO(geo=geoNum, destdir=gse_folder)

# go through gse folder and unzip file and save new unzipped file in gse folder
# deletes all the .gz files in the gse folder

files = os.listdir(gse_folder)

for item in files:
	if item.endswith(extension):

		with gzip.open(gse_folder + item, 'rb') as f_in:
			with open(gse_folder + item[:-3], 'wb') as f_out:
				shutil.copyfileobj(f_in, f_out)

for item in files:
	if item.endswith(extension):
		os.remove(gse_folder + item)