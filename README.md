# invisibility-cloak-computer-vision-learn
I'm currently in the process of learning computer vision, I'm documenting what I've learned using online resources and websites that teach these concepts.

This project creates an "invisible cloak" effect using a webcam feed by leveraging the OpenCV library. It works by capturing the background when there is no user in the frame, detecting a specific color range (such as blue), and replacing the detected color with the background, making it appear as if the object wearing the color has disappeared. 

## Libraries Used:
1. OpenCV (cv2) - 
- This is a tool that helps work with pictures and videos. It can:
     - Turn on your webcam to capture live video.
     - Change how colors look in an image (like switching from regular colors to something easier for computers to understand).
     - Create "masks," which are like filters to highlight certain parts of the picture.
     - Combine or separate parts of images to create cool effects.
2. NumPy (numpy) -
- This is like a calculator for working with big groups of numbers, like pixels in an image. It helps:
  - Organize image data into grids (arrays) that are easy to work with.
  - Find the middle value (median) of multiple pictures to create a clean background.
  - Adjust or combine masks (filters) for image effects.
3. time:
- This tool is super simple—it lets you add pauses in the program. For example: If you want to wait a bit before taking the next picture or frame, you can use this.

## Functions and Their Purpose:
1. create_background(cap, num_frames=30)
- Captures a series of frames from the webcam when the user moves out of the frame.
- Computes the median of these frames to create a static background image.
- Steps:
   - Reads num_frames frames from the webcam.
   - Stores the frames in a list.
   - Computes the median of these frames along the pixel axis using np.median.
   - Returns the median frame as the background.

2. create_mask(frame, lower_color, upper_color)
- Creates a mask to detect a specific color range (e.g., blue).
- Steps:
   - Converts the frame from BGR to HSV color space using cv2.cvtColor.
   - Creates a binary mask where pixels in the specified color range are white, and others are black (cv2.inRange).
   - Applies morphological transformations (cv2.MORPH_OPEN and cv2.MORPH_DILATE) to remove noise and improve mask quality.

3. apply_cloak_effect(frame, mask, background)
- Combines the frame, mask, and background to create the "invisible cloak" effect.
- Steps:
   - Inverts the mask using cv2.bitwise_not so the cloak area becomes black, and other areas remain white.
   - Extracts the non-cloak parts of the frame using cv2.bitwise_and with the inverted mask.
   - Extracts the cloak parts of the background using cv2.bitwise_and with the mask.
   - Combines the two images using cv2.add.
4. main()
- Coordinates the overall workflow.
- Steps:
   - Opens the webcam using cv2.VideoCapture.
   - Captures the background using create_background.
   - Detects a specific color (blue in this case) in each frame using create_mask.
   - Applies the cloak effect using apply_cloak_effect.
   - Displays the output using cv2.imshow.
   - Ends the loop and releases resources when the 'q' key is pressed.
## Example Workflow:
1. Background Capture: The program waits for the user to move out of the frame and captures multiple background images. These images are combined to create a clean, static background.
2. Color Detection: The user wears a blue cloak or holds an object of a specific color. The program identifies this color using an HSV mask.
3. Cloak Effect: The detected color (cloak) is replaced with the captured background, creating an illusion of invisibility.
4. Display: The processed frames are displayed in real-time.

## Applications:
This is a simplified implementation of augmented reality (AR) concepts. It demonstrates techniques used in object detection, background subtraction, and image blending. The techniques in this code have significant applications in filmmaking and videography, particularly for special effects and real-time editing. The use of OpenCV for color detection and masking underpins green screen technology, widely used to replace backgrounds in movies. This enables filmmakers to superimpose actors onto digitally created environments. The "invisible cloak" effect demonstrates object removal and invisibility, valuable for creating sci-fi or fantasy scenes. Real-time processing allows directors to preview effects during shooting, improving on-set decision-making. Background subtraction, achieved by capturing a static background, can isolate subjects for dynamic overlays or scene replacements. Additionally, color-based object detection can guide automated cinematography systems, adjusting lighting or camera focus based on detected elements. These tools not only enhance creative possibilities but also streamline production workflows, enabling seamless integration of visual effects and real-time pre-visualization in modern filmmaking.




