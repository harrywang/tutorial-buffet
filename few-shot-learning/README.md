## About

This is my revised code of the tutorial at: https://medium.com/@barnrang/re-implementation-of-the-prototypical-network-for-few-shot-learning-using-tensorflow-2-0-keras-b2adac8e49e0

The related paper is: Jake Snell and Kevin Swersky and Richard S. Zemel (2017). Prototypical Networks for Few-shot LearningCoRR, abs/1703.05175. https://arxiv.org/abs/1703.05175
## Setup

Setup virtual environment and install packages

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Then, you can use `jupyter notebook` or use VSCode `code .` to open the notebooks.

## Prepare Datasets
Download dataset at https://drive.google.com/file/d/1UQEdAv4g_Mh2t15YtorNHkoHfQZJfmoE/view?usp=sharing

For omniglot dataset:

```
cd datasets/omniglot
mkdir data
unzip images_background.zip -d data/
unzip images_evaluation.zip -d data/
mv data/images_evaluation/* data/images_background/
python dataloader_omniglot.py
```

Note that we split (1200 * 4(rotate 4 direction)) classes for training and the rest for the test set. The dataset will be collected into a numpy file .npy

## Train and Test

To train:

In the root folder of this repo, run `python train_omniglot.py` to train 2 epochs by default (about 10 minutes on MacBook Pro). 

You can use different arguments:

- `python train_omniglot.py --epoch 100`
- `python train_omniglot.py --train_way 60 --train_query 5 --val_way 20 --shot 1 --gpu 0[for specify the gpu]`

temp checkpoints (with the format `omniglot_conv_{epoch}_{shot}_{val_way}`) and the final model `omniglot_conv` are saved in the `/model` folder (ignored by git)

Show training visualization using Tensorboard, run `tensorboard --logdir=./logs --port=6006`

Then, you can access TensorBoard at http://localhost:6006/

<img width="729" alt="Screen Shot 2020-09-28 at 4 35 40 PM" src="https://user-images.githubusercontent.com/595772/94483335-b2c01b80-01a8-11eb-852c-b204fca31a10.png">

To test: 

`python test_omniglot.py --model model/omniglot_conv --shot 1 --test_way 20`


