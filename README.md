# Amazon Rekognition Object Detection

Hey there! 👋 Welcome to my Amazon Rekognition Object Detection project!

## What's this all about?

I created this project to learn how to use Amazon Rekognition, a super cool service that can detect objects in images and videos. It's like magic, but with code! 🪄✨

## What does it do?

This Python script does some pretty awesome stuff:
1. It takes a video file as input.
2. It goes through the video, frame by frame.
3. For each frame, it uses Amazon Rekognition to detect objects.
4. It saves the detected objects' information and the video frames.

## Why did I make this?

I'm really excited about computer vision and wanted to learn how to use Amazon Rekognition. This project helped me understand how to:
- Work with video files in Python
- Use Amazon Rekognition for object detection
- Save detection results in a format that can be used for other cool projects

## How to use it?

1. Make sure you have Python installed on your computer.
2. Install the required packages:
   ```
   pip install boto3 opencv-python python-dotenv
   ```
   OR
   ```
   pip install -r requirements.txt
   ```
4. Set up your Amazon credentials in a `.env` file:
   ```
   AWS_ACCESS_KEY_ID="your_access_key"
   AWS_SECRET_ACCESS_KEY="your_secret_key"
   ```
5. Run the script:
   ```
   python amazon-rekognition.py
   ```

## What can you detect?

Amazon Rekognition can detect a whole bunch of things! Check out the [complete list of labels](https://docs.aws.amazon.com/rekognition/latest/dg/labels.html) to see all the possibilities.

## Shout out!

A big thank you to Felipe Tambasco and his YouTube channel [Computer Vision Engineer](https://www.youtube.com/@ComputerVisionEngineer) for the awesome tutorial that helped me create this project!

## Let's connect!

If you're as excited about computer vision as I am, let's chat! Feel free to open an issue or reach out to me on LinkedIn.

Happy coding! 🚀💻
