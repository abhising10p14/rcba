import logging

LOGLEVEL = 3 #TODO: this should be taken from config 
LOGOBJ = None


def getLogger():
    global LOGOBJ
    if LOGOBJ is None:
        LOGOBJ = logging.getLogger(__name__)
        LOGOBJ.setLevel(LOGLEVEL)
        LOGOBJ.basicConfig(format='%(levelname)s:%(message)s',filename='logFile.log', level=logging.DEBUG)
    return LOGOBJ



