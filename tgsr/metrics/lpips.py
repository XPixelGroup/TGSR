import cv2
import glob
import numpy as np
import os.path as osp
from torchvision.transforms.functional import normalize
from basicsr.utils.registry import METRIC_REGISTRY
from basicsr.utils import img2tensor

try:
    import lpips
except ImportError:
    print('Please install lpips: pip install lpips')

@METRIC_REGISTRY.register()
def calculate_lpips(img, img2, crop_border, input_order='HWC', convert_to='y', **kwargs):

    loss_fn_vgg = lpips.LPIPS(net='vgg').cuda()  # RGB, normalized to [-1,1]
    mean = [0.5, 0.5, 0.5]
    std = [0.5, 0.5, 0.5]

    img_restored  = img.astype(np.float32) / 255.
    img_gt = img2.astype(np.float32) / 255.

    img_gt, img_restored = img2tensor([img_gt, img_restored], bgr2rgb=True, float32=True)
    # norm to [-1, 1]
    normalize(img_gt, mean, std, inplace=True)
    normalize(img_restored, mean, std, inplace=True)

    # calculate lpips
    lpips_val = loss_fn_vgg(img_restored.unsqueeze(0).cuda(), img_gt.unsqueeze(0).cuda())
    lpips_val = lpips_val.item()

    return lpips_val
