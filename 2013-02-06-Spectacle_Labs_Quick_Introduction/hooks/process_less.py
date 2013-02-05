import subprocess
import glob
import os
import os.path
import shutil

def process_less(output_path):
    less_path = os.path.join(output_path, "less")
    include_path = os.path.join(less_path, "include")
    css_path = os.path.join(output_path, "css")

    if not os.path.exists(css_path):
        os.makedirs(css_path)

    fileNames = glob.glob(os.path.join(less_path, "*"))
    for fileName in fileNames:
        if not os.path.isfile(fileName):
            continue
        command = ["lessc", "--include-path={}".format(include_path), fileName]
        output = subprocess.check_output(command)

        fileName = os.path.basename(fileName)
        fileName = os.path.splitext(fileName)[0] + ".css"

        with open(os.path.join(css_path, fileName), "w") as f:
            f.write(output.decode("utf-8"))

    # Delete the less folder as it is now unecessary
    shutil.rmtree(less_path)
