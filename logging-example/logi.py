import logging
# https://webdevblog.ru/logging-v-python/

def fun():
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


if __name__ == '__main__':
    print("="*30)
    fun()
