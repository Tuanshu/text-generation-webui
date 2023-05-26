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
        "max_new_tokens": 512,  # 512
        "do_sample": True,  # True
        "temperature": 0.7,  # 1.3 0.1
        "top_p": 0.5,  # 0.1        # 如果 1
        "typical_p": 1,
        "repetition_penalty": 1.1,  # 1.1
        "top_k": 40,  # 40               2
        "min_length": 0,
        "no_repeat_ngram_size": 0,
        "num_beams": 1,
        "penalty_alpha": 0,
        "length_penalty": 1,  # 1
        "early_stopping": False,
        "seed": 17,  # -1
        "add_bos_token": True,  # True
        "truncation_length": 2048,
        "ban_eos_token": False,
        "skip_special_tokens": True,  # True
        "stopping_strings": ["禁止事項"],
        # try add
        "preset_menu": "Default",
        "name1": "User",
        "name2": "Assistant",
        "greeting": "",
        "context": "Transcript of a dialog, where the User interacts with an Assistant. Assistant is kind, honest, and never fails to answer the User's requests immediately.",
        "turn_template": "",
        "chat_prompt_size": 2048,
        "chat_generation_attempts": 1,
        "stop_at_newline": False,
        "mode": "cai-chat",
        "instruction_template": "None",
        "character_menu": "None",
        "cpu_memory": 0,
        "auto_devices": True,
        "disk": False,
        "cpu": False,
        "bf16": False,
        "load_in_8bit": False,
        "wbits": "None",
        "groupsize": "None",
        "model_type": "None",
        "pre_layer": 0,
        "gpu_memory_0": 20000,
        "gpu_memory_1": 20000,
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
    prompt = """Transcript of a dialog, where the User interacts with an Assistant. Assistant is kind, honest, and never fails to answer the User's requests immediately.
User: [A context]: 越南商務簽類型與費用  普通件4天  急件2天(10:00前送抵旅行社)  越南簽證申請的種類（效期⾧短／ 單次簽／多次簽…等），是依據越 南政府批文的 內容，辦理簽證效期  辦理越南入境批文 12-15天，急件 加費70萬VND。(天數請洽水玲)  越南人資－黎氏水玲通知，目前外 幹都申請三個月多次簽，每次入境 不可超過30天，㇐年可入境3次

[B context]: 越南商務簽需備資料 1)越南政府批文(取得商務簽證批文後才能辦理簽證) 2)護照影本(半年以上效期) 3)二吋照片㇐張 以上可提供電子檔，批文及護照請1:1比例。  越南簽證辦理窗口： 顏妏君 分機510-10148 hana.wj.yen@foxconn.com  越南入境批文辦理窗口： 黎氏水玲 分機535-26574 Leasa.lee88@gmail.com 填寫以下二個表單，發Mail給水玲辦理，辦理批文約12-15天。  外籍人士申辦DN簽證批文之個人資料表  入境登记表

[C context]: 越南出差申請流程 員工填寫 國外出差單 主管/經管/人資 /總經理核准 員工辦理簽證/ 行政中心出票 會計/財務入帳 至員工薪資帳戶 主管/經管 /總經理 核准 員工填寫國外銷差單 出差結束返台後 【出差/銷差申請作業流程】 1) 出差人於出差前登入『集團員工差旅暨費用報銷系統』申請『國外出差申請表』。 2) 部門主管審核工 作目標、行程安排、拜訪對象、事前連繫及預期成果等作仔細初核。 3) 若出差當地設有事業群之事業單位時，則須會簽出差當地之部門主管。 4) 會知各單位行政部門辦理出國等手續。 5) 國外出差申請表逐級完成簽核後，由行政中心購買機票。 6) 出差完成返國十日內，登入『集團員工差旅暨費用報銷系統』提出『國外銷差申請表』提請各級 直屬主管審核。 7) 經管主 管審核出差費用報支之內容單據。 8) 銷差單經權限主管核准後，系統會自動轉送會計/財務入帳至員工薪資帳戶。

User: 請排序上述文本與“What is the process of applying for a business trip to Vietnam?”之相關度, 由高至低
Assistant:"""

    prompt = """[AAA]: 越南商務簽類型與費用  普通件4天  急件2天(10:00前送抵旅行社)  越南簽證申請的種類（效期⾧短／ 單次簽／多次簽…等），是依據越 南政府批文的 內容，辦理簽證效期  辦理越南入境批文 12-15天，急件 加費70萬VND。(天數請洽水玲)  越南人資－黎氏水玲通知，目前外 幹都申請三個月多次簽，每次入境 不可超過30天，㇐年可入境3次

[BBB]: 越南出差申請流程 員工填寫 國外出差單 主管/經管/人資 /總經理核准 員工辦理簽證/ 行政中心出票 會計/財務入帳 至員工薪資帳戶 主管/經管 /總經理 核准 員工填寫國外銷差單 出差結束返台後 【出差/銷差申請作業流程】 1) 出差人於出差前登入『集團員工差旅暨費用報銷系統』申請『國外出差申請表』。 2) 部門主管審核工 作目標、行程安排、拜訪對象、事前連繫及預期成果等作仔細初核。 3) 若出差當地設有事業群之事業單位時，則須會簽出差當地之部門主管。 4) 會知各單位行政部門辦理出國等手續。 5) 國外出差申請表逐級完成簽核後，由行政中心購買機票。 6) 出差完成返國十日內，登入『集團員工差旅暨費用報銷系統』提出『國外銷差申請表』提請各級 直屬主管審核。 7) 經管主 管審核出差費用報支之內容單據。 8) 銷差單經權限主管核准後，系統會自動轉送會計/財務入帳至員工薪資帳戶。

[CCC]: 越南商務簽需備資料 1)越南政府批文(取得商務簽證批文後才能辦理簽證) 2)護照影本(半年以上效期) 3)二吋照片㇐張 以上可提供電子檔，批文及護照請1:1比例。  越南簽證辦理窗口： 顏妏君 分機510-10148 hana.wj.yen@foxconn.com  越南入境批文辦理窗口： 黎氏水玲 分機535-26574 Leasa.lee88@gmail.com 填寫以下二個表單，發Mail給水玲辦理，辦理批文約12-15天。  外籍人士申辦DN簽證批文之個人資料表  入境登记表

Input: What is the process of applying for a business trip to Vietnam?

User: Can you tell me which context below is the most relevant to the Input?

Assistant: Sure, the most relevant context to the Input is ["""

    prompt = """越南出差申請流程 員工填寫 國外出差單 主管/經管/人資 /總經理核准 員工辦理簽證/ 行政中心出票 會計/財務入帳 至員工薪資帳戶 主管/經管 /總經理核准 員工填寫 國外銷差單 出 差 結 束 返 台 後 【出差/銷差申請作業流程】 1) 出差人於出差前登入『集團員工差旅暨費用報銷系統』申請『國外出差申請表』。 2) 部門主 管審核工作目標、行程安排、拜訪對象、事前連繫及預期成果等作仔細初核。 3) 若出差當地設有事業群之事業單位時，則須會簽出差當地之部門主管。 4) 會知各單位行政部門辦理出國等手續。 5) 國外出差申請表逐級完成簽核後，由行政中心購買機票。 6) 出差完成返國十日內，登入『集團員工差旅暨費用報銷系統』提出『國外銷差申請表』提請各級 直屬主管審核。 7) 經管主管審核出差費用報支之內容單據。 8) 銷差單經權限主管核准後，系統會自動轉送會計/財務入帳至員工薪資帳戶。

越南商務簽類型與費用  普通件4天  急件2天(10:00前送抵旅行社)  越南簽證申請的種類（效期⾧短／ 單次簽／多次簽…等），是依據越 南政府批文的內容，辦理簽證效期  辦理越南入境批文 12-15天，急件 加費70萬VND。(天數請洽水玲)  越南人資－黎氏水玲通知，目前外 幹都申請三個月多次簽，每次入境 不可超過30天，㇐年可入境3次

越南商務簽需備資料 1)越南政府批文(取得商務簽證批文後才能辦理簽證) 2)護照影本(半年以上效期) 3)二吋照片㇐張 以上可提供電子檔，批文及護照請1:1比例。  越南簽證辦理窗口： 顏妏君 分機510-10148 hana.wj.yen@foxconn.com  越南入境批文辦理窗口： 黎氏水玲 分機535-26574 Leasa.lee88@gmail.com 填寫以下二個 表單，發Mail給水玲辦理，辦理批文約12-15天。  外籍人士申辦DN簽證批文之個人資料表  入境登记表


User: What is the process of applying for a business trip to Vietnam? Please translate the contexts above to answer my question in English.


Assistant:"""

    prompt = """越南商務簽類型與費用  普通件4天  急件2天(10:00前送抵旅行社)  越南簽證申請的種類（效期⾧短／ 單次簽／多次簽…等），是依據越 南政府批文的 內容，辦理簽證效期  辦理越南入境批文 12-15天，急件 加費70萬VND。(天數請洽水玲)  越南人資－黎氏水玲通知，目前外 幹都申請三個月多次簽，每次入境 不可超過30天，㇐年可入境3次

越南商務簽需備資料 1)越南政府批文(取得商務簽證批文後才能辦理簽證) 2)護照影本(半年以上效期) 3)二吋照片㇐張 以上可提供電子檔，批文及護照請1:1比例。  越南簽證辦理窗口： 顏妏君 分機510-10148 hana.wj.yen@foxconn.com  越南入境批文辦理窗口： 黎氏水玲 分機535-26574 Leasa.lee88@gmail.com 填寫以下二個表單，發Mail給水玲辦理，辦理批文約12-15天。  外籍人士申辦DN簽證批文之個人資料表  入境登记表

越南出差申請流程 員工填寫 國外出差單 主管/經管/人資 /總經理核准 員工辦理簽證/ 行政中心出票 會計/財務入帳 至員工薪資帳戶 主管/經管 /總經理 核准 員工填寫國外銷差單 出差結束返台後 【出差/銷差申請作業流程】 1) 出差人於出差前登入『集團員工差旅暨費用報銷系統』申請『國外出差申請表』。 2) 部門主管審核工 作目標、行程安排、拜訪對象、事前連繫及預期成果等作仔細初核。 3) 若出差當地設有事業群之事業單位時，則須會簽出差當地之部門主管。 4) 會知各單位行政部門辦理出國等手續。 5) 國外出差申請表逐級完成簽核後，由行政中心購買機票。 6) 出差完成返國十日內，登入『集團員工差旅暨費用報銷系統』提出『國外銷差申請表』提請各級 直屬主管審核。 7) 經管主 管審核出差費用報支之內容單據。 8) 銷差單經權限主管核准後，系統會自動轉送會計/財務入帳至員工薪資帳戶。


User: 請問越南出差申請流程為何?  請重整上述文本以回答我的問題


Assistant:"""

    asyncio.run(print_response_stream(prompt))

    # wizard, vicuna, stable     # wizard, vicuna, stable (似乎要### Human: ### Assistant: )
