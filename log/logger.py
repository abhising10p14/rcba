import logging

LOGLEVEL = 3 #TODO: this should be taken from config 
LOGOBJ = None


def getLogger():
    global LOGOBJ
    if LOGOBJ is None:
        LOGOBJ = logging.getLogger(__name__)
        LOGOBJ.setLevel(LOGLEVEL)
    return LOGOBJ

def getLogLevel():
	return LOGLEVEL

def setLogLevel():
	if LOGOBJ is not None:
		LOGOBJ.setLevel(LOGLEVEL)
	else:
		
