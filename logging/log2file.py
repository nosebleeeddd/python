import logging

# set level to display all messages
logging.basicConfig(level=logging.DEBUG)

# create logging and set logging level
logger = logging.getLogger("my logger")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("mylog.log")
# only log INFO,WARNING,CRITICAL,ERROR, to file no DEBUG
handler.setLevel(logging.INFO)

# YOU CAN ALSO SET A FORMAT
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)


# add handler to log to file
logger.addHandler(handler)

logger.debug("This is a debug message")
logger.info("this is important information!")
