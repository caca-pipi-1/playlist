def replace_url(name, new_url):
    with open("all.m3u", "r+") as f:
        content = f.read()
        
        link_start_position = content.index(name + "\n") + len(name) + 1
        link_end_position = content.index("\n", link_start_position)
        
        content = content[:link_start_position] + new_url + content[link_end_position:]
        
        f.seek(0)
        f.write(content)
        f.truncate()