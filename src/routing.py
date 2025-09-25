import flet as ft
from pages.home import HomePage
from pages.chat import ChatPage
from pages.feed import FeedPage
from components.navigation_bar import NavigationBarComponent


def route_change(e: ft.RouteChangeEvent):
    """Handle route changes"""
    page = e.page
    page.views.clear()
    
    # สร้าง navigation bar
    nav_bar = NavigationBarComponent(page).build()
    
    # กำหนด route และ page ที่สอดคล้องกัน
    if page.route == "/" or page.route == "/home":
        view = ft.View(
            route="/home",
            controls=[HomePage(page).build()],
            navigation_bar=nav_bar
        )
        page.views.append(view)
    elif page.route == "/chat":
        view = ft.View(
            route="/chat",
            controls=[ChatPage(page).build()],
            navigation_bar=nav_bar
        )
        page.views.append(view)
    elif page.route == "/feed":
        view = ft.View(
            route="/feed",
            controls=[FeedPage(page).build()],
            navigation_bar=nav_bar
        )
        page.views.append(view)
    else:
        # Default route
        view = ft.View(
            route="/home",
            controls=[HomePage(page).build()],
            navigation_bar=nav_bar
        )
        page.views.append(view)
    
    page.update()