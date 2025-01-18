# DFS Wrapper
A simple Python wrapper for DFS Books API to fetch player stats, leagues, and other game data.

## Installation
Install the package directly from PyPI:
pip install api-dfs-wrapper==0.3.0

## Usage

### Import PrizePick wrapper
from DFS_Wrapper import PrizePick

### Import Underdog Wrapper
from DFS_Wrapper import Underdog

### Initialize PrizePick wrapper
prizepick = PrizePick()

### Initialize Underdog wrapper
underdog = Underdog()

### Get PrizePick data
pp_data = prizepick.get_data()

### Get Underdog data
ud_data = underdog.get_data()

### Get PrizePick Leagues
pp_leagues = prizepick.get_leagues()

### Get Underdog Leagues
ud_leagues = underdog.get_leagues()


### Methods
get_data(organize_data): Fetches PrizePick data. If organize_data is set to true, 
this will return a dictionary of leagues with key being the league name. organize_data is defaulted to true.
If organize_data is fale, will return a list of all data, non-organized.[PrizePick Only]

get_data(): Fetches Underdog game data [Underdog Only]

get_leagues(): Returns a dictionary of leagues with their IDs. [PrizePick Only]

get_leagues(): Returns a set of leagues [Underdog Only]

### Example JSON Return for Prizepicks
```json
[
    {
        "player_id": "225032",
        "player_name": "Danielle Hunter",
        "is_live": false,
        "league": "NFL1H",
        "league_id": "35",
        "odds_type": "standard",
        "stat_type": "Sacks",
        "status": "pre_game",
        "team": "HOU",
        "opponent": "KC",
        "line_score": 0.13,
        "start_time": "2025-01-18T16:30:00-05:00"
    },
    {
        "player_id": "211159",
        "player_name": "Ka'imi Fairbairn",
        "is_live": false,
        "league": "NFL",
        "league_id": "9",
        "odds_type": "demon",
        "stat_type": "FG Made",
        "status": "pre_game",
        "team": "HOU",
        "opponent": "KC",
        "line_score": 2.5,
        "start_time": "2025-01-18T16:30:00-05:00"
    }
]
```
### Example JSON Return for Underdog
```
[
    {
        "player_name": "LaMelo Ball",
        "player_id": "b78ba991-272a-438e-81d6-901d66c7e09a",
        "sport_id": "NBA",
        "match_id": 85801,
        "match_type": "Game",
        "team_id": "11cfe154-8ba6-4c22-be8f-2365656fb4da",
        "stat_id": "872f2308-db67-41e8-95f0-1c20d4061b1b",
        "team": "CHA",
        "opponent": "CHI",
        "stats": [
            {
                "stat_type": "Points",
                "line_value": 30.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Pts + Rebs + Asts",
                "line_value": 45.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "1Q Points",
                "line_value": 7.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Assists",
                "line_value": 8.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Rebounds",
                "line_value": 5.5,
                "over_multiplier": 0.92,
                "under_multiplier": 1.07
            },
            {
                "stat_type": "1Q Pts + Rebs + Asts",
                "line_value": 12.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Pts+Reb+Ast in First 5 Min.",
                "line_value": 6.5,
                "over_multiplier": 1.04,
                "under_multiplier": 0.93
            },
            {
                "stat_type": "Points in First 5 Min.",
                "line_value": 4.5,
                "over_multiplier": 1.07,
                "under_multiplier": 0.91
            },
            {
                "stat_type": "Rebounds + Assists",
                "line_value": 14.5,
                "over_multiplier": 1.04,
                "under_multiplier": 0.94
            },
            {
                "stat_type": "1Q Rebounds",
                "line_value": 1.5,
                "over_multiplier": 1.05,
                "under_multiplier": 0.93
            },
            {
                "stat_type": "3-Pointers Made",
                "line_value": 4.5,
                "over_multiplier": 0.87,
                "under_multiplier": 1.12
            },
            {
                "stat_type": "1Q Assists",
                "line_value": 2.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Points + Rebounds",
                "line_value": 36.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Assists in First 5 min.",
                "line_value": 1.5,
                "over_multiplier": 1.62,
                "under_multiplier": 0.69
            },
            {
                "stat_type": "Points + Assists",
                "line_value": 39.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Double Doubles",
                "line_value": 0.5,
                "over_multiplier": 1.15,
                "under_multiplier": 0.85
            },
            {
                "stat_type": "1Q 3-Pointers Made",
                "line_value": 0.5,
                "over_multiplier": null,
                "under_multiplier": 2.14
            },
            {
                "stat_type": "Steals",
                "line_value": 1.5,
                "over_multiplier": 1.16,
                "under_multiplier": 0.83
            },
            {
                "stat_type": "1H Pts + Rebs + Asts",
                "line_value": 23.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "1H Assists",
                "line_value": 4.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "1H Points",
                "line_value": 16.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "1H 3-Pointers Made",
                "line_value": 2.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Fantasy Points",
                "line_value": 52.45,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "FT Made",
                "line_value": 5.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            },
            {
                "stat_type": "Turnovers",
                "line_value": 3.5,
                "over_multiplier": 1,
                "under_multiplier": 1
            }
        ]
    },
]
```

### Error Handling
Raises a custom RateLimit exception on status code 429 (rate-limited).

General exceptions for other API errors.

### Dependencies
requests: For making API calls.