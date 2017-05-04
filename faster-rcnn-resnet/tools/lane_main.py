import lane_image
reload(lane_image)
from lane_image import process_image
import lane_video
reload(lane_video)
from lane_video import process_video
import os
import glob
import argparse
import time
import cv2
import imutils
from skimage import io
from moviepy.editor import VideoFileClip
import cv


def parse_args():
    # Parse input arguments.
    parser = argparse.ArgumentParser(description='Lane Detection Demo')
    parser.add_argument('--vdo', dest='video_mode', help='Use video file for scan/input',
                        action='store_true')
    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = parse_args()

    input_dir = '/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/input/'
    input_dir += '/*'

    output_dir = '/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/output/'
    
    ipdir = glob.glob(input_dir)

    if args.video_mode:
        ## Process video files as an input
        for video in ipdir:
 
            video_name = os.path.basename(video)
            print 'Demo for video named {}'.format(video_name)

            clip = VideoFileClip(video)
            start = time.time()

            # Transform video and perform image lane detection
            new_clip = clip.fl_image(process_video)
            
            # Write a video to a file
            output_vid = (os.path.join(output_dir,video_name))
            new_clip.write_videofile(output_vid, audio=False)
	    end = time.time()
            
            # Get the total duration required for video transformation
            total_time = (end - start)
            total_dur = time.strftime("%H:%M:%S", time.gmtime(total_time))
            clip_len = time.strftime("%H:%M:%S", time.gmtime(clip.duration))

            print((('Lane detection took {} = {:.3f}s for '
                    '{} long video').format(total_dur, total_time, clip_len)))
    else:
        for image in ipdir:
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            image_name = os.path.basename(image)

            print 'Demo for image named {}'.format(image_name)
            # print(matplotlib.backends.backend)
            img = io.imread(image)
            pimg = process_image(img)                      # processed image

            ## Show output frame
            # cv2.imshow("output", pimg)
            # cv2.waitKey(0)
            # plt.show()

            cv2.imwrite(os.path.join(output_dir, 'processesd_'+ image_name), pimg)
            print ('Output written at ')
            print (output_dir + 'processed_'+ image_name)
