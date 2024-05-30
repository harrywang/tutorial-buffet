import argparse
import os

from tensorflow.keras import callbacks as cb
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model, Model, save_model
from tensorflow.keras.layers import *

# import from custom modules
from loader_omniglot import DataGenerator
from model_omniglot import conv_net
from util.tensor_op import *
from util.loss import *

# command line argument parser
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train_way', dest='train_way', type=int, default=60)
    parser.add_argument('--train_query', dest='train_query', type=int, default=5)
    parser.add_argument('--val_way', dest='val_way', type=int, default=20)
    parser.add_argument('--shot', dest='shot', type=int, default=1)
    parser.add_argument('--gpu', dest='gpu', type=int, default=0)
    parser.add_argument('--epochs', dest='epochs', type=int, default=2)

    return parser.parse_args()

args = parser()
os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

# get values from the command line arguments
train_way = args.train_way
train_query = args.train_query
val_way = args.val_way
shot = args.shot
epochs = args.epochs

# specify model parameters
input_shape = (None, 28, 28, 1)
batch_size = 20
lr = 0.002

def scheduler(epoch):
    global lr
    if epoch % 100 == 0:
        lr /= 2
    return lr

class SaveConv(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        if epoch % 50 == 0:
            save_model(conv, f"model/omniglot_conv_{epoch}_{shot}_{val_way}")

if __name__ == "__main__":
    conv = conv_net()
    sample = Input(input_shape)
    conv_5d = TimeDistributed(conv)
    out_feature = conv_5d(sample)
    out_feature = Lambda(reduce_tensor)(out_feature)
    inp = Input(input_shape)
    map_feature = conv_5d(inp)
    map_feature = Lambda(reshape_query)(map_feature)
    # proto_dist is from util/loss.py
    pred = Lambda(proto_dist)([out_feature, map_feature]) #negative distance
    combine = Model([sample, inp], pred)

    optimizer = Adam(0.001)
    combine.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['categorical_accuracy'])

    train_loader = DataGenerator(way=train_way, query=train_query, shot=shot, num_batch=1000)
    val_loader = DataGenerator(data_type='val',way=val_way, shot=shot)

    (x,y), z = train_loader[0]
    print(x.shape, y.shape, z.shape)
    print(combine.summary())

    save_conv = SaveConv()
    reduce_lr = cb.ReduceLROnPlateau(monitor='val_loss', factor=0.4, patience=2, min_lr=1e-8)
    lr_sched = cb.LearningRateScheduler(scheduler)
    tensorboard = cb.TensorBoard()

    combine.fit_generator(
        train_loader, 
        epochs=epochs, 
        validation_data=val_loader, 
        use_multiprocessing=False, 
        workers=4, 
        shuffle=False, 
        callbacks=[save_conv, lr_sched, tensorboard]
        )

    save_model(conv, "model/omniglot_conv")
