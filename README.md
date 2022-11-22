# Edith
Edith- A voice assistant
The Voice Assistant is programmed in python using speech recognition models. The application takes the input through voice and it gets converted into text using pyttsx3 model. The application has various functions to automate different activities and tasks in a desktop. The user can use this application to perform different tasks and get information just through his voice itself rather than typing and performing them. And the voice assistant interacts with the user through voice. Every time when a user runs the application, the main function is being called and it detects the keywords said by the user to run functions relevant to those keywords. 

The various tasks and automations we programmed in this application are as follows :

1. Sending an email.
2. Send whatsapp message
3. Date and time.
4. Searching anything on google.
5. Extracting information of any topic from wikipedia.
6. Playing youtube videos.
7. Fetching news on any topic.
8. Read out text from the clipboard.
9. Tells about covid cases.
10. Gives information about live weather.
11. Takes a screenshot and stores it in a folder.
12. Remember sentences and store them in a text file.
13. Generate a random strong password.
14. Flips a coin and rolls a dice.
15. Tell a joke.

The voice assistant application uses API’s and web automation tools to fetch the data from different websites and collects them in a json file or a list data type and after applying slicing and indexing, the proper output which is required by the user is automated with voice commands. For email, it uses smtp library through a port and sends a message after authenticating the account being used to send emails. 
The voice assistant catches the exceptions and performs smoothly without any trouble to the user. 

---------------------------------------------------------------------------------------------------------------------------------------------

we will use an HC-05 Bluetooth module and a smartphone to send voice commands to control LED and servo motors to receive voice commands. We have made an application which we will be using to send voice commands. The speech is received by a microphone and processed by the voice module using voice command. The voice command is given by using mobile to the Bluetooth which has certain features like controlling servo motor, LED on and off.
When we control the voice, speech recognition is a technology where the system understands the words given through speech. The main aim of this project is to control LED and servo motors through the human voice. In this system, we have used a voice recognition module to recognize the voice of the user for controlling the servo motor and LED turning on and off. The advancement of use in this project is to control home appliances by using voice commands. This project can also work as a home automation system. The command was set in the Arduino board. The home appliances can be controlled by two methods, by giving voice commands or by using mobile as a remote controller. Arduino is a simple integrated development environment that runs on any PC and allows users to write programs for Arduino in C or C++ language. The entire program is installed in an Arduino controller for any commands.
Components:

1.	Arduino Uno
2.	Bluetooth module (HC 05)
3.	Breadboard
4.	Servo motor 
5.	Resistor
6.	Jump wires
7.	LED
