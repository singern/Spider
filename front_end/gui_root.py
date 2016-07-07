from tkinter import *


class SpiderGui():

    def __init__(self, NAME, VERSION):
        frame_main = Tk()
        frame_main.title(NAME + " - " + VERSION)

        w = 1000  # width for the Tk root
        h = 700  # height for the Tk root

        #frame_main.resizable(width=FALSE, height=FALSE)

        #******************* LAYOUT CREEATION **********************************

        frame_main.rowconfigure(0, weight=0)
        frame_main.rowconfigure(1, weight=1)
        frame_main.rowconfigure(2, weight=0)
        frame_main.rowconfigure(3, weight=1)

        frame_main.columnconfigure(0, weight=1)
        frame_main.columnconfigure(1, weight=1)
        frame_main.columnconfigure(2, weight=1)

        RELIEF_SETTING=SUNKEN

        frame_main_commandcenter_label = Label(text="Command Center")
        frame_main_commandcenter_label.grid(row=0, column=0, sticky=N)
        frame_main_commandcenter = Frame(frame_main, bd=1, relief=RELIEF_SETTING)
        frame_main_commandcenter.grid(row=1, column=0, sticky=N+S+E+W)

        frame_main_statistics_label = Label(text="Application Statistics",width=round(w / 3))
        frame_main_statistics_label.grid(row=2, column=0, sticky=N)
        frame_main_statistics = Frame(frame_main, bd=1, relief=RELIEF_SETTING)
        frame_main_statistics.grid(row=3, column=0, sticky=N+S+E+W)

        frame_main_threadinfo_label = Label(text="Live Thread Information")
        frame_main_threadinfo_label.grid(row=0, column=1, columnspan=2, sticky=N)
        frame_main_threadinfo = Frame(frame_main, bd=1, relief=RELIEF_SETTING, height=round(h / 2))
        frame_main_threadinfo.grid(row=1, column=1, columnspan=2, sticky=N+S+E+W)

        frame_main_queue_label = Label(text="Queue Feed",width=round(w / 3))
        frame_main_queue_label.grid(row=2, column=1, sticky=N)
        frame_main_queue = Frame(frame_main, bd=1, relief=RELIEF_SETTING)
        frame_main_queue.grid(row=3, column=1, sticky=N+S+E+W)

        frame_main_crawled_label = Label(text="Crawled Feed",width=round(w / 3))
        frame_main_crawled_label.grid(row=2, column=2, sticky=N)
        frame_main_crawled = Frame(frame_main, bd=1, relief=RELIEF_SETTING, height=round(h / 2))
        frame_main_crawled.grid(row=3, column=2, sticky=N+S+E+W)

        # get screen width and height
        ws = frame_main.winfo_screenwidth()  # width of the screen
        hs = frame_main.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        frame_main.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # *******************  END LAYOUT CREATION *******************************

        # add a frame and put a text area into it
        queue_textFrame = Frame(frame_main_queue)
        queuetextarea = Text(queue_textFrame)

        # add a vertical scroll bar to the text area
        queuescrollbar = Scrollbar(queue_textFrame)
        queuetextarea.configure(yscrollcommand=queuescrollbar.set)
        queuescrollbar.configure(command=queuetextarea.yview)
        queuetextarea.configure(bg='#EEFEEE')

        # pack everything
        queue_textFrame.grid_columnconfigure(0, weight=1)
        queue_textFrame.grid_columnconfigure(1, weight=0)
        queue_textFrame.grid_rowconfigure(0, weight=1)

        queue_textFrame.pack(expand=1, fill=BOTH)
        queuescrollbar.grid(row=0, column=1, sticky=N+S+E+W)
        queuetextarea.grid(row=0, column=0, sticky=N+S+E+W)

        queuetextarea.configure(state=DISABLED)

        def printToQueuePanel(input):
            queuetextarea.configure(state=NORMAL)
            queuetextarea.insert(INSERT, input+'\n')
            queuetextarea.configure(state=DISABLED)

        # add a frame and put a text area into it
        crawled_textFrame = Frame(frame_main_crawled)
        crawledtextarea = Text(crawled_textFrame)

        # add a vertical scroll bar to the text area
        crawledscrollbar = Scrollbar(crawled_textFrame)
        crawledtextarea.configure(yscrollcommand=crawledscrollbar.set)
        crawledscrollbar.configure(command=crawledtextarea.yview)
        crawledtextarea.configure(bg='#EEEEFE')

        # pack everything
        crawled_textFrame.grid_columnconfigure(0, weight=1)
        crawled_textFrame.grid_columnconfigure(1, weight=0)
        crawled_textFrame.grid_rowconfigure(0, weight=1)

        crawled_textFrame.pack(expand=1, fill=BOTH)
        crawledscrollbar.grid(row=0, column=1, sticky=N + S + E + W)
        crawledtextarea.grid(row=0, column=0, sticky=N + S + E + W)

        crawledtextarea.configure(state=DISABLED)

        def printToCrawledPanel(input):
            crawledtextarea.configure(state=NORMAL)
            crawledtextarea.insert(INSERT, input + '\n')
            crawledtextarea.configure(state=DISABLED)



        frame_main.mainloop()
