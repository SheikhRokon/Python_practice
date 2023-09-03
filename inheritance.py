# multiple inheritance
class baba:
    car = 'BMW'
    home = "10 floor"
    tk = "100 M"
    
class kaka1:
    bike = 'R1 5'
    Mobile = 'iphone'
    
class kaka2:
    bike = 'suzuki'
    Mobile = 'Redmi'
class kaka3(baba,kaka1):
    bike = 'suzuki'
    Mobile = 'Redmi'
    
print(kaka3.tk)        