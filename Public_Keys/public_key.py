def handler(context, inputs):
    #Add requester email, and github usernames, of potential requesters.
    users = {
        "user1_email": "user1_githubusername",
        "user2_email": "user2_githubusername"
    }
    
    #Get input
    requester = str(inputs["__metadata"]["userName"]) 
    print ("Requester is : ",requester)
    
    #Copy Input to output
    outputs = {}
    outputs["customProperties"] = inputs["customProperties"]
    
    #Set new value based on requester
    outputs["customProperties"]["github"] = users[requester]
    print ("Github Username is : " + users[requester])

    return outputs