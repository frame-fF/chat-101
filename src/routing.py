import flet as ft
from pages.home import HomePage
from pages.chat import ChatPage
from pages.feed import FeedPage
from pages.setting import SettingPage
from components.navigation_bar import NavigationBarComponent
from components.app_bar import AppBarComponent
from components.navigation_drawer import NavigationDrawerComponent

def route_change(e: ft.RouteChangeEvent):
    """Handle route changes"""
    page = e.page
    page.views.clear()
    
    # สร้าง navigation drawer
    def open_drawer(e):
        page.open(navigation_drawer)
    
    def handle_drawer_selection(selected_index):
        """Handle navigation drawer selection"""
        routes = ["/home", "/chat", "/feed", "/settings"]
        if selected_index < len(routes):
            page.go(routes[selected_index])
    
    navigation_drawer = NavigationDrawerComponent(
        page,
        on_destination_select=handle_drawer_selection
    ).build()
    
    # สร้าง app bar
    app_bar = AppBarComponent(page, on_menu_click=open_drawer).build(
        title="Chat 101",
        show_menu=True
    )
    
    # สร้าง navigation bar
    nav_bar = NavigationBarComponent(page).build()
    
    # กำหนด route และ page ที่สอดคล้องกัน
    if page.route == "/" or page.route == "/home":
        view = ft.View(
            route="/home",
            controls=[HomePage(page).build()],
            appbar=app_bar,
            navigation_bar=nav_bar,
            drawer=navigation_drawer
        )
        page.views.append(view)
    elif page.route == "/chat":
        view = ft.View(
            route="/chat",
            controls=[ChatPage(page).build()],
            appbar=app_bar,
            navigation_bar=nav_bar,
            drawer=navigation_drawer
        )
        page.views.append(view)
    elif page.route == "/feed":
        view = ft.View(
            route="/feed",
            controls=[FeedPage(page).build()],
            appbar=app_bar,
            navigation_bar=nav_bar,
            drawer=navigation_drawer
        )
        page.views.append(view)
    elif page.route == "/settings":
        view = ft.View(
            route="/settings",
            controls=[SettingPage(page).build()],
            appbar=app_bar,
            drawer=navigation_drawer
        )
        page.views.append(view)
    else:
        # Default route
        view = ft.View(
            route="/home",
            controls=[HomePage(page).build()],
            appbar=app_bar,
            navigation_bar=nav_bar,
            drawer=navigation_drawer
        )
        page.views.append(view)
    
    page.update()