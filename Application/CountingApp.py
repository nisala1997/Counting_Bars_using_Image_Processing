import numpy as np
import cv2
from PIL import Image, ImageTk
import tkinter.filedialog as tkFileDialog
import argparse
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import CountingApp_support

refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
        
	global refPt, cropping
	
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True

	elif event == cv2.EVENT_LBUTTONUP:
                
		refPt.append((x, y))
		cropping = False

def getImageRectangle():
    path = tkFileDialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        clone = image.copy()
        cv2.namedWindow("image",cv2.WINDOW_KEEPRATIO)
        cv2.setMouseCallback("image", click_and_crop)

        while True:
                cv2.namedWindow('image',cv2.WINDOW_KEEPRATIO)
                cv2.imshow("image", image)
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord("r"):
                        image = clone.copy()
                        
                elif key == ord("c"):
                        break

        if len(refPt) == 2:
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                roi2 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
##                cv2.namedWindow('ROI',cv2.WINDOW_KEEPRATIO)
##                cv2.imshow("ROI", roi)
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                kernel = np.ones((85,110),np.uint8)
                blur = cv2.medianBlur(roi,15)
                ret,thresh=cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
                dilation = cv2.dilate(thresh,kernel,iterations = 1)
                ret,thresh1=cv2.threshold(dilation,127,255,cv2.THRESH_BINARY_INV)
                
                
                im2,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                print(len(contours)-3)
                
                text="count : "+ str(len(contours)-3)
                #cv2.drawContours(roi2, contours, -1, (0,255,0), 3)
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(roi2,text,(50,150), font, 3,(0,255,255),4,cv2.LINE_AA)
                cv2.namedWindow('ROI',cv2.WINDOW_KEEPRATIO)
                cv2.imshow("ROI", roi2)

                cv2.waitKey(0)
                
        cv2.destroyAllWindows()

def getImageSquare():
    path = tkFileDialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        clone = image.copy()
        cv2.namedWindow("image",cv2.WINDOW_KEEPRATIO)
        cv2.setMouseCallback("image", click_and_crop)

        while True:
                cv2.namedWindow('image',cv2.WINDOW_KEEPRATIO)
                cv2.imshow("image", image)
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord("r"):
                        image = clone.copy()
                        
                elif key == ord("c"):
                        break

        if len(refPt) == 2:
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                roi2 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                cv2.namedWindow('ROI',cv2.WINDOW_KEEPRATIO)
                cv2.imshow("ROI", roi)
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                kernel = np.ones((50,50),np.uint8)
                blur = cv2.medianBlur(roi,15)
                ret,thresh=cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
                dilation = cv2.dilate(thresh,kernel,iterations = 1)
                ret,thresh1=cv2.threshold(dilation,127,255,cv2.THRESH_BINARY_INV)
                
                
                im2,contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                print(len(contours)-3)
                
                text="count : "+ str(len(contours)-3)
                #cv2.drawContours(roi2, contours, -1, (0,255,0), 3)
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(roi2,text,(50,150), font, 3,(0,255,255),4,cv2.LINE_AA)
                
                cv2.namedWindow('ROI',cv2.WINDOW_KEEPRATIO)
                cv2.imshow("ROI", roi2)
                
                cv2.waitKey(0)
                
        cv2.destroyAllWindows()

def circles():
    path = tkFileDialog.askopenfilename()
    if len(path) > 0:
        image = cv2.imread(path)
        clone = image.copy()
        cv2.namedWindow("image",cv2.WINDOW_KEEPRATIO)
        cv2.setMouseCallback("image", click_and_crop)

        while True:
                cv2.namedWindow('image',cv2.WINDOW_KEEPRATIO)
                cv2.imshow("image", image)
                key = cv2.waitKey(1) & 0xFF
                
                if key == ord("r"):
                        image = clone.copy()
                        
                elif key == ord("c"):
                        break

        if len(refPt) == 2:
                roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
                roi2 = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
##                cv2.namedWindow('ROI',cv2.WINDOW_KEEPRATIO)
##                cv2.imshow("ROI", roi)
                roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                roi=cv2.medianBlur(roi,5)
                
                circles = cv2.HoughCircles(roi,cv2.HOUGH_GRADIENT,1,120,param1=40,param2=50,minRadius=20,maxRadius=120)
                #circles = cv2.HoughCircles(roi,cv2.HOUGH_GRADIENT,1,50,param1=30,param2=30,minRadius=15,maxRadius=50)
                circles = np.uint16(np.around(circles))

                for i in circles[0,:]:
                    cv2.circle(roi2,(i[0],i[1]),i[2],(0,255,0),2)
                    cv2.circle(roi2,(i[0],i[1]),2,(0,0,255),3)

                print(circles.shape[1])
                
                text="count : "+ str(circles.shape[1]-3)
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(roi2,text,(50,150), font, 3,(0,255,255),4,cv2.LINE_AA)

                cv2.namedWindow('detected circles',cv2.WINDOW_KEEPRATIO)
                cv2.imshow('detected circles',roi2)
                
                

                
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    CountingApp_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    CountingApp_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font12 = "-family Tahoma -size 24 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font13 = "-family {Segoe UI Emoji} -size 10 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"

        top.geometry("849x569+388+115")
        top.title("Counting App")
        top.configure(background="#d9d9d9")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=-0.05, rely=-0.02, relheight=1.13, relwidth=1.05)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#e8e8e8")
        self.Frame1.configure(width=895)

##        self.Label1 = Label(self.Frame1)
##        self.Label1.place(relx=0.08, rely=0.64, height=126, width=782)
##        self.Label1.configure(background="#d9d9d9")
##        self.Label1.configure(disabledforeground="#a3a3a3")
##        self.Label1.configure(foreground="#000000")
##        self._img1 = PhotoImage(file="icons.jpg")
##        self.Label1.configure(image=self._img1)
##        self.Label1.configure(text='''Label''')
##        self.Label1.configure(width=782)

        self.Button1 = Button(self.Frame1,command=getImageSquare)
        self.Button1.place(relx=0.12, rely=0.51, height=43, width=126)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Square''')
        self.Button1.configure(width=126)

        self.Button2 = Button(self.Frame1,command=getImageRectangle)
        self.Button2.place(relx=0.32, rely=0.51, height=43, width=126)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Rectangular''')
        self.Button2.configure(width=126)

        self.Button3 = Button(self.Frame1,command=circles)
        self.Button3.place(relx=0.55, rely=0.51, height=43, width=116)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Circular''')
        self.Button3.configure(width=116)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.77, rely=0.51, height=43, width=116)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Rods''')
        self.Button4.configure(width=116)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.31, rely=0.08, height=76, width=352)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Counting App''')
        self.Label2.configure(width=352)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.26, rely=0.34, height=56, width=452)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font13)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Select the cross section and load the image''')
        self.Label3.configure(width=452)






if __name__ == '__main__':
    vp_start_gui()



