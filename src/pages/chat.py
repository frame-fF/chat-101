import flet as ft


class ChatPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.messages = []
        self.message_input = ft.TextField(
            hint_text="Type your message...",
            expand=True,
            on_submit=self.send_message
        )
        self.messages_column = ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO,
            auto_scroll=True,
            expand=True
        )
    
    def send_message(self, e):
        """Send a new message"""
        message_text = self.message_input.value.strip()
        if message_text:
            # Add user message
            self.add_message(message_text, is_user=True)
            self.message_input.value = ""
            
            # Add bot response (simulate)
            self.add_bot_response(message_text)
            
            self.page.update()
    
    def add_message(self, text, is_user=True):
        """Add a message to the chat"""
        message_container = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        "You" if is_user else "Bot",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE if is_user else ft.Colors.GREEN
                    ),
                    ft.Text(text, selectable=True)
                ],
                spacing=2
            ),
            padding=10,
            margin=ft.margin.only(bottom=10),
            bgcolor=ft.Colors.BLUE_50 if is_user else ft.Colors.GREEN_50,
            border_radius=10,
            alignment=ft.alignment.center_left if not is_user else ft.alignment.center_right
        )
        
        self.messages_column.controls.append(message_container)
    
    def add_bot_response(self, user_message):
        """Add bot response (simulated)"""
        responses = [
            "That's interesting! Tell me more.",
            "I understand what you mean.",
            "Thanks for sharing that with me.",
            "How can I help you with that?",
            "That sounds great!",
            f"You said: '{user_message}'. Is that correct?"
        ]
        
        import random
        response = random.choice(responses)
        self.add_message(response, is_user=False)
    
    def build(self):
        """Build the chat page content"""
        # Add some initial messages
        if not self.messages_column.controls:
            self.add_message("Hello! How can I help you today?", is_user=False)
        
        return ft.Column(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(
                                name=ft.Icons.CHAT,
                                size=40,
                                color=ft.Colors.GREEN
                            ),
                            ft.Text(
                                "Chat",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                text_align=ft.TextAlign.CENTER
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5
                    ),
                    padding=ft.padding.only(bottom=10)
                ),
                ft.Container(
                    content=self.messages_column,
                    border=ft.border.all(1, ft.Colors.GREY_300),
                    border_radius=10,
                    padding=10,
                    expand=True
                ),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            self.message_input,
                            ft.IconButton(
                                icon=ft.Icons.SEND,
                                on_click=self.send_message,
                                bgcolor=ft.Colors.BLUE,
                                icon_color=ft.Colors.WHITE
                            )
                        ],
                        spacing=10
                    ),
                    padding=ft.padding.only(top=10)
                )
            ],
            expand=True
        )
