import GEOparse
import json

with open('GEOnum.json') as f:
	data = json.load(f)
	for num in data['data']:
		print(num)
		geoNum = "GSE" + num
		print(geoNum)
		gse = GEOparse.get_GEO(geo=geoNum, destdir='./GSE') # Get GSE object
		print(gse)

		
		# Summary
		if 'summary' in gse.metadata:
			print('Summary: %s' % gse.metadata['summary'][0])
			
		# Contributors
		if 'contributor' in gse.metadata:
			print('Contributors: %s' % ', '.join(gse.metadata['contributor']))
			
		# PubMed IDs
		if 'pubmed_id' in gse.metadata:
			print('PubMed ID: %s' % gse.metadata['pubmed_id'][0])
			
		# Supplementary file download links
		if 'supplementary_file' in gse.metadata:
			print('Supplementary files: %s' % gse.metadata['supplementary_file'])
		