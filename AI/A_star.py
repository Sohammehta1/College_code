g_n = {
    'Katraj': {'Bibvewadi': 3.5, 'Sahakarnagar': 5},
    'Bibvewadi': {'Katraj': 3.5, 'Sahakarnagar': 2, 'Lokmanyanagar': 6, 'Sinhgad_rd': 5},
    'Sahakarnagar': {'Katraj': 5, 'Bibvewadi': 2, 'Parvati': 1.5, 'Lokmanyanagar': 3, 'Sinhgad_rd': 2.5},
    'Parvati': {'Lokmanyanagar': 2},
    'Lokmanyanagar': {'Bibvewadi': 6, 'Sahakarnagar': 3, 'Parvati': 2, 'Sinhgad_rd': 1, 'Kothrud': 3},
    'Sinhgad_rd': {'Bibvewadi': 5, 'Sahakarnagar': 2.5, 'Lokmanyanagar': 1, 'Kothrud': 2.5},
    'Kothrud': {'Lokmanyanagar': 3, 'Sinhgad_rd': 2.5}
}
h_n = {
    'Katraj': 10,
    'Bibvewadi': 8,
    'Sahakarnagar': 7,
    'Parvati': 5,
    'Lokmanyanagar': 3,
    'Sinhgad_rd': 2,
    'Kothrud': 0
}

def find_goal(gn, hn, path : list, curr, goal,cost)->list:
    if curr == goal:
        return [cost, path,1]
    f_n = {}
    fmax = -1
    next = ''
    if curr != 'Katraj':
        path.append(curr)
    
    for key in gn[curr] and key not in path:
        f_n[key] = hn[key]+gn[curr][key]
        if fmax < f_n[key]:
            next = key
            fmax = f_n[key]
    cost += g_n[curr][next]
    #We have fmax from neighbouring nodes
    #Now we need to find the fmax value for it's neighbours
        
    metrics = find_goal(gn,hn, path,next, goal, cost)
    if metrics[2]==1: # Goal state has been reached
        print()
    else:
        for key in gn[curr] and key not in metrics[1]:
            if fmax < f_n[key]:
                cost -= fmax
                path = (metrics[1].pop()).append(key) # popping the current next
                next = key
                fmax = f_n[key]
        
                
                
    cost += g_n[curr][next]
    

    
    

    return [0,[]]

def A_star(g_n,h_n):
    start = 'Katraj'
    end = 'Kothrud'
    path = [start]
    metrics = [0, [],0]
    cost = 0
    return  find_goal(g_n,h_n, path,start, end, cost)

cost, path = A_star(g_n, h_n)

    