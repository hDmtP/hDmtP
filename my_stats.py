from github_contributions import GithubUser
from datetime import datetime, date
import pytz
from quotes import *

tz_NY = pytz.timezone('Asia/Kolkata')
datetime_NY = datetime.now(tz_NY)

user = GithubUser('hdmtp')
contribs = user.contributions()

contribs_2021 = user.contributions(
    start_date=str(date.today()), end_date=str(date.today()))

sc = '''
<h2 align="center">Hello there<img src="https://user-images.githubusercontent.com/88626025/135751180-b3d128a5-ba6f-496d-a6d0-1503b568ee88.gif" width="30px"></h2>

![Tests](https://github.com/hdmtp/hdmtp/actions/workflows/main.yml/badge.svg)
<h3 align="center" margin=30px>
''' + f"\"{choice()}\"" + '''
</h3>
<br>
<br>
<br>
<p align="center">
<img src="https://user-images.githubusercontent.com/65482473/137200814-7c1f94cc-d38b-4ec1-a93f-4b16c8768256.gif" align="center">
</p>

<hr>

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=hDmtP&langs_count=12)](https://github.com/hDmtP/github-readme-stats)

<h2> Visitor count 👀</h2>

<p><img src="https://profile-counter.glitch.me/{hdmtp}/count.svg" alt="hdmtp :: Visitor's Count" /></p>

<br>

![My GitHub stats](https://github-readme-stats.vercel.app/api?username=hdmtp&show_icons=true&theme=radical) 

<hr>

Time last updated      | Contributions Today
:--------------:|:----------------:
''' + f"**{datetime_NY}** | **{sum([day.count for day in contribs_2021.days])}**"

f = open("README.md", "w")
f.write(sc)
f.close()
