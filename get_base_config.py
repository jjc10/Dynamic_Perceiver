class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def get_args(EPOCH, BATCH_SIZE, OUTPUT_DIR,JEIDNN, CE_IC):
    args = Namespace(batch_size=BATCH_SIZE, 
    epochs=EPOCH,
    update_freq=1, 
    model='mobilenetV3_0x75_perceiver_t128', 
    classifier_type='cnn', 
    drop_path=0, 
    dropout=0, 
    input_size=224, 
    num_latent_channels=None, 
    SA_widening_factor=4, 
    num_SA_heads=None, 
    depth_factor=[1, 1, 1, 3], 
    spatial_reduction=True, 
    with_last_CA=True, 
    with_x2z=True, 
    with_z2x=True, 
    with_dwc=True, 
    with_isc=True, 
    with_kd=True, 
    T_kd=1.0, 
    alpha_kd=0.5, 
    layer_scale_init_value=1e-06, 
    model_ema=True, 
    model_ema_decay=0.9999, 
    model_ema_force_cpu=False, 
    model_ema_eval=True, 
    opt='adamw', 
    opt_eps=1e-08, 
    opt_betas=None, 
    clip_grad=None, 
    momentum=0.9, 
    weight_decay=0.05, 
    weight_decay_end=None, 
    lr=0.001, 
    layer_decay=1.0, 
    min_lr=1e-06, 
    warmup_epochs=0, 
    warmup_steps=-1, 
    loss_cnn_factor=1.0, 
    loss_att_factor=0.5, 
    loss_merge_factor=1.0, 
    color_jitter=0.4, 
    aa='rand-m9-mstd0.5-inc1', 
    smoothing=0.1, 
    train_interpolation='bicubic', 
    crop_pct=None, 
    reprob=0.25, 
    remode='pixel', 
    recount=1, 
    resplit=False, 
    mixup=0.8, 
    cutmix=1.0, 
    cutmix_minmax=None, 
    mixup_prob=1.0, 
    mixup_switch_prob=0.5, 
    mixup_mode='batch', 
    finetune='', 
    head_init_scale=1.0, 
    model_key='model|module|state_dict_ema', 
    model_prefix='', 
    data_path='/workspace/DyLLM/dynn/data/ILSVRC/Data/CLS-LOC', 
    eval_data_path=None, 
    nb_classes=1000, 
    imagenet_default_mean_and_std=True, 
    data_set='IMNET', 
    output_dir=OUTPUT_DIR, 
    log_dir=None, 
    device='cuda', 
    seed=0, 
    resume='', 
    auto_resume=True, 
    save_ckpt=True, 
    save_ckpt_freq=1, 
    save_ckpt_num=3, 
    start_epoch=0, 
    eval=False, 
    dist_eval=True, 
    disable_eval=False, 
    num_workers=10, 
    pin_mem=True, 
    world_size=1, 
    local_rank=-1, 
    dist_on_itp=False, 
    dist_url='env://', 
    use_amp=False, 
    enable_wandb=False, 
    project='convnext', 
    wandb_ckpt=False, 
    cka=False, 
    visualize=False, 
    jeidnn=JEIDNN , 
    ce_ic_tradeoff=CE_IC, 
    bilevel_epochs=5, 
    distributed=False)
    return args