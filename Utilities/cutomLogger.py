import logging.handlers
import logging
class LogGen:
    @staticmethod
    def loggen():

        logging.basicConfig(filename="Logs/OrangeHRMAutomationLog.log",format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',filemode='W')
        rotate_file = logging.handlers.RotatingFileHandler(
            "Logs/OrangeHRMAutomationLog.log", maxBytes=1024 * 1024 * 20, backupCount=3
        )
        #logging.basicConfig(filename= "C:\\Users\\bala_\\PycharmProjects\\PageObjectModelSample\\Logs\\automation.log")
        logger = logging.getLogger()
        logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger