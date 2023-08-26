# Pothole Detection

The "Pothole Detection Project" aims to automatically detect and highlight potholes in images using computer vision and deep learning techniques. This project is an example of analyzing road surface images and identifying potholes, which can be useful for road maintenance and repair.

## Project Features

- Automatic detection and highlighting of potholes in images.
- Support for processing multiple images at once for batch analysis.
- Integration with YOLO (You Only Look Once) object detection model for accurate results.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required dependency `ultralytics`.
3. Download [weights](https://www.dropbox.com/s/5csa554niatn9ty/weights.zip?dl=1) and place `.pt` file in the `weights` directory

## Usage

1. Place the images you want to analyze in the `data` directory.
2. Run the pothole detection script using `python predict.py`.
3. Detected potholes will be outlined in the processed images saved in the `runs/detect/predict` directory.

## More Techniques

For more information about YOLO features visit [documentation](https://docs.ultralytics.com/modes/predict/).