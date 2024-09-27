# Live ASCII Video in Python

This program captures live video from your webcam and converts each frame into colorful ASCII art. The result is displayed in your terminal, with live updates to simulate a video feed in ASCII format.

## Features

- Converts live webcam video into colorful ASCII art.
- Adjusts the aspect ratio for better viewing.
- Uses ANSI escape codes to display RGB colors in the terminal.
- Easy-to-use interface: simply run the program and see the live ASCII video.
- Press `q` to quit the program.

## Prerequisites

- Python 3.x
- OpenCV (cv2)
- NumPy

## Installation

1. Clone this repository or download the `ascii_video.py` file.
2. Install the required libraries:

    ```bash
    pip install opencv-python numpy
    ```

## How to Run

1. Ensure your webcam is connected and working.
2. Run the Python script:

    ```bash
    python ascii_video.py
    ```

3. The live video will be displayed as ASCII art in your terminal.
4. Press `q` to exit the program.

## How It Works

1. **Frame Capture**: The program captures frames from your webcam using OpenCV.
2. **Frame Resizing**: The frames are resized for faster processing and to maintain an appropriate aspect ratio for ASCII display.
3. **Brightness Calculation**: For each pixel, the program calculates the brightness and selects a corresponding ASCII character based on the brightness level.
4. **Color Mapping**: The program maps the RGB values of each pixel to ANSI escape codes, allowing the ASCII characters to retain the original colors of the video.
5. **Live Update**: The terminal is cleared for each frame to create a live video effect.

## Code Structure

- **`rgb_to_ansi(r, g, b)`**: Converts RGB values to an ANSI escape code for colored terminal output.
- **`resize_frame(frame, new_width=80)`**: Resizes the video frame while maintaining the aspect ratio.
- **`frame_to_ascii(frame)`**: Converts a video frame into an ASCII art string, with RGB colors applied.
- **`clear_console()`**: Clears the terminal screen.
- **`live_ascii_video()`**: Main function that captures video, converts it to ASCII art, and displays it in the terminal.

## Customization

- **Frame Width**: You can adjust the width of the ASCII video by modifying the `new_width` parameter in the `resize_frame` function.
- **ASCII Characters**: You can change the characters used for different brightness levels by modifying the `ASCII_CHARS` string.

## Known Limitations

- This program is designed to run in terminals that support ANSI escape codes. Some terminals may not fully support colored output.
- Performance may vary based on system capabilities and the webcam's frame rate.

## Example Output

