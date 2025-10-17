from datetime import datetime
import os

import cv2


def record_fpv(camera_index=0, output_file=None, fps=30):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    videos_dir = os.path.join(base_dir, "videos")
    os.makedirs(videos_dir, exist_ok=True)

    if output_file is None:
        output_file = os.path.join(
            videos_dir, f"fpv_capture_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.mp4"
        )

    cap = cv2.VideoCapture(camera_index)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    print(f"Recording {width}x{height} at {fps} FPS to {output_file}. Press 'q' to stop")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        cv2.imshow("FPV Recording", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    record_fpv()
