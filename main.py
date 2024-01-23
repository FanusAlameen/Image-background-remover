from rembg import remove #rembg library is used to remove background from images.
import easygui #easygui is a python module that allows for simple and easy GUI programming.
from PIL import Image #Pillow abbreviated as 'PIL' is a fork of the 'Python Imaging Library'.
from io import BytesIO #BytesIO is a class in Python's 'io' module that provides an in-memory stream of bytes.

input_path = easygui.fileopenbox(title='Select an Image File', filetypes=["*.png", "*.jpeg", "*.jpg"]) #opens an easygui selectable file dialogue box.

if not input_path: #If no images are selected then an easygui message dialogue box pops up with the message below.
    easygui.msgbox('No image was selected. Exiting...')
else: #If an image is selected then a save file dialogue box pops up from easygui.
    save_output_path = easygui.filesavebox(title='Save image file at...', default='.png', filetypes=['*.png']) #The selected image's save path is extracted and stored in this variable.

    if save_output_path: #This condition gets executed if the user saves the selected image.
        input_image = Image.open(input_path)

        #Converts the Pillow Image to Bytes
        with BytesIO() as buffer:
            input_image.save(buffer, format='PNG')
            input_data = buffer.getvalue()
        
        #Removes bakground from the Selected Image
        output_data = remove(input_data)

        #Convertes output bytes to Pillow Image 
        background_removed_image = Image.open(BytesIO(output_data))

        #Saves the background removed image
        background_removed_image.save(save_output_path)
        easygui.msgbox(f"Background was removed successfully. Image saved to {save_output_path}")
    else:
        easygui.msgbox('No save path was selected. Exiting.')