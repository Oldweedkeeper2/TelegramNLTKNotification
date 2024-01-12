import pygame


def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)  # Воспроизведение звука в бесконечнейшем цикле


def stop_sound():
    pygame.mixer.music.stop()
    alert_window.destroy()


def show_alert_window():
    import tkinter as tk
    from tkinter import ttk
    global alert_window
    alert_window = tk.Tk()
    alert_window.title("Алерт")
    
    window_width = 300
    window_height = 100
    
    # Получение размеров экрана
    screen_width = alert_window.winfo_screenwidth()
    screen_height = alert_window.winfo_screenheight()
    
    # Расчет x и y координат для Tkinter окна
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    
    # Устанавливаем размер и позицию окна
    alert_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    alert_window.attributes("-topmost", True)  # Окно всегда поверх других
    
    # Настройка стиля кнопки
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), background="red")
    
    # Создание кнопки с красивым стилем
    stop_button = ttk.Button(alert_window, text="Остановить воспроизведение", command=stop_sound, style="TButton")
    stop_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Активировать и выбрать окно
    alert_window.focus_force()
    alert_window.mainloop()
