# import necessary libraries
import cv2 # OpenCV library for capturing and processing video frames
import supervision as sv # Library for object detection
from ultralytics import YOLO # Library for loading and using the YOLO model
from ultralytics.yolo.utils.plotting import Annotator # Annotator class for labeling detected objects

def main():
    
    # Set resolution and capture video from default camera (index 0)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Load pre-trained YOLOv5 model
    model = YOLO("yolov8n.pt")

    # Loop through video frames
    while True:
        
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # Convert frame to RGB and make predictions using YOLO model
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model.predict(img)

        # Annotate detected objects with bounding boxes and labels
        for r in results:
            
            # Create annotator object for the current frame
            annotator = Annotator(frame)
            
            # Loop through detected objects in the current frame
            boxes = r.boxes
            for box in boxes:
                
                # Get box coordinates and class ID
                b = box.xyxy[0]
                c = box.cls
                
                # Label the detected object with its class name
                annotator.box_label(b, model.names[int(c)])
        
        # Get annotated frame and display it in a window
        frame = annotator.result()
        cv2.imshow("yolov8", frame)

        # Break the loop when the user presses the escape key
        if (cv2.waitKey(1) == 27):
            cv2.destroyAllWindows()
            break
            
    # Release the capture and close the window
    cap.release()
    cv2.destroyAllWindows()

# Run the main function if this script is being run as the main program
if __name__ == "__main__":
    main()
