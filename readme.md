# YOLO Webcam Object Detection

This is a Python program that uses YOLO (You Only Look Once), a real-time object detection algorithm, to detect and label objects in a webcam video stream. The program uses OpenCV for capturing the video stream and YOLO for object detection.

## Prerequisites

Before running this program, you will need to have the following installed:

- Python 3.6 or higher
- OpenCV (`pip install opencv-python`)
- Ultralytics YOLO (`pip install Ultralytics)

## Getting Started

To get started with this program, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies as listed in the `Prerequisites` section.
3. Navigate to the repository directory and run the `webcamcvrfm.py` file using the command `python webcamcvrfm.py`.

The program will start running and the webcam video stream will be displayed. Objects detected by the YOLO model will be highlighted with bounding boxes and labeled with their class names.

## Modifying the Program

You can modify the program to customize the object detection parameters and output format. For example, you can change the resolution of the video stream or adjust the confidence threshold for object detection. You can also modify the output format to save the annotated video stream as a file.

## License

YOLOv8 is available under two different licenses:

- **GPL-3.0 License**: See [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for details.
- **Enterprise License**: Provides greater flexibility for commercial product development without the open-source requirements of GPL-3.0. Typical use cases are embedding Ultralytics software and AI models in commercial products and applications. Request an Enterprise License at [Ultralytics Licensing](https://ultralytics.com/license).

## Acknowledgements

This program was created using the Ultralytics YOLO implementation and OpenCV library. Special thanks to the developers of these libraries for making this program possible.