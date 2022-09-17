import requests
import random
import time
from concurrent.futures.thread import ThreadPoolExecutor

token_wx = ""
token_dy = ""

request_header = {
    "Host": "cat-match.easygame2021.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33",
    "t": token_wx
}

rank_stage_info = "https://cat-match.easygame2021.com/sheep/v1/game/rank_stage_info?"
map_api = "https://cat-match.easygame2021.com/sheep/v1/game/map_info?map_id=%s"
finish_sheep = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_role=1&skin=%s&rank_time=%s"
finish_topic = "https://cat-match.easygame2021.com/sheep/v1/game/topic_game_over?rank_score=1&rank_state=1&rank_role=2&skin=%s&rank_time=%s"


def finish():
    i = 1
    while True:
        print("闯关开始" + str(i))
        i += 1
        while True:
            try:
                res = requests.get(finish_sheep % (1, random.randint(1, 3600)), headers=request_header, timeout=10,
                                   verify=True)
                if res.json()["err_code"] == 0:
                    print("成功")
                else:
                    print(res.json() + "失败")
                break
            except Exception as e:
                print("TIME OUT")
                pass
        time.sleep(random.uniform(1, 2))
        while True:
            try:
                res = requests.get(finish_topic % (1, random.randint(1, 3600)), headers=request_header, timeout=10,
                                   verify=True)
                if res.json()["err_code"] == 0:
                    print("成功")
                else:
                    print(res.json() + "失败")
                break
            except Exception as e:
                print("TIME OUT")
                pass
        time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    with ThreadPoolExecutor(16) as e:
        e.submit(finish())
