import pygame
from src.controller import Controller  # Import your Controller class

def main():
    pygame.init()
    # Create an instance of your Controller object
    controller = Controller()
    # Call your main loop to start the game
    controller.run()

    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######
    
# https://codefather.tech/blog/if-name-main-python/

    # User Interaction Guidelines for the Virtual World Photography Game

    """
    User Interaction Guide:
    
    1. **Launching the Game**:
        - Run the application by executing the main.py file.
        - Upon startup, the main menu will appear with the following options:
            - **Start Game**: Starts the game and brings up the virtual world.
            - **Exit Game**: Closes the application.
    
    2. **Main Menu**:
        - Use the **mouse** to click on the buttons:
            - **Start Game**: Starts the game.
            - **Exit Game**: Closes the application.

    3. **In-Game Interaction**:
        - **Movement Controls**:
            - Use **Arrow Keys** (Left/Right/Up/Down) or **W/A/S/D** to move the camera or character in the virtual world.
            - **Mouse Scroll**: Zoom in or zoom out.
        
        - **Taking Photos**:
            - Press **Spacebar** to take a photo of the current scene.
        
        - **Camera Rotation**:
            - Hold and drag the **Left Mouse Button** to rotate the camera view.
            - **Right Mouse Button**: Zoom in or out by holding the right mouse button and moving the mouse.
        
        - **Pause and Resume**:
            - Press **Esc Key** to pause the game and bring up the pause menu.
            - The pause menu will have the following options:
                - **Resume Game**: Continues the game.
                - **Save Progress**: Saves your current game progress.
                - **Main Menu**: Returns to the main menu.
                - **Exit Game**: Exits the game.
    
    4. **Game Modes**:
        - **Level 1: Exploration Mode**: Explore the virtual world and capture photos of different objects or scenes.
        - **Level 2: Challenge Mode**: Complete specific tasks such as photographing an object from a specific angle.

    5. **User Feedback**:
        - After taking a photo, a notification will appear with the saved image's name or ID.
        - Scores and progress may be shown on the screen.
        - Upon "Game Over", options to retry or return to the main menu will be displayed.
        
    6. **Exiting the Game**:
        - Click the "X" button in the top right corner of the game window to exit.
        - Press **Esc** to access the pause menu and select "Exit Game" to quit the game.

    7. **Troubleshooting**:
        - If the screen freezes, press **Esc** to pause and then resume the game.
        - Ensure your computer meets the system requirements for running the game. If the game crashes, check for error messages in the console.

    """

if __name__ == '__main__':
    main()