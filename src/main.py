import flet as ft
from components.navigation_bar import NavigationBarComponent
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

    page.navigation_bar = NavigationBarComponent(page).build()
    page.on_route_change = route_change
    page.update()




ft.app(target=main)
