import speech_recognition as sr
import multiprocessing
from time import sleep
from word2number import w2n

def convert_second_word_to_number(text):
    first, second = text.split()
    number = w2n.word_to_num(second)
    return f"{first} {number}"

def callback(recognizer, audio, command_queue):
    try:
        print("listening...")
        command = recognizer.recognize_sphinx(audio).lower()
        print("Sphinx Recognition thinks you said:", command)

        if "next" in command:
            print("Command recognized: Turning the page.")
            command_queue.put("next")  
        elif "stop" in command:
            print("Command recognized: Stopping the program.")
            command_queue.put("stop")
        if "turn" in command:
            secondnumber = convert_second_word_to_number(command)
            print(f"Command recognized: turning {secondnumber} pages")
            command_queue.put(secondnumber)


    except sr.UnknownValueError:
        print("Sphinx Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

def start_listening(command_queue):
    r = sr.Recognizer()
    r.energy_threshold = 6000
    m = sr.Microphone(device_index=2)
    
    with m as source:
        r.adjust_for_ambient_noise(source, duration = 5)

    stop_listening = r.listen_in_background(m, lambda recognizer, audio: callback(recognizer, audio, command_queue),phrase_time_limit = 3)

    try:
        while True:
            sleep(0.1)
            pass  # Keep running
    except KeyboardInterrupt:
        print("Stopping listener...")
        stop_listening(wait_for_stop=True)

if __name__ == "__main__":
    command_queue = multiprocessing.Queue()
    start_listening(command_queue)