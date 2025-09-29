# tasks/task3.py

def solve():    
# Ниже пишите решение задачи
    Zet, Goida = map(int,input().split())
    Vsego = Zet + Goida - 1
    Harry_promazal = Vsego - Zet
    Larry_promazal = Vsego - Goida
    print(Harry_promazal, Larry_promazal)



# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()