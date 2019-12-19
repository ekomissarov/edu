import logging
import logging.config
# https://webdevblog.ru/logging-v-python/

def example1():
    val = "QKRQ!"

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    # filename='app.log', filemode='w',

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical(f'This is a critical message {val}', exc_info=True)

    a = 5
    b = 0
    try:
        c = a / b
    except Exception as msg:
        # logging.error("Exception occurred", exc_info=True)
        logging.exception("Exception occurred")
        '''
        Совет: если вы логируете в обработчике исключений (try..except…), используйте метод logging.exception(), 
        который регистрирует сообщение с уровнем ERROR и добавляет в сообщение информацию об исключении. 
        Проще говоря, вызов logging.exception() похож на вызов logging.error (exc_info = True). 
        Но поскольку этот метод всегда выводит информацию об исключении, его следует вызывать только в обработчике исключений.
        '''


def example2():
    '''
        Использование Handlers
    '''
    logger = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('file.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    logger.warning('This is a warning')
    logger.error('This is an error')


def example3():
    logging.config.fileConfig(fname='log_config.txt', disable_existing_loggers=False)
    # Get the logger specified in the file
    logger = logging.getLogger(__name__)
    logger.debug('This is a debug message')


if __name__ == '__main__':
    print("="*30)
    #example1()
    #example2()
    example3()
