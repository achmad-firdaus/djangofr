import os

path = './'
name = 'Input.mp4'
for filename in os.listdir(path):
    if (filename.endswith(".mp4")):  # or .avi, .mpeg, whatever.
        os.system(
            # "ffmpeg -i {0} -f image2 -vf fps=fps=1 output%d.hls".format(filename))
            "ffmpeg -i " + str(name) + " -profile:v baseline -level 3.0 -s 640x360 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls index.m3u8")
        print("%d-{0}")
    else:
        continue


# ffmpeg -i input.mp4 -profile:v baseline -level 3.0 -s 640x360 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls index.m3u8
