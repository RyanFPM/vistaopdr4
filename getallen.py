print("typ 5 getallen gescheiden door een spatie. Dezen getallen zullen gesorteerd worden.:")
try :
    getallen = list(map(int, input().split()))
    getallen.sort()
    getallen.reverse()
    print("Na het sorteren van dezen getallen:")
    print(*getallen)
except ValueError: 
    print("het is fout gegaan")
    