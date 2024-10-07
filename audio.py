import speech_recognition as sr
from gpiozero import LED
from time import sleep

# Initialize the LED on GPIO pin 22 of the Raspberry Pi
led = LED(22)

# Initialize the recognizer object for speech recognition
recognizer = sr.Recognizer()

# Function to listen for voice commands
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")  # Inform the user that the system is listening
        audio = recognizer.listen(source)  # Capture audio input from the microphone

        try:
            # Recognize the spoken command using Google's speech recognition service
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")  # Print the recognized command
            return command
        except sr.UnknownValueError:
            # Error handling if the speech is unintelligible
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            # Error handling if there's an issue with the Google API request (e.g., no internet)
            print("Request failed; check your internet connection.")
        return ""

# Function to control the LED based on the recognized voice command
def control_light(command):
    if "turn on" in command:
        # If the command contains "turn on", turn the LED on
        print("Turning ON the light")
        led.on()
    elif "turn off" in command:
        # If the command contains "turn off", turn the LED off
        print("Turning OFF the light")
        led.off()
    else:
        # If the command is not recognized, inform the user
        print("Command not recognized")

# Main loop to continuously listen and control the light
while True:
    command = listen_for_command()  # Listen for a voice command
    control_light(command)          # Control the light based on the command
    sleep(2)  # Small delay between successive commands to avoid overwhelming the system
