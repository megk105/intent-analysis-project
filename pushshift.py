import datetime as d
import pandas as pd
from psaw import PushshiftAPI

api = PushshiftAPI()

after_date = int(d.datetime(2022, 9, 18).timestamp())
before_date = int(d.datetime(2022, 11, 1).timestamp())

filtered_results = []

results = list(api.search_comments(after=after_date,
                            before=before_date,
                            subreddit='worldnews',
                            filter=['parent_id', 'body'],
                            limit=5000, 
                            sort="score:desc",
                            author="!automoderator",
                            q="-\"[removed]\""
                            )
                        )

for res in results:
    if ("t3_" in res.parent_id and "[deleted]" not in res.body):
        filtered_results.append(res.body)
    if (len(filtered_results) == 1000):
        break

print(len(filtered_results))
df = pd.DataFrame(filtered_results)
df.to_csv("results.csv", index=False, sep='|')