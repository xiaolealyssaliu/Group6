divisor=(80,120,140,160,180,200,220,240,260,300)
values=(0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)
def length(data):
    split_text=data.split()
    count=0
    for word in split_text:
        count=count+1
    print(count)
    if count<divisor[0]: #if the length less than 80, all will be attributed to 0.0
        return values[0]
    if count>divisor[9]:
        return values[10]
    for i in range(1,len(divisor)): 
        if count/divisor[i-1]>=1 and count/divisor[i]<1: #if the word count is less than (i+1)-th divisor but greater or equal to the i-th divisor, score given will be the (i+1)-th value.
            return values[i+1]
       
