def save_to_file(out_put_directory, filename: str, content: str):
    file = open(out_put_directory + filename, 'w')
    file.write(content)

