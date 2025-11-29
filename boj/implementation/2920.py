# 음계
# 251129

seq = list(map(int, input().split()))
point = seq[0]
ascending,descending,mixed = False,False,False

if point == 8: descending = True
elif point == 1: ascending = True
else: mixed = True
            
for i in range(1,8):
    if mixed: break
    if point < seq[i] and ascending: point = seq[i]
    elif point > seq[i] and ascending: mixed = True; break
    if point > seq[i] and descending: point = seq[i]
    elif point < seq[i] and descending: mixed = True; break

if mixed: print('mixed')
elif ascending: print('ascending')
elif descending: print('descending')