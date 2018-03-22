from app import *

categories = ['future concerns','exam stress','lack of sleep','overload at work','physical appearance','confrontations with parents']#TODO
subcateg = [['Low self esteem',' Low confidence','Resistant to change','Competition'],['External pressure','Internal pressure','Lack of preparation'],['Chronological Illness',
'Work pressure','Addiction'],['Environmental factors','Heatlh issues','Negativity','Low productivity'],['Media comparison','Genetic','Low self esteem'],['Authority figure',
'Generation gap','Grades','Underestimation of the elder generation']]
solutions =[['take up aptitude tests in terms of careers','Mix with people of your own strata initially to increase your self-confidence','one needs to start becoming strong emotionally in order to consider future in terms of family and friends',' Learn from your competitor’s strategies and success instead of getting demotivated.'],['Have faith in your preparation and don’t get demotivated by others.','- do not procrastinate','time management'],
['Consult a doctor','time management','Set time and frequency limits and follow them rigorously.'],['Keep a balance between everything you do','Consult a docor and follow the regime prescribed','subjective solutions on the basis of work','Be confident and work on  your weaknesses to perform well'],
['increase self esteem','one needs to understand that everyone is different and everyone has different ways of living life.','its okay to be the way I am kinda attitude should be inculcated!'],
['Best way is to talk and find a mutual solution.','Try to explain your perspective without opposing theirs','Perform self-analysis and do your best.','inculcating empathy for the elder generation! ']]
 
lencateg = len(categories)
useroptions = []
i = 0
for i in range(lencateg):
    #useroptions.append([])
	ip = input('Are you worried about ' + categories[i])
	#get input from user forgot the code about it
	#intput = getinput() #correct this pls TODO
	intput = str(m)
	if (input == 'yes'): #TODO
		useroptions.append(i) #useroptions=[0]
	i = i+1
print(useroptions)
i=0
while i< len(useroptions):
	tmplist = (subcateg[useroptions[i]])
	p=0
	while p < len(tmplist):
		ip = input(tmplist[p])
		if(ip == '1'):
			print (solutions[i][p])
		p = p+1
	i=i+1

'''while i< len(useroptions):
	#solutions.append(usersuboptions[i])
	#print(solutions[usersuboptions[i]])#usersuboptions=[1,2,5]
	tmplist = solutions[usersuboptions[i]]
	p=0
	while p < len(tmplist):
		print(tmplist[p])
		p = p+1
	i=i+1
	'''