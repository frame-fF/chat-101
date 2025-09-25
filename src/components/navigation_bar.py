import flet as ft


class NavigationBarComponent:
    def __init__(self, page: ft.Page, on_destination_select=None):
        self.page = page
        self.route = page.route
        self.routes = {
            0: "/home",
            1: "/feed",
            2: "/chat",
        }
        # สร้าง reverse mapping เพื่อหา index จาก route
        self.route_to_index = {
            "/": 0,
            "/home": 0,
            "/feed": 1,
            "/chat": 2,
        }
    
    def set_page(self, e):
        self.page.go(self.routes[e.control.selected_index])
    
    def get_selected_index(self):
        """Get the selected index based on current route"""
        return self.route_to_index.get(self.page.route, 0)
    
    def build(self):
        """Build the NavigationBar component"""
        return ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(label="Home", icon=ft.Icons.HOME),
                ft.NavigationBarDestination(label="Feed", icon=ft.Icons.FEED),
                ft.NavigationBarDestination(label="Chat", icon=ft.Icons.CHAT),
            ],
            selected_index=self.get_selected_index(),
            on_change=lambda e: self.set_page(e)
        )