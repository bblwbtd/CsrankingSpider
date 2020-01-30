import pickle


def save_to_file(out_put_directory, filename: str, content: str):
    file = open(out_put_directory + filename, 'wb')
    pickle.dump(content, file)
