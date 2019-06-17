import logging

extData = {
    'user': 'john@doe.com'
}
def anotherFunc():

    logging.debug("This is debug message", extra=extData)

def main():
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User: %(user)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"

    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    logging.debug("this is debug message", extra=extData)
    logging.info("this is info message", extra=extData)
    logging.warning("this is warning message", extra=extData)
    logging.error("this is error message", extra=extData)
    logging.critical("this is critical message", extra=extData)

    logging.info("This is test with variable {}".format("string"), extra=extData)
    anotherFunc()

if __name__ == "__main__":
    main()