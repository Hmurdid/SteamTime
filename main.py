from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Static, Input, Button
import time
import os

from module_1 import getSteamTime

class SubmitButton(Button):
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        #Initializing left-content as result_display to change text in left box
        result_display = self.app.query_one("#left-content", Static)
        result_display.update("Loading . . .")
        
        #Getting information via getSteamTime() function in module_1.py
        steam_api_input = self.app.query_one("#STEAM_API_KEY", Input)
        steam_id_input = self.app.query_one("#STEAM_ID", Input)
        api_key = steam_api_input.value
        steam_id = steam_id_input.value
        result = getSteamTime(api_key, steam_id)
        
        #Result checking
        if result['success']:
            result_display.update(result['games_list_text'])
        else:
            result_display.update(f"Error:\n{result['error']}")



class MyApp(App):
    CSS_PATH = "styles.tcss"
    
    def compose(self) -> ComposeResult:
        with Horizontal():
            with VerticalScroll(id="left"):
                yield Static("Information will apear after you will submit API & ID", id="left-content")
                
                
            
            with Vertical(id="right"):
                with VerticalScroll(id="top"):
                    yield Static(
                                f"This application shows information about the time spent on games on Steam. "
                                f"To start using the application, you need to get your Steam API key from the link below.\n\n"
                                f"NEVER SHOW YOUR API TO ANYONE:\nhttps://steamcommunity.com/dev/apikey \n"
                                f"Note: You may need Steam Guard on your phone to verify that it's really you who is creating the API key.\n\n\n"
                                f"After you go to the site and get the API key, you will only need to enter the ID of the desired Steam account.\n\n"
                                f"WARNING:\n1. Your Steam account must be public. Without this, you will not be able to do anything.\n\n"
                                f"2. Make sure that your ID is clean from the URL. This program only accepts clean IDs. Example: "
                                f"76561198085278333\nHave fun >:)\n")
                                
                with Vertical(id="bottom"):
                    with Vertical(id="inputs-container"):
                        yield Input(placeholder="Enter your Steam API", id="STEAM_API_KEY")
                        yield Input(placeholder="Enter your Steam (ID64)", id="STEAM_ID")
                    with Vertical(id="button-container"):
                        yield SubmitButton("Submit", id="submit")

if __name__ == "__main__":
    app = MyApp()
    app.run()