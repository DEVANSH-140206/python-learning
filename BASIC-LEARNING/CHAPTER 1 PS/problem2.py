import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Text you want the engine to say
text = "meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow meow."

# Have the engine say the text
engine.say(text)

# Run the speech process and wait for it to complete
engine.runAndWait()

# Optional: Stop the engine
engine.stop()
