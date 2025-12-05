import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    
    greeting_text = ft.Text(value='Hello world')

    
    greeting_history = []
    history_text = ft.Text(value="История приветствий:")

    
    favorite_names = []
    favorite_text = ft.Text(value="Избранные имена:")

    
    last_name = {"value": None}

    
    def on_button_click(_):
        name = name_input.value.strip()
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f"{timestamp} Hello {name}"
            greeting_text.color = None

            last_name["value"] = name

            
            greeting_history.append(f"{timestamp} — {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

            
            favorite_names.append(name)
            favorite_text.value = "Избранные имена:\n" + "\n".join(favorite_names)

            name_input.value = ""
        else:
            greeting_text.value = "Введите корректное имя"
            greeting_text.color = ft.Colors.RED

        page.update()

    
    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    
    name_input = ft.TextField(
        label="Введите имя",
        on_submit=on_button_click,
        expand=True
    )

    
    send_btn = ft.ElevatedButton(text="send", on_click=on_button_click)
    clear_btn = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    
    page.add(
        ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([name_input, send_btn, clear_btn]),
        ft.Divider(),
        history_text,
        ft.Divider(),
        favorite_text     
    )

ft.app(target=main, view=ft.WEB_BROWSER)
 




 