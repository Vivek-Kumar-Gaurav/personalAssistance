# Voice Assistant (Jarvis)

## Overview
Jarvis is a simple voice assistant built using Python. It uses **speech recognition**, **text-to-speech synthesis**, and various APIs to perform tasks such as searching Wikipedia, opening websites, telling the time, and sending emails.

## Features
- Greets the user based on the time of day.
- Recognizes voice commands and executes tasks.
- Searches Wikipedia and reads results aloud.
- Opens popular websites like Google, YouTube, and Instagram.
- Tells the current time.
- Sends emails using SMTP.
- Supports an exit command to stop execution.

## Technologies Used
- **Python** (Programming language)
- **pyttsx3** (Text-to-Speech conversion)
- **SpeechRecognition** (Speech input processing)
- **Wikipedia API** (Fetching data from Wikipedia)
- **smtplib** (Sending emails)
- **webbrowser** (Opening websites)
- **datetime** (Handling time-based functions)

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Install Required Libraries
Run the following command to install dependencies:
```bash
pip install pyttsx3 SpeechRecognition wikipedia smtplib
```

## How to Run
1. Clone the repository or download the script.
2. Run the script using:
   ```bash
   python jarvis.py
   ```
3. Speak commands when prompted.

## Usage
### Voice Commands
You can give commands such as:
- "Search Wikipedia for Python programming"
- "Open YouTube"
- "What is the time?"
- "Email to [recipient name]"
- "Exit" (to stop the assistant)

## Exit Command
To stop the assistant, say **"exit"**, **"quit"**, or **"stop"**.

## Future Improvements
- Add weather updates using an API.
- Improve voice recognition accuracy.
- Enhance email security using OAuth authentication.

## License
This project is open-source. Feel free to modify and enhance it!

