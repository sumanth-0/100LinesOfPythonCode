
# Body Pose Estimator

import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def estimate_pose(image):
    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_image)

    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            height, width, _ = image.shape
            cx, cy = int(landmark.x * width), int(landmark.y * height)
            cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1)

    return image

def main():
    cap = cv2.VideoCapture(0)  # Use webcam for real-time video

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = estimate_pose(frame)
        cv2.imshow("Body Pose Estimator", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
