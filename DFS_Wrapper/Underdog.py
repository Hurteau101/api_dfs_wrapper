from DFS_Wrapper.DFS_Base import DFS

class Underdog(DFS):
    # Mapping Index for _map_team_opponent due to different sports having different formats.
    OTHER_MAPPING_TEAM_INDEX = ("MASL", "ESPORTS", "UNRIVALED", "VAL", "CS", "LOL", "DOTA")

    def __init__(self):
        super().__init__('underdog')
        self.api_data = self._get_api_data('underdog')


    def _get_underdog_data_(self):
        """
        Get Underdog Data
        :return: Returns the Underdog Data
        """
        return self._get_player_information()

    def _get_player_information(self):
        """
        Gets all player information.
        :return: Returns the player information in a list of dictionaries.
        """
        return [
            {
                "player_name": self._fix_name(player["first_name"], player["last_name"]),
                "player_id": player["id"],
                "sport_id": player["sport_id"],
                **{key: value for match in self._add_match_details(player["id"]) for key, value in match.items()},
            }
            for player in self.api_data["players"]
        ]

    def _get_stats(self, stat_id):
        """
        Get the stats for the player
        :param stat_id: Stat ID of player.
        :return: Returns the stats for the player.
        """
        return [
            {
                "stat_type": stat["over_under"]["appearance_stat"]["display_stat"].strip(),
                "line_value": float(stat["stat_value"]),
                "over_multiplier": self.get_multiplier(stat, over=True),
                "under_multiplier": self.get_multiplier(stat),
            }
            for stat in self.api_data["over_under_lines"]
            if stat_id == stat["over_under"]["appearance_stat"]["appearance_id"]
        ]

    def get_multiplier(self, stat_details, over=False):
        """
        Get the multiplier for the player
        :param stat_details: Pass in the stat details dictionary.
        :param over: Set to True if wanting the over multiplier, False for the under multiplier.
        :return: Returns the multiplier for the player.
        """
        for option in stat_details["options"]:
            if option["choice_display"] == "Higher" and over:
                return float(option["payout_multiplier"])
            elif option["choice_display"] != "Higher" and not over:
                return float(option["payout_multiplier"])

    def _add_match_details(self, player_id):
        """
        Add Match IDs
        :param player_id: Player ID
        :return: Returns Match IDS, Team ID, Stat ID, Game Details, Solo Game, and Stats.
        """
        return (
            {
                "match_id": match["match_id"],
                "match_type": match["match_type"],
                "team_id": match["team_id"],
                "stat_id": match["id"],
                **{key: value for game_details in self._get_team_details(match["match_id"], match["team_id"]) for key, value in game_details.items()},
                **{key: value for match in self._solo_game(match["match_id"]) for key, value in match.items()},
                "stats": self._get_stats(match["id"]),
            }
            for match in self.api_data["appearances"]
            if player_id == match["player_id"]
        )


    def _get_team_details(self, match_id, team_id):
        """
        Get Team Details
        :param match_id: Match ID
        :param team_id: Team ID
        :return: Returns the team details.
        """
        return (
            {
                **{key: value for key, value in self._map_team_opponent(team_id, game).items()},
            }

            for game in self.api_data["games"]
            if game["id"] == match_id
        )

    def _map_team_opponent(self, team_id, game):
        """
        Map Team Opponent. Keep in mind different sports have different formats for team/opponent.
        :param team_id: Team ID
        :param game: Game Instance
        :return: Returns the team and opponent.
        """
        if game["sport_id"] in self.OTHER_MAPPING_TEAM_INDEX:
            match_title = self._fix_title(game["title"])
            if team_id == game["home_team_id"]:
                return {
                    "team": match_title.replace(".", "").split("vs")[1].strip(),
                    "opponent": match_title.replace(".", "").split("vs")[0].strip()
                }
            elif team_id == game["away_team_id"]:
                return {
                    "team": match_title.replace(".", "").split("vs")[0].strip(),
                    "opponent": match_title.replace(".", "").split("vs")[1].strip()
                }

        if team_id == game["home_team_id"]:
            return {
                "team": game["title"].split("@")[1].strip() if "@" in game["title"] else game["title"].replace(".", "").split("vs")[0].strip(),
                "opponent": game["title"].split("@")[0].strip() if "@" in game["title"] else game["title"].replace(".", "").split("vs")[1].strip(),
            }
        elif team_id == game["away_team_id"]:
            return {
                "team": game["title"].split("@")[0].strip() if "@" in game["title"] else game["title"].replace(".","").split("vs")[1].strip(),
                "opponent": game["title"].split("@")[1].strip() if "@" in game["title"] else game["title"].replace(".", "").split("vs")[0].strip(),
            }

        return self._solo_game(game["match_id"])

    def _fix_title(self, match_title):
        """
        Fix the title of the match.
        :param match_title: Match Title
        :return: Fixed matches.
        """
        if ":" in match_title:
            return match_title.split(":")[1].strip()
        return match_title

    def _solo_game(self, match_id):
        """
        Get Solo Game
        :param match_id: Match ID
        :return: Returns the solo game details.
        """
        return [
            {
                "start_time": solo_game["scheduled_at"],
                "match": solo_game["title"],

            }
            for solo_game in self.api_data["solo_games"]
            if solo_game["id"] == match_id
        ]


    def _fix_name(self, first_name, last_name):
        """
        Fixes the players name, as Esports don't have first name.
        :param first_name: API First Name.
        :param last_name: API Last Name
        :return: Returns the players name.
        """
        if first_name is None or ":" in first_name or first_name == "":
            return last_name.strip()
        return f"{first_name} {last_name}"

    def _organize_data(self, underdog_data):
        """
        Organize the data by league
        :param underdog_data: Underdog Data
        :return: Returns  a dictionary of data organized by league.
        """
        organized_data = {}

        for data in underdog_data:
            league = data["sport_id"]

            if league not in organized_data:
                organized_data[league] = []

            organized_data[league].append({
                "player_name": data["player_name"],
                "player_id": data["player_id"],
                **(
                    {
                        "team": data.get("team"),
                        "opponent": data.get("opponent"),
                    }
                    if data.get("team") else {
                        "match": data["match"],
                    }
                ),
                "match_id": data["match_id"],
                "match_type": data["match_type"],
                "team_id": data["team_id"],
                "stat_id": data["stat_id"],
                "stats": data["stats"]
            })

        return organized_data


    def get_data(self, organized_data=True):
        """
        Get the Underdog API Data.
        :return: Returns the Underdog API data in a list of dictionaries if organize_data is False,
        else returns a dictionary of data organized by league.
        """
        underdog_data = self._get_player_information()
        if not organized_data:
            return underdog_data

        return self._organize_data(underdog_data)


    def _get_leagues_(self):
        """
        Get Leagues
        :return: Returns the League in a set.
        """
        return set(
            league["sport_id"]
            for league in self.api_data["players"] if league.get("sport_id") is not None
        )

    def get_leagues(self, organized_data=True):
        """
        Get Leagues
        :return: Returns leagues in a set.
        """
        return self._get_leagues_()

