from csv import DictWriter, writer as writerCsv, reader
import os

def generateCsv(tracks, filePath, filesName):
    fields = ['index', 'name', 'folder']
    keepfile = filePath + '\\' + filesName[0] + '.csv'
    tmpfile = filePath + '\\' + filesName[1] + '.csv'

    data = []
    for track in tracks.getTracks():
        col = {
            'index': track.index,
            'name': track.name,
            'folder': track.folderIndex
        }
        data.append(col)

    with open(keepfile, mode='w') as csvfile:
        writer = DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

    with open(keepfile, newline='') as in_file:
        with open(tmpfile, 'w', newline='') as out_file:
            writer = writerCsv(out_file)

            for row in reader(in_file):
                if any(row):
                    writer.writerow(row)

    os.remove(keepfile)
    os.rename(tmpfile, keepfile)
