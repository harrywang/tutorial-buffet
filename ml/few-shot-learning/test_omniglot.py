import argparse
import os

from tensorflow.keras import callbacks as cb
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model, Model, save_model
from tensorflow.keras.layers import *

from loader_omniglot import DataGenerator
from model_omniglot import conv_net
from util.tensor_op import *
from util.loss import *


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_way', dest='test_way', type=int, default=5)
    parser.add_argument('--shot', dest='shot', type=int, default=1)
    parser.add_argument('--gpu', dest='gpu', type=int, default=0)
    parser.add_argument('--model', dest='model')

    return parser.parse_args()

args = parser()
os.environ["CUDA_VISIBLE_DEVICES"]=str(args.gpu)
test_way = args.test_way
shot = args.shot
model_path = args.model

input_shape = (None, 28, 28, 1)
batch_size = 20
lr = 0.002


def scheduler(epoch):
    global lr
    if epoch % 15 == 0:
        lr /= 2
    return lr


class SaveConv(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if epoch % 5 == 0:
            save_model(conv, f"model/omniglot_conv_{epoch}_{shot}_{val_way}")


if __name__ == "__main__":
    conv = load_model(model_path)
    sample = Input(input_shape)
    conv_5d = TimeDistributed(conv)
    out_feature = conv_5d(sample)
    out_feature = Lambda(reduce_tensor)(out_feature)
    inp = Input(input_shape)
    map_feature = conv_5d(inp)
    map_feature = Lambda(reshape_query)(map_feature)
    pred = Lambda(proto_dist)([out_feature, map_feature]) #negative distance
    combine = Model([sample, inp], pred)

    optimizer = Adam(0.001)
    combine.compile(loss='categorical_crossentropy', optimizer=optimizer,
        metrics=['categorical_accuracy'])
    test_loader = DataGenerator(data_type='test', way=test_way, shot=shot, num_batch=10000)

    combine.evaluate(test_loader)