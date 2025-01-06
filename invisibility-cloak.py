import cv2
import numpy as np
import time

def create_background(cap, num_frames=30):
    print("Capturing background. Please move out of frame.")
    backgrounds = []
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            backgrounds.append(frame)
        else:
            print(f"Warning: Could not read frame {i+1}/{num_frames}")
        time.sleep(0.1)
    if backgrounds:
        return np.median(backgrounds, axis=0).astype(np.uint8)
    else:
        raise ValueError("Could not capture any frames for background")

def create_mask(frame, lower_color1, upper_color1, lower_color2=None, upper_color2=None):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, lower_color1, upper_color1)
    
    # Handle the wrap-around case for red hues
    if lower_color2 is not None and upper_color2 is not None:
        mask2 = cv2.inRange(hsv, lower_color2, upper_color2)
        mask = cv2.bitwise_or(mask1, mask2)
    else:
        mask = mask1

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
    return mask

def apply_cloak_effect(frame, mask, background):
    mask_inv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)
    return cv2.add(fg, bg)

def main():
    print("OpenCV version:", cv2.__version__)

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        background = create_background(cap)
    except ValueError as e:
        print(f"Error: {e}")
        cap.release()
        return

    # Maroon color ranges in HSV
    lower_maroon1 = np.array([0, 100, 50])   # First part of red range
    upper_maroon1 = np.array([10, 255, 255])
    lower_maroon2 = np.array([170, 100, 50]) # Second part of red range
    upper_maroon2 = np.array([180, 255, 255])

    print("Starting main loop. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            time.sleep(1)
            continue

        mask = create_mask(frame, lower_maroon1, upper_maroon1, lower_maroon2, upper_maroon2)
        result = apply_cloak_effect(frame, mask, background)

        cv2.imshow('Invisible Cloak - Maroon', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
