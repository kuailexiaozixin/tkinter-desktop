import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os

class ImageProcessorApp:
    def __init__(self, root):
        """
        Initializes the application's main window and user interface.
        'root' is the main window object from tkinter.
        """
        self.root = root
        self.root.title("Dagham.com - Bulk Image Processor")
        self.root.geometry("600x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#1c1c1c')

        try:
            icon_image = tk.PhotoImage(file='icon.png')
            self.root.iconphoto(False, icon_image)
        except tk.TclError:
            print("icon.png not found. Make sure it's in the same folder as the script.")

        # --- Style Configuration (Dark Theme with Red Accent) ---
        self.accent_color = '#ff1222'
        self.bg_color = '#1c1c1c'
        self.fg_color = '#ffffff'
        self.entry_bg_color = '#2a2a2a'
        self.button_fg_color = '#ffffff'

        style = ttk.Style()
        style.theme_use('clam')

        style.configure('TFrame', background=self.bg_color)
        style.configure('TLabel', background=self.bg_color, foreground=self.fg_color, font=('Helvetica', 11))
        style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'))
        style.configure('TCheckbutton', background=self.bg_color, foreground=self.fg_color, font=('Helvetica', 11))
        style.map('TCheckbutton', foreground=[('active', self.accent_color)])
        style.configure('TRadiobutton', background=self.bg_color, foreground=self.fg_color, font=('Helvetica', 11))
        style.configure('TButton', font=('Helvetica', 11, 'bold'), padding=10, background=self.accent_color, foreground=self.button_fg_color)
        style.map('TButton', background=[('active', '#cc0e1b')])
        style.configure('TEntry', fieldbackground=self.entry_bg_color, foreground=self.fg_color, insertcolor=self.fg_color, font=('Helvetica', 11))
        style.configure('TMenubutton', background=self.entry_bg_color, foreground=self.fg_color, font=('Helvetica', 11), padding=5)
        style.configure('Horizontal.TScale', background=self.bg_color, troughcolor=self.entry_bg_color)
        style.map('Horizontal.TScale', background=[('active', self.accent_color)])
        style.configure('red.Horizontal.TProgressbar', troughcolor=self.entry_bg_color, background=self.accent_color)

        # --- Main Frame ---
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Folder Selection Section ---
        ttk.Label(main_frame, text="1. Select Folders", style='Header.TLabel').grid(row=0, column=0, columnspan=3, sticky='w', pady=(0, 10))
        self.input_folder = tk.StringVar()
        self.output_folder = tk.StringVar()
        ttk.Button(main_frame, text="Select Input Folder", command=self.select_input_folder).grid(row=1, column=0, sticky='ew', padx=(0, 5))
        ttk.Entry(main_frame, textvariable=self.input_folder, state='readonly').grid(row=1, column=1, columnspan=2, sticky='ew')
        ttk.Button(main_frame, text="Select Output Folder", command=self.select_output_folder).grid(row=2, column=0, sticky='ew', padx=(0, 5), pady=5)
        ttk.Entry(main_frame, textvariable=self.output_folder, state='readonly').grid(row=2, column=1, columnspan=2, sticky='ew')

        # --- Processing Options Section ---
        ttk.Label(main_frame, text="2. Choose Processing Options", style='Header.TLabel').grid(row=3, column=0, columnspan=3, sticky='w', pady=(20, 10))

        # Resizing Options
        self.resize_var = tk.BooleanVar()
        ttk.Checkbutton(main_frame, text="Resize Images", variable=self.resize_var).grid(row=4, column=0, sticky='w')
        self.resize_width = tk.StringVar(value="1920")
        self.resize_height = tk.StringVar(value="1080")
        ttk.Label(main_frame, text="Width:").grid(row=5, column=0, sticky='e', padx=5)
        ttk.Entry(main_frame, textvariable=self.resize_width, width=8).grid(row=5, column=1, sticky='w')
        ttk.Label(main_frame, text="Height:").grid(row=5, column=1, sticky='e', padx=5)
        ttk.Entry(main_frame, textvariable=self.resize_height, width=8).grid(row=5, column=2, sticky='w')

        # Watermark Options
        self.watermark_var = tk.BooleanVar()
        ttk.Checkbutton(main_frame, text="Add Watermark", variable=self.watermark_var).grid(row=6, column=0, sticky='w', pady=(10, 0))
        self.watermark_text = tk.StringVar(value="© Dagham.com")
        ttk.Label(main_frame, text="Text:").grid(row=7, column=0, sticky='e', padx=5)
        ttk.Entry(main_frame, textvariable=self.watermark_text).grid(row=7, column=1, columnspan=2, sticky='ew')

        # Format Conversion Options
        self.convert_var = tk.BooleanVar()
        ttk.Checkbutton(main_frame, text="Convert Format", variable=self.convert_var).grid(row=8, column=0, sticky='w', pady=(10, 0))
        self.convert_format = tk.StringVar(value="JPEG")
        formats = ["JPEG", "PNG", "WEBP", "GIF", "BMP"]
        format_menu = ttk.OptionMenu(main_frame, self.convert_format, formats[0], *formats, style='TMenubutton')
        format_menu.grid(row=9, column=1, columnspan=2, sticky='w')

        # --- NEW: Compression Options (Universal) ---
        self.compress_var = tk.BooleanVar()
        # Changed the label text
        ttk.Checkbutton(main_frame, text="Compress Images", variable=self.compress_var).grid(row=10, column=0, sticky='w', pady=(10, 0))
        
        # Set default to 100 (best quality)
        self.compress_quality = tk.IntVar(value=100)
        
        # Create a frame to hold the slider and the new label
        quality_frame = ttk.Frame(main_frame)
        quality_frame.grid(row=11, column=1, columnspan=2, sticky='ew')
        
        # The slider, now linked to the update_quality_label function
        quality_slider = ttk.Scale(quality_frame, from_=1, to=100, orient=tk.HORIZONTAL, variable=self.compress_quality, command=self.update_quality_label)
        quality_slider.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # The new label that shows the percentage
        self.quality_label = ttk.Label(quality_frame, text="100%", width=5)
        self.quality_label.pack(side=tk.LEFT, padx=(10, 0))

        ttk.Label(main_frame, text="Quality:").grid(row=11, column=0, sticky='e', padx=5)

        # --- Process Button ---
        ttk.Button(main_frame, text="Start Processing", command=self.process_images).grid(row=12, column=0, columnspan=3, sticky='ew', pady=(30, 10))

        # --- Progress Bar & Status ---
        self.progress = ttk.Progressbar(main_frame, orient=tk.HORIZONTAL, length=100, mode='determinate', style='red.Horizontal.TProgressbar')
        self.progress.grid(row=13, column=0, columnspan=3, sticky='ew')
        self.status_label = ttk.Label(main_frame, text="Ready. Select folders and options.")
        self.status_label.grid(row=14, column=0, columnspan=3, sticky='w', pady=(10,0))
        
        main_frame.grid_columnconfigure(1, weight=1)

    def update_quality_label(self, value):
        """NEW: This function is called every time the slider moves."""
        # Updates the text label to show the current quality value.
        # The value from the slider is a float, so we convert it to an integer.
        self.quality_label.config(text=f"{int(float(value))}%")

    def select_input_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path: self.input_folder.set(folder_path)

    def select_output_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path: self.output_folder.set(folder_path)

    def process_images(self):
        in_path = self.input_folder.get()
        out_path = self.output_folder.get()

        if not in_path or not out_path:
            messagebox.showerror("Error", "Please select both input and output folders.")
            return
        if in_path == out_path:
            messagebox.showerror("Error", "Input and output folders cannot be the same.")
            return

        try:
            files = [f for f in os.listdir(in_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))]
            if not files:
                messagebox.showinfo("Information", "No image files found in the input folder.")
                return
        except Exception as e:
            messagebox.showerror("Error", f"Could not read input folder: {e}")
            return

        self.progress['maximum'] = len(files)
        for i, filename in enumerate(files):
            try:
                self.status_label.config(text=f"Processing {i+1}/{len(files)}: {filename}")
                self.root.update_idletasks()

                file_path = os.path.join(in_path, filename)
                img = Image.open(file_path).convert("RGBA")

                if self.resize_var.get():
                    try:
                        width = int(self.resize_width.get())
                        height = int(self.resize_height.get())
                        img = img.resize((width, height), Image.Resampling.LANCZOS)
                    except ValueError:
                        messagebox.showerror("Error", "Invalid width or height for resizing.")
                        return

                if self.watermark_var.get():
                    draw = ImageDraw.Draw(img)
                    text = self.watermark_text.get()
                    try:
                        font_size = int(img.size[1] * 0.05)
                        font = ImageFont.truetype("arial.ttf", font_size)
                    except IOError:
                        font_size = 15
                        font = ImageFont.load_default()
                    text_bbox = draw.textbbox((0, 0), text, font=font)
                    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
                    x, y = img.size[0] - text_width - 15, img.size[1] - text_height - 15
                    draw.rectangle((x-5, y-5, x + text_width + 10, y + text_height + 10), fill=(0,0,0,128))
                    draw.text((x, y), text, font=font, fill=(255, 255, 255, 220))

                output_filename = os.path.splitext(filename)[0]
                save_format = self.convert_format.get() if self.convert_var.get() else img.format or 'PNG'
                
                if save_format.upper() == 'JPEG' and img.mode == 'RGBA':
                    img = img.convert('RGB')

                output_filepath = os.path.join(out_path, f"{output_filename}.{save_format.lower()}")
                
                # --- Universal Compression Logic ---
                save_options = {}
                if self.compress_var.get():
                    quality_val = self.compress_quality.get()
                    # Apply quality setting for lossy formats
                    if save_format.upper() in ['JPEG', 'WEBP']:
                        save_options['quality'] = quality_val
                    # Apply compress_level setting for lossless PNG
                    elif save_format.upper() == 'PNG':
                        # We map the 1-100 quality slider to PNG's 9-0 compress_level.
                        # 100 quality -> level 0 (fastest, least compression)
                        # 1 quality -> level 9 (slowest, most compression)
                        save_options['compress_level'] = round(9 - (quality_val - 1) * 9 / 99)
                
                img.save(output_filepath, **save_options)
                self.progress['value'] = i + 1

            except Exception as e:
                messagebox.showwarning("Processing Error", f"Could not process file: {filename}\nError: {e}")
                continue

        self.status_label.config(text="Processing complete!")
        messagebox.showinfo("Success", f"Successfully processed {len(files)} images.")
        self.progress['value'] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
