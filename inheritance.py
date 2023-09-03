# multiple inheritance
# class baba:
#     car = 'BMW'
#     home = "10 floor"
#     tk = "100 M"
    
# class kaka1:
#     bike = 'R1 5'
#     Mobile = 'iphone'
    
# class kaka2:
#     bike = 'suzuki'
#     Mobile = 'Redmi'
# class kaka3(baba,kaka1):
#     bike = 'suzuki'
#     Mobile = 'Redmi'
    
# print(kaka3.tk)

# pultilevel Inheritance

class baba:
    car = 'BMW'
    home = "10 floor"
    tk = "100 M"
    
class son1(baba):
    bike = 'R1 5'
    Mobile = 'iphone'
    
class son2(son1):
    bike = 'suzuki'
    Mobile = 'Redmi'
class son3(son2):
    bike = 'TVS'
    Mobile = 'Oppo'
    
print(son3.car)    

       