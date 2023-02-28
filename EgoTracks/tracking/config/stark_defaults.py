from fvcore.common.config import CfgNode


"""
Add default config for STARK-ST Stage2.
"""
cfg = CfgNode()
cfg.OUTPUT_DIR = None
cfg.SEED = -1
cfg.CUDNN_BENCHMARK = False
cfg.MODEL_TYPE = "STARK"

# MODEL
cfg.MODEL = CfgNode()
cfg.MODEL.HEAD_TYPE = "CORNER"
cfg.MODEL.NLAYER_HEAD = 3
cfg.MODEL.HIDDEN_DIM = 256
cfg.MODEL.NUM_OBJECT_QUERIES = 1
cfg.MODEL.POSITION_EMBEDDING = "sine"  # sine or learned
cfg.MODEL.PREDICT_MASK = False
cfg.MODEL.WEIGHTS = None
# MODEL.BACKBONE
cfg.MODEL.BACKBONE = CfgNode()
cfg.MODEL.BACKBONE.TYPE = "resnet50"  # resnet50, resnext101_32x8d
cfg.MODEL.BACKBONE.OUTPUT_LAYERS = ["layer3"]
cfg.MODEL.BACKBONE.STRIDE = 16
cfg.MODEL.BACKBONE.DILATION = False
# MODEL.TRANSFORMER
cfg.MODEL.TRANSFORMER = CfgNode()
cfg.MODEL.TRANSFORMER.NHEADS = 8
cfg.MODEL.TRANSFORMER.DROPOUT = 0.1
cfg.MODEL.TRANSFORMER.DIM_FEEDFORWARD = 2048
cfg.MODEL.TRANSFORMER.ENC_LAYERS = 6
cfg.MODEL.TRANSFORMER.DEC_LAYERS = 6
cfg.MODEL.TRANSFORMER.PRE_NORM = False
cfg.MODEL.TRANSFORMER.DIVIDE_NORM = False

# TRAIN
# General TRAIN config
TRAIN = CfgNode()
TRAIN.TRAIN_CLS = False
TRAIN.LR = 0.0001
TRAIN.WEIGHT_DECAY = 0.0001
TRAIN.EPOCH = 50
TRAIN.LR_DROP_EPOCH = 40
TRAIN.BATCH_SIZE = 16
TRAIN.NUM_WORKER = 8
TRAIN.OPTIMIZER = "ADAMW"
TRAIN.BACKBONE_MULTIPLIER = 0.1
TRAIN.DEEP_SUPERVISION = False
TRAIN.FREEZE_BACKBONE_BN = True
TRAIN.FREEZE_LAYERS = ["conv1", "layer1"]
TRAIN.PRINT_INTERVAL = 50
TRAIN.VAL_EPOCH_INTERVAL = 20
TRAIN.GRAD_CLIP_NORM = 0.1
TRAIN.CHECKPOINT_PERIOD = 10
# TRAIN.SCHEDULER
TRAIN.SCHEDULER = CfgNode()
TRAIN.SCHEDULER.TYPE = "step"
TRAIN.SCHEDULER.DECAY_RATE = 0.1
TRAIN.LOSS_FUNCTIONS = ["giou", "l1"]
TRAIN.LOSS_WEIGHTS = [2.0, 5.0]

cfg.TRAIN = TRAIN.clone()

cfg.TRAIN_STAGE_1 = TRAIN.clone()
cfg.TRAIN_STAGE_2 = TRAIN.clone()

cfg.TRAIN_STAGE_2.EPOCH = 10
cfg.TRAIN_STAGE_2.CHECKPOINT_PERIOD = 1
cfg.TRAIN_STAGE_2.TRAIN_CLS = True
cfg.TRAIN_STAGE_2.LOSS_FUNCTIONS = ["cls"]
cfg.TRAIN_STAGE_2.LOSS_WEIGHTS = [1.0]

# DATA
cfg.DATA = CfgNode()
cfg.DATA.SAMPLER_MODE = "trident_pro"  # sampling methods
cfg.DATA.MEAN = [0.485, 0.456, 0.406]
cfg.DATA.STD = [0.229, 0.224, 0.225]
cfg.DATA.MAX_SAMPLE_INTERVAL = [200]
# We fetch data from different manifold folders
cfg.DATA.COCO_DATA_DIR = "manifold://fair_vision_data/tree/"
cfg.DATA.TRACKINGNET_DATA_DIR = "manifold://tracking/tree/data/trackingnet"
cfg.DATA.CACHED_TRACKINGNET_SEQUENCE_LIST_DIR: str = (
    "manifold://tracking/tree/data/trackingnet/cache"
)
cfg.DATA.LASOT_DATA_DIR: str = "manifold://fai4ar/tree/datasets/LaSOTBenchmark"
cfg.DATA.GOT10K_DATA_DIR: str = "manifold://tracking/tree/data/got10k"
cfg.DATA.CACHED_GOT10K_META_INFO_DIR: str = "manifold://tracking/tree/data/got10k/cache"
cfg.DATA.EGO4DLTT_ANNOTATION_PATH = (
    "/checkpoint/haotang/data/EgoTracks/annotations/train_v1.json"
)
cfg.DATA.EGO4DLTT_DATA_DIR = "/checkpoint/haotang/data/EgoTracks/clips_frames"
cfg.DATA.DATA_FRACTION = None
# DATA.TRAIN
cfg.DATA.TRAIN = CfgNode()
cfg.DATA.TRAIN.DATASETS_NAME = ["LASOT", "GOT10K_vottrain", "COCO17", "TRACKINGNET"]
cfg.DATA.TRAIN.DATASETS_RATIO = [1, 1, 1, 1]
cfg.DATA.TRAIN.SAMPLE_PER_EPOCH = 60000
# DATA.VAL
cfg.DATA.VAL = CfgNode()
cfg.DATA.VAL.DATASETS_NAME = ["GOT10K_votval"]
cfg.DATA.VAL.DATASETS_RATIO = [1]
cfg.DATA.VAL.SAMPLE_PER_EPOCH = 10000
# DATA.SEARCH
cfg.DATA.SEARCH = CfgNode()
cfg.DATA.SEARCH.NUMBER = 1  # number of search frames for multiple frames training
cfg.DATA.SEARCH.SIZE = 320
cfg.DATA.SEARCH.FACTOR = 5.0
cfg.DATA.SEARCH.CENTER_JITTER = 4.5
cfg.DATA.SEARCH.SCALE_JITTER = 0.5
# DATA.TEMPLATE
cfg.DATA.TEMPLATE = CfgNode()
cfg.DATA.TEMPLATE.NUMBER = 2
cfg.DATA.TEMPLATE.SIZE = 128
cfg.DATA.TEMPLATE.FACTOR = 2.0
cfg.DATA.TEMPLATE.CENTER_JITTER = 0
cfg.DATA.TEMPLATE.SCALE_JITTER = 0

# TEST
cfg.TEST = CfgNode()
cfg.TEST.TEMPLATE_FACTOR = 2.0
cfg.TEST.TEMPLATE_SIZE = 128
cfg.TEST.SEARCH_SIZE = 320
cfg.TEST.SEARCH_FACTOR = 5.0
cfg.TEST.TEST_BATCHSIZE = 8
cfg.TEST.IS_SEARCH_LOCAL = True
cfg.TEST.UPDATE_INTERVALS = CfgNode()
# This attribute will be overwritten during evaluation,
# to correctly set the update_intervals for different datasets
cfg.TEST.UPDATE_INTERVALS.UPDATE_INTERVALS = [100]
cfg.TEST.UPDATE_INTERVALS.LASOT = [200]
cfg.TEST.UPDATE_INTERVALS.GOT10K = [200]
cfg.TEST.UPDATE_INTERVALS.GOT10K_TEST = [200]
cfg.TEST.UPDATE_INTERVALS.TRACKINGNET = [25]
cfg.TEST.UPDATE_INTERVALS.VOT20 = [10]
cfg.TEST.UPDATE_INTERVALS.VOT20LT = [200]
cfg.TEST.UPDATE_INTERVALS.EGO4DVQTracking = [1]
cfg.TEST.UPDATE_INTERVALS.EGO4DLTTracking = [30]

# Eval
cfg.EVAL = CfgNode()
cfg.EVAL.EVAL_DATASETS = ["EGO4DLTTracking"]
cfg.EVAL.OUTPUT_DIR = None
cfg.EVAL.NUM_WORKERS = 8
cfg.EVAL.PRINT_FREQ = 10
# Ego4D VQ dataset config
cfg.EVAL.EGO4DVQ = CfgNode()
cfg.EVAL.EGO4DVQ.ANNOTATION_PATH = (
    "manifold://tracking/tree/ego4d/v1/annotations/vq_val.json"
)
cfg.EVAL.EGO4DVQ.CLIP_DIR = "manifold://tracking/tree/ego4d/clip"
cfg.EVAL.EGO4DVQ.VIDEO_DIR = (
    "manifold://tracking/tree/ego4d/intermediate/canonical/v7/full_scale/canonical"
)
cfg.EVAL.EGO4DVQ.IS_READ_5FPS_CLIP = True
cfg.EVAL.EGO4DVQ.IS_SEARCH_LOCAL = True
cfg.EVAL.EGO4DVQ.TRACK_MODE = "first_bbox"
cfg.EVAL.EGO4DVQ.VISUALIZE = False
cfg.EVAL.EGO4DVQ.RETURN_5FPS_FRAMES = False

cfg.EVAL.GOT10K = CfgNode()
cfg.EVAL.GOT10K.VISUALIZE = False

# Ego4D Lt track dataset config
cfg.EVAL.EGO4DLT = CfgNode()
cfg.EVAL.EGO4DLT.ANNOTATION_PATH = (
    "/checkpoint/haotang/data/EgoTracks/annotations/challenge_test_v1_unannotated.json"
)
cfg.EVAL.EGO4DLT.DATA_DIR = "/checkpoint/haotang/data/EgoTracks/clips_frames"
cfg.EVAL.EGO4DLT.SAMPLE_5FPS = True
cfg.EVAL.EGO4DLT.TRACK_MODE = "forward_backward_from_vcrop"
cfg.EVAL.EGO4DLT.USE_VISUAL_CLIP = False
cfg.EVAL.EGO4DLT.EVAL_RATIO = 1.0
cfg.EVAL.EGO4DLT.PRE_DOWNLOAD = False
	
