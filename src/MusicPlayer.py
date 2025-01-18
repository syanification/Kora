from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
import Actions


class MyKivyApp(App):

    def build(self):
        # Set the window size and background color
        Window.size = (400, 300)
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Dark background color

        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Music Player Layout
        music_layout = BoxLayout(
            orientation="vertical", size_hint=(None, None), padding=20, spacing=20
        )
        music_layout.size = (300, 200)  # Ensure the music layout fits on screen

        # Song Title Display
        song_title = Label(
            text="Now Playing:",
            color=(1, 1, 1, 1),
            font_size=24,
            bold=True,
            size_hint=(1, None),
            size_hint_y=None,
            height=50,
            halign="center",
        )
        music_layout.add_widget(song_title)

        # Music Controls
        controls = BoxLayout(size_hint=(None, 0.3), width=280, spacing=10)

        # Create buttons with consistent styling
        play_button = Button(
            text="Play",
            size_hint=(None, None),
            size=(130, 50),
            background_normal="",
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size=18,
        )
        pause_button = Button(
            text="Pause",
            size_hint=(None, None),
            size=(130, 50),
            background_normal="",
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size=18,
        )
        next_button = Button(
            text="Next",
            size_hint=(None, None),
            size=(130, 50),
            background_normal="",
            background_color=(0.2, 0.2, 0.2, 1),
            color=(1, 1, 1, 1),
            font_size=18,
        )

        # Attach callbacks to buttons
        play_button.bind(on_press=lambda instance: Actions.play_action())
        pause_button.bind(on_press=lambda instance: Actions.pause_action())
        next_button.bind(on_press=lambda instance: Actions.next_action())

        # Add buttons to the controls layout
        controls.add_widget(play_button)
        controls.add_widget(pause_button)
        controls.add_widget(next_button)

        # Add the controls to the music layout
        music_layout.add_widget(controls)

        # Center music layout vertically in the main layout
        center_layout = BoxLayout(
            orientation="vertical", size_hint=(1, 1), padding=[10, 0], spacing=20
        )
        center_layout.add_widget(
            Widget(size_hint_y=0.35)
        )  # Spacer to center vertically
        center_layout.add_widget(music_layout)
        center_layout.add_widget(
            Widget(size_hint_y=0.35)
        )  # Spacer to center vertically

        main_layout.add_widget(center_layout)

        return main_layout


if __name__ == "__main__":
    MyKivyApp().run()
