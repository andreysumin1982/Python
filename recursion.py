arr = [1,'w',3,'c',5,'g',7,8,9,10,11,12,'s',14,'b']
#
def recurse_dict_2(arr):
    if arr:
        fist = arr[0]
        d = {fist : recurse_dict_2(arr[1:]) }
        return d
print(recurse_dict_2(arr))
print('*' * 30)
#
def recurse_dict_3(defain):
    try:
        for k,v in defain.items():
            print(k, end=' ')
            recurse_dict_3(v)
    except: print()
#
arr_p = []
arr.append(recurse_dict_3(recurse_dict_2(arr)))
print(arr[:-1])
#--
n= 1
for i in range(1, 5+1):
    n *= i  #   Факториал
    print(n)
#
def fac(f): #  Рекурсия факториала
    if f != 0:
        return f*fac(f-1)
    return 1
print(fac(3))
#--  Выводим элементы списка рекурсией (без цикла)
arr = [1,'a',3,'z',5]
def reverse(n, k=0):  # k=0, не обязaтельный аргумент
    if k != len(n):
        print(n[k])
        k+=1
        reverse(n, k)
reverse(arr)
#--
print('*'*20)
dict_namespace = {'global': {'parrent': 'None', 'var': ['a','q']}, 'foo': {'parrent': 'global', 'var': ['b']}, 'boo': {'parrent': 'foo', 'var': ['c','b']}}
arr_keys = ['global','foo','boo']
#
def recurse2(name, namespace, d):    # Ф-ция (рекурсией) ищет в словаре ключи и значения.
    list_key = arr_keys[::-1]
    #print(list_key)
    if name in list_key :
        if namespace in d[name]['var']:
            print(name); return
        else:
            index = list_key.index(name)
            for key in list_key[index+1:]:
                if namespace in d[key]['var']:
                    print(key); return
                print('None'); return

#--
namespace = 'q'
name = 'foo'
recurse2(name, namespace, dict_namespace)
