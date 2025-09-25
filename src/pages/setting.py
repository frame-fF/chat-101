import flet as ft


class SettingPage:
    def __init__(self, page: ft.Page):
        self.page = page
    
    def build(self):
        """Build the Setting page"""
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Settings", 
                        size=30, 
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.PRIMARY
                    ),
                    ft.Divider(),
                    
                    # Profile Section
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.PERSON),
                                    title=ft.Text("Profile"),
                                    subtitle=ft.Text("Manage your profile information"),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                                ),
                            ]),
                            padding=10,
                        )
                    ),
                    
                    # Account Settings
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.ACCOUNT_CIRCLE),
                                    title=ft.Text("Account"),
                                    subtitle=ft.Text("Account settings and privacy"),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                                ),
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.NOTIFICATIONS),
                                    title=ft.Text("Notifications"),
                                    subtitle=ft.Text("Manage notification preferences"),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                                ),
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.SECURITY),
                                    title=ft.Text("Security"),
                                    subtitle=ft.Text("Password and security settings"),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                                ),
                            ]),
                            padding=10,
                        )
                    ),
                    
                    # App Settings
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.DARK_MODE),
                                    title=ft.Text("Dark Mode"),
                                    subtitle=ft.Text("Toggle dark/light theme"),
                                    trailing=ft.Switch(value=False),
                                ),
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.LANGUAGE),
                                    title=ft.Text("Language"),
                                    subtitle=ft.Text("Change app language"),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                                ),
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.STORAGE),
                                    title=ft.Text("Storage"),
                                    subtitle=ft.Text("Manage app storage"),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                                ),
                            ]),
                            padding=10,
                        )
                    ),
                    
                    # Support Section
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.HELP),
                                    title=ft.Text("Help & Support"),
                                    subtitle=ft.Text("Get help and contact support"),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                                ),
                                ft.ListTile(
                                    leading=ft.Icon(ft.Icons.INFO),
                                    title=ft.Text("About"),
                                    subtitle=ft.Text("App information and version"),
                                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                                ),
                            ]),
                            padding=10,
                        )
                    ),
                ],
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=20,
        )
