import gradio as gr

if __name__ == '__main__':
    with gr.Blocks() as demo:
        gr.HTML(
            """
            <div align='center'> <img src='/file=./assets/gvlab_logo.png' style='height:70px'/> </div>
            <p align="center"><a href="https://github.com/OpenGVLab/InternGPT"><b>GitHub</b></a>&nbsp;&nbsp;&nbsp;&nbsp; 
            <a href="https://arxiv.org/pdf/2305.05662.pdf"><b>Report</b></a>&nbsp;&nbsp;&nbsp;
            <a href="https://github.com/OpenGVLab/InternGPT/assets/13723743/8fd9112f-57d9-4871-a369-4e1929aa2593"><b>Video Demo</b></a></p>
            """
        )
        
        gr.HTML(
        """
        <body>
        <div align='center'><p style="font-family:verdana;color:#000000";> <b> You can try our demo via <a href="https://igpt.opengvlab.com">https://igpt.opengvlab.com</a> </b> </p> </div>
        
        

        <div align='center'><p style="font-family:verdana;color:#000000";> <b>To run this app on Hugging Face, you may need to duplicate the repo into your own space. </b></p></div>
        </body>
        """)

        gr.Markdown(
            '''
            **User Manual:**

            After uploading the image, you can have a **multi-modal dialogue** by sending messages like: `"what is it in the image?"` or `"what is the background color of the image?"`.
            
            You also can interactively operate, edit or generate the image as follows:
            - You can click the image and press the button **`Pick`** to **visualize the segmented region** or press the button **`OCR`** to **recognize the words** at chosen position;
            - To **remove the masked region** in the image, you can send the message like: `"remove the masked region"`;
            - To **replace the masked region** in the image, you can send the message like: `"replace the masked region with {your prompt}"`;
            - To **generate a new image**, you can send the message like: `"generate a new image based on its segmentation describing {your prompt}"`.
            - To **create a new image by your scribble**, you should press button **`Whiteboard`** and draw in the board. After drawing, you need to press the button **`Save`** and send the message like: `"generate a new image based on this scribble describing {your prompt}"`.
            '''
        )
        gr.HTML(
            """
            <body>
            <p style="font-family:verdana;color:#11AA00";>More features are coming soon. Hope you have fun with our demo!</p>
            </body>
            """
        )
    demo.launch()