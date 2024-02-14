import cv2

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def get_frame(self):
        # Your frame capture logic here
        success, frame = self.video.read()
        if not success:
            return None

        # Convert the frame to JPEG format
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        return frame_bytes
