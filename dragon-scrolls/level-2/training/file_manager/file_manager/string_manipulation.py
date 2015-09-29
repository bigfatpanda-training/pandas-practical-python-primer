def remove_List_From_String(p_string, p_removal_list):
    for item in p_removal_list:
        p_string = p_string.replace(item, '') 
    return p_string