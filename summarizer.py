#
# Author: Adrian Martinez
# Description: Program  reads game log file, process' the information and prints out a summary.
# Program will output the winning team, scores, number of scoring players, which player scored
# first and which player scored last.
#

def main():
    teams = []
    total_scores = []
    players = []
    file_name = input('enter gamelog file name:\n')
    game_log = open(file_name, 'r')
    game_log_lists(game_log, teams, players, total_scores)
    team_list = lst_update(teams)
    player_list = lst_update(players)
    team_points = score_lst(teams, team_list, total_scores)
    if team_points[0] > team_points[1]:         # prints out winning team by comparing point
                                                # positions
        print(team_list[0] + ' won!')
    else:
        print(team_list[1] + ' won!')
    for i in range(2):                          # prints each teams total points
        print(team_list[i] + ' scored', team_points[i], 'points.')
    print(int(len(player_list)), 'players scored.')
    print(players[0] + ' scored first.')
    print(players[int(len(players) -1)] + ' scored last.')

def game_log_lists(game_log, teams, players, total_scores):
    '''
     function iterates through each line of initial user specified file and assigns positions to
     new lists according to initial position and strips \n escape
    :param game_log: initial log file
    :param teams: list of both teams, maintaining list positions
    :param players: list of players, maintaining list positions
    :param total_scores: list of player scores, maintaining list positions
    :return: updated lists
    '''
    for line in game_log:               # iterates through game_log
        line_split = line.split(' ')    # splits list into correct positions
        teams.append(line_split[0])     # assigns first position to team list
        players.append(line_split[1])   # second position to player list
        total_scores.append(line_split[2].strip('\n'))  # this position to score list removes escape

def lst_update(old_lst):
    '''
    function uses initial lists as parameters, and removes duplicates, maintaining scoring
    position in new list.
    :param old_lst: list with duplicates taken from initial game log
    :return: updated list with no duplicates
    '''
    new_lst = []                        # placeholder for updated return list
    for i in range(len(old_lst)):       # iterates through list
        if old_lst[i] not in new_lst:   # checks if value is in placeholder list
            new_lst.append(old_lst[i])  # adds value
    return new_lst

def score_lst(teams, team_list, total_scores):
    '''
    function adds points to seperate variables according to which team scored, appending to a new
    list total team points
    :param teams: initial list containing order of points by corresponding team
    :param team_list: updated list with only two teams, used to set order for total points list
    :param total_scores: initial list containing points, listed in chronological sequence
    :return: lists containing unique values, both teams in scoring order, total points in
    sequence of which team scored first, and list with players with no duplicates
    '''
    team_points = []
    team_1 = 0
    team_2 = 0
    for i in range(len(total_scores)):      # iterates through list
        if teams[i] == team_list[0]:        # compares position to reference list
            team_1 += int(total_scores[i])  # if equal, adds point to corresponding position
        else:
            team_2 += int(total_scores[i])  # adds point to second team if initial position
                                            # not the same
    team_points.append(team_1)              # appends points to new list
    team_points.append(team_2)
    return team_points

main()



