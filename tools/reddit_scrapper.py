from dotenv import dotenv_values
import praw
import prawcore


def reddit_scrapper(input_list):
    """
    Scrapes given subreddit's today's top posts for a number of posts.

    Parameters:
    input_list (list): A list containing the name of the subreddit and the number of tweets to scrape.
        - The first element is the name of the subreddit.
        - The second element is the number of posts to scrape.

        Example format: ["cats", "5"]

    Returns:
    (str): The formatted weather or an error message if something goes wrong.

    Raises:
    praw.exceptions.PRAWException: For general PRAW-related errors.
    prawcore.exceptions.RequestException: If there is a network issue while making a request to Reddit.
    prawcore.exceptions.ResponseException: If Reddit returns an invalid response.
    prawcore.exceptions.ServerError: If Reddit's servers experience an issue (5xx errors).
    prawcore.exceptions.Forbidden: If access to the specified subreddit is forbidden.
    prawcore.exceptions.NotFound: If the specified subreddit does not exist.
    praw.exceptions.RedditAPIException: For API errors like rate limiting.
    ValueError: If the input list is incorrectly formatted.
    TypeError: If the input_list is not a list or contains incorrect types.
    AttributeError: If there's an issue accessing attributes or methods.
    """
    CONFIG = dotenv_values("config/.env")
    subreddit_name = input_list[0]
    num_posts = int(input_list[1])

    # Initialize Reddit instance
    reddit = praw.Reddit(
        client_id=CONFIG["CLIENT_ID"],
        client_secret=CONFIG["CLIENT_SECRET"],
        user_agent="Scrapper"
    )

    try:
        # Get the subreddit
        subreddit = reddit.subreddit(subreddit_name)
        top_posts = subreddit.top(limit=num_posts, time_filter="day")

        result = []
        for post in top_posts:
            result.append(
                f"Title: {post.title}\nScore: {post.score}\nBody: {post.selftext}")

        return "\n\n".join(result) + "\n"

    except Exception as e:
        return f"Error occurred: {e}"

