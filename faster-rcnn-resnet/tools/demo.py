#!/usr/bin/env python

# --------------------------------------------------------
# Faster R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""
Demo script showing detections in sample images.

See README.md for installation instructions before running.
"""

import sys
#sys.path.insert(0,"/home/student/objectDetection/caffe/python")
sys.path.insert(0,"/home/student/cmpe295-masters-project/faster-rcnn-resnet/py-faster-rcnn/caffe-fast-rcnn/python")
# sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import VideoFileClip

import matplotlib
import glob
import os
import warnings
import _init_paths
from fast_rcnn.config import cfg
from fast_rcnn.test import im_detect
from fast_rcnn.nms_wrapper import nms
from utils.timer import Timer
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe, os, sys, cv2
import argparse
import cv2
import time

CLASSES = ('__background__',
           'aeroplane', 'bicycle', 'bird', 'boat',
           'bottle', 'bus', 'car', 'cat', 'chair',
           'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor')

NETS = {'vgg16': ('VGG16',
                  'VGG16_faster_rcnn_final.caffemodel'),
        'zf': ('ZF',
                  'ZF_faster_rcnn_final.caffemodel'),
        }

default_net = None

def vis_detections(im, class_name, dets, thresh=0.5):
    """Draw detected bounding boxes."""
    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        return

    im = im[:, :, (2, 1, 0)]
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.imshow(im, aspect='equal')
    for i in inds:
        bbox = dets[i, :4]
        score = dets[i, -1]

        ax.add_patch(
            plt.Rectangle((bbox[0], bbox[1]),
                          bbox[2] - bbox[0],
                          bbox[3] - bbox[1], fill=False,
                          edgecolor='red', linewidth=3.5)
            )
        ax.text(bbox[0], bbox[1] - 2,
                '{:s} {:.3f}'.format(class_name, score),
                bbox=dict(facecolor='blue', alpha=0.5),
                fontsize=14, color='white')

    ax.set_title(('{} detections with '
                  'p({} | box) >= {:.1f}').format(class_name, class_name,
                                                  thresh),
                  fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.draw()

def demo(net, image_name):
    """Detect object classes in an image using pre-computed object proposals."""

    # Load the demo image
    img_name = os.path.basename(image_name)
    # im_file = image_name
    # im = cv2.imread(im_file)
    im_file = os.path.join(cfg.DATA_DIR, 'demo', image_name)
    im = cv2.imread(im_file)

    # Detect all object classes and regress object bounds
    timer = Timer()
    timer.tic()
    scores, boxes = im_detect(net, im)
    timer.toc()
    print ('Detection took {:.3f}s for '
           '{:d} object proposals').format(timer.total_time, boxes.shape[0])

    # Visualize detections for each class
    CONF_THRESH = 0.8
    NMS_THRESH = 0.3
    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1 # because we skipped background
        cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
        cls_scores = scores[:, cls_ind]
        dets = np.hstack((cls_boxes,
                          cls_scores[:, np.newaxis])).astype(np.float32)
        keep = nms(dets, NMS_THRESH)
        dets = dets[keep, :]
        # vis_detections(im, cls, dets, thresh=CONF_THRESH)
	"""
	op = vis_detections(im, cls, dets, img_name, thresh=CONF_THRESH)
        print 'Returned op value is {}'.format(op)
        if op is not None and "output-images" in op:
                print 'OUTPUT IMAGES IS INSIDE OP STRING'
                opVar = op
                op = op
        elif op == None:
                if opVar is not None:
                        op = opVar
                else:
                        op = im_file

        """

	font = cv2.FONT_HERSHEY_SIMPLEX
	# print 'class index is {}'.format(cls_ind)

	color = (0, 0, 255)	
	inds = np.where(dets[:, -1] >= CONF_THRESH)[0]
    	if len(inds) > 0:
	   for i in inds:
            	bbox = dets[i, :4]
            	score = dets[i, -1]
            	cv2.rectangle(im,(bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
            	cv2.putText(im,'{:s} {:.3f}'.format(cls, score),(bbox[0], (int)((bbox[1]- 2))), font, 0.5, (255,255,255), 1)

    """	
    # Display the resulting frame
    cv2.imshow('{:s}'.format(image_name),im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """

    # Write the resulting frame
    print 'Final image name is {}'.format(img_name)
    splitName = os.path.splitext(img_name)[0]
    # print (os.path.splitext(img_name)[0])
    # print splitName
    # cv2.imwrite('{:s}_output.jpg'.format(splitName), im)
    opDir = '/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/output-images/'
    cv2.imwrite(os.path.join(opDir, img_name), im)

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Faster R-CNN demo')
    parser.add_argument('--gpu', dest='gpu_id', help='GPU device id to use [0]',
                        default=0, type=int)
    parser.add_argument('--cpu', dest='cpu_mode',
                        help='Use CPU mode (overrides --gpu)',
                        action='store_true')
    parser.add_argument('--net', dest='demo_net', help='Network to use [vgg16]',
                        choices=NETS.keys(), default='vgg16')

    args = parser.parse_args()

    return args

def demoVideo(image):
    
    im = image
    # Detect all object classes and regress object bounds
    timer = Timer()
    timer.tic()
    scores, boxes = im_detect(default_net, im)
    timer.toc()
    print ('Detection took {:.3f}s for '
           '{:d} object proposals').format(timer.total_time, boxes.shape[0])

    # Visualize detections for each class
    CONF_THRESH = 0.8
    NMS_THRESH = 0.3
    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1 # because we skipped background
        cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
        cls_scores = scores[:, cls_ind]
        dets = np.hstack((cls_boxes,
                          cls_scores[:, np.newaxis])).astype(np.float32)
        keep = nms(dets, NMS_THRESH)
        dets = dets[keep, :]
	font = cv2.FONT_HERSHEY_SIMPLEX

	color = (0, 0, 255)	
	inds = np.where(dets[:, -1] >= CONF_THRESH)[0]
    	if len(inds) > 0:
	   for i in inds:
            	bbox = dets[i, :4]
            	score = dets[i, -1]
            	cv2.rectangle(im,(bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
                cv2.putText(im,'{:s} {:.3f}'.format(cls, score),(bbox[0], (int)((bbox[1]- 2))), font, 0.5, (255,255,255), 1)

    # opDir = '/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/output-images/'
    # cv2.imwrite(os.path.join(opDir, img_name), im)
    return im


if __name__ == '__main__':
    cfg.TEST.HAS_RPN = True  # Use RPN for proposals

    args = parse_args()

    prototxt = os.path.join(cfg.MODELS_DIR, NETS[args.demo_net][0],
                            'faster_rcnn_alt_opt', 'faster_rcnn_test.pt')
    caffemodel = os.path.join(cfg.DATA_DIR, 'faster_rcnn_models',
                              NETS[args.demo_net][1])

    if not os.path.isfile(caffemodel):
        raise IOError(('{:s} not found.\nDid you run ./data/script/'
                       'fetch_faster_rcnn_models.sh?').format(caffemodel))

    if args.cpu_mode:
        caffe.set_mode_cpu()
    else:
        caffe.set_mode_gpu()
        caffe.set_device(args.gpu_id)
        cfg.GPU_ID = args.gpu_id
    net = caffe.Net(prototxt, caffemodel, caffe.TEST)
    # default_net = net

    print '\n\nLoaded network {:s}'.format(caffemodel)

    # Warmup on a dummy image
    im = 128 * np.ones((300, 500, 3), dtype=np.uint8)
    for i in xrange(2):
        _, _= im_detect(net, im)

    im_dir = '/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/input-images/'
    im_dir += '/*'
    bsdr = glob.glob(im_dir)
   
    for im_name in bsdr:
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'Demo for {}'.format(im_name)
        print(matplotlib.backends.backend)
        demo(net, im_name)

    """
    ### Process video files as an input
    clip = VideoFileClip("/home/student/cmpe295-masters-project/faster-rcnn-resnet/data/demo/P1_example.mp4")

    start = time.time()
    # Transform video and perform image flip
    new_clip = clip.fl_image(demoVideo)

    # Write a video to a file
    new_clip.write_videofile("output-P1_example.mp4", audio=False)

    end = time.time()
    total_time = (end - start)

    clip_len = time.strftime("%H:%M:%S", time.gmtime(clip.duration))
    print((('Image transformations took {:.3f}s for '
            '{} long video').format(total_time, clip_len)))
    """
