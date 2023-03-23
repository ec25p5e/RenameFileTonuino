import os, shutil

src = 'D:\\arduinoNanoSong - Copia'
dest = 'D:\\arduinoNanoSong'


# =================== #
# ====== DELETE ===== #
# =================== #

for filename in os.listdir(dest):
    file_path = os.path.join(dest, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

        print("Deleting...")
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


# =================== #
# ====== COPY ======= #
# =================== #

print("Coping...")
shutil.copytree(src, dest, dirs_exist_ok=True)