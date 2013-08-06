import os
import os.path
import shutil
import glob

# Move all media to output/media
def seperate_media(config, output_path):
    media = glob.glob(os.path.join(output_path, "*"))

    media_path = os.path.join(output_path, "media")

    os.makedirs(media_path)

    for item in media:
        shutil.move(item, media_path)
    
