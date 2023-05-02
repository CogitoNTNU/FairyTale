import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# initialize tokenizer and model from pretrained GPT2 model
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2LMHeadModel.from_pretrained('gpt2')

import tkinter as tk
  
# Top level window
frame = tk.Tk()
frame.title("Fairytale!")
frame.geometry('700x400')

# Function for getting Input
# from textbox and printing it 
# at label widget
  
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("vicclab/FolkGPT")

model = AutoModelForCausalLM.from_pretrained("vicclab/FolkGPT")

def printAndRetrieveInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Your prompt: "+inp)
    prompt = inp
    inputs = tokenizer.encode(prompt, return_tensors = 'pt')

    # we pass a maximum output length of 200 tokens
    # outputs = model.generate(inputs, max_length= 200, do_sample=True, temperature=5)
    outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=0.7)

    fairytale = tokenizer.decode(outputs[0],skip_special_tokens=True)
        
    lbl.config(text=fairytale, wraplength = frame.winfo_width()-50, font=('Algerian',17,'bold'))         #wraplength gjør at den skriver tekst på ny linje etter lengden av teksten har nådd verdien til wraplength
    print(fairytale)
    # print(a2)
  
# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 8,
                   width = 25)
  
inputtxt.pack()

# frame.place(anchor='center', relx=0.5,rely=0.5)

# Button Creation
generateButton = tk.Button(frame,
                        text = "Generate", 
                        command = printAndRetrieveInput,)
generateButton.pack()
  
bg = tk.PhotoImage(file = r"FairyTale\src\book.png") 
# open-old-book-blank-texture-background-full-frame-vintage-fairy-tale-concept-78679471.jpg
label1 = tk.Label(frame, image = bg, width=700, height=600)
label1.place(relx=0,
             rely=0,
             anchor='ne')
label1.pack()

# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()


# print(prompt)
frame.mainloop()



