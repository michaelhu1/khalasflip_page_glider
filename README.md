# Khalas Flip Page Glider
The Page Glider is an automatic reader designed to assist the disabled, older readers, and institutions that seek to enhance accessibility. It provides a hands-free reading experience that benefits users with mobility impairments, dexterity limitations, arthritis, and neurological disorders such as Parkinson's. As the market for assistive technology is worth $25 billion in 2020 and increasing by 7.5% annually through 2026, there is a clear requirement for solutions offering independent reading capabilities. Additionally, 65% of Americans read books more than digital counterparts, further validating the need for an accessible page turner. While existing products like the PageFlip Firefly and Viking Easy Turn are addressing some of the needs for accessibility, they are not affordable or fully automated. The Page Glider is going to bridge this gap with its cost-effectively priced, flexible, and user-friendly innovation that enhances the reading experience for different users.

## Features

- Voice-activated page turning ("next", "turn two", etc.)
- Physical button trigger for manual page turns
- Adjustable for different book types/sizes
- Speech recognition with CMU Sphinx (offline)
- Affordable and accessible design

---


## Hardware Requirements

- Raspberry Pi (any model with GPIO support)
- 2x Servo motors (for flipping and wheel turning)
- 1x Physical push button
- Jumper wires and breadboard
- USB Microphone (set to device_index=2 in `recognition.py`)
- Power supply for servos
---
## Installation

1. Check Python version is 3.9+
2. Generate a new virtual environment using `python -m venv env`
3. Activate virtual environment using `source env/bin/activate`
4. Install SpeechRecognition using `pip install SpeechRecognition`
5. Install PyAudio using `pip install PyAudio`
6. Install CMUSphinx using `pip3 install pocketsphinx`
7. Install word2number using `pip install word2number`
8. Clone the repository using `git clone https://github.com/michaelhu1/khalasflip_page_glider`
---
## Usage

1. Make sure your Raspberry Pi is powered and connected to the servo motors.
2. Run the main script:
   python main.py

 Say voice commands like:
 - "next" to turn one page
 - "turn three" to turn three pages
 - "stop" to stop the system
   
---
## Troubleshooting

- **Microphone not detected**: Make sure your USB mic is connected and check `device_index` in `recognition.py`.
- **Speech not recognized**: Ensure background noise is minimized and you wait for the "listening..." prompt.
- **Servos not moving**: Check power supply and GPIO pin numbers in `main.py` and `servo.py`.


