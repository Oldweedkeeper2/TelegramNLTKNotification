from pyrogram import filters, Client
from pyrogram.types import Message

import config
from core import app
from core.alert.interface import play_sound, show_alert_window
from core.alert.utils import is_alert_text, is_test_group_text


@app.on_message(filters.private | filters.chat(config.FORWARD_GROUP_ID))
async def handle_message(client: Client, message: Message):
    if message.from_user and message.from_user.is_self:
        return
    
    # Проверка и обработка алертов
    if message.text and is_alert_text(message.text):
        print("Алерт: Найдено совпадение для текста алерта!\n", message.text)
        # Пересылка сообщений в группу
        
        # Здесь можно добавить код для внешнего алерта, например, отправку уведомления
        await client.forward_messages(config.FORWARD_GROUP_ID, message.chat.id, message.id)
        play_sound(config.ALERT_SOUND_PATH)  # Воспроизведение звука алерта
        show_alert_window()
    
    # Проверка на сообщения из тестовой группы
    if message.text and is_test_group_text(message.text):
        print("Тестовая группа: Найдено совпадение для текста тестовой группы!\n", message.text)
        # Пересылка сообщений в группу
        
        await client.forward_messages(config.FORWARD_GROUP_ID, message.chat.id, message.id)
