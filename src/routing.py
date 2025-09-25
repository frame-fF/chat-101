import flet as ft
from pages.home import HomePage
from pages.chat import ChatPage
from pages.feed import FeedPage


def route_change(e: ft.RouteChangeEvent):
    """Handle route changes"""
    page = e.page
    page.views.clear()
    
    # กำหนด route และ page ที่สอดคล้องกัน
    if page.route == "/" or page.route == "/home":
        page.views.append(HomePage(page).build())
    elif page.route == "/chat":
        page.views.append(ChatPage(page).build())
    elif page.route == "/feed":
        page.views.append(FeedPage(page).build())
    else:
        # Default route
        page.views.append(HomePage(page).build())
    
    page.update()