# -*- coding: utf-8 -*-
POINTS_NAME_LOVE = "Love"
POINTS_NAME_FIFTEEN = "Fifteen"
POINTS_NAME_THIRTY = "Thirty"
POINTS_NAME_FORTY = "Forty"

POINTS_VALUE_LOVE = 0
POINTS_VALUE_FIFTEEN = 1
POINTS_VALUE_THIRTY = 2
POINTS_VALUE_FORTY = 3


def _get_points_category(score):
    return {
        POINTS_VALUE_LOVE: POINTS_NAME_LOVE,
        POINTS_VALUE_FIFTEEN: POINTS_NAME_FIFTEEN,
        POINTS_VALUE_THIRTY: POINTS_NAME_THIRTY,
        POINTS_VALUE_FORTY: POINTS_NAME_FORTY,
    }[score]


class TennisGame1:

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if self._is_game_over():
            result = "Win for " + self._currently_leading_player()

        else:
            result = self._in_progress_game_score()

        return result

    def _in_progress_game_score(self):
        if self._is_tied():
            result = self._tied_game_score()

        elif self._is_advantage():
            result = "Advantage " + self._currently_leading_player()

        else:
            player1_score = _get_points_category(self.player1_points)
            player2_score = _get_points_category(self.player2_points)
            result = f"{player1_score}-{player2_score}"
        return result

    def _currently_leading_player(self):
        if self.player1_points > self.player2_points:
            leading_player = self.player1_name
        else:
            leading_player = self.player2_name

        return leading_player

    def _is_game_over(self):
        return (
                (self.player1_points > POINTS_VALUE_FORTY or self.player2_points > POINTS_VALUE_FORTY) and
                self._more_than_one_point_ahead()
        )

    def _more_than_one_point_ahead(self):
        return abs(self.player1_points - self.player2_points) > 1

    def _is_tied(self):
        return self.player1_points == self.player2_points

    def _is_advantage(self):
        return self.player1_points >= POINTS_VALUE_FORTY and self.player2_points >= POINTS_VALUE_FORTY

    def _tied_game_score(self):
        if self.player1_points >= POINTS_VALUE_FORTY:
            result = "Deuce"
        else:
            player_points = _get_points_category(self.player1_points)
            result = f"{player_points}-All"
        return result


class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if self._either_player_has_more_than(POINTS_VALUE_FORTY) and self._lead_at_least_two_points():
            result = "Win for " + self._currently_winning_player_name()
        else:
            result = self._in_progress_game_score()

        return result

    def _in_progress_game_score(self):
        if self._tied_game():
            if self.player1_points < POINTS_VALUE_FORTY:
                result = _get_points_category(self.player1_points)
                result += "-All"
            else:
                result = "Deuce"

        elif self._both_players_have_at_least(POINTS_VALUE_FORTY) and self._lead_by_one_point():
            result = "Advantage " + self._currently_winning_player_name()

        else:
            player1_score = _get_points_category(self.player1_points)
            player2_score = _get_points_category(self.player2_points)
            result = player1_score + "-" + player2_score
        return result

    def _currently_winning_player_name(self):
        return self.player1_name if self.player1_points > self.player2_points else self.player2_name

    def _either_player_has_more_than(self, points):
        return self.player1_points > points or self.player2_points > points

    def _lead_at_least_two_points(self):
        return abs(self.player2_points - self.player1_points) >= 2

    def _both_players_have_at_least(self, points):
        return self.player1_points >= points and self.player2_points >= points

    def _lead_by_one_point(self):
        return abs(self.player2_points - self.player1_points) == 1

    def _tied_game(self):
        return self.player1_points == self.player2_points


class TennisGame3:
    point_descriptions = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if self._player_has_points_for_win() and self._player_lead() >= 2:
            result = "Win for " + self._currently_winning()

        elif self._deuce_has_been_reached() and self._player_lead() == 1:
            result = "Advantage " + self._currently_winning()

        elif self.player1_points == self.player2_points:
            result = self._tied_game_score()

        else:
            player1_score = self.point_descriptions[self.player1_points]
            player2_score = self.point_descriptions[self.player2_points]
            result = player1_score + "-" + player2_score

        return result

    def _player_has_points_for_win(self):
        return self.player1_points > 3 or self.player2_points > 3

    def _tied_game_score(self):
        if self._deuce_has_been_reached():
            return "Deuce"
        else:
            score = self.point_descriptions[self.player1_points]
            return score + "-All"

    def _deuce_has_been_reached(self):
        return self.player1_points >= 3 and self.player2_points >= 3

    def _player_lead(self):
        return abs(self.player1_points - self.player2_points)

    def _currently_winning(self):
        return (
            self.player1_name
            if self.player1_points > self.player2_points
            else self.player2_name
        )
