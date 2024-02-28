from robocorp import windows
from time import sleep
from PIL import ImageGrab, ImageDraw

paint = windows.find_window('executable:mspaint.exe')
for i in range(10):
    print(i)
    print("sleeping 10 secs")
    sleep(10)
    elements = paint.find_many("control:ButtonControl", search_strategy="all")
    len(elements)

    visible_elements = [b for b in elements if b.ui_automation_control.GetClickablePoint()[2]]

    screenshot = ImageGrab.grab()
    screenshot_1 = ImageDraw.Draw(screenshot)
    screenshot.save("02_" + str(i) +"_image.png") 

    output = []
    for b in elements:
        cp = b.ui_automation_control.GetClickablePoint()
        if cp[2]:
            if cp[0]==b.xcenter and cp[1]==b.ycenter:
                screenshot_1.rectangle(b.rectangle, outline ="blue")
                output.append(str([b, b.rectangle, b.xcenter, b.ycenter])+"\n")
            else:
                screenshot_1.rectangle(b.rectangle, outline ="yellow")
        else:
            pass
            #screenshot_1.rectangle(b.rectangle, outline ="red")

    screenshot.save("02_" + str(i) +"_image_debug.png") 
    screenshot.close()
    
    output_file = open("02_" + str(i) +"_output.txt", "w")
    output_file.writelines(output)
    output_file.close()