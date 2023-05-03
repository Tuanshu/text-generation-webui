python download-model.py mayaeary/pygmalion-6b-4bit-128g
python3 gptj.py models/pygmalion-6b_b8344bb4eb76a437797ad3b19420a13922aaabe1 c4 --wbits 4 --groupsize 128 --save_safetensors models/pygmalion-6b-4bit-128g.safetensors

python server.py --chat --wbits 4 --groupsize 128 --cpu

https://github.com/oobabooga/text-generation-webui/wiki/LLaMA-model

https://huggingface.co/anon8231489123/gpt4-x-alpaca-13b-native-4bit-128g/discussions/6

https://github.com/qwopqwop200/GPTQ-for-LLaMa/issues/161


cpp complier, try this
https://hackmd.io/@liaojason2/vscodecppwindows
https://code.visualstudio.com/docs/cpp/config-mingw 



https://github.com/oobabooga/text-generation-webui/wiki/llama.cpp-models

pip install -r requirements.txt -U


https://pytorch.org/tutorials/advanced/cpp_extension.html


nvidia_cublas_cu11-11.10.3.66-py3-none-manylinux1_x86_64.whl
nvidia_cudnn_cu11-8.5.0.96-2-py3-none-manylinux1_x86_64.whl

https://files.pythonhosted.org/packages/dc/30/66d4347d6e864334da5bb1c7571305e501dcb11b9155971421bb7bb5315f/nvidia_cudnn_cu11-8.5.0.96-2-py3-none-manylinux1_x86_64.whl#sha256=402f40adfc6f418f9dae9ab402e773cfed9beae52333f6d86ae3107a1b9527e7
https://files.pythonhosted.org/packages/dc/30/66d4347d6e864334da5bb1c7571305e501dcb11b9155971421bb7bb5315f/nvidia_cudnn_cu11-8.5.0.96-2-py3-none-manylinux1_x86_64.whl