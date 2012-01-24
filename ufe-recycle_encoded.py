#!/usr/bin/python
# coding: utf-8

from lib.config import *
from lib.functions import *
import os

# Inicializo variable
check_pending=1

# Empiezo el loop - lo corto si no hay nada para borrar
while check_pending==1 :
	# Busco el proximo a reciclar
	pending_encoded_recycle, t_created, vhash, encode_time, vpid, encode_file = select_next_encoded_recycle()
	# Hay algo para reciclar?
	if pending_encoded_recycle == 1 :
		# Borro el video para liberar espacio
		# (el directorio y las imagenes se borran cuando se borra el video original)
		os.unlink(encoded+"/"+vhash+"/"+encode_file)
		logthis('%s/%s/%s was erased.' % (encoded, vhash, encode_file))
		# actualizo el estado
		update_encoded_recycle_status(3, vhash, vpid)
	else :
		print "No encoded videos left to recycle."
		check_pending=0
