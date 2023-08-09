import json
import cv2
from deepface import DeepFace


def display_results(title, data):
    print(title + ":")
    sorted_data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    formatted_data = json.dumps(sorted_data, indent=4)
    print(formatted_data[2:-2])


def main():
    img_path = "img.jpg"
    img = cv2.imread(img_path)

    cv2.imshow("Image", img)
    cv2.waitKey(0)

    analysis = DeepFace.analyze(img, actions=("emotion", "age", "gender", "race"))
    analysis = analysis[0]

    print(f"Age: {analysis['age']}")
    display_results("Emotions", analysis['emotion'])
    display_results("Gender", analysis['gender'])
    display_results("Race", analysis['race'])


if __name__ == "__main__":
    main()
