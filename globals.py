def init():
    global HOST
    HOST = None
    
    global CURRENT_IMAGE
    CURRENT_IMAGE = "show.jpg"
    
    global PAGES
    PAGES = dict()
    
    global SERVER_RUNNING
    SERVER_RUNNING = False

    global IMAGE_PANEL
    IMAGE_PANEL = None
    
    global UPLOADED_FILE
    UPLOADED_FILE = None