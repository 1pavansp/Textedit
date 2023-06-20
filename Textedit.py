import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")

        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_application)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=False)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        menubar.add_cascade(label="Edit", menu=edit_menu)

    def new_file(self):
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
            except IOError:
                messagebox.showerror("Error", "Failed to open file.")

    def save_file(self):
        content = self.text_area.get("1.0", tk.END)
        if content:
            file_path = filedialog.asksaveasfilename(title="Save File", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if file_path:
                try:
                    with open(file_path, "w") as file:
                        file.write(content)
                except IOError:
                    messagebox.showerror("Error", "Failed to save file.")
        else:
            messagebox.showwarning("Warning", "No content to save.")

    def save_file_as(self):
        content = self.text_area.get("1.0", tk.END)
        if content:
            file_path = filedialog.asksaveasfilename(title="Save File As", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if file_path:
                try:
                    with open(file_path, "w") as file:
                        file.write(content)
                except IOError:
                    messagebox.showerror("Error", "Failed to save file.")
        else:
            messagebox.showwarning("Warning", "No content to save.")

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def exit_application(self):
        self.root.quit()

# Create the Tkinter application window
root = tk.Tk()

# Create the text editor
editor = TextEditor(root)

# Run the Tkinter event loop
root.mainloop()
