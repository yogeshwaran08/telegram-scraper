from linkpreview import link_preview
telegram_default_img = "https://telegram.org/img/t_logo.png"
telegram_default_desc = ""


def telegram_validater(uname):
    link = f"https://t.me/{uname}"
    preview = link_preview(link)
    if(preview.image != telegram_default_img):
        return f"https://t.me/{uname}"
    
    return None