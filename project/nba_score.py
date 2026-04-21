import warnings
from pprint import PrettyPrinter

import requests
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings (CDN works with SSL verification, but just in case)
warnings.filterwarnings("ignore", category=InsecureRequestWarning)

# Headers to mimic a real browser (some endpoints require this)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
}

# CDN base URL - live NBA data endpoint (public, no auth required)
BASE_URL = "https://cdn.nba.com"
SCOREBOARD_ENDPOINT = "/static/json/liveData/scoreboard/todaysScoreboard_00.json"

printer = PrettyPrinter()


def get_scoreboard():
    """
    Fetch and display today's NBA scoreboard.
    Uses the live CDN endpoint which returns real-time game data.
    """
    try:
        response = requests.get(BASE_URL + SCOREBOARD_ENDPOINT, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()

        games = data["scoreboard"]["games"]
        if not games:
            print("No games scheduled for today.")
            return

        for game in games:
            home = game["homeTeam"]
            away = game["awayTeam"]
            game_clock = game.get("gameClock", "")
            period = game.get("period", "")

            print("------------------------------------------")
            print(f"{home['teamTricode']} vs {away['teamTricode']}")
            print(f"{home['score']} - {away['score']}")
            if game_clock:
                print(f"{game_clock} - Period {period}")
            else:
                print(f"Period {period}")

    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching scoreboard: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error parsing scoreboard data: {e}")


def get_stats():
    """
    League team stats leaders.
    NOTE: The original endpoint (data.nba.net/leagueTeamStatsLeaders) is deprecated.
    The NBA now requires API keys or uses different endpoints (stats.nba.com) that are
    behind bot protection. As a learning example, we show a placeholder.
    """
    print("=" * 45)
    print("Stats endpoint is no longer publicly available.")
    print("Options to restore functionality:")
    print("1. Use SportsDataAPI (requires API key)")
    print("2. Use stats.nba.com with advanced headers (may still block)")
    print("3. Use a local dataset/CSV for demonstration")
    print("=" * 45)


if __name__ == "__main__":
    print("NBA Live Scoreboard")
    print("=" * 42)
    get_scoreboard()
    print()
    get_stats()
