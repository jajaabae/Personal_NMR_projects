def textForBond(B, color, cnt):
    #print str(B[0]), str(B[1])
    #print str(B[0]).replace(HPrefix, HPrefixNum).replace(CPrefix, CPrefixNum), str(B[1]).replace(HPrefix, HPrefixNum).replace(CPrefix, CPrefixNum)
    #return ('<b color="'+str(color)+'" B="'+str(B[0]).replace(HPrefix, HPrefixNum).replace(CPrefix, CPrefixNum)+'" E="'+str(B[1]).replace(HPrefix, HPrefixNum).replace(CPrefix, CPrefixNum)+'" />\n')
    [HPrefix, HPrefixNum, CPrefix, CPrefixNum] = cnt.getPrefixes()
    return ('<b color="'+str(color)+'" B="'+str(B[0]).replace(HPrefix, HPrefixNum).replace(CPrefix, CPrefixNum)+'" E="'+str(B[1]).replace(HPrefix, HPrefixNum).replace(CPrefix, CPrefixNum)+'" />\n')
