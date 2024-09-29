"""
Created on Sat Sep 29,2024
@author: Pramith

"""

import time
import keyboard
import random

# Global Variables
Start_time = None
End_time = None
Stop_timer = False
Char_counter = 0
Word_counter = 0
random_sentences = [
    "Blockchain technology is revolutionizing data security by providing decentralized systems that enhance transparency and prevent fraud.",
    "The increasing reliance on cloud services has made cloud security a top priority, necessitating robust identity and access management practices.",
    "artificial intelligence is transforming the world.",
    "typing speed is measured in words per minute.",
    "Machine learning algorithms are being used to detect anomalies in network traffic, helping security teams respond to threats in real-time.",
    "Ethical hacking plays a crucial role in cybersecurity by identifying weaknesses in systems before malicious hackers can exploit them.",
    "data science and machine learning are in high demand."
]
ignore_keys = [
    'capslock', 'enter',
]


# Live Tracking Mode
def live_tracking_mode():
    global Start_time, End_time, Char_counter, Word_counter, Stop_timer

    # Open a log file to record keypresses (in append mode)
    file_path = "Live_Keyboard_Log.txt"
    with open(file_path, "a") as log_file:
        print("Start Typing....   (Press ESC to stop)")
        Start_time = time.time()

        while not Stop_timer:
            event = keyboard.read_event()

            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'esc':
                    Stop_timer = True
                
                elif event.name in ignore_keys:
                    pass

                elif event.name == 'space':  # Count spaces as words
                    Word_counter += 1
                    Char_counter += 1
                
                elif len(event.name) == 1:  # Count regular characters
                    Char_counter += 1

        End_time = time.time()
        elapsed_time = (End_time - Start_time) / 60  # in minutes

        WPM = (Char_counter / 5) / elapsed_time if elapsed_time > 0 else 0

        print(f"\nTime Taken: {elapsed_time:.2f} minutes")
        print(f"Characters Typed: {Char_counter}")
        print(f"Words Typed: {Word_counter}")
        print(f"WPM: {WPM:.2f}")

        log_file.write(f"----------------\n")    
        log_file.write(f"Live Tracking Mode WPM: {WPM:.2f}\n")
        log_file.write(f"----------------\n\n")


# Random Sentences Mode
def random_sentences_mode():
    global Start_time, End_time, Char_counter, Word_counter, Stop_timer

    # Open a log file to record keypresses (in append mode)
    file_path = "Random_Sentence_Keyboard_Log.txt"
    with open(file_path, "a") as log_file:
        # Select a random sentence
        sentence = random.choice(random_sentences)
        print(f"Type the following sentence:\n\"{sentence}\"\n")
        
        input_sentence = ''
        actual_keyboard_input = ''
        input_length = 0
        Start_time = time.time()
        
        while not Stop_timer and input_length < len(sentence):
            event = keyboard.read_event()

            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'esc':
                    Stop_timer = True

                elif event.name in ignore_keys:
                    pass

                elif event.name == 'backspace' and input_length > 0:
                    actual_keyboard_input += ' '
                    actual_keyboard_input += '\''
                    actual_keyboard_input += event.name
                    actual_keyboard_input += '\''
                    actual_keyboard_input += ' '
                    input_sentence = input_sentence[:-1]
                    input_length -= 1
                    Char_counter -= 1

                elif len(event.name) == 1:  # Regular characters
                    actual_keyboard_input += event.name
                    input_sentence += event.name
                    Char_counter += 1
                    input_length += 1

                elif event.name == 'space':  # Space
                    actual_keyboard_input += ' '
                    actual_keyboard_input += '\''
                    actual_keyboard_input += event.name
                    actual_keyboard_input += '\''
                    actual_keyboard_input += ' '
                    input_sentence += ' '
                    Char_counter += 1
                    input_length += 1

        End_time = time.time()

        # Calculate time elapsed in minutes
        elapsed_time = (End_time - Start_time) / 60  # in minutes
        WPM = (Char_counter / 5) / elapsed_time if elapsed_time > 0 else 0

        # Calculate accuracy
        correct_chars = sum(1 for i in range(min(len(input_sentence), len(sentence))) if input_sentence[i] == sentence[i])
        accuracy = (correct_chars / len(sentence)) * 100

        print(f"Sentence Typed: {input_sentence}")
        print(f"Actual Keyboard Input: {actual_keyboard_input}")
        print(f"\nTime Taken: {elapsed_time:.2f} minutes")
        print(f"WPM: {WPM:.2f}")
        print(f"Accuracy: {accuracy:.2f}%")

        log_file.write(f"----------------\n")
        log_file.write(f"Random Sentence Mode\n")
        log_file.write(f"Sentence Typed:        {input_sentence}\n")
        log_file.write(f"Actual Keyboard Input: {actual_keyboard_input}\n")
        log_file.write(f"WPM:                   {WPM:.2f}\n")
        log_file.write(f"Accuracy:              {accuracy:.2f}%\n")
        log_file.write(f"----------------\n\n")


# Main function
def main():
    print("Choose Mode:")
    print("1. Live Tracking Mode")
    print("2. Random Sentences Mode")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        live_tracking_mode()
    elif choice == '2':
        random_sentences_mode()
    else:
        print("Invalid choice. Exiting...")


if __name__ == "__main__":
    main()
