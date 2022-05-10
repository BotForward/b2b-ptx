# (c) @AbirHasan2005

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("18446044"))
    API_HASH = os.environ.get("c1b4b6c77841e456c50520e990460d94")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("1ApWapzMBuxhmORBeJSOPiawVupfg0sFCPkj4VCRmYVh8EWIl6gY1V0tWQjP4pqMy_uiTz5vfiBSYUzqZ4mqUDl4JtTt0Sml9LBQIVyGcFTfbA3o61BzGW41jORPYBa3JdGpd0inKny7FD_lWZYVi7wt1JGgReqa0iSQ0r6Rq8AcvPFIeMJNw5ABcq_WWDYQKp6pVQHEJ-kmmZYpZRo0WmKQqNfS8MKRwbgs8Ws8FFgEFzZ9CzFmTZL3-0rl-3Y5L9zwegEUiUHC9tJO4lADAtZ3SjQY5RxS5f5aIMK7ExpltfZwlsfHGTxI7wbqHQ2L4p1dXdvR1XhVkat_jUyLQTQD8BK5wXRI=")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("5307340432 ", "-100").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("5379943214", "-100").split()))
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("f0fe9ede-79ce-478d-aea9-298a21953b95")
    HEROKU_APP_NAME = os.environ.get("b2b-forward-peyzen")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
