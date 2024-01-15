# Program To Read video 
# and Extract Frames 

import cv2 

def capture_specific_frame(video_path, frame_number, output_file):
    # Open the video file
    vidObj = cv2.VideoCapture(video_path)

    # Set the position to the desired frame number
    vidObj.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the frame
    success, frame = vidObj.read()

    # Check if the frame is successfully read
    if success:
        # Save the frame as an image file
        # save the frame inside  the frames folder
        cv2.imwrite(output_file, frame)
        print(f"Frame {frame_number} captured and saved as {output_file}")
    else:
        print(f"Error capturing frame {frame_number}")

    # Release the video capture object
    vidObj.release()

def get_frame_count(video_path):
    # Open the video file
    vidObj = cv2.VideoCapture(video_path)

    # Get the number of frames
    frame_count = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))

    # Release the video capture object
    vidObj.release()

    return frame_count

def get_video_fps(video_path):
    # Open the video file
    vidObj = cv2.VideoCapture(video_path)

    # Get the frames per second (fps)
    fps = vidObj.get(cv2.CAP_PROP_FPS)

    # Release the video capture object
    vidObj.release()

    return fps


def detect_objects(frame_path, output_path):
    # Load the Haar Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the input frame
    frame = cv2.imread(frame_path)

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.11, minNeighbors=7, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Save the output frame with rectangles around detected faces
    cv2.imwrite(output_path, frame)
    print(f"Objects detected in {frame_path}. Results saved to {output_path}")

# Driver Code 
if __name__ == '__main__': 

    fps_of_video = get_video_fps("videoplayback.mp4")
    number_of_frames = get_frame_count("videoplayback.mp4")
    
    
    time = 60 # in seconds
    interval=fps_of_video * time

    frame_number = 0
    frames_gen_list = []
    while frame_number < number_of_frames:
        capture_specific_frame("videoplayback.mp4", frame_number, f"frame{frame_number}.jpg")
      
        frames_gen_list.append(f"frame{frame_number}.jpg")
        frame_number += interval

    for frame in frames_gen_list:
        frame_path = frame
        output_path = f"detected_objects{frame}"
        detect_objects(frame_path, output_path)