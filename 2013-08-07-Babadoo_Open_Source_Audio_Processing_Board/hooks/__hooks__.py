from seperate_media import seperate_media
from process_less import process_less

hooks = {
    "site.output.post" : [process_less, seperate_media],
}
