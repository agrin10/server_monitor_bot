# Server Monitor Bot 🖥️

A Telegram bot that monitors your server's CPU, RAM, disk usage, and uptime, and sends real-time alerts to an admin when configurable thresholds are exceeded. Built with [aiogram](https://docs.aiogram.dev/), [psutil](https://github.com/giampaolo/psutil), and Redis.

## Features

- 📊 **`/status`** — On-demand snapshot of CPU, RAM, disk usage, and uptime
- 🚨 **Automatic alerts** — Background task checks resource usage on an interval and DMs the admin when CPU or RAM crosses a threshold
- ⚙️ **`/set_threshold`** — Update CPU/RAM alert thresholds on the fly, no restart needed
- 🧊 **Alert cooldown** — Uses Redis keys with expiry to avoid spamming repeat alerts
- 🔒 **Admin-only access** — Every command is restricted to a single authorized Telegram user ID
- 🌐 **Optional SOCKS proxy support** — Useful for reaching the Telegram API from restricted networks
- 🐳 **Docker-ready** — Ships with a `Dockerfile` and `docker-compose.yaml` (bot + Redis)

## How it works

The bot polls Telegram for commands via long polling and runs a background task (`monitor_system`) alongside it. That task checks CPU and RAM usage every `CHECK_INTERVAL` seconds, compares them against thresholds stored in Redis, and sends an alert message to the admin if a threshold is crossed — then sets a short-lived Redis key so it won't re-alert until the cooldown expires or usage drops back down.

## Project structure

```
server_monitor_bot/
├── main.py                      # Entry point: bot setup, routers, background task
├── bot/
│   ├── config.py                 # Loads settings from environment variables
│   ├── handlers/
│   │   ├── start.py               # /start
│   │   ├── status.py              # /status
│   │   └── set_threshold.py       # /set_threshold
│   ├── services/
│   │   ├── monitor.py             # Background monitoring loop + alerting
│   │   └── settings.py            # Thin wrapper around threshold settings
│   ├── database/
│   │   ├── redis_client.py        # Redis connection
│   │   └── settings_repo.py       # Read/write thresholds & alert cooldowns in Redis
│   └── utils/
│       └── system.py              # psutil helpers (CPU, RAM, disk, uptime)
├── requirements.txt
├── Dockerfile
└── docker-compose.yaml
```

## Requirements

- Python 3.12+ (or Docker)
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- Redis (used to store thresholds and alert cooldowns)

## Configuration

The bot is configured entirely through environment variables (loaded via `python-dotenv`). Create a `.env` file in the project root:

| Variable | Required | Default | Description |
|---|---|---|---|
| `BOT_TOKEN` | ✅ | — | Telegram bot token from BotFather |
| `ADMIN_ID` | ✅ | — | Your numeric Telegram user ID — the only account allowed to use the bot |
| `PROXY_URL` | ❌ | — | SOCKS proxy URL, if Telegram needs to be reached through a proxy |
| `CHECK_INTERVAL` | ❌ | `60` | Seconds between background resource checks |
| `CPU_ALERT_THRESHOLD` | ❌ | `80` | Initial CPU alert threshold (%) — can be changed later via `/set_threshold` |
| `MEMORY_ALERT_THRESHOLD` | ❌ | `80` | Initial RAM alert threshold (%) — can be changed later via `/set_threshold` |
| `REDIS_HOST` | ❌ | `localhost` | Redis host (set to `redis` when using Docker Compose) |
| `REDIS_PORT` | ❌ | `6379` | Redis port |

## Getting started

### Option 1: Docker Compose (recommended)

This spins up both the bot and a Redis container.

```bash
git clone https://github.com/agrin10/server_monitor_bot.git
cd server_monitor_bot
```

Create a `.env` file with at least `BOT_TOKEN` and `ADMIN_ID` set, then:

```bash
docker compose up -d --build
```

> **Note:** the bot container runs with `network_mode: host`, `pid: host`, and `privileged: true` in `docker-compose.yaml` so that `psutil` reports the **host machine's** resource usage rather than the container's. Adjust this if you're deploying somewhere that doesn't support host networking (e.g. most managed cloud platforms) — you'll need to rework it to monitor the container instead.

### Option 2: Run locally

```bash
git clone https://github.com/agrin10/server_monitor_bot.git
cd server_monitor_bot
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Make sure Redis is running locally (or point `REDIS_HOST`/`REDIS_PORT` at a remote instance), create your `.env` file, then:

```bash
python main.py
```

## Commands

| Command | Description |
| ---|---|
| `/start` | Shows a welcome message and available commands |
| `/status` | Returns current CPU, RAM, disk usage, and uptime |
| `/set_threshold cpu <value>` | Sets the CPU alert threshold (1–100) |
| `/set_threshold ram <value>` | Sets the RAM alert threshold (1–100) |

All commands are restricted to the Telegram user ID set as `ADMIN_ID`; anyone else receives an "unauthorized" reply.

## License

No license specified yet — add one if you plan to share or accept contributions.
