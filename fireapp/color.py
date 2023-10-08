import cv2
import numpy as np

def calculate_red_percentage(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB (OpenCV loads images as BGR by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the lower and upper bounds for the red color in RGB format
    lower_red = np.array([150, 0, 0])
    upper_red = np.array([255, 100, 100])

    # Create a mask to identify red pixels
    mask = cv2.inRange(image_rgb, lower_red, upper_red)

    # Calculate the total number of pixels in the image
    total_pixels = mask.size

    # Calculate the number of red pixels
    red_pixels = cv2.countNonZero(mask)

    # Calculate the percentage of red color
    red_percentage = (red_pixels / total_pixels) * 100

    return red_percentage

if __name__ == "__main__":
    image_path = "static/images/mainscreen4.png"  # Replace with the path to your image
    red_percentage = calculate_red_percentage(image_path)
    print(f"Percentage of red color in the image: {red_percentage:.2f}%")
