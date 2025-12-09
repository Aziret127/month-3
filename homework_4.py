import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')
    
    greeting_history = []
    history_text = ft.Text(value="история приветствия")
    greeting_history.clear()
    
    def on_button_click(_):
        
        name = name_input.value.strip()
        
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")
        
        if name:
            greeting_text.value = f'{timestamp} Hello {name}'          
            greeting_text.color = None
            name_input.value = None
            
            greeting_history.append(f"{timestamp}-{name}")  
                    
            history_text.value = "история приветсвие:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED
            
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True )

    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    
    def clear_history(_):
        greeting_history.clear()
        history_text.value = "история приветствия:"
        page.update()
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    def remove_history(_): 
        if greeting_history:
          greeting_history.pop()
          history_text.value = "история приветсвие:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "история пуст"
        page.update()
    remove_button = ft.IconButton(icon=ft.Icons.REMOVE, on_click=remove_history)

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)
    
    page.add(view_greeting_text,greeting_text,ft.Row([name_input, button_elevated, clear_button, remove_button]), history_text)

ft.app(target=main, view=ft.WEB_BROWSER)