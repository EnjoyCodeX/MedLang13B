<<<<<<< HEAD
version https://git-lfs.github.com/spec/v1
oid sha256:81e9a5c94e917c73d6625c125f5d7bc8180d355d99f1b956022cee828753e93b
size 874
=======
## 部署

1. 安装项目依赖环境

   `pip install -r requirements.txt`

2. 利用Hugging Face的Transformers模块推理

   ```python
   >>> import torch
   >>> from transformers import AutoModelForCausalLM, AutoTokenizer
   >>> from transformers.generation.utils import GenerationConfig
   >>> tokenizer = AutoTokenizer.from_pretrained("MedLang-13B文件地址", use_fast=False, trust_remote_code=True)
   >>> model = AutoModelForCausalLM.from_pretrained("MedLang-13B文件地址", device_map="auto", torch_dtype=torch.float16, trust_remote_code=True)
   >>> model.generation_config = GenerationConfig.from_pretrained("MedLang-13B文件地址")
   >>> messages = []
   >>> messages.append({"role": "user", "content": "我感觉自己颈椎非常不舒服，每天睡醒都会头痛"})
   >>> response = model.chat(tokenizer, messages)
   >>> print(response)
   ```

MedLang-13B SFT Data: https://drive.google.com/file/d/1lF95g_Mnl_uoU7svsYT-Ft5wNT68ARay/view?usp=drive_link
>>>>>>> cdf77237dbde4d726b04054648ecfe983fb177ad