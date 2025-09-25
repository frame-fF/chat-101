import flet as ft


class NavigationDrawerComponent:
    def __init__(self, page: ft.Page, on_destination_select=None, on_dismiss=None):
        self.page = page
        self.on_destination_select = on_destination_select
        self.on_dismiss = on_dismiss
        self.drawer = None
    
    def handle_dismissal(self, e):
        """Handle drawer dismissal"""
        print("Drawer dismissed!")
        if self.on_dismiss:
            self.on_dismiss()

    def handle_change(self, e):
        """Handle drawer destination selection"""
        selected_index = e.control.selected_index
        print(f"Selected Index changed: {selected_index}")
        if self.drawer:
            self.page.close(self.drawer)
        
        if self.on_destination_select:
            self.on_destination_select(selected_index)
    
    def build(self):
        """Build the NavigationDrawer component"""
        self.drawer = ft.NavigationDrawer(
            on_dismiss=self.handle_dismissal,
            on_change=self.handle_change,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Home", 
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.HOME),
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.CHAT_OUTLINED),
                    label="Chat",
                    selected_icon=ft.Icons.CHAT,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.FEED_OUTLINED),
                    label="Feed",
                    selected_icon=ft.Icons.FEED,
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.SETTINGS_OUTLINED),
                    label="Settings",
                    selected_icon=ft.Icons.SETTINGS,
                ),
            ],
        )
        return self.drawer
