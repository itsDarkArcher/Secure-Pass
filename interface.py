import tkinter
import customtkinter  #import the CustomTkinter module

root_tk = tkinter.Tk()  # create the Tk window like you normally do
root_tk.geometry("700x450")
root_tk.title("Cipher")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, corner_radius=10)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

customtkinter.set_appearance_mode("Dark") # Other: "Light", "System" (only macOS)

