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