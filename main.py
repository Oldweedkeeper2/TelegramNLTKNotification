#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from core.alert.texts.art import purple_ascii_art, created_by_text, attention_text
    import asyncio
    from core import app
    
    loop = asyncio.get_event_loop()
    try:
        print(purple_ascii_art)
        print(created_by_text)
        print(attention_text)
        try:
            loop.run_until_complete(app.run())
            
        except Exception as e:
            # print(f"Произошла ошибка: {e}")
            # traceback.print_exc()  # Вывод трассировки стека
            pass
    except EOFError as e:
        pass
    except KeyboardInterrupt as e:
        pass
