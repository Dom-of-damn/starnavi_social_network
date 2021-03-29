# Social Network Backend

## Endpoints

- ``GET api/post/analytics/`` - post analytic with params: ``date_from`` and ``date_to``, format should be similar
  2020-20-20
- ``POST api/post/create/`` - create post with ``title`` and ``text`` keys
- ``GET api/post/list/`` - get all posts
- ``GET|POST api/post/feedback/`` - create post feedback with keys: ``post`` and ``text``, also you can get all
  feedbacks(without key) and get feedbacks for concrete post with key: ``post_id``.<br />
  **User can leave a feedback once for concrete post!**
  
- ``PUT|PATCH|DELETE api/post/feedback/<pk>/`` - implement put,patch,delete method for concrete feedback
- ``POST api/token/`` - login by token with ``email``and ``passowrd`` keys
- ``POST api/token/refresh/`` - refresh token with ``refresh`` key
- ``POST api/user/create/`` - create user with keys: ``password, email``

# Testing Bot

For run testing bot u should run testing_bot/main.py file,\
also you can change settings.json file for another settings for the bot.