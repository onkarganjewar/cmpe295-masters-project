import lane_detect
reload(lane_detect)
from lane_detect import process_image
import os
import cv2
import imutils
from skimage import io
from moviepy.editor import VideoFileClip


folder_name = '/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/input/'
folder_name_res = '/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/output/'
t_images = os.listdir(folder_name)
    
for d in range(len(t_images)):
    # if "00" not in t_images[d]:
    img = io.imread(folder_name+t_images[d])
    pimg = process_image(img)                      # processed image	

    ## Show output frame
    # cv2.imshow("output", pimg)
    # cv2.waitKey(0)
    # plt.show()

    cv2.imwrite(os.path.join(folder_name_res, 'processesd_'+ t_images[d]), pimg)
    print (folder_name_res + 'processed_'+ t_images[d])
