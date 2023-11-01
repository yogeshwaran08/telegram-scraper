from linkpreview import link_preview

def freelancer_validater(uname):
    link = f"https://www.freelancer.com/u/{uname}"
    try:
        link_preview(link)
        return f"https://www.freelancer.com/u/{uname}"
    except:
        return None