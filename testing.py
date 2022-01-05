import GEOparse
import json
import gzip
import shutil
import os

with open('GEOnum.json') as f:
	data = json.load(f)
	for num in data['data']:
		print(num)
		geoNum = "GSE" + num
		print(geoNum)
		gse = GEOparse.get_GEO(geo=geoNum, destdir='./GSE') # Get GSE object
		print(gse)
		
gz_folder = './GZ/'
gse_folder = './GSE/'
extension = ".gz"

files = os.listdir(gz_folder)
for item in files:
	print("item is: ")
	print(item)
	if item.endswith(extension):

		with gzip.open(gz_folder + item, 'rb') as f_in:
			with open(gse_folder + item, 'x') as f_out:
				shutil.copyfileobj(f_in, f_out)


		
		