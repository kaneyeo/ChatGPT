from tkinter import*
import customtkinter
import openai
import os
import pickle

#Initate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x500')
root.iconbitmap('ai_lt.ico')#https://tkinter.com/images/ai_lt.ico

# Submit To ChatGPT
def speak():
	if chat_entry.get():
		# Define our filename
		filename = "api_key"
		try:
			if os.path.isfile(filename):
		   	 input_file = open(filename, 'rb')

		   	 # Load the data from file into a variable
		   	 stuff = pickle.load(input_file)


		   	 # Query ChatGPT
		   	 # Define our API Key to ChatGPT
		   	 #openai.ai_key = stuff
		   	 #openai.ai_key = os.getenv("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")
		   	 #openai.ai_key = os.getenv("OPENAI_API_KEY")
		   	 #openai.ai_key = "Bearer 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"
		   	 openai.ai_key = os.getenv("OPENAI_API_KEY")


		   	 # Create an instance
		   	 openai.Model.list()

		   	 # Define our Query or Response
		   	 response = openai.Completion.create(
		   	 	model="text-davinci-003",
		   	 	prompt=chat_entry.get(),
		   	 	temperature=0,
		   	 	max_tokens=60,
		   	 	top_p=1.0,
		   	 	frequency_penalty=0.6,
		   	 	presence_penalty=0.0,
		   	 	)
		   	 my_text.insert(END, response["choices"][0]["text"].strip())
		   	 my_text.insert(END, "\n\n")
		   	
			else:
		   	 # Create the file
		   	 input_file = open(filename, 'wb')
		   	 # Close the file
		   	 input_file.close()
		   	 # Error message
		   	 my_text.insert(END, "\n\nYou need AN API Key to Talk With ChatGPT. Click here:\nhttps://beta.openai.com/account/api-keys")

		except Exception as e:
			my_text.insert(END, f"\n\n There was error\n\n{e}")
	else:
	   my_text.insert(END, "\n\nHey! You Forgot to Type Something")



# Clear The Screen
def clear():
	# Clear The Main Text Box
	my_text.delete(1.0, END)
	# Clear The Query Entry Widget
	chat_entry.delete(0, END)

# Do API Stuff
def key():
	# Define our filename
	filename = "api_key"
	try:
		if os.path.isfile(filename):
	   	 input_file = open(filename, 'rb')

	   	 # Load the data from file into a variable
	   	 stuff = pickle.load(input_file)

	   	 # Output stuff to our entry box
	   	 api_entry.insert(END, stuff)
		else:
	   	 # Create the file
	   	 input_file = open(filename, 'wb')

	   	 # Close the file
	   	 input_file.close()

	except Exception as e:
		my_text.insert(END, f"\n\n There was error\n\n{e}")

	# Resize App Larger
	root.geometry('600x700')
	# Unhide API Frame
	api_frame.pack(pady=30)

# Save The API Key
def save_key():
	# Define our filename
	filename = "api_key"
	#  Open file
	out_file = open(filename, 'wb')
	# Actually add the data to the file
	pickle.dump(api_entry.get(), out_file)
	# Delete Entry Box
	api_entry.delete(0, END)
	# Hide API Frame
	api_frame.pack_forget()
	# Resize App Smaller
	root.geometry('600x600')

#Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)
# Add Text Widget To Get ChatGPT Responses
my_text = Text(text_frame,
	      bg="#343638", 
	      width=65,
	      bd=1, 
	      fg="#d6d6d6", 
	      relief="flat", 
	      wrap=WORD, 
	      selectbackground="#1f538d")

my_text.grid(row=0, column=0)

# Create Scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame,
	                                     command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")
# Add the scollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)


# Entry Widget To Type Texts to ChatGPT
chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Type Something To ChatGPT...",
	width=500,
	height=50,
	border_width=1)
chat_entry.pack(pady=10)

# Create Button Frame
button_frame = customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)

# Create Submit Button
submit_button = customtkinter.CTkButton(button_frame,
	text="Speak To ChatGPT",
	command=speak)
submit_button.grid(row=0, column=0, padx=25)

# Create Clear Button
clear_button = customtkinter.CTkButton(button_frame,
	text="Clear Responses",
	command=clear)
clear_button.grid(row=0, column=1, padx=25)

# Create API Key Button
api_key_button = customtkinter.CTkButton(button_frame,
	text="Update API Key",
	command=key)
api_key_button.grid(row=0, column=2, padx=25)

# Add API Key Frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=30)

# Add API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame,
	placeholder_text="Enter Your API key",
	width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

# Add API Save Button
api_save_button = customtkinter.CTkButton(api_frame,
	text="Save Key",
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)








root.mainloop()
