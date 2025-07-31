import cv2
import base64
from dotenv import load_dotenv
load_dotenv() 
from groq import Groq
client=Groq()
def capture_image() -> str:
    """
    Captures one frame from the default webcam, resizes it,
    encodes it as Base64 JPEG (raw string), saves it as 'sample.jpg',
    and returns the base64 string.
    """
    for idx in range(4):
        cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)  # Use DirectShow backend on Windows
        if cap.isOpened():
            for _ in range(10):  # Warm up the camera
                cap.read()

            ret, frame = cap.read()
            cap.release()

            if not ret or frame is None:
                continue

            # Save the image
            success = cv2.imwrite("sample.jpg", frame)
            if not success:
                raise RuntimeError("Failed to save image.")

            # Encode to JPEG and then base64
            ret, buf = cv2.imencode('.jpg', frame)
            if ret:
                return base64.b64encode(buf).decode('utf-8')

    raise RuntimeError("Could not open any webcam (tried indices 0-3)")

# capture_image()

# def analyze_img_with_query():

def analyze_image_with_query(query: str) -> str:
    """
    Captures an image and sends it along with the query to Groq's Vision model.
    Returns the response text.
    """
    if not query:
        return "Error: Query string is empty."

    try:
        img_b64 = capture_image()
    except Exception as e:
        return f"Error capturing image: {e}"

    if not img_b64:
        return "Error: Image capture failed."

    model = "meta-llama/llama-4-maverick-17b-128e-instruct"

    try:
        client = Groq()  # Ensure API key is set in env or passed directly
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img_b64}",
                        },
                    },
                ],
            }
        ]

        response = client.chat.completions.create(
            model=model,
            messages=messages
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Groq API error: {e}"


# # Example usage:
# query = "How many people are in this image?"
# print(analyze_image_with_query(query))
