import speech_recognition as sr
import multiprocessing

def callback(recognizer, audio, command_queue):
    try:
        command = recognizer.recognize_google(audio).lower()
        print("Google Speech Recognition thinks you said:", command)

        if command in ["next", "next page"]:
            print("Command recognized: Turning the page.")
            command_queue.put("next")  # Send signal to main.py

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

def start_listening(command_queue):
    r = sr.Recognizer()
    m = sr.Microphone()
    
    with m as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(m, lambda recognizer, audio: callback(recognizer, audio, command_queue))

    try:
        while True:
            pass  # Keep running
    except KeyboardInterrupt:
        print("Stopping listener...")
        stop_listening(wait_for_stop=True)

if __name__ == "__main__":
    command_queue = multiprocessing.Queue()
    start_listening(command_queue)