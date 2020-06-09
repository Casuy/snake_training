from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
from nets.ssd import SSD300
from nets.ssd_training import MultiboxLoss,Generator
from utils.utils import BBoxUtility
from utils.anchors import get_anchors
from tensorflow.keras.optimizers import Adam
import numpy as np
if __name__ == "__main__":
    log_dir = "logs/"
    annotation_path = 'train_data/ssd_train.txt'
    
    NUM_CLASSES = 12 # 11+1
    input_shape = (300, 300, 3)
    priors = get_anchors()
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
    model.load_weights('logs/ep035-loss3.218-val_loss3.121.h5', by_name=True, skip_mismatch=True)

    # 训练参数设置
    logging = TensorBoard()
    checkpoint = ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5',
        monitor='val_loss', save_weights_only=True, save_best_only=True, period=1)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, verbose=1)
    early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1)

    BATCH_SIZE = 8
    gen = Generator(bbox_util, BATCH_SIZE, lines[:num_train], lines[num_train:],
                    (input_shape[0], input_shape[1]),NUM_CLASSES)

    
    for i in range(81):
        model.layers[i].trainable = False
    if False:
        model.compile(optimizer=Adam(lr=1e-4, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0),
                        loss=MultiboxLoss(NUM_CLASSES, neg_pos_ratio=3.0).compute_loss)
        model.fit_generator(gen.generate(True), 
                steps_per_epoch=num_train//BATCH_SIZE/2,
                validation_data=gen.generate(False),
                validation_steps=num_val//BATCH_SIZE,
                epochs=25, 
                initial_epoch=0,
                callbacks=[logging, checkpoint, reduce_lr, early_stopping])

    for i in range(81):
        model.layers[i].trainable = True
    BATCH_SIZE = 4
    if True:
        model.compile(optimizer=Adam(lr=1e-3, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0),loss=MultiboxLoss(NUM_CLASSES, neg_pos_ratio=3.0).compute_loss)
        # model.compile(optimizer=SGD(lr=1e-4,momentum=0.9,decay=5e-4),loss=MultiboxLoss(NUM_CLASSES, neg_pos_ratio=3.0).compute_loss)
        model.fit_generator(gen.generate(True), 
                steps_per_epoch=num_train//BATCH_SIZE,
                validation_data=gen.generate(False),
                validation_steps=num_val//BATCH_SIZE,
                epochs=250,
                initial_epoch=35,
                callbacks=[logging, checkpoint, reduce_lr, early_stopping])
