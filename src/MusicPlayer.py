from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
import Actions


class MyKivyApp(App):
    def build(self):
        # Set the window size and background color
        Window.size = (600, 250)
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Dark background color

        # Create a root layout to hold the background and main layout
        root_layout = FloatLayout()

        # Background Image
        background = Image(source="../img/bkg.png", allow_stretch=True, size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})

        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(None, None), size=(600, 250), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Music Player Layout
        music_layout = BoxLayout(orientation='vertical', size_hint=(None, None), padding=20, spacing=20)
        music_layout.size = (300, 200)  # Ensure the music layout fits on screen

        # Replace direct song_title addition with a FloatLayout
        title_layout = FloatLayout(size_hint=(None, None), size=(300, 60))

        song_title = Label(
            text="SONG TITLE AVAILABLE",
            color=(1, 1, 1, 1),
            font_size=24,
            bold=True,
            size_hint=(None, None),
            halign='left',
            valign='bottom',
            pos=(250,250),
            text_size=(300, None)  # Limit the width to 300 pixels
        )

        # Bind the size to the texture_size to ensure the height adjusts based on the text content
        song_title.bind(
            texture_size=lambda instance, size: setattr(instance, 'size', (300, size[1]))
        )

        # Add the label to the float layout
        title_layout.add_widget(song_title)

        # Add the float layout to the music layout
        music_layout.add_widget(title_layout)

        # Music Controls
        controls = BoxLayout(orientation='vertical', size_hint=(None, 0.3), width=280, spacing=20, padding=[15, 0, 0, -25])

        # Create ImageButtons with consistent styling
        speak_button = Image(source="../img/mic.png", size_hint=(None, None), size=(100, 100))
        pause_button = Image(source="../img/pause.png", size_hint=(None, None), size=(40, 40))
        next_button = Image(source="../img/skip.png", size_hint=(None, None), size=(40, 40))

        # Define the image sources for the pressed state
        speak_button_down = "../img/mic_down.png"
        pause_button_down = "../img/pause_down.png"
        next_button_down = "../img/skip_down.png"

        # Attach callbacks to buttons
        speak_button.bind(on_touch_down=lambda instance, touch: self.on_button_down(instance, touch, speak_button_down, Actions.speak_action))
        speak_button.bind(on_touch_up=lambda instance, touch: self.on_button_up(instance, touch, "../img/mic.png"))
        pause_button.bind(on_touch_down=lambda instance, touch: self.on_button_down(instance, touch, pause_button_down, Actions.toggle_action))
        pause_button.bind(on_touch_up=lambda instance, touch: self.on_button_up(instance, touch, "../img/pause.png"))
        next_button.bind(on_touch_down=lambda instance, touch: self.on_button_down(instance, touch, next_button_down, Actions.next_action))
        next_button.bind(on_touch_up=lambda instance, touch: self.on_button_up(instance, touch, "../img/skip.png"))

        # Create a horizontal BoxLayout for pause and next
        button_row = BoxLayout(orientation='horizontal', size_hint=(None, None), spacing=150, padding=[0,0,0,-25])

        # Add pause and next to the horizontal layout
        button_row.add_widget(pause_button)
        button_row.add_widget(next_button)

        # Create a vertical layout for the speak button
        speak_layout = BoxLayout(orientation='vertical', size_hint=(None, None), padding=[65,0,0,-85])
        speak_layout.add_widget(speak_button)

        # Add the speak_layout and button_row to the controls
        controls.add_widget(speak_layout)
        controls.add_widget(button_row)

        # Add the controls to the music layout
        music_layout.add_widget(controls)

        # Center music layout vertically in the main layout
        center_layout = BoxLayout(orientation='horizontal', size_hint=(1, 1), padding=[0, 0], spacing=0)
        center_layout.add_widget(Widget(size_hint_y=0.35))  # Spacer to center vertically
        center_layout.add_widget(music_layout)
        center_layout.add_widget(Widget(size_hint_y=0.35))  # Spacer to center vertically

        main_layout.add_widget(center_layout)

        # Add background and main layout to root layout
        root_layout.add_widget(background)
        root_layout.add_widget(main_layout)

        # Create another FloatLayout with an image you want on top
        top_layout = FloatLayout(size_hint=(None, None), size=(100, 100), pos_hint={'center_x': 0.5, 'center_y': 0.9})

        top_image = Image(
            source="../img/empty.png",
            size_hint=(None, None),
            allow_stretch=True,
            size=(180, 180),
            pos=(56,115)
        )

        top_layout.add_widget(top_image)
        root_layout.add_widget(top_layout)

        return root_layout

    def on_button_down(self, instance, touch, down_image, action):
        if instance.collide_point(*touch.pos):
            instance.source = down_image
            action()

    def on_button_up(self, instance, touch, up_image):
        if instance.collide_point(*touch.pos):
            instance.source = up_image

if __name__ == "__main__":
    MyKivyApp().run()
