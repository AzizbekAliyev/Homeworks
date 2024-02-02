asl_baho = int(input())

def baholash(asl_baho):
    if asl_baho < 38:
        return asl_baho
    
    elif (asl_baho + 2) % 5 == 0:
        return asl_baho + 2
    
    return asl_baho

bahoni_hisoblash = baholash(asl_baho)

print(bahoni_hisoblash)
