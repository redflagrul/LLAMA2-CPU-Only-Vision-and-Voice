import cv2
from transformers import pipeline
from playht_voice_cpu import get_voice_response

# Initialize LLAMA2 using transformers on CPU
llama_model = pipeline("text-generation", model="openai/gpt-3", device="cpu")

def get_llama_response(prompt):
    response = llama_model(prompt, max_length=50, do_sample=True)
    return response[0]["generated_text"]

cap = cv2.VideoCapture(0)  # Open the webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the webcam feed
    cv2.imshow("Webcam", frame)

    # Dummy text prompt (replace with actual vision task if you add it later)
    detected_text = "Describe what I see"

    # Get response from LLAMA2
    llama_response = get_llama_response(detected_text)
    print("LLAMA2 Response:", llama_response)

    # Convert the response to speech with PlayHT
    get_voice_response(llama_response)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
