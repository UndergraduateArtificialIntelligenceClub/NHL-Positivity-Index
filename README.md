# NHL-Positivity-Index

Inspired by Shannon Skanes' "Panic Index" series, we developed the NHL Positivity Index to quantitatively evaluate NHL fanbase sentiment using AI. Employing natural language processing and sentiment analysis, we analyze discussions and media commentary, primarily from Reddit, to gauge the mood and tone of fanbases over time.

Model Used: cardiffnlp/twitter-roberta-base-sentiment-latest from HuggingFace Models

The Team:
Jacob Winch, Statistics Student

Tanmay Munjal, Computer Science & Physics Student

Heiby Lau, Computer Science Student

Alexander Bradley, Computer Engineering Student

Arden Monaghan, Computer Science Student

Yukesh Subedi, Computer Science Student

William Luo, Electrical Nano-Engineering Student

## code

- `calc_positivity_score.py`: Calculates positivity scores for teams based on a dataset of the submissions.
- `chart_dashboard.py`: generates a visual dashboard using matplotlib to display these rankings, team logos, and positivity scores in a table format, complete with custom styling and additional informational text. The dashboard is displayed and saved as a PDF file
- `comment_preprocessing.py`: Using regular expressions to take out unwanted characters from all of the reddit comments from a specific time period.
- `constants.py`: All of the variables used between all of the different python files.
- `label_data.py`: The model labelling all of the data from the json file of comments within a specific time period with positive, negative, neutral ratings.
- `main.py`:
- `reddit_login.py`: Logging into the Reddit API to extract data.
- `reddit.py`: Extracting all of the Comments from Reddit under users u/HockeyMod, from Specific users posting Game Threads, and From Flaired Posts
- `utils.py`: Searches for and collect subreddit submissions based on post flairs.

## data

Contains all of the data for the comments in JSON format.

## data-nhllogos

Contains all of the images of nhl teams in pdf formatting.

## figures/dashboards

All of the NHL dashboards generated.

## Analyzing Models

## References

Skanes, S. [The Hockey Guy]. (n.d.). Panic Index [Playlist]. YouTube. Retrieved February 25, 2024, from https://www.youtube.com/playlist?list=PL4KmQCGTJmgz9urZusFDiGC9Bzh2S67gM

Envall, D., & Blåberg Kristoffersson, P. (2022). The buzz behind the stock market: Analysis and characterization of the social media activity around the time of big stock valuation changes.

Barbieri, F., Camacho-Collados, J., Espinosa-Anke, L., & Neves, L. (2020). TweetEval: Unified Benchmark and Comparative Evaluation for Tweet Classification. In Proceedings of Findings of EMNLP.

Nguyen, D. Q., Vu, T., & Nguyen, A. T. (2020). BERTweet: A pre-trained language model for English Tweets. arXiv preprint arXiv:2005.10200.
