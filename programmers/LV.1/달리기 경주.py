def solution(players, callings):
    answer = []
    p_dict = {player:idx for idx, player in enumerate(players)}
    for calling in callings:
        p_dict[calling] -= 1
        p_dict[players[p_dict[calling]]] += 1
        players[p_dict[calling]], players[p_dict[calling] + 1] = players[p_dict[calling] + 1], players[p_dict[calling]] 
    

    return players