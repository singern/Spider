from tkinter import *


class SpiderGui():

    def __init__(self, NAME, VERSION):
        frame_main = Tk()
        frame_main.title(NAME + " - " + VERSION)
        
        threadCount = IntVar()

        w = 1000  # width for the Tk root
        h = 700  # height for the Tk root

        #******************* LAYOUT CREEATION **********************************

        frame_main.rowconfigure(0, weight=0)
        frame_main.rowconfigure(1, weight=150)
        frame_main.rowconfigure(2, weight=0)
        frame_main.rowconfigure(3, weight=10)

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

        # **** LIST BOX CREATIOON ****
        threadlist = Listbox(frame_main_threadinfo)
        threadlist.pack(expand=1, fill=BOTH)



        #Threads columns
        # thread number     parsing/crawling/queued/crawled     url

        # *** COMMAND & CONTROL ****
        #
        #Directory
        #
        #Threads selector as buttons with 1/2/4/8/16/32/64/128
        #
        #Checkbox for 'stay in domain'
        #
        #Start Pause Stop
        #
        #Export

        frame_main_commandcenter.columnconfigure(0, weight=1)

        frame_main_commandcenter_control_label = Label(frame_main_commandcenter, text="Execution")
        frame_main_commandcenter_control_label.grid(row=0)
        frame_main_commandcenter_control_container = Frame(frame_main_commandcenter)
        frame_main_commandcenter_control_container.grid(row=1)
        frame_main_commandcenter_control_start = Button(frame_main_commandcenter_control_container, text="Start")
        frame_main_commandcenter_control_start.pack(side=LEFT)
        frame_main_commandcenter_control_pause = Button(frame_main_commandcenter_control_container, text="Pause")
        frame_main_commandcenter_control_pause.pack(side=LEFT)
        frame_main_commandcenter_control_stop = Button(frame_main_commandcenter_control_container, text="Stop")
        frame_main_commandcenter_control_stop.pack(side=LEFT)

        frame_main_commandcenter_domaintocrawl_label = Label(frame_main_commandcenter, text="Target Domain")
        frame_main_commandcenter_domaintocrawl_label.grid(row=2)
        frame_main_commandcenter_domaintocrawl_textbox = Entry(frame_main_commandcenter)
        frame_main_commandcenter_domaintocrawl_textbox.grid(row=3)

        def setThreadButtonColor(thread_count):

            frame_main_commandcenter_threads_button1.configure(bg="red")
            frame_main_commandcenter_threads_button2.configure(bg="red")
            frame_main_commandcenter_threads_button4.configure(bg="red")
            frame_main_commandcenter_threads_button8.configure(bg="red")
            frame_main_commandcenter_threads_button16.configure(bg="red")
            frame_main_commandcenter_threads_button32.configure(bg="red")
            frame_main_commandcenter_threads_button64.configure(bg="red")
            frame_main_commandcenter_threads_button128.configure(bg="red")

            if not thread_count == 1:
                frame_main_commandcenter_threads_button1.configure(bg="blue")

            if not thread_count == 2:
                frame_main_commandcenter_threads_button2.configure(bg="blue")

            if not thread_count == 4:
                frame_main_commandcenter_threads_button4.configure(bg="blue")

            if not thread_count == 8:
                frame_main_commandcenter_threads_button8.configure(bg="blue")

            if not thread_count == 16:
                frame_main_commandcenter_threads_button16.configure(bg="blue")

            if not thread_count == 32:
                frame_main_commandcenter_threads_button32.configure(bg="blue")

            if not thread_count == 64:
                frame_main_commandcenter_threads_button64.configure(bg="blue")

            if not thread_count == 128:
                frame_main_commandcenter_threads_button128.configure(bg="blue")

        def setThread_1():
            if not self.threadCount == 1:
                setThreadButtonColor(1)
                threadCount = 1
            else:
                setThreadButtonColor(0)

        def setThread_2():
            if not self.threadCount == 2:
                setThreadButtonColor(2)
                threadCount = 2
            else:
                setThreadButtonColor(0)

        def setThread_4():
            if not self.threadCount == 4:
                setThreadButtonColor(4)
                threadCount = 4
            else:
                setThreadButtonColor(0)

        def setThread_8():
            if not self.threadCount == 8:
                setThreadButtonColor(8)
                threadCount = 8
            else:
                setThreadButtonColor(0)

        def setThread_16():
            if not self.threadCount == 16:
                setThreadButtonColor(16)
                threadCount = 16
            else:
                setThreadButtonColor(0)

        def setThread_32():
            if not self.threadCount == 32:
                setThreadButtonColor(32)
                threadCount = 32
            else:
                setThreadButtonColor(0)

        def setThread_64():
            if not self.threadCount == 64:
                setThreadButtonColor(64)
                threadCount = 64
            else:
                setThreadButtonColor(0)

        def setThread_128():
            if not self.threadCount == 128:
                setThreadButtonColor(128)
                threadCount = 128
            else:
                setThreadButtonColor(0)

        frame_main_commandcenter_threads_label = Label(frame_main_commandcenter, text="Thread Control")
        frame_main_commandcenter_threads_label.grid(row=4)
        frame_main_commandcenter_threads_container = Frame(frame_main_commandcenter)
        frame_main_commandcenter_threads_container.grid(row=5)
        frame_main_commandcenter_threads_container.columnconfigure(1, weight=1)
        frame_main_commandcenter_threads_button1 = Button(frame_main_commandcenter_threads_container, text="1", command=setThread_1())
        frame_main_commandcenter_threads_button1.grid(column=1, row=0)
        frame_main_commandcenter_threads_button2 = Button(frame_main_commandcenter_threads_container, text="2")
        frame_main_commandcenter_threads_button2.grid(column=2, row=0)
        frame_main_commandcenter_threads_button4 = Button(frame_main_commandcenter_threads_container, text="4")
        frame_main_commandcenter_threads_button4.grid(column=3, row=0)
        frame_main_commandcenter_threads_button8 = Button(frame_main_commandcenter_threads_container, text="8")
        frame_main_commandcenter_threads_button8.grid(column=4, row=0)
        frame_main_commandcenter_threads_button16 = Button(frame_main_commandcenter_threads_container, text="16")
        frame_main_commandcenter_threads_button16.grid(column=5, row=0)
        frame_main_commandcenter_threads_button32 = Button(frame_main_commandcenter_threads_container, text="32")
        frame_main_commandcenter_threads_button32.grid(column=6, row=0)
        frame_main_commandcenter_threads_button64 = Button(frame_main_commandcenter_threads_container, text="64")
        frame_main_commandcenter_threads_button64.grid(column=7, row=0)
        frame_main_commandcenter_threads_button128 = Button(frame_main_commandcenter_threads_container, text="128")
        frame_main_commandcenter_threads_button128.grid(column=8, row=0)

        setThreadButtonColor(0)

        remainindomain = 0
        frame_main_commandcenter_remainindomain_checkbox = Checkbutton(frame_main_commandcenter, text="Remain In Domain",
                                                                       variable = remainindomain, onvalue = 1, offvalue = 0)
        frame_main_commandcenter_remainindomain_checkbox.invoke()
        frame_main_commandcenter_remainindomain_checkbox.grid(row=6)

        frame_main_commandcenter_savedirectory_label = Label(frame_main_commandcenter, text="Cache Dump / Save Directory")
        frame_main_commandcenter_savedirectory_button = Button(frame_main_commandcenter, text="Browse")
        frame_main_commandcenter_savedirectory_directory = Entry(frame_main_commandcenter)

        frame_main_commandcenter_export_button = Button(frame_main_commandcenter, text="Export Known Paths")

        # **** Statstics *****

        #frame_main_statistics.rowconfigure(0, weight=1)
        #frame_main_statistics.rowconfigure(1, weight=1)
        #frame_main_statistics.rowconfigure(2, weight=1)
        #frame_main_statistics.rowconfigure(3, weight=1)

        frame_main_statistics.columnconfigure(0, weight=28)
        frame_main_statistics.columnconfigure(1, weight=72)

        frame_main_statistics_timerunning_label = Label(frame_main_statistics, text="Time Running:")
        frame_main_statistics_timerunning_label.grid(row=0, column=0, sticky=E)
        frame_main_statistics_timerunning_value = Label(frame_main_statistics, text="0:00")
        frame_main_statistics_timerunning_value.grid(row=0, column=1, sticky=W)

        frame_main_statistics_threadcount_label = Label(frame_main_statistics, text="Thread Count:")
        frame_main_statistics_threadcount_label.grid(row=1, column=0, sticky=E)
        frame_main_statistics_threadcount_value = Label(frame_main_statistics, text="0")
        frame_main_statistics_threadcount_value.grid(row=1, column=1, sticky=W)

        frame_main_statistics_urlqueued_label = Label(frame_main_statistics, text="Queued URL Count:")
        frame_main_statistics_urlqueued_label.grid(row=2, column=0, sticky=E)
        frame_main_statistics_urlqueued_value = Label(frame_main_statistics, text="0")
        frame_main_statistics_urlqueued_value.grid(row=2, column=1, sticky=W)

        frame_main_statistics_urlcralwed_label = Label(frame_main_statistics, text="Crawled URL Count:")
        frame_main_statistics_urlcralwed_label.grid(row=3, column=0, sticky=E)
        frame_main_statistics_urlcralwed_value = Label(frame_main_statistics, text="0")
        frame_main_statistics_urlcralwed_value.grid(row=3, column=1, sticky=W)

        #Menu Bar potentially, im not sure what i would want to add to it yet
        # though so ill leave this blank for now

        frame_main.mainloop()
