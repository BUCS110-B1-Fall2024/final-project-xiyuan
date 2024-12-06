# Virtual World Photography
## CS110 B1 Final Project  Fall 2024

## Team Members

Xiyuan Li

***

## Project Description

The Virtual World Photography project allows users to explore a procedurally generated virtual environment and take stunning photographs of landscapes, wildlife, and dynamic events like sunsets or rainstorms. The application mimics the real-world experience of photography, offering customizable camera settings and the ability to save captured shots. With features like interactive challenges and a gallery, the project combines creativity, exploration, and technology.

***    

## GUI Design

### Initial Design
- The interface features:
  1. A main exploration window for viewing and navigating the virtual world.
  2. A control panel for camera settings (e.g., zoom, focus, and filters).
  3. A photo gallery preview to display thumbnails of captured photos.

![initial gui](assets/gui.jpg)

### Final Design
- Enhancements include:
  1. Improved navigation controls for smoother movement.
  2. A menu bar for accessing settings, tutorials, and saved galleries.
  3. Real-time weather and lighting effects for a more immersive experience.
  4. High-quality visuals for better user engagement.

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Procedurally Generated Virtual World: Users explore unique, dynamically created environments.
2. Interactive Camera Settings: Control zoom, focus, exposure, and filters to enhance photo quality.
3. Photo Challenges: Complete creative objectives like capturing rare wildlife or dramatic sunsets.
4. Dynamic Events: Experience changing weather, time of day, and wildlife behavior for diverse photography opportunities.
5. Photo Gallery: Save, view, and manage captured photographs within the application.

### Classes

- World: Manages terrain, objects, and events in the virtual environment.
- Camera: Handles all camera-related functionality, including settings and taking photographs.
- Photo: Stores data for each captured image, including metadata like timestamp and score.
- Gallery: Manages saved photos and provides functionality for displaying them.

## ATP

## ATP

| Step | Procedure                                              | Expected Results                                                         |
|------|--------------------------------------------------------|------------------------------------------------------------|
|  1   | Launch the program by running `main.py`.               | A GUI window opens, showing the virtual environment.       |
|  2   | Use arrow keys or WASD to navigate the virtual world.  | The camera view moves smoothly across the terrain.         |
|  3   | Click the "Take Photo" button or press the spacebar.   | A photo is captured and saved to the gallery.              |
|  4   | Adjust the camera settings (zoom, exposure, etc.).     | The camera view updates to reflect the new settings.       |
|  5   | Open the gallery from the menu or toolbar.             | A gallery window appears, showing all saved photos.        |
|  6   | Select a photo in the gallery and click "Delete".      | The selected photo is removed from the gallery.            |
|  7   | Wait for a dynamic event like a sunset or rainstorm.   | The environment updates to show the event in real-time.    |
|  8   | Exit the program using the "Quit" button or hotkey.    | The application closes gracefully without errors.          |
