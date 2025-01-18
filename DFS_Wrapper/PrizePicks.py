from DFS_Wrapper.DFS_Base import DFS

class PrizePick(DFS):
    def __init__(self):
        super().__init__('prizepick')
        self.leagues = self._get_leagues_()
        self.api_data = self._get_api_data('prizepick')

    def _get_leagues_(self):
        """
        Get Leagues / League ID
        :return: League Name : League ID
        """
        return {
           league["attributes"]["league"]: league["relationships"]["league"]["data"]["id"]
           for league in self.api_data["included"] if league.get("attributes") and league["attributes"].get("league") is not None
        }

    def _get_prizepick_data(self):
        """
        Get PrizePick Data
        :return: PrizePick Data
        """
        return [
            {
                "player_id": game_details["relationships"]["new_player"]["data"]["id"],
                "player_name": self._get_player_information(game_details["relationships"]["new_player"]["data"]["id"])[
                    "attributes"]["display_name"],
                "is_live": game_details["attributes"]["is_live"],
                "league": self._get_player_information(game_details["relationships"]["new_player"]["data"]["id"])[
                    "attributes"]["league"],
                "league_id": self._get_player_information(game_details["relationships"]["new_player"]["data"]["id"])[
                    "relationships"]["league"]["data"]["id"],
                "odds_type": game_details["attributes"]["odds_type"],
                "stat_type": game_details["attributes"]["stat_type"],
                "status": game_details["attributes"]["status"],
                "team": self._get_player_information(game_details["relationships"]["new_player"]["data"]["id"])[
                    "attributes"]["team"],
                "opponent": game_details["attributes"]["description"].split(" ")[0],
                **(
                    {
                        "promo": game_details["attributes"].get("flash_sale_line_score"),
                        "discount_name": game_details["attributes"].get("discount_name"),
                        "discount_percentage": game_details["attributes"].get("discount_percentage"),
                        "end_promo_date": game_details["attributes"].get("end_time"),
                    }
                    if game_details["attributes"].get("flash_sale_line_score") else {
                        "line_score": game_details["attributes"]["line_score"], }
                ),
                "start_time": game_details["attributes"]["start_time"],
            }
            for game_details in self.api_data["data"]
        ]

    def _get_player_information(self, player_id):
        """
        Get Player Information
        :param player_id: Player ID
        :return: Returns dictionary of player information
        """
        return next(
            (player for player in self.api_data["included"] if player.get("attributes").get("display_name") is not None and player["id"] == player_id),
            None
        )

    def get_data(self):
        """
        Get PrizePick Data
        :return: Returns a list of PrizePick Data
        """
        return self._get_prizepick_data()

    def get_leagues(self):
        """
        Get Leagues
        :return: Returns the League Name: League ID
        """
        return self.leagues
