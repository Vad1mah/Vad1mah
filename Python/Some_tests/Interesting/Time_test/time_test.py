import time

st1 = 'qwertyuiopa sdfghjklzxcvbnm' * 100000
st2 = 'mnbvcxzlkjhg fdsapoiuytrewq' * 100000

def main1():
    pass

def main2():
    pass

start_time = time.time()
main1()
print("main1 --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
main2()
print("main2 --- %s seconds ---" % (time.time() - start_time))