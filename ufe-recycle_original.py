#!/usr/bin/python
# coding: utf-8

from lib.config import *
from lib.functions import *
import os
import shutil

# Search next video to recycle
pending_original_recycle, pending_video_list = select_next_original_recycle()
if pending_original_recycle == 1 :
	for registry in pending_video_list :
		vhash = registry[0]
		filename_san = registry[1]
		# Name of thumbnail	
		#filename_san_n, filename_san_e = os.path.splitext(filename_san)
		#thumbnail_name = "%s.jpg" % (filename_san_n) 
		# Delete the file
		os.unlink(original+"/"+filename_san)
		logthis('The file %s/%s was erased.' % (original, filename_san))
		# Delete the thumbnail
                #os.unlink(original+"/"+thumbnail_name)
                #logthis('The file %s/%s was erased.' % (original, thumbnail_name)	
		# Delete the directory 	
                shutil.rmtree(encoded+"/"+vhash)
		logthis('The directory %s/%s was erased' % (encoded, vhash))		
		# Update status
		update_original_recycle_status(3, vhash)
else :
	print "No original videos left to recycle."
