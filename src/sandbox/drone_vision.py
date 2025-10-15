import cv2
from ultralytics import YOLO

CAM_INDEX = 0
MODEL = "yolov8n.pt"
CONFIDENCE_THRESHOLD = 0.25
ONLY_PERSON = False


def main():
    cap = cv2.VideoCapture(CAM_INDEX)
    if not cap.isOpened():
        print(f"Could not open camera {CAM_INDEX}")
        return

    model = YOLO(MODEL)
    names = model.model.names

    print("Camera opened. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        res = model.predict(frame, imgsz=640, conf=CONFIDENCE_THRESHOLD, verbose=False)[0]
        if res.boxes is not None:
            for box in res.boxes:
                class_id = int(box.cls[0]) if box.cls is not None else -1
                if ONLY_PERSON and names.get(class_id, "") != "person":
                    continue
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0]) if box.conf is not None else 0.0
                label = f"{names.get(class_id, str(class_id))} {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    label,
                    (x1, max(15, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )
        cv2.imshow("FPV Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
