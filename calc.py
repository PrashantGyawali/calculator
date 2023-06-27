expr=input("Give expression:")
operators=["/","*","-","+"]
allnums=list("1234567890.")
expr_split=expr.split()
expr_joined="".join(expr_split)

nums=[]
operatorsorder=[]

num=""
try:
    for letternum in range(0,len(expr_joined)):
        if expr_joined[letternum] in operators:
            if(letternum!=0):
                nums.append(float(num))
                operatorsorder.append(expr_joined[letternum])
                num=""
            else:
                num+=expr_joined[letternum]
                continue
        
        elif expr_joined[letternum] in allnums:
            if(letternum==len(expr_joined)-1):
                num+=expr_joined[letternum] 
                nums.append(float(num))
            else:
                num+=expr_joined[letternum]
    try:
        if(len(operatorsorder)>len(nums)):
            _x=1
    except:
        print("not valid expressoin")
        



    
except:
    print("not valid expressoin")
    
    
def calc(op1,op2,operator):
    match operator:
        case "*":
            t=op1*op2
        case "+":
            t= op1+op2
        case "/":
            t= op1/op2
        case "-":
            t= op1-op2
    return t
        
        
n=len(operatorsorder)-1

while n>=0:
    for operator in operators:
        k=0

        while k<=n:
            if(operatorsorder[k]==operator):
                nums[k]=calc(float(nums[k]),float(nums[k+1]),operatorsorder[k])
                operatorsorder[k]="t"
                nums[k+1]="t"
                nums=[i for i in nums if i != "t"]
                operatorsorder=[i for i in operatorsorder if i != "t"]
                n-=1
            k+=1

print(expr_joined,"=",nums[0])
