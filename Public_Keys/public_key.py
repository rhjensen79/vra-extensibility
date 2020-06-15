def handler(context, inputs):
    #Get input
    requester = str(inputs["__metadata"]["userName"]) 
    print ("Requester is : ",requester)
    
    outputs = {}
    outputs["customProperties"] = inputs["customProperties"]
    
    #Set new value based on input
    if requester == 'xxx@xxx.xx':
        outputs["customProperties"]["github"] = 'xxxxxx'
    if requester == 'xxx@xxx.xx':
        outputs["customProperties"]["github"] = 'xxxxxx'
    else:
        outputs["customProperties"]["github"] = 'xxxxxx'

    print ("Github Username is :",outputs["customProperties"]["github"])
    return outputs