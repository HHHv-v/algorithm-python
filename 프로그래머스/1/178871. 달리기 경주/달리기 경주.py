def solution(players, callings):
    player={p:i for i,p in enumerate(players)}
    
    for calling in callings:
        faster=player[calling]
        players[faster],players[faster-1]=players[faster-1],players[faster]
        
        player[players[faster-1]]=faster-1
        player[players[faster]]=faster
        
    return players