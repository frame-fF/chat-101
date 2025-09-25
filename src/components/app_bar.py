import flet as ft


class AppBarComponent:
    def __init__(self, page: ft.Page, on_menu_click=None):
        self.page = page
        self.on_menu_click = on_menu_click
    
    def check_item_clicked(self, e):
        """Handle popup menu item click"""
        e.control.checked = not e.control.checked
        self.page.update()
    
    def build(self, title="AppBar Example", show_menu=True, leading_widget=None):
        """Build the AppBar component"""
        leading = leading_widget
        if leading is None and show_menu:
            leading = ft.IconButton(
                icon=ft.Icons.MENU,
                on_click=self.on_menu_click if self.on_menu_click else lambda e: None
            )
        
        return ft.AppBar(
            leading=leading,
            leading_width=40,
            title=ft.Text(title),
            center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[
                ft.IconButton(ft.Icons.FILTER_3),
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item", 
                            checked=False, 
                            on_click=self.check_item_clicked
                        ),
                    ]
                ),
            ],
        )
