# 🖐️ AI Dynamic Virtual Keyboard

An advanced human-computer interaction project that uses computer vision to create a fully functional, dynamic virtual keyboard. The application tracks the user's hand in real-time via a webcam, allowing them to type by "pressing" keys in the air.

This project goes beyond simple object tracking by implementing a complete, interactive UI with hover effects, click confirmations, sound feedback, and support for special keys like Caps Lock, Spacebar, and Backspace.

---

## ✨ Key Features

-   **Gesture-Based Typing:** Uses the distance between the thumb and index finger to detect a "pinch" gesture, which simulates a key press.
-   **Dynamic & Interactive UI:**
    -   The keyboard is drawn programmatically with Pygame, not a static image.
    -   **Hover Effect:** Keys light up when the user's index finger is over them.
    -   **Click Confirmation:** Keys flash a different color upon a successful press.
    -   **Audio Feedback:** A satisfying "click" sound is played for each key press.
-   **Full Keyboard Functionality:**
    -   Includes numbers, uppercase, and lowercase letters.
    -   A working **CapsLock** key that toggles the keyboard layout.
    -   A functional **Spacebar** and **Backspace** key.
-   **High-Fidelity Hand Tracking:** Powered by **Google's MediaPipe** for robust, real-time tracking of hand landmarks.
-   **Clean User Experience:** The application starts cleanly, suppressing all backend informational logs, and provides clear visual feedback for all interactions.

---

## 🛠️ Technology Stack

-   **Python**
-   **OpenCV:** For webcam capture and core image processing.
-   **MediaPipe:** For high-performance hand and landmark detection.
-   **Pygame:** For creating the display window, drawing the dynamic UI, and handling audio.
-   **NumPy:** For programmatically generating the click sound effect.

---

## 🚀 Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

-   Python 3.9+
-   A webcam connected to your computer.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Zaid2044/AI-Dynamic-Virtual-Keyboard.git
    cd AI-Dynamic-Virtual-Keyboard
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install opencv-python mediapipe numpy pygame
    ```

---

## ⚡ Usage

To run the application, execute the `main.py` script from the project root:

```bash
python src/main.py
```

-  A window will open showing your webcam feed with the keyboard overlay.
-  Hover: Move your index finger over a key to see it light up.
-  Click: While hovering, touch your thumb and index fingertips together.
-  The typed text will appear in the display bar at the top of the screen.
-  Press 'q' or the Esc key to quit. The final typed message will be printed to your console.