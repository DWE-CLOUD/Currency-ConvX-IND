from tabulate import tabulate
with open('CT.txt') as c:
    lines = c.readlines()
headers=['Reason','AMT']
Reason = []
#exp_done = []
AMT = []
t_amt=0
input24 = int(input("[1] Calculate Expenses / [2] Use Calculator Directly :  "))
if input24 == 1:
    print("Use '=' to provide amount || ex. Price of Paracetamol = 100 ; | When finished just press Enter .. ")
    aq=True
    while aq:
        input_exp = input(">> ")
        swd=0
        if "=" in input_exp:
            wer = list(input_exp)
            q = wer.index("=")
            #print(q)
            #print(wer)
            str2 =""
            for dew in range(0, q):
                str2+=wer[dew]
            Reason.append(str2)
            yo=1
            while yo==1:
                if wer[q+1].isspace()==True:
                    #print("HI")
                    q=q+1
                else:
                    yo=0
            q=q+1
            intstr=""
            for amtdew in range(q,len(wer)):
                intstr+=wer[amtdew]
            #print(intstr)
            AMT.append(intstr)
            #exp_done_o=str2,intstr
            #exp_done.append(exp_done_o)
            #swd=swd+1
        else:
            for qw in range(len(AMT)):
                t_amt=t_amt+int(AMT[qw].replace('"',''))
            Reason.append("<<<<<<<TOTAL>>>>>>>")
            AMT.append("-------------------")
            Reason.append("")
            AMT.append(t_amt)
            print("")
            aq=False
    #print(exp_cal)
    #print(exp_cal_amt)
    #print("")
    table = zip(Reason, AMT)
    print(tabulate(table, headers=headers, floatfmt=".4f"))
else:
    print("")
#while range(len(exp_cal)):
#print(exp_done)
#print(tabulate(exp_done, headers=["Reason", "Amount"]))
azin = numin = 1
in12 = []
count = []
yui = []
rt = []
print("")
inputy=int(input("Want To List Countries / Currencies .. [1] YES , [2] NO : "))
if inputy==1:
    for line in lines:
        lister = line.split()
        print(lister[0] + " " + lister[1])
else:
    print("")
po = input("From Currency / Country Name : ")
if (' ' in po) == True:
    no = po.split()
    # print(no)
    yui.append(no[0].replace('"', ''))
else:
    yui.append(po)
# print(yui)
op = yui[0].replace('"', '')
yui.clear()
if op.isupper() == True:
    op1 = op.lower()
    input1 = op.capitalize()
if op.islower() == True:
    input1 = op.capitalize()
else:
    op2 = op.lower()
    input1 = op2.capitalize()

# print(input1)

for line in lines:
    qwerty = line.split()
    if input1 in qwerty:
        # print(qwerty)
        azs = qwerty[0] + " " + qwerty[1]
        # print(azs)
        count.append(azs)

# print(count)
if len(count) > 1:
    print("")
    print("We Found", len(count), "results , Please Specify Name or Number From Below :  ")
    print("")
    for sew in range(0, len(count)):
        print(str(azin) + "] ", count[sew], sep='')
        azin = azin + 1
    print("")
    input0006 = input(" >> ")
    if input0006.isnumeric() == True:
        numin = 0

    if (' ' in input0006) == True:
        ono1 = input0006.split()
        ono = ono1[0].replace('"', '')
        if ono.isupper() == True:
            op1 = ono.lower()
            no = op1.capitalize()
        if ono.islower() == True:
            no = ono.capitalize()
        else:
            op2 = ono.lower()
            no = op2.capitalize()
        # print(no)
        yui.append(no.replace('"', ''))
        input016 = yui[0].replace('"', '')
        input06 = str(input016)
    else:
        if type(input0006) == str:
            if input0006.isupper() == True:
                op1 = op.lower()
                input006 = op.capitalize()
            if input0006.islower() == True:
                input006 = op.capitalize()
            else:
                op2 = input0006.lower()
                input006 = op2.capitalize()
            rt.append(str(input006))
        elif numin == 0:
            rt.append(int(input0006))
        else:
            breakpoint(exit())
        # print(rt)
        # input016 = rt[0]
        # print(input016)
        input06 = input016 = rt[0]
    # print(input06)
    if numin == 0:
        tobr = count[int(input06) - 1].replace('"', '')
        input06 = tobr
    elif type(input06) == str:
        print("")
    else:
        print("Cannot Determine")
    # print(count)
    if input06:
        for line in lines:
            splitter = line.split()
            if input06 in line:
                boi = line.split()
                print("Okay Going Forward With Your Selection : ", boi[0], boi[1])
            else:
                azop = 0
        print("")
        in12.append(input06)
    else:
        print("")
        print("No Input Given ! Exitting ")
        breakpoint(exit())
else:
    print("Okay Going Forward With Your Selection : ", count[0].replace('"', ''))
    in12 = count
# print(in12)
# Made By Akshit Ohri , DAV KHARGHAR
print("")
print("To Currency : INR")

if t_amt!=0:
    print("")
    print("Amount in INR : ₹",t_amt)
    amtin = int(t_amt)
    input7 = in12[0]
    # print(input7)
    for line in lines:
        splitter = line.split()
        if input7 in line:
            # print("LINE",line)
            # print("SPLIT:" , line.split())
            a = line.split()
            print("")
            print("Made By AKSHIT OHRI (AKA DWE CLOUD ) , DAV INTERNATIONAL SCHOOL , KHARGHAR")
            print("")
            print("")
            print("Current Exchange Rate Against", in12[0], "is : ₹" + a[-1])
            print("")
            print("The Amount ₹", amtin, " Is Equivalent to ", amtin / float(a[-1]), "in", in12[0])
            print("")
            print("")
            print("")
            inputbreak = input("Enter to Exit !")
            if inputbreak:
                breakpoint(exit())
            else:
                breakpoint(exit())

elif t_amt==0:
    amt = input("Amount in INR : ")
    print("")
    print("Amount in INR : ₹",amt)
    amtin = int(amt)
    input7 = in12[0]
    # print(input7)
    for line in lines:
        splitter = line.split()
        if input7 in line:
            # print("LINE",line)
            # print("SPLIT:" , line.split())
            a = line.split()
            print("")
            print("Made By AKSHIT OHRI (AKA DWE CLOUD ) , DAV INTERNATIONAL SCHOOL , KHARGHAR")
            print("")
            print("")
            print("Current Exchange Rate Against", in12[0], "is : ₹" + a[-1])
            print("")
            print("The Amount ₹", amtin, " Is Equivalent to ", amtin / float(a[-1]), "in", in12[0])
            print("")
            print("")
            print("")
            inputbreak = input("Enter to Exit !")
            if inputbreak:
                breakpoint(exit())
            else:
                breakpoint(exit())


    print("")
    print("Nothing Defined ! Exitted Program ")

print("")
