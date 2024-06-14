import time

class Score:
    def __init__(self):
        self.rounds = 5
        self.current_round = 1
        self.player_scores = [0, 0]
        self.round_wins = [0, 0]
        self.round_start_time = time.time()

    def start_round(self):
        self.round_start_time = time.time()

    def end_round(self, winner):
        round_duration = time.time() - self.round_start_time
        points = max(100, 1000 - int(round_duration * 10))
        self.player_scores[winner] += points
        self.round_wins[winner] += 1
        self.current_round += 1

    def is_game_over(self):
        return self.current_round > self.rounds

    def get_winner(self):
        if self.player_scores[0] > self.player_scores[1]:
            return 0
        elif self.player_scores[1] > self.player_scores[0]:
            return 1
        else:
            return -1  # draw

    def reset(self):
        self.current_round = 1
        self.player_scores = [0, 0]
        self.round_wins = [0, 0]

    def display_scores(self):
        print(f"Player 1 Score: {self.player_scores[0]}, Rounds Won: {self.round_wins[0]}")
        print(f"Player 2 Score: {self.player_scores[1]}, Rounds Won: {self.round_wins[1]}")