**README.md**

# Accelerating Insights Projects which was assigned me for Internship

## Video Analysis with Object Detection

### Overview

This project facilitates the analysis of videos downloaded from YouTube by extracting frames at one-minute intervals and applying object detection to each frame. The primary objective is to provide a visual overview of the video content and identify objects or entities present in the frames.

### Program Overview

The provided Python script serves the following purposes:

1. **Frame Extraction:**
   - Reads a video file and extracts frames at one-minute intervals.
   - Saves each extracted frame as an image file in the 'frames' folder.

2. **Object Detection:**
   - Utilizes the Haar Cascade Classifier for face detection as an example.
   - Detects faces in each extracted frame and draws rectangles around them.
   - Saves the processed frames with rectangles around detected faces in the 'detected_objects' folder.

### Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/selfmanish01/Accelerating_Insights_Projects.git
   cd Accelerating_Insights_Projects
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:**
   - Ensure your video file is named "videoplayback.mp4" or modify the script accordingly.
   ```bash
   python video_analysis.py
   ```

4. **Explore Results:**
   - Extracted frames are saved in the 'frames' folder.
   - Processed frames with detected objects are saved in the 'detected_objects' folder.

### Customization

- **Object Detection Model:**
  - Users can customize the object detection model by replacing the Haar Cascade Classifier with their preferred model. Update the `detect_objects` function accordingly.

- **Video Input:**
  - If your video file has a different name, modify the `get_video_fps` and `get_frame_count` calls with the correct file name.

- **Output Paths:**
  - Users can customize the output paths for extracted frames and detected objects by modifying the paths in the script.

### Example Configuration

- The script is configured to extract frames at one-minute intervals and detect faces using the Haar Cascade Classifier.

### Contribution

- Contributions, feedback, and enhancements are welcome.
- Feel free to share your use cases, additional features, or improvements to the object detection pipeline.

### License

This project is licensed under the [MIT License](LICENSE). 
Feel free to use, modify, and distribute the code for your purposes.
Email- selfmanish01@gmail.com
