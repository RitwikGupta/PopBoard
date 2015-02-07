# Module for stringing together images (frames) and audio file to create video

# Written by rajat mehndiratta (github/knyte)
# credit to Daniel Stutzbach and Richard Bronosky on StackOverflow
# as well as Peter Mortensen and ifLoop

import subprocess
import os
import os.path

def makeVideo(movieName, framePrefix, fps):
    assert(type(fps) == int)
    assert(type(movieName) == str)
    assert(type(framePrefix) == str)
    command = "ffmpeg -f image2 -r " + str(fps) + " -i " + framePrefix + "%05d.png -vcodec mpeg4 -y " + movieName + ".mp4"
    subprocess.call(command, shell=True)

def getFrameRate(framePrefix, directory=".", filename):
    allFiles = [name for name in os.listdir(directory) if os.path.isfile(name)]
    prefixedFiles = [fileItem for fileItem in allFiles if framePrefix in fileItem]
    result = subprocess.Popen(["ffprobe", filename],
                              stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    duration = [x for x in result.stdout.readlines() if "Duration" in x]
    if len(duration) < 1:
        return 24
    else:
        timeLine = duration[0]
    return 42
        
