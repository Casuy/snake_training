import tensorflow as tf
from nets.ssd import SSD300
from nets.ssd_training import MultiboxLoss,Generator
from utils.utils import BBoxUtility
import numpy as np
import pickle
if __name__ == "__main__":
    log_dir = "logs/"
    annotation_path = 'train_data/ssd_train.txt'
    
    NUM_CLASSES = 12
    input_shape = (300, 300, 3)
    priors = pickle.load(open('model_data/prior_boxes_ssd300.pkl', 'rb'))
    bbox_util = BBoxUtility(NUM_CLASSES, priors)

    # 0.05用于验证，0.95用于训练
    val_split = 0.05
    with open(annotation_path) as f:
        lines = f.readlines()
    np.random.seed(10101)
    np.random.shuffle(lines)
    np.random.seed(None)
    num_val = int(len(lines)*val_split)
    num_train = len(lines) - num_val
    
    model = SSD300(input_shape, num_classes=NUM_CLASSES)
    model.load_weights('logs/ep052-loss0.561-val_loss0.968.h5', by_name=True,skip_mismatch=True)
    # 训练参数设置
    logging = tf.keras.callbacks.TensorBoard()
    checkpoint = tf.keras.callbacks.ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5',
        monitor='loss', save_weights_only=True, save_best_only=True, period=1)
    reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='loss', factor=0.5, patience=2, verbose=1)
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='loss', min_delta=0, patience=16, verbose=1)

    BATCH_SIZE = 12
    gen = Generator(bbox_util, BATCH_SIZE, lines[:num_train], lines[num_train:],
                    (input_shape[0], input_shape[1]),NUM_CLASSES, do_crop=True)

    if False:
        model.compile(optimizer=tf.keras.optimizers.Adam(lr=1e-4),loss=MultiboxLoss(NUM_CLASSES, neg_pos_ratio=5.0).compute_loss)
        model.fit_generator(gen.generate(True), 
                steps_per_epoch=num_train//BATCH_SIZE,
                validation_data=gen.generate(False),
                validation_steps=num_val//BATCH_SIZE,
                epochs=20,
                initial_epoch=0,
                callbacks=[logging, checkpoint, reduce_lr, early_stopping])

    if True:
        model.compile(optimizer=tf.keras.optimizers.Adamax(lr=1e-5),loss=MultiboxLoss(NUM_CLASSES, neg_pos_ratio=3.0).compute_loss)
        model.fit_generator(gen.generate(True), 
                steps_per_epoch=num_train//BATCH_SIZE,
                validation_data=gen.generate(False),
                validation_steps=num_val//BATCH_SIZE,
                epochs=250,
                initial_epoch=52,
                callbacks=[logging, checkpoint, reduce_lr, early_stopping])