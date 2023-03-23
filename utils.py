# CONSTANTS
MAX_TRACK_FOLDER = 256

# FUNCTIONS

def composeIndex(index):
    if index < 10:
        return '00' + str(index)
    elif index < 100:
        return '0' + str(index)
    elif index > 100:
        return index