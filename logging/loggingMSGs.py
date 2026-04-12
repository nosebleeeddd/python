# Ways to implement logging to your scripts
import logging

# sets it so you can see INFO msgs, hidden by default
logging.basicConfig(level=logging.INFO)

logging.info("You have got 20 mails in your inbox!")
logging.critical("All components failed!")

logger = logging.getLogger("My logger")
logger.info("The best logger was just created!")
logger.critical("YOUR SYSTEM GONNA EXPLODE MAN!")
logger.log(logging.ERROR, "An error occured!")
