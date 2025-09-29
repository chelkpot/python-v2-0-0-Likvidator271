# tasks/task2.py

def solve():    
# Ниже пишите решение задачи
    Z,O,V = map(int,input().split())
    karandash = 3
    Ruchka = 5
    Flomaster = 12
    stoimost = karandash * Z + Ruchka * O + Flomaster * V
    print(stoimost)
 
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()