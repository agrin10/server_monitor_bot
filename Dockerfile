FROM python:3.12-slim

# set workdirectory
WORKDIR /app

# copy requirements and install dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements.txt,target=/app/requirements.txt \
	python -m pip install pyuwsgi -r /app/requirements.txt
# copy project files 
COPY  . .

# Expose port if needed (not strictly necessary for Telegram bot)
EXPOSE 8000

# start the bot
CMD [ "python" , "main.py" ]