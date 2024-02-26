h_n = {
    'Katraj': 10,
    'Bibvewadi' : 8,
    'Sahakarnagar':7,
    'Parvati': 5,
    'Lokmanyanagar' : 3,
    'Sinhgad_rd' : 2,
    'Kothrud': 0
}

g_n = {
    'Katraj':{'Bibvewadi': 3.5, 'Sahakarnagar': 5},
    'Bibvewadi':{'Katraj':3.5, 'Sahakarnagar': 2,'Lokmanyanagar': 6, 'Singad_rd': 5},
    'Sahakarnagar':{'Katraj':5,'Bibvewadi': 2, 'Parvati': 1.5,'Lokmanyanagar':3,'Sinhgad_rd': 2.5},
    'Lokmanyanagar': {'Bibvewadi': 6, 'Sahakarnagar': 3, 'Sinhgad_rd': 1, 'kothrud': 3},
    'Sinhgad_rd' : {'Bibvewadi': 5, 'Sahakarnagar': 2.5, 'Lokmanyanagar': 1, 'Kothrud' : 2.5},
    'Kothrud' : {'Lokmanyanagar' : 3, 'Sinhgad_rd': 2.5}
}


start =  'Katraj'
goal = 'Kothrud'

def A_star(head):
    visited_ = {head:False}
    min_val = float('inf')
    next = ''
    for  key in g_n[head]:
        visited_[key] = False
        curr = g_n[head][key] + h_n[key]
        if curr < min_val:
            next = key
            min_val =  curr
        # selecting minimum f(n) values from the neighbours.
    visited_[next] = True
        
    
    #print(min_val)
    
    

A_star(start)

    