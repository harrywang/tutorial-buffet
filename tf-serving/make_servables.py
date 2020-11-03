import tensorflow as tf
import tensorflow_hub as hub


class AddTwo(tf.Module):
    @tf.function(input_signature=[tf.TensorSpec(shape=[None, 3], dtype=tf.float32, name='x')])
    def add_two(self, x):
        return x + 2


class CustomMobileNet(tf.keras.Model):
    model_handler = "https://tfhub.dev/google/imagenet/mobilenet_v2_035_224/classification/4"
     
    def __init__(self):
        super(CustomMobileNet, self).__init__()
        self.model = hub.load(self.__class__.model_handler)
        self.labels = None

    @tf.function(input_signature=[tf.TensorSpec(shape=None, dtype=tf.string)])
    def call(self, input_img):
        def _preprocess(img_file):
            img_bytes = tf.reshape(img_file, [])
            img = tf.io.decode_jpeg(img_bytes, channels=3)
            img = tf.image.convert_image_dtype(img, tf.float32)
            return tf.image.resize(img, (224, 224))
 
        labels = tf.io.read_file(self.labels)
        labels = tf.strings.split(labels, sep='\n')
        img = _preprocess(input_img)[tf.newaxis,:]
        logits = self.model(img)
        get_class = lambda x: labels[tf.argmax(x)]
        class_text = tf.map_fn(get_class, logits, fn_output_signature=tf.string)
        return class_text # index of the class

# create a servable from a tf function
tf_func_servable = AddTwo()
tf.saved_model.save(tf_func_servable, "models/add_two/1")

# create a servable from a pre-trian model downloaded from tf hub
tf_model_servable = CustomMobileNet()
tf_model_servable.labels = tf.saved_model.Asset("data/ImageNetLabels.txt") # save lables txt as an asset
tf.saved_model.save(tf_model_servable, "models/mobilenet_v2_test/1/")
