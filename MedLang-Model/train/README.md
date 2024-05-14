<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:9306e92812fd54c6d84cc6d39c371a9ec70838e6d52b551d9a23ab73a682f3e2
size 1724
=======
## SFT.json：train/train_args/dsconfig.json

如需加速，可添加`deepspeed`到配置文件中

- output_dir：训练输出目录，存储checkpiont、tokenizer、tensorboard等
- model_name_or_path：预训练的本地目录，或huggingface上的模型名称
- train_file：训练数据集路径。
- num_train_epochs：训练轮次。
- per_device_train_batch_size：每张显卡的batch size
- gradient_accumulation_steps：梯度累积步数。`global batch = num_gpus * per_device_train_batch_size * gradient_accumulation_steps`
- gradient_checkpointing：开启后模型不缓存激活状态，而进行两次forward计算，以节省显存。
- learning_rate：学习率。全量微调时，建议小，如1e-5。lora训练时，根据模型大小不同，建议设置为2e-4或1e-4。
- max_seq_length：训练时的最大长度。
- loogging_steps：每隔多少步打印一次train loss，结果打印到日志中，也保存在tensorboard中。
- save_steps：每隔多少步保存一次模型。
- save_total_limit：output_dir目录最多保存多少个checkpoint，超出会删除最旧的。
- lr_scheduler_type：学习率变化策略。
- warmup_steps：warm up步数。学习率经过多少步，增长到指定数值。
- optim：优化器。全量微调建议adamw_hf。qlora微调建议paged_adamw_32bit。
- seed：随机种子，用于复现实验结果。
- fp16：使用fp16混合精度。
- bf16：使用fp16混合精度。
- lora_rank：qlora矩阵的秩。一般设置为8、16、32、64等。在qlora论文中作者设为64。越大则参与训练的参数量越大。
- lora_alpha：qlora中的缩放参数。一般设为16、32即可。
- lora_dropout：lora权重中的dropout rate。

>>>>>>> cdf77237dbde4d726b04054648ecfe983fb177ad
