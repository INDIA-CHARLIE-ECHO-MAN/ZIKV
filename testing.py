import GEOparse
import datetime

geo = 'GSE132323'
gse = GEOparse.get_GEO(geo=geo, destdir='./') # Get GSE object
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
