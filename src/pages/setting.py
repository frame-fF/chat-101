import flet as ft


class SettingPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.theme_toggle = ft.Switch(
            label="Dark Theme",
            value=self.page.theme_mode == ft.ThemeMode.DARK,
            on_change=self.theme_changed
        )
    
    def theme_changed(self, e):
        """Handle theme mode change"""
        if self.theme_toggle.value:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()
    
    def build(self):
        """Build the settings page content"""
        return ft.Column(
            controls=[
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.DARK_MODE),
                                    title=ft.Text("Appearance"),
                                    subtitle=ft.Text("Switch between light and dark theme"),
                                ),
                                ft.Container(
                                    content=self.theme_toggle,
                                    padding=ft.padding.only(left=16, right=16, bottom=16)
                                )
                            ],
                            spacing=0
                        ),
                        padding=16
                    ),
                    elevation=2
                ),
                ft.Container(height=20),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.INFO),
                                    title=ft.Text("About"),
                                    subtitle=ft.Text("App information"),
                                ),
                                ft.Container(
                                    content=ft.Text(
                                        "Flet Course Book App\nVersion 1.0.0",
                                        text_align=ft.TextAlign.LEFT
                                    ),
                                    padding=ft.padding.only(left=16, right=16, bottom=16)
                                )
                            ],
                            spacing=0
                        ),
                        padding=16
                    ),
                    elevation=2
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )