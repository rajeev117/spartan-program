#Mission 1


import sys

def pof(n):
    return n*n*n*n
def process(nos,index,count):
    if index>= len(nos):
        return count
    if nos[index]<= 0:
        count+= pof(nos[index])
    return process(nos,index+1,count)
def test_case():
    try:
        x= int(input().strip())
        line= input().strip()
        if not line:
            nos=[]
        else:
            nos= list(map(int,line.split()))

        if len(nos)!= x:
            return -1
        if x==0:
            return 0
        return process(nos,0,0)
    except:
        return -1

def process_cases(n, case_num,result):
    if case_num>= n:
        return result

    test_result= test_case()
    result.append(test_result)
    return process_cases(n,case_num+1,result)

def output(result, index=0):
    if index== len(result):
        return
    print(result[index])
    output(result,index+1)

def main():
    try:
        n= int(input().strip())
        result= process_cases(n,0,[])
        output(result)
    except:
        pass


if __name__== "__main__":
    main()

        
