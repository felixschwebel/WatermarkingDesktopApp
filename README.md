# WatermarkingDesktopApp
A project to review the Tkinter module and create an application for **watermarking pictures with Pillow in Python**. 

The user can upload an image, type some text that should be displayed as a watermark and choose the **position, font, color, and size of the text**. 

<img width="952" alt="final_UI" src="https://user-images.githubusercontent.com/111788725/212690712-0b0fec77-831e-4b3e-95d3-3d6ce5637f1f.png">

Before displaying the new image, it’s **resized to fit the window**. 

<img width="892" alt="Screenshot 2023-01-16 at 14 35 45" src="https://user-images.githubusercontent.com/111788725/212690789-cf888c3c-2216-4e39-a083-190d54b0960e.png">

When the Preview Button is pressed, and a picture was uploaded the program gets hold of the text and position. The position is then *“translated”* into coordinates on the resized picture. In the last step the size, color and font are saved and used to change the ``text_containter`` - Canvas object. 

<img width="880" alt="Screenshot 2023-01-16 at 14 36 18" src="https://user-images.githubusercontent.com/111788725/212690866-89a81977-b804-4c1a-a47c-cd1935c64b76.png">

If no picture was uploaded the user will be asked to upload one. 

<img width="886" alt="Screenshot 2023-01-16 at 14 36 34" src="https://user-images.githubusercontent.com/111788725/212690926-d9b1f330-d048-47af-8ae9-3d8883256841.png">


When the user wants to download the picture, the final watermark with the original size coordinates is created and drawn with the **Pillow’s ImageDraw**. Finally, the new filename gets the ``watermarked_``-prefix and the user is asked to provide a location. 

<img width="958" alt="Screenshot 2023-01-16 at 14 37 00" src="https://user-images.githubusercontent.com/111788725/212690997-5cf4136c-b426-4053-b035-95babfe44fcf.png">

