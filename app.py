from src.mlproject.logger import logging
from src.mlproject.exception import CustomerException
import sys


if __name__=="__main__":
    logging.info("The Execution has started")


    try:
        a = (1 / 0)
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomerException(e,sys) # type: ignore
    