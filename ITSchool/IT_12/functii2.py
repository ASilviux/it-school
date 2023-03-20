def box_price(height, lenght, width, t):
    raw_price= height * lenght * width * 25
    if t == 1:
        return raw_price
    if t == 2:
        return raw_price * 1.1
    if t == 3:
        return raw_price * 1.2
    
print(box_price(1, 2, 3))
print(box_price(t=2 , width=3, height=1, lenght=2))