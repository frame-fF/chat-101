import flet as ft


class HomePage:
    def __init__(self, page: ft.Page):
        self.page = page
    
    def build(self):
        """Build the home page content"""
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(
                                name=ft.Icons.HOME,
                                size=80,
                                color=ft.Colors.BLUE
                            ),
                            ft.Text(
                                "Welcome to Home Page",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Text(
                                "This is the main home page of the application.",
                                size=16,
                                text_align=ft.TextAlign.CENTER,
                                color=ft.Colors.GREY_700
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                    ),
                    padding=40,
                    alignment=ft.alignment.center
                ),
                ft.Container(height=20),
                ft.Row(
                    controls=[
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(ft.Icons.DASHBOARD, size=40, color=ft.Colors.GREEN),
                                        ft.Text("Dashboard", weight=ft.FontWeight.BOLD),
                                        ft.Text("View your dashboard", size=12, color=ft.Colors.GREY_600)
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5
                                ),
                                padding=20,
                                width=150,
                                height=120
                            ),
                            elevation=2
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(ft.Icons.ANALYTICS, size=40, color=ft.Colors.ORANGE),
                                        ft.Text("Analytics", weight=ft.FontWeight.BOLD),
                                        ft.Text("View analytics", size=12, color=ft.Colors.GREY_600)
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5
                                ),
                                padding=20,
                                width=150,
                                height=120
                            ),
                            elevation=2
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(ft.Icons.NOTIFICATIONS, size=40, color=ft.Colors.RED),
                                        ft.Text("Notifications", weight=ft.FontWeight.BOLD),
                                        ft.Text("Check updates", size=12, color=ft.Colors.GREY_600)
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5
                                ),
                                padding=20,
                                width=150,
                                height=120
                            ),
                            elevation=2
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    wrap=True
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
