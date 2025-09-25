import flet as ft
from components.navigation_bar import NavigationBarComponent


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

    page.navigation_bar = NavigationBarComponent(page).build()

    page.update()




ft.app(target=main)
