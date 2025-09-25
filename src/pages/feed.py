import flet as ft
from datetime import datetime, timedelta
import random


class FeedPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.feed_items = self.generate_feed_items()
    
    def generate_feed_items(self):
        """Generate sample feed items"""
        items = []
        authors = ["Alice Johnson", "Bob Smith", "Carol Davis", "David Wilson", "Eva Brown"]
        contents = [
            "Just finished an amazing project using Flet! The possibilities are endless. 🚀",
            "Beautiful sunset today! Sometimes we need to pause and appreciate the simple things in life. 🌅",
            "Learning new programming concepts every day. The journey never ends! 💻",
            "Great coffee and good vibes at the local café. Perfect way to start the morning! ☕",
            "Excited to share my latest creation with the community. Feedback is always welcome! 🎨",
            "Working on improving my coding skills. Practice makes perfect! 📚",
            "Nature walk was exactly what I needed today. Fresh air and clear thoughts. 🌲",
            "Team collaboration at its finest! Amazing what we can achieve together. 🤝"
        ]
        
        for i in range(10):
            time_ago = datetime.now() - timedelta(minutes=random.randint(5, 1440))
            items.append({
                "id": i,
                "author": random.choice(authors),
                "content": random.choice(contents),
                "time": time_ago,
                "likes": random.randint(0, 50),
                "comments": random.randint(0, 15),
                "liked": False
            })
        
        return items
    
    def format_time_ago(self, time):
        """Format time ago string"""
        now = datetime.now()
        diff = now - time
        
        if diff.days > 0:
            return f"{diff.days}d ago"
        elif diff.seconds > 3600:
            hours = diff.seconds // 3600
            return f"{hours}h ago"
        else:
            minutes = diff.seconds // 60
            return f"{minutes}m ago"
    
    def toggle_like(self, item_id):
        """Toggle like status for a feed item"""
        def handler(e):
            for item in self.feed_items:
                if item["id"] == item_id:
                    item["liked"] = not item["liked"]
                    if item["liked"]:
                        item["likes"] += 1
                        e.control.icon = ft.Icons.FAVORITE
                        e.control.icon_color = ft.Colors.RED
                    else:
                        item["likes"] -= 1
                        e.control.icon = ft.Icons.FAVORITE_BORDER
                        e.control.icon_color = ft.Colors.GREY
                    
                    # Update the likes count text
                    parent_row = e.control.parent
                    likes_text = parent_row.controls[1]  # Assuming likes text is the second control
                    likes_text.value = str(item["likes"])
                    break
            
            self.page.update()
        
        return handler
    
    def create_feed_item(self, item):
        """Create a single feed item card"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        # Header with author and time
                        ft.Row(
                            controls=[
                                ft.CircleAvatar(
                                    content=ft.Text(
                                        item["author"][0],
                                        color=ft.Colors.WHITE,
                                        weight=ft.FontWeight.BOLD
                                    ),
                                    bgcolor=ft.Colors.BLUE,
                                    radius=20
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            item["author"],
                                            weight=ft.FontWeight.BOLD,
                                            size=14
                                        ),
                                        ft.Text(
                                            self.format_time_ago(item["time"]),
                                            size=12,
                                            color=ft.Colors.GREY_600
                                        )
                                    ],
                                    spacing=2,
                                    expand=True
                                )
                            ],
                            spacing=10
                        ),
                        # Content
                        ft.Container(
                            content=ft.Text(
                                item["content"],
                                size=14,
                                selectable=True
                            ),
                            padding=ft.padding.only(top=10, bottom=10)
                        ),
                        # Actions
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.FAVORITE if item["liked"] else ft.Icons.FAVORITE_BORDER,
                                    icon_color=ft.Colors.RED if item["liked"] else ft.Colors.GREY,
                                    on_click=self.toggle_like(item["id"])
                                ),
                                ft.Text(str(item["likes"]), size=12, color=ft.Colors.GREY_600),
                                ft.IconButton(
                                    icon=ft.Icons.COMMENT_OUTLINED,
                                    icon_color=ft.Colors.GREY
                                ),
                                ft.Text(str(item["comments"]), size=12, color=ft.Colors.GREY_600),
                                ft.IconButton(
                                    icon=ft.Icons.SHARE_OUTLINED,
                                    icon_color=ft.Colors.GREY
                                )
                            ],
                            spacing=5
                        )
                    ],
                    spacing=5
                ),
                padding=15
            ),
            elevation=1,
            margin=ft.margin.only(bottom=10)
        )
    
    def refresh_feed(self, e):
        """Refresh the feed with new items"""
        self.feed_items = self.generate_feed_items()
        self.page.update()
    
    def build(self):
        """Build the feed page content"""
        feed_column = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(
                                name=ft.Icons.FEED,
                                size=30,
                                color=ft.Colors.ORANGE
                            ),
                            ft.Text(
                                "Feed",
                                size=20,
                                weight=ft.FontWeight.BOLD
                            ),
                            ft.IconButton(
                                icon=ft.Icons.REFRESH,
                                on_click=self.refresh_feed,
                                tooltip="Refresh feed"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    padding=ft.padding.only(bottom=10)
                )
            ] + [self.create_feed_item(item) for item in self.feed_items],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=0
        )
        
        return feed_column
