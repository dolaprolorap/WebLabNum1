def init():
    global HOST
    HOST = None
    
    global CURRENT_IMAGE
    CURRENT_IMAGE = "show.jpg"
    
    global PAGES
    PAGES = dict()
    
    global ROOT_PAGE
    ROOT_PAGE = None
    
    global SERVER_RUNNING
    SERVER_RUNNING = False