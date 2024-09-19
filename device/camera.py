import picamera2
import time
import RPi.GPIO as GPIO
import pytesseract  # OCR tool
import requests # To send HTTP requests 

# GPIO pin configuration
sensor_pin = 17  # Break beam sensor pin
led_pin = 27 # LED pin

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

# Initialize the camera
camera = picamera2.Picamera2()

# Capture an image with the Raspberry Pi camera
def capture_image(image_path):
    config = camera.create_still_configuration() # To set the image resolution
    camera.configure(config) # Load the configuration 
    camera.start()
    time.sleep(2)  # Allow the camera to adjust settings
    camera.capture_file(image_path)
    camera.stop()
    print(f"Photo saved at: {image_path}")

# Use OCR to extract text from the captured image
def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(image_path)  # Extract text from the image
    print(f"Extracted Text: {text}")
    return text

# Send the extracted text to ChatGPT for further analysis
def send_text_to_chatgpt(extracted_text):
    # OpenAI API call to send extracted text for analysis
    chatgpt_api_endpoint = "https://api.openai.com/v1/completions"
    headers = {
        "Authorization": f"Bearer YOUR_OPENAI_API_KEY",  #!!! API key required 
        "Content-Type": "application/json"
    }
    prompt = f"Extract the sender address from the following text:\n\n{extracted_text}"
    
    data = {
        "model": "gpt-4",  # Specify the GPT model
        "prompt": prompt,
        "max_tokens": 150
    }

    response = requests.post(chatgpt_api_endpoint, json=data, headers=headers)
    print("ChatGPT response:", response.json())

# Main Program
try:
    print("Waiting for mail insertion...")
    # Wait for mail to be inserted, beam interruption (assuming high level indicates the signal)
    while GPIO.input(sensor_pin) == 0:
        time.sleep(0.1)  # Polling interval

    print("Mail detected!, Turning on the LED...")
    GPIO.output(led_pin, GPIO.HIGH)  # Turn on the LED
    time.sleep(1)  # Wait for 1 second

    print("Capturing image...")
    image_path = "C:\Users\Documents\IoT Project\smart-mailbox\images\mail_image.jpg"
    capture_image(image_path)

    print("Extracting text from image...")
    extracted_text = extract_text_from_image(image_path)

    print("Sending extracted text to ChatGPT for analysis...")
    send_text_to_chatgpt(extracted_text)

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    GPIO.output(led_pin, GPIO.LOW)  # Turn off the LED
    GPIO.cleanup()  # Clean up GPIO settings
