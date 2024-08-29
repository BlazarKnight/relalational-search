

def remove_duplicates(lst):
    seen = []
    return [x for i, x in enumerate(lst) if x not in seen or not seen.append(x)]


def openchop(filename,rt):
    g=0
    chumbucet=()
    opendfl = open(filename,"r")
    for d in opendfl:
        splut= d.split()
        for wo in splut:

            chumbucet = chumbucet+tuple(wo)
    opendfl.close()
    opendfl = open(filename, "r")
    raw = opendfl.read()
    rep = raw.replace(" \n , . ! - : ", ' ')

    bits = sorted({x for x in chumbucet})
    opendfl.close()

    #chumbucet= chumbucet.replace('\n', ' ')
    #overbord = chumbucet.split('<')
    if rt=='over':
        return overbord
    if rt=='bitdit':
        return bits

def seter():
    dike = openchop('input.txt', 'bitdit')
    listofdp = openchop('input.txt', 'over')
    matrixs=[]
    fu = ''
    for word in listofdp:
        try:
            dikindex = dike.index(word)
            docindex = word.index(listofdp)
            word[docindex]=dikindex


        except(ValueError):
            fu= fu+word
            print(fu)

    matrixs.append()

    return matrixs,fu

def main():

if __name__ == '__main__':
    print(openchop('input.txt', 'bitdit'))
    #print(seter())
