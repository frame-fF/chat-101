import flet as ft


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

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(label="Home", icon=ft.Icons.HOME),
            ft.NavigationBarDestination(label="Feed", icon=ft.Icons.FEED),
            ft.NavigationBarDestination(label="Chat", icon=ft.Icons.CHAT),
        ]
    )

    page.update()




ft.app(target=main)
