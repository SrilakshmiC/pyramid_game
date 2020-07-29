"""Skeleton for Pyramid game
The code below is still the same as for Rock-Paper-Scissors.
Modify to implement the Pyramid game.
"""

from db_sqlite import Game


class Pyramid(Game):

    movesremaining=[[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], [('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]]

#    rounds = 0

    def valid_moves(self, username):
        """Return list of pairs with valid moves for this player and how to display them.
        For example [('r', 'Rock'), ('p', 'Paper'), ('s', 'Scissors')]
        :param username: The moves valid for this user
        :return: List of pairs
        """
        index = self.player_index(username)
        return self.movesremaining[index]


    def add_player_move(self, username, move):
        """Add a new move by a player to the game.
        :param username: Username of player who moves
        :param move: One of the strings 'r', 'p', 's'
        """
        # Discard move if Game not in play (i.e. state != 1), or the move is not r(ock), p(aper) or s(cissors)
        if self.state != 1 or move not in ('0', '1', '2', '3', '4', '5'):
            return

        # Find the index (position) of this player in the list of players in the game.
        # In the case of RPS games this value will be 0 or 1 since RPS always has 2 players.
        index = self.player_index(username)
        print("Index :" + str(index))
        
        for i in range(len(self.movesremaining[index])):
            #print("Length:"+ str(len(self.movesremaining[index])))
            if str(move) == self.movesremaining[index][i][0]:
                #print("Removing:"+ str(i))
                self.movesremaining[index].remove(self.movesremaining[index][i])
                break
#        self.rounds += 1
#        print(self.rounds)

        # If there are no game rounds yet, or the last one is complete
        if not self.turns or not [None for m in self.turns[-1] if m is None]:  # No turns or last complete
            new_turn = [None] * len(self.players)
            new_turn[index] = move
            self.turns.append(new_turn)
            self.save_game_state()

        # If opponent(s) moved in last round but user has not
        elif self.turns[-1][index] is None:
            last_turn = self.turns[-1]
            last_turn[index] = move
            # Check if turn is complete and if so calculate scores

            print("goal: " + str(self.goal))

            if not [None for m in last_turn if m is None]:
                if last_turn[0] == last_turn[1] and last_turn[0] == last_turn[2]:
                    self.players[0]['score'] += 1
                    self.save_score_for_player(0)
                    if self.players[0]['score'] == self.goal:
                        self.set_game_over()
                    self.players[1]['score'] += 1
                    self.save_score_for_player(1)
                    if self.players[1]['score'] == self.goal:
                        self.set_game_over()
                    self.players[2]['score'] += 1
                    self.save_score_for_player(2)
                    if self.players[2]['score'] == self.goal:
                        self.set_game_over()

                elif last_turn[0] == last_turn[1] and last_turn[0] > last_turn[2]:
                    self.players[0]['score'] += 1
                    self.save_score_for_player(0)
                    if self.players[0]['score'] == self.goal:
                        self.set_game_over()
                    self.players[1]['score'] += 1
                    self.save_score_for_player(1)
                    if self.players[1]['score'] == self.goal:
                        self.set_game_over()

                elif last_turn[1] == last_turn[2] and last_turn[1] > last_turn[0]:
                    self.players[1]['score'] += 1
                    self.save_score_for_player(1)
                    if self.players[1]['score'] == self.goal:
                        self.set_game_over()
                    self.players[2]['score'] += 1
                    self.save_score_for_player(2)
                    if self.players[2]['score'] == self.goal:
                        self.set_game_over()

                elif last_turn[0] == last_turn[2] and last_turn[0] > last_turn[1]:
                    self.players[0]['score'] += 1
                    self.save_score_for_player(0)
                    if self.players[0]['score'] == self.goal:
                        self.set_game_over()
                    self.players[2]['score'] += 1
                    self.save_score_for_player(2)
                    if self.players[2]['score'] == self.goal:
                        self.set_game_over()
                    
                            
                elif last_turn[0]>last_turn[1]:
                    if last_turn[0]>last_turn[2]:
                        self.players[0]['score'] += 2
                        self.save_score_for_player(0)
                        if self.players[0]['score'] == self.goal:
                            self.set_game_over()
                    else:
                        self.players[2]['score'] += 2
                        self.save_score_for_player(2)
                        if self.players[2]['score'] == self.goal:
                            self.set_game_over()

                else:
                    if last_turn[1]>last_turn[2]:
                        self.players[1]['score'] += 2
                        self.save_score_for_player(1)
                        if self.players[1]['score'] == self.goal:
                            self.set_game_over()
                    else:
                        self.players[2]['score'] += 2
                        self.save_score_for_player(2)
                        if self.players[2]['score'] == self.goal:
                            self.set_game_over()
                
            self.save_game_state()
            
            '''
            if not [None for m in last_turn if m is None]:
                if last_turn in (['5', '4'], ['5', '3'], ['5', '2'], ['5', '1'],['5', '0'], ['4', '3'], ['4', '2'], ['4', '1'], ['4', '0'], ['3', '2'], ['3', '1'], ['3', '0'], ['2', '1'], ['2', '0'], ['1', '0']):
                    self.players[0]['score'] += 1
                    self.save_score_for_player(0)
                    if self.players[0]['score'] == self.goal:
                        self.set_game_over()
                elif last_turn in (['4', '5'], ['3', '5'], ['2', '5'], ['1', '5'], ['0', '5'], ['3', '4'], ['2', '4'], ['1', '4'], ['0', '4'], ['2', '3'], ['1', '3'], ['0', '3'], ['1', '2'], ['0', '2'], ['0', '1']):
                    self.players[1]['score'] += 1
                    self.save_score_for_player(1)
                    if self.players[1]['score'] == self.goal:
                        self.set_game_over()
            self.save_game_state()
            '''

    def decorated_moves(self, username):
        """Return a list of moves with formatting information.
        :param username: Player's username
        :return: Formatted list of moves
        """
        if not self.turns:
            return []

        last_turn = self.turns[-1]
        if [None for m in last_turn if m is None]:  # Everybody has not yet moved in last turn, it is incomplete
            incomplete_last_turn = last_turn
            complete_turns = self.turns[:-1] 
        else:
            incomplete_last_turn = None
            complete_turns = self.turns
        translate = {'0': '0', '1': '1', '2': '2', '3':'3', '4':'4', '5':'5'}
        decorated_turns = []

        #index = self.player_index(username)

        print("last turn: " + str(last_turn))
        print("complete turns: " + str(complete_turns))


        for turn in complete_turns:
            if turn[0] == turn[1] == turn[2]:
                decorated_turns.append([(translate[turn[0]], True), (translate[turn[1]], True), (translate[turn[2]], True)])

            elif turn[0] == turn[1] and turn[0] > turn[2]:
                decorated_turns.append([(translate[turn[0]], True), (translate[turn[1]], True), (translate[turn[2]], False)])

            elif turn[1] == turn[2] and turn[1] > turn[0]:
                decorated_turns.append([(translate[turn[0]], False), (translate[turn[1]], True), (translate[turn[2]], True)])

            elif turn[0] == turn[2] and turn[0] > turn[1]:
                decorated_turns.append([(translate[turn[0]], True), (translate[turn[1]], False), (translate[turn[2]], True)])

            
            elif turn[0]>turn[1]:
                if turn[0]>turn[2]:
                    decorated_turns.append([(translate[turn[0]], True), (translate[turn[1]], False), (translate[turn[2]], False)])
                else:
                    decorated_turns.append([(translate[turn[0]], False), (translate[turn[1]], False), (translate[turn[2]], True)])    

            else:
                if turn[1]>turn[2]:
                    decorated_turns.append([(translate[turn[0]], False), (translate[turn[1]], True), (translate[turn[2]], False)])
                else:
                    decorated_turns.append([(translate[turn[0]], False), (translate[turn[1]], False), (translate[turn[2]], True)])
            
            
        if incomplete_last_turn:
            index = self.player_index(username)
            decorated_last_turn = []
            for i, m in enumerate(incomplete_last_turn):
                if m is None:
                    decorated_last_turn.append(('', False))
                elif i == index or incomplete_last_turn[index]:
                    decorated_last_turn.append((translate[m], False))
                else:
                    decorated_last_turn.append(('?', False))
            decorated_turns.append(decorated_last_turn)

        return decorated_turns

#       for turn in complete_turns:
#            if turn in (['5', '4'], ['5', '3'], ['5', '2'], ['5', '1'],['5', '0'], ['4', '3'], ['4', '2'], ['4', '1'], ['4', '0'], ['3', '2'], ['3', '1'], ['3', '0'], ['2', '1'], ['2', '0'], ['1', '0']):
#                decorated_turns.append([(translate[turn[0]], True), (translate[turn[1]], False)])
#            elif turn in (['4', '5'], ['3', '5'], ['2', '5'], ['1', '5'], ['0', '5'], ['3', '4'], ['2', '4'], ['1', '4'], ['0', '4'], ['2', '3'], ['1', '3'], ['0', '3'], ['1', '2'], ['0', '2'], ['0', '1']):
#                decorated_turns.append([(translate[turn[0]], False), (translate[turn[1]], True)])
#            else:
#                decorated_turns.append([(translate[turn[0]], False), (translate[turn[1]], False)])


    def is_players_turn(self, username):
        """Check if it is player's turn. 
        :param username: Player's username
        :return: boolean
        """
        if self.state != 1:  # Game not in play
            return False
        if not self.turns:  # Nobody has made any moves yet
            return True

        latest_turn = self.turns[-1]
        if not latest_turn[self.player_index(username)]:  # User not yet moved in latest turn
            return True
        if not [None for m in latest_turn if m is None]:  # Latest turn is complete, start new turn
            return True
