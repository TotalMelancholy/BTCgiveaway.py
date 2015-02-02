import praw

import time


###########################
# READ ALL COMMENTS FIRST #
###########################

print('TO END SCRIPT EARLY: Ctrl + C')

r = praw.Reddit('Giveaway script: auto tips written by /u/TotalMelancholy')
r.login('USERNAME', 'PASSWORD') #Edit these fields, don't worry only you can see them
already_done = []
ignore = [''] #add your username to this list the you don't try to tip yourself
total = 0
count = 0

maxPeople = 10 #change this to the number of people you want to tip
tip = '$0.10' #change this to whatever you want to tip (can be USD or bits!) ex. '100 bits'


while count < maxPeople: 
    submission = r.get_submission('SUBMISSIN_LINK') #copy and paste the URL to your giveaway post here
    all_comments = submission.comments
    flat_comments = praw.helpers.flatten_tree(submission.comments)    

    for comment in flat_comments:
        if not comment.author:
            continue
        author = comment.author
        user = author.name
        cmt = comment.body
        
        if author not in already_done and user not in ignore:
            comment.reply(tip + ' /u/changetip')
            already_done.append(author)
            count = count + 1
            total = total + tip
            print('You have tipped ' +str(count) ' people')

    time.sleep(15)
    
if count >= maxPeople:
    print('Maximum participants met. Script ended')    
    
                   


