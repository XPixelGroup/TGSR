## TGSR: Real-world super-resolution as multi-task learning, NeurIPS 2023 [[Paper Link]](https://proceedings.neurips.cc/paper_files/paper/2023/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf) 

[Wenlong zhang](https://wenlongzhang0517.github.io/)<sup>1,2</sup>, [Xiaohui Li](https://github.com/xh9998)<sup>2,3</sup>, [Guangyuan Shi](https://scholar.google.com.hk/citations?user=fL_osukAAAAJ&hl=zh-CN)<sup>1</sup>, [Xiangyu Chen](https://chxy95.github.io/)<sup>2,4,5</sup>, [Yu Qiao](https://scholar.google.com.hk/citations?user=gFtI-8QAAAAJ&hl=zh-CN&oi=ao)<sup>2,5</sup>, [Xiaoyun Zhang](https://scholar.google.com.hk/citations?hl=zh-CN&user=0m0aIqsAAAAJ&view_op=list_works&sortby=pubdate)<sup>2</sup>, [Xiaoming Wu](http://www4.comp.polyu.edu.hk/~csxmwu/)<sup>1</sup> and [Chao Dong](https://scholar.google.com.hk/citations?user=OSDCB0UAAAAJ&hl=zh-CN)<sup>2,5</sup>

<sup>1</sup>The HongKong Polytechnic University
<sup>2</sup>Shanghai AI Laboratory
<sup>3</sup>Shanghai Jiao Tong University <br>
<sup>4</sup>University of Macau
<sup>5</sup>Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences



<!-- ## :new:Update

- **2024.0.07**: Repo is released. -->

<!-- ## :climbing:TODO
- [x] Release code and pretrained models:computer:. -->

## Environment
- [PyTorch >= 1.7](https://pytorch.org/)
- [BasicSR == 1.3.4.9](https://github.com/XPixelGroup/BasicSR/blob/master/INSTALL.md) 

```shell
cd TGSR
pip install -r requirements.txt
python setup.py develop
```


## How To Test


- Refer to `./options/test` for the configuration file of the model to be tested, and prepare the testing data and pretrained model.  
- The pretrained models are available at
[Google Drive](https://drive.google.com/drive/folders/1Q27_PvPFbEdJG3JglmsCUlMWGmC14FXQ?usp=sharing).
- Then run the following codes (taking `RealHATGAN-TG.pth` as an example):
```
python tgsr/test.py -opt options/test/HAT_SRx4_ImageNet-pretrain.yml
```
The testing results will be saved in the `./results` folder.  

- Refer to `./options/test/test_Real_HAT_GAN_TG.yml` for **inference** without the ground truth image.



## Citations
#### BibTeX

    @inproceedings{zhang2023real,
    title={Real-World Image Super-Resolution as Multi-Task Learning},
    author={Zhang, Wenlong and Li, Xiaohui and Guangyuan, SHI and Chen, Xiangyu and Qiao, Yu and Zhang, Xiaoyun and Wu, Xiao-Ming and Dong, Chao},
    booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
    year={2023}
    }