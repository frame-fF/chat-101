import flet as ft
from routing import route_change


def main(page: ft.Page):
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            android=ft.PageTransitionTheme.NONE,
            ios=ft.PageTransitionTheme.NONE,
            linux=ft.PageTransitionTheme.NONE,
            macos=ft.PageTransitionTheme.NONE,
            windows=ft.PageTransitionTheme.NONE,
        )
    )

    page.on_route_change = route_change
    page.go("/home")  # เริ่มต้นที่หน้า home
    page.update()




ft.app(target=main)
