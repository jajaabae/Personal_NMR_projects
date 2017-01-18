def textForCorrelation(cor, cor_color, cnt):
    [HPrefix, HPrefixNum, CPrefix, CPrefixNum] = cnt.getPrefixes()
    
    arrowText = """<arrow
 id="%s"
 color="%s"
 FillType="%s"
 ArrowheadHead="%s"
 ArrowheadType="%s"
 HeadSize="%s"
 ArrowheadCenterSize="%s"
 ArrowheadWidth="%s"
 AngularSize="%s"
 ArrowSource="%s"
 ArrowTarget="%s"
/>\n"""
    arrowId="66"
    color="4"
    FillType="None"
    ArrowheadHead="HalfRight"
    ArrowheadType="Solid"
    HeadSize="400"
    ArrowheadCenterSize="400"
    ArrowheadWidth="200"
    AngularSize="30"
    ArrowSource=cor[0].replace(HPrefix, HPrefixNum).replace(CPrefix, CPrefixNum)
    ArrowTarget=cor[1].replace(HPrefix, HPrefixNum).replace(CPrefix, CPrefixNum)
    #print 'cor', cor


    color = cor_color
    
    arrowText = arrowText % (arrowId, color, FillType, ArrowheadHead, ArrowheadType, HeadSize, ArrowheadCenterSize, ArrowheadWidth, AngularSize, ArrowSource, ArrowTarget)
    """
    if cor[2]=='c':
        #print cor
        #color="7"
        arrowText = arrowText % (arrowId, color, FillType, ArrowheadHead, ArrowheadType, HeadSize, ArrowheadCenterSize, ArrowheadWidth, AngularSize, ArrowSource, ArrowTarget)
        #print arrowText
        return arrowText
    if cor[2]=='m':
        #print 'cor', cor
        #color="8"
        arrowText = arrowText % (arrowId, color, FillType, ArrowheadHead, ArrowheadType, HeadSize, ArrowheadCenterSize, ArrowheadWidth, AngularSize, ArrowSource, ArrowTarget)
        #print arrowText
        return arrowText
    if cor[2]=='r':
        #print 'cor', cor
        #color="4"
        arrowText = arrowText % (arrowId, color, FillType, ArrowheadHead, ArrowheadType, HeadSize, ArrowheadCenterSize, ArrowheadWidth, AngularSize, ArrowSource, ArrowTarget)
        #print arrowText
        return arrowText
    return ''
    """
    #print color, cor
    return arrowText
