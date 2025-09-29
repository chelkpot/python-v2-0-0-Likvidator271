# tasks/task2.py

def solve():    
# Ниже пишите решение задачи
    Z,O,V = map(int,input().split())
    Penic_stoimost = 3
    Ruchka_stoimost = Penic_stoimost + 2
    Flomaster_stoimost = Ruchka_stoimost + 7
    Stoimost_vsego = Z * Penic_stoimost + O * Flomaster_stoimost + V * Ruchka_stoimost
    print(Stoimost_vsego)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()