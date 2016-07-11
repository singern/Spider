from tkinter import *
from tkinter import filedialog
from core.main import *

class SpiderGui():

    def __init__(self, NAME, VERSION):
        main = Tk()
        main.title(NAME + " - " + VERSION)

        w = 1000  # width for the Tk root
        h = 700  # height for the Tk root

        thread_count = 0
        remain_in_domain='true'

        #******************* LAYOUT CREEATION **********************************

        main.rowconfigure(0, weight=0)
        main.rowconfigure(1, weight=150)
        main.rowconfigure(2, weight=0)
        main.rowconfigure(3, weight=10)

        main.columnconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)
        main.columnconfigure(2, weight=1)

        RELIEF_SETTING=SUNKEN

        main_commandcenter_label = Label(text="Command Center")
        main_commandcenter_label.grid(row=0, column=0, sticky=N)
        main_commandcenter = Frame(main, bd=1, relief=RELIEF_SETTING)
        main_commandcenter.grid(row=1, column=0, sticky=N+S+E+W)

        main_statistics_label = Label(text="Application Statistics",width=round(w / 3))
        main_statistics_label.grid(row=2, column=0, sticky=N)
        main_statistics = Frame(main, bd=1, relief=RELIEF_SETTING)
        main_statistics.grid(row=3, column=0, sticky=N+S+E+W)

        main_threadinfo_label = Label(text="Live Thread Information")
        main_threadinfo_label.grid(row=0, column=1, columnspan=2, sticky=N)
        main_threadinfo = Frame(main, bd=1, relief=RELIEF_SETTING, height=round(h / 2))
        main_threadinfo.grid(row=1, column=1, columnspan=2, sticky=N+S+E+W)

        main_queue_label = Label(text="Queue Feed",width=round(w / 3))
        main_queue_label.grid(row=2, column=1, sticky=N)
        main_queue = Frame(main, bd=1, relief=RELIEF_SETTING)
        main_queue.grid(row=3, column=1, sticky=N+S+E+W)

        main_crawled_label = Label(text="Crawled Feed",width=round(w / 3))
        main_crawled_label.grid(row=2, column=2, sticky=N)
        main_crawled = Frame(main, bd=1, relief=RELIEF_SETTING, height=round(h / 2))
        main_crawled.grid(row=3, column=2, sticky=N+S+E+W)

        # get screen width and height
        ws = main.winfo_screenwidth()  # width of the screen
        hs = main.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        main.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # *******************  END LAYOUT CREATION *******************************

        # add a frame and put a text area into it
        queue_textFrame = Frame(main_queue)
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
        crawled_textFrame = Frame(main_crawled)
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
        threadlist = Listbox(main_threadinfo)
        threadlist.pack(expand=1, fill=BOTH)

        #Threads columns
        # thread number     parsing/crawling/queued/crawled     url

        # *** COMMAND & CONTROL ****
        #
        #Export Results

        main_commandcenter.columnconfigure(0, weight=0)
        main_commandcenter.rowconfigure(1, weight=1)
        main_commandcenter.rowconfigure(2, weight=1)
        main_commandcenter.rowconfigure(3, weight=1)
        main_commandcenter.rowconfigure(4, weight=1)
        main_commandcenter.rowconfigure(5, weight=1)
        main_commandcenter.rowconfigure(6, weight=1)
        main_commandcenter.rowconfigure(7, weight=1)
        main_commandcenter.rowconfigure(8, weight=1)
        main_commandcenter.rowconfigure(9, weight=1)
        main_commandcenter.rowconfigure(10, weight=1)

        main_commandcenter = Frame(main_commandcenter)
        main_commandcenter.pack()

        main_commandcenter_control_label = Label(main_commandcenter, text="Execution")
        main_commandcenter_control_label.grid(row=0)
        main_commandcenter_control_container = Frame(main_commandcenter)
        main_commandcenter_control_container.grid(row=1)
        main_commandcenter_control_start = Button(main_commandcenter_control_container, text="Start")
        main_commandcenter_control_start.pack(side=LEFT, fill=BOTH, padx=5)
        main_commandcenter_control_pause = Button(main_commandcenter_control_container, text="Pause")
        main_commandcenter_control_pause.pack(side=LEFT, fill=BOTH, padx=5)
        main_commandcenter_control_stop = Button(main_commandcenter_control_container, text="Stop")
        main_commandcenter_control_stop.pack(side=LEFT, fill=BOTH, padx=5)

        def execute_start():
            HOMEPAGE=main_commandcenter_domaintocrawl_textbox.get()
            Spider("PROJECTNAME", HOMEPAGE, get_domain_name(HOMEPAGE))
            create_workers
            crawl
        def execute_pause():
            pass
        def execute_stop():
            pass

        main_commandcenter_control_start.configure(command=execute_start)

        main_commandcenter_domaintocrawl_label = Label(main_commandcenter, text="Target Domain")
        main_commandcenter_domaintocrawl_label.grid(row=2)
        main_commandcenter_domaintocrawl_textbox = Entry(main_commandcenter)
        main_commandcenter_domaintocrawl_textbox.grid(row=3)

        check_var=IntVar()

        main_commandcenter_remainindomain_checkbox = Checkbutton(main_commandcenter, text="Remain In Domain",
                                                                                 variable=check_var)
        main_commandcenter_remainindomain_checkbox.invoke()
        main_commandcenter_remainindomain_checkbox.grid(row=4)

        main_commandcenter_remainindomain_checkbox.configure(command=lambda: print("State Of Checkbox Is: " + str(check_var.get())))

        main_commandcenter_threads_label = Label(main_commandcenter, text="Thread Control")
        main_commandcenter_threads_label.grid(row=5)
        main_commandcenter_threads_container = Frame(main_commandcenter)
        main_commandcenter_threads_container.grid(row=6)
        main_commandcenter_threads_container.columnconfigure(1, weight=1)
        main_commandcenter_threads_button1 = Button(main_commandcenter_threads_container, text="1")
        main_commandcenter_threads_button1.grid(column=1, row=0, padx=2)
        main_commandcenter_threads_button2 = Button(main_commandcenter_threads_container, text="2")
        main_commandcenter_threads_button2.grid(column=2, row=0, padx=2)
        main_commandcenter_threads_button4 = Button(main_commandcenter_threads_container, text="4")
        main_commandcenter_threads_button4.grid(column=3, row=0, padx=2)
        main_commandcenter_threads_button8 = Button(main_commandcenter_threads_container, text="8")
        main_commandcenter_threads_button8.grid(column=4, row=0, padx=2)
        main_commandcenter_threads_button16 = Button(main_commandcenter_threads_container, text="16")
        main_commandcenter_threads_button16.grid(column=5, row=0, padx=2)
        main_commandcenter_threads_button32 = Button(main_commandcenter_threads_container, text="32")
        main_commandcenter_threads_button32.grid(column=6, row=0, padx=2)
        main_commandcenter_threads_button64 = Button(main_commandcenter_threads_container, text="64")
        main_commandcenter_threads_button64.grid(column=7, row=0, padx=2)
        main_commandcenter_threads_button128 = Button(main_commandcenter_threads_container, text="128")
        main_commandcenter_threads_button128.grid(column=8, row=0, padx=2)

        color_blue = '#EEEEFE'
        color_red = '#FFEEEE'

        main_commandcenter_threads_button1.configure(bg=color_blue)
        main_commandcenter_threads_button2.configure(bg=color_blue)
        main_commandcenter_threads_button4.configure(bg=color_blue)
        main_commandcenter_threads_button8.configure(bg=color_blue)
        main_commandcenter_threads_button16.configure(bg=color_blue)
        main_commandcenter_threads_button32.configure(bg=color_blue)
        main_commandcenter_threads_button64.configure(bg=color_blue)
        main_commandcenter_threads_button128.configure(bg=color_blue)

        def set_thread(thread_number):

            def set_selected_button(button):
                main_commandcenter_threads_button1.configure(bg=color_blue)
                main_commandcenter_threads_button2.configure(bg=color_blue)
                main_commandcenter_threads_button4.configure(bg=color_blue)
                main_commandcenter_threads_button8.configure(bg=color_blue)
                main_commandcenter_threads_button16.configure(bg=color_blue)
                main_commandcenter_threads_button32.configure(bg=color_blue)
                main_commandcenter_threads_button64.configure(bg=color_blue)
                main_commandcenter_threads_button128.configure(bg=color_blue)

                if button == 1:
                    main_commandcenter_threads_button1.configure(bg=color_red)
                elif button == 2:
                    main_commandcenter_threads_button2.configure(bg=color_red)
                elif button == 4:
                    main_commandcenter_threads_button4.configure(bg=color_red)
                elif button == 8:
                    main_commandcenter_threads_button8.configure(bg=color_red)
                elif button == 16:
                    main_commandcenter_threads_button16.configure(bg=color_red)
                elif button == 32:
                    main_commandcenter_threads_button32.configure(bg=color_red)
                elif button == 64:
                    main_commandcenter_threads_button64.configure(bg=color_red)
                elif button == 128:
                    main_commandcenter_threads_button128.configure(bg=color_red)
                else:
                    pass

            if thread_number == 1:
                thread_count = 1
                set_selected_button(1)
            elif thread_number == 2:
                thread_count = 2
                set_selected_button(2)
            elif thread_number == 4:
                thread_count = 4
                set_selected_button(4)
            elif thread_number == 8:
                thread_count = 8
                set_selected_button(8)
            elif thread_number == 16:
                thread_count = 16
                set_selected_button(16)
            elif thread_number == 32:
                thread_count = 32
                set_selected_button(32)
            elif thread_number == 64:
                thread_count = 64
                set_selected_button(64)
            elif thread_number == 128:
                thread_count = 128
                set_selected_button(128)

            print("Thread Count Set To: " + str(thread_count))

        set_thread(8)

        main_commandcenter_threads_button1.configure(command=lambda: set_thread(1))
        main_commandcenter_threads_button2.configure(command=lambda: set_thread(2))
        main_commandcenter_threads_button4.configure(command=lambda: set_thread(4))
        main_commandcenter_threads_button8.configure(command=lambda: set_thread(8))
        main_commandcenter_threads_button16.configure(command=lambda: set_thread(16))
        main_commandcenter_threads_button32.configure(command=lambda: set_thread(32))
        main_commandcenter_threads_button64.configure(command=lambda: set_thread(64))
        main_commandcenter_threads_button128.configure(command=lambda: set_thread(128))

        main_commandcenter_savedirectory_label = Label(main_commandcenter, text="Cache Dump / Save Directory")
        main_commandcenter_savedirectory_label.grid(row=7)
        main_commandcenter_savedirectory_container = Frame(main_commandcenter)
        main_commandcenter_savedirectory_container.grid(row=8)
        main_commandcenter_savedirectory_button = Button(main_commandcenter_savedirectory_container, text="Browse")
        main_commandcenter_savedirectory_button.pack(side=LEFT, padx=5)
        main_commandcenter_savedirectory_directory = Entry(main_commandcenter_savedirectory_container)
        main_commandcenter_savedirectory_directory.pack(side=LEFT)

        def set_working_directory():
            working_directory = filedialog.askdirectory()
            main_commandcenter_savedirectory_directory.delete(0, END)
            main_commandcenter_savedirectory_directory.insert(0, working_directory)
            print("Working Directory Set To: " + working_directory)



        main_commandcenter_savedirectory_button.configure(command=set_working_directory)

        main_commandcenter_export_label = Label(main_commandcenter, text="Export")
        main_commandcenter_export_label.grid(row=9)
        main_commandcenter_export_button = Button(main_commandcenter, text="Export Execution Stats")
        main_commandcenter_export_button.grid(row=10)

        # **** Statstics *****

        #main_statistics.rowconfigure(0, weight=1)
        #main_statistics.rowconfigure(1, weight=1)
        #main_statistics.rowconfigure(2, weight=1)
        #main_statistics.rowconfigure(3, weight=1)

        main_statistics.columnconfigure(0, weight=28)
        main_statistics.columnconfigure(1, weight=72)

        main_statistics_timerunning_label = Label(main_statistics, text="Time Running:")
        main_statistics_timerunning_label.grid(row=0, column=0, sticky=E)
        main_statistics_timerunning_value = Label(main_statistics, text="0:00")
        main_statistics_timerunning_value.grid(row=0, column=1, sticky=W)

        main_statistics_thread_count_label = Label(main_statistics, text="Thread Count:")
        main_statistics_thread_count_label.grid(row=1, column=0, sticky=E)
        main_statistics_thread_count_value = Label(main_statistics, text="0")
        main_statistics_thread_count_value.grid(row=1, column=1, sticky=W)

        main_statistics_urlqueued_label = Label(main_statistics, text="Queued URL Count:")
        main_statistics_urlqueued_label.grid(row=2, column=0, sticky=E)
        main_statistics_urlqueued_value = Label(main_statistics, text="0")
        main_statistics_urlqueued_value.grid(row=2, column=1, sticky=W)

        main_statistics_urlcralwed_label = Label(main_statistics, text="Crawled URL Count:")
        main_statistics_urlcralwed_label.grid(row=3, column=0, sticky=E)
        main_statistics_urlcralwed_value = Label(main_statistics, text="0")
        main_statistics_urlcralwed_value.grid(row=3, column=1, sticky=W)

        #Menu Bar potentially, im not sure what i would want to add to it yet
        # though so ill leave this blank for now

        main.mainloop()
