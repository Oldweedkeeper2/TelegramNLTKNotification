from os import environ

from environs import Env, EnvError

env = Env()
env.read_env()

try:
    API_ID: str = env.str("API_ID")
    API_HASH: str = env.str("API_HASH")
    APP_NAME: str = env.str("APP_NAME")
    SHORT_NAME: str = env.str("SHORT_NAME")
    FORWARD_GROUP_ID: str = env.str("FORWARD_GROUP_ID")
    ALERT_SOUND_PATH: str = env.str("ALERT_SOUND_PATH")
    environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
except EnvError as e:
    print(f"Ошибка при чтении переменных окружения: {e}")
