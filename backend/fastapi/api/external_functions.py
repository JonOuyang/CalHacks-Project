from manim import *
import tempfile
import subprocess
import time

config.media_width = "100%"
config.verbosity = "WARNING"

prevManim = "This is your first code generation. There is currently no previous code to analyze"

def speak_to_user(text_to_speech):
    """
    Speak to user (verbal feedback), using text to speech via an API
    
    Args:
        text_to_speech: the text in the form of a string that will be spoken verbally to user
        
    Returns:
        0 on successful call
    """
    print('===== function speak_to_user called =====')
    print(f'Gemini: {text_to_speech}') #temporary
    return 0

def animate_with_manim(code):
    """
    Generate manim code
    
    Args:
        code: manim code passed as a string
    """
    global prevManim
    startTime = time.time()
    print('===== function animate_with_manim called =====')
    if "from manim import *" not in code:
        manimImport = "from manim import *"
        code = manimImport + code
    print(code) #temporary
    
    #with tempfile.NamedTemporaryFile(suffix=".py") as tmp:
    with open("manim_script.py", "w") as tmp:
        # Write the code to run the generated class to the temporary file
        tmp.write(code)
        tmp.flush()

        # Run the temporary file as a manim animation
        try:
            subprocess.run(["manim", tmp.name, "video", "-qh"])
        except subprocess.CalledProcessError as e:
            print(f"Error running Manim: {e}")
            
    endTime = time.time()
    print(f"Time taken to run Manim: {round((endTime - startTime), 2)} seconds")
    
    prevManim = code

def clear_chat():
    global prevManim
    code = """from manim import *
class video(Scene):
    def construct(self):
        line1 = Text("Hey, I'm Montgomery!").scale(1.2)
        self.play(Write(line1))
        self.play(line1.animate.shift(UP))
        line2 = Text("Start by asking me anything!").scale(0.5).next_to(line1, DOWN)
        self.play(Write(line2))
    """
    
    with open("manim_script.py", "w") as tmp:
        # Write the code to run the generated class to the temporary file
        tmp.write(code)
        tmp.flush()

        # Run the temporary file as a manim animation
        try:
            subprocess.run(["manim", tmp.name, "video", "-qh"])
        except subprocess.CalledProcessError as e:
            print(f"Error running Manim: {e}")
            
    prevManim = "This is your first code generation. There is currently no previous code to analyze"