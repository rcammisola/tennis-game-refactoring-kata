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
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        if (self.p1points > POINTS_VALUE_FORTY or self.p2points > POINTS_VALUE_FORTY) and abs(self.p2points - self.p1points) >= 2:
            result = "Win for " + self._currently_winning_player_name()

        elif (self.p1points >= POINTS_VALUE_FORTY and self.p2points >= POINTS_VALUE_FORTY) and abs(self.p2points - self.p1points) == 1:
            result = "Advantage " + self._currently_winning_player_name()

        else:
            if self.p1points == self.p2points:
                if self.p1points < POINTS_VALUE_FORTY:
                    result = self._points(self.p1points)
                    result += "-All"
                else:
                    result = "Deuce"

            else:
                P2res = self._points(self.p2points)
                P1res = self._points(self.p1points)
                result = P1res + "-" + P2res

        return result

    def _currently_winning_player_name(self):
        return self.player1Name if self.p1points > self.p2points else self.player2Name

    def _points(self, player_points):
        if player_points == POINTS_VALUE_LOVE:
            point_title = "Love"
        elif player_points == POINTS_VALUE_FIFTEEN:
            point_title = "Fifteen"
        elif player_points == POINTS_VALUE_THIRTY:
            point_title = "Thirty"
        elif player_points == POINTS_VALUE_FORTY:
            point_title = "Forty"
        else:
            raise ValueError(f"Unexpected points value: {player_points}")

        return point_title

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1) else "Win for " + s
