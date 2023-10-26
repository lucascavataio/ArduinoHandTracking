# ArduinoHandTracking
Control the light intensity of an LED with tracking in your hand. Using the firmata library in Arduino IDE.

### Controlling LED Intensity with Hand Gestures and MediaPipe Hands

This project demonstrates how to control the intensity of an LED light using hand gestures with MediaPipe Hands.

## Requirements:

- Python 3.7 - 3.10, MediaPIpe only works between these versions...
- OpenCV 4.4 or higher
- MediaPipe 0.8.8 or higher
- Arduino board with PWM pin
- LED connected to PWM pin

## Arduino IDE Instructions:

1. Install the Firmata library

2. Go to File/Examples/Firmata/StandardFirmata, then upload to your microcontroller

## Python Instructions:

1. Install the required dependencies:

    ```bash
    pip install pyfirmata2 opencv-python mediapipe
    ```

2. Connect the LED to a PWM pin on your Arduino board.

3. Open the `main.py` file in a text editor and update the `targetLedPin` variable to match the PWM pin that the LED is connected to.

4. Connect the Arduino board to your computer using a USB cable.

5. Run the `main.py` file.

## Usage:

To control the intensity of the LED, place your hand in front of the camera. The distance between your thumb and index finger will determine the intensity of the LED. How far your thumb and index finger are, the brighter the LED will be.

To exit the program, press Ctrl+C.

## Troubleshooting:

If you are having problems running the program, please check the following:

- Make sure that you have the required dependencies installed.
- Ensure that the LED is connected to a PWM pin on your Arduino board.
- Verify that the Arduino board is connected to your computer using a USB cable.
- Double-check that the `targetLedPin` variable in the `main.py` file matches the PWM pin that the LED is connected to.

If you are still having problems, please open an issue on this repo.