import cv2
import numpy as np
import os

# ASCII characters based on brightness levels
ASCII_CHARS = "Ñ@#W$9876543210?!abc;:+=-,._"

# Function to convert RGB to ANSI color escape code
def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

# Resize the frame
def resize_frame(frame, new_width=80):
    height, width, _ = frame.shape
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # Adjust height to keep aspect ratio
    return cv2.resize(frame, (new_width, new_height))

# Convert the frame to ASCII art
def frame_to_ascii(frame):
    ascii_frame = ""
    for j in range(frame.shape[0]):
        for i in range(frame.shape[1]):
            r, g, b = frame[j, i]
            brightness = int(np.mean([r, g, b]))  # Calculate brightness
            char_index = int((brightness / 255) * (len(ASCII_CHARS) - 1))
            ascii_char = ASCII_CHARS[char_index]
            ascii_frame += rgb_to_ansi(r, g, b) + ascii_char  # Add color
        ascii_frame += "\033[0m\n"  # Reset color after each row
    return ascii_frame

# Clear the terminal for live updating
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function to capture live video and display ASCII art
def live_ascii_video():
    cap = cv2.VideoCapture(0)  # Capture video from webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR to RGB to fix color tint
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resized_frame = resize_frame(frame)  # Resize the frame for faster processing
        ascii_art = frame_to_ascii(resized_frame)

        clear_console()  # Clear the console for each new frame
        print(ascii_art)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    live_ascii_video()

