import torch


# initialize tokenizer and model from pretrained GPT2 model
from transformers import GPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# initialize tokenizer and model from finetuned model trained on a set of fairytales
# from transformers import AutoTokenizer, AutoModelForCausalLM
# tokenizer = AutoTokenizer.from_pretrained("vicclab/FolkGPT")
# model = AutoModelForCausalLM.from_pretrained("vicclab/FolkGPT")

# initialize tokenizer and model from bert-based-cased
# from transformers import AutoTokenizer, AutoModelForMaskedLM
# tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
# model = AutoModelForMaskedLM.from_pretrained("bert-base-cased")

# initialize tokenizer and model from norbert model
# from transformers import AutoTokenizer, AutoModelForMaskedLM
# tokenizer = AutoTokenizer.from_pretrained("ltg/norbert2")
# model = AutoModelForMaskedLM.from_pretrained("ltg/norbert2")

# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("pere/norwegian-gpt2")

# model = AutoModelForCausalLM.from_pretrained("pere/norwegian-gpt2")




# def findPunct(text):
#     for i in range(len(text)-1,0, -1):
#         print(i)
#         if (text[i] == '.'):
#             text[:i-1]
#             text += str('..')
#             return text






import tkinter as tk
from PIL import Image, ImageTk

# Top level window
frame = tk.Tk()
frame.title("Fairytale!")
frame.geometry('960x540')


# Set background color
frame.configure(bg="#8da683")





def printAndRetrieveInput():
    inp = inputtxt.get(1.0, "end-1c")
    # lbl.config(text = "Your prompt: "+inp, bg='#bedab1')
    prompt = inp
    inputs = tokenizer.encode(prompt, return_tensors = 'pt')

    # we pass a maximum output length of 200 tokens
    # outputs = model.generate(inputs, max_length= 200, do_sample=True, temperature=5)
    outputs = model.generate(inputs, max_length=100, do_sample=True, temperature=0.7)

    fairytale = tokenizer.decode(outputs[0],skip_special_tokens=True)

    lbl = tk.Label(frame, text = fairytale, wraplength=frame.winfo_width()-50,  bg='#bedab1', font=('Calibri',12))
   
    lbl.pack(side='top',pady=10)
 




# TextBox Creation
inputtxt = tk.Text(frame,
                   height = 8,
                   width = 24, bg='#bedab1',font=('Calibri',12) )
  

inputtxt.pack(side='top', pady=10)


# Button Creation
generateButton = tk.Button(frame,
                        text = "Generate", 
                        command = printAndRetrieveInput,)

generateButton.pack(side='top',pady=10)
  

frame.mainloop()


