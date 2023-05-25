import asyncio
import json
import sys

try:
    import websockets
except ImportError:
    print("Websockets package not found. Make sure it's installed.")

# For local streaming, the websockets are hosted without ssl - ws://
HOST = "10.62.161.193:5005"
URI = f"ws://{HOST}/api/v1/stream"

# For reverse-proxied streaming, the remote will likely host with ssl - wss://
# URI = 'wss://your-uri-here.trycloudflare.com/api/v1/stream'


async def run(context):
    # Note: the selected defaults change from time to time.
    request = {
        "prompt": context,
        "max_new_tokens": 1024,  # 512
        "do_sample": True,  # True
        "temperature": 0.7,  # 1.3 0.1
        "top_p": 1,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1.18, # 1.1
        "top_k": 40,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": 17,  # -1
        "add_bos_token": True, #True
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": False, #True
        "stopping_strings": ["禁止事項"],
    }

    async with websockets.connect(URI, ping_interval=None) as websocket:
        await websocket.send(json.dumps(request))

        yield context  # Remove this if you just want to see the reply

        while True:
            incoming_data = await websocket.recv()
            incoming_data = json.loads(incoming_data)

            match incoming_data["event"]:
                case "text_stream":
                    yield incoming_data["text"]
                case "stream_end":
                    return


async def print_response_stream(prompt):
    async for response in run(prompt):
        print(response, end="")
        sys.stdout.flush()  # If we don't flush, we won't see tokens in realtime.


if __name__ == "__main__":
    prompt = """越
口
文約12-15天  外籍人士申辦DN簽證批文之個人資料表 入境登记表
User: what material should I prepare for a business trip to vietnam?
Assistant: """
    asyncio.run(print_response_stream(prompt))
