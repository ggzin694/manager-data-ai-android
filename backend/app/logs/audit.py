import logging
logger=logging.getLogger('manager_data_ai')
def audit(event,**data):logger.info('%s %s',event,data)
