def valid_string(string):
    import re
    
    # substituting and replace special characters and consecutive white spaces
    valid_string = re.sub(r'[^\w\s.,?!\'"()\-]|^\s+|\s+$', '', string)
    valid_string = re.sub(r'\s{2,}', '', valid_string)
    valid_string = re.sub(r'[\(\)/?!\\]', '', valid_string)

    return valid_string