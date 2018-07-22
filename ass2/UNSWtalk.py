#!/web/cs2041/bin/python3.6.3
# written by andrewt@cse.unsw.edu.au October 2017
# as a starting point for COMP[29]041 assignment 2
# https://cgi.cse.unsw.edu.au/~cs2041/assignments/UNSWtalk/
import os,re, glob
from pathlib import Path
from collections import defaultdict
from flask import Flask, render_template, session, request
from datetime import datetime
students_dir = "static/dataset-medium";
app = Flask(__name__)
# Show unformatted details for student "n"
# Increment n and store it in the session cookie


@app.route('/', methods=['GET','POST'])
def home():
	session['zid'] = ''
	return render_template('login.html',error = "Welcome to UNSWTalk")

@app.route('/<f_id>', methods=['GET','POST'])
def friends(f_id):
	student_to_show = f_id
	details_filename = os.path.join(students_dir, student_to_show, "student.txt") # dataset-medium/z5555555/student.txt
	img_filename = os.path.join(students_dir, student_to_show, "img.jpg") # dataset-medium/z5555555/student.txt
	post_filename = os.path.join(students_dir, student_to_show) 

	user = session['zid'] 
	comment = request.form.get('comment', '')
	student = request.form.get('zid_name', '')
	filename = request.form.get('filename', '')
	postlist = extract_one_user_post_comment(student)
	if comment != '':
		num = int(re.sub('.txt','',filename))
		length = len(postlist[num]['comment'])
		new_file = str(num)+"-"+str(length)+".txt"
		now = datetime.utcnow()
		now = re.sub('\.[0-9]*','',str(now))
		filename = os.path.join(students_dir, student, new_file)
		with open(filename, 'w+') as f:
			f.write("from: "+ user+ "\n")
			f.write("message: "+comment+"\n")
			f.write("time:" + now + "\n")
			f.close
	personal = extract_user_personal_info(user)
	profile = extract_user_personal_info(student_to_show)
	friends = extract_user_friends_info(student_to_show)
	post = extract_post(student_to_show)
	post_with_comment = extract_one_user_post_comment(student_to_show)
	return render_template('friends.html', person = personal, friends = friends, post_comment = post_with_comment, order = reversed(sorted(post)), profile = profile, order_comment = reversed(sorted(post_with_comment.keys())))



@app.route('/first', methods=['GET','POST'])
def first():	

	zid = request.form.get('zid', '')
	password = request.form.get('password', '')
	zid = re.sub(r'\D', '', zid)
	zid = "z"+ zid

	filename = os.path.join(students_dir, zid) 
	if os.path.exists(filename):
		correct_password = read_student_password(zid)
		if password != correct_password:
			errorinfo = "wrong password"
			return render_template('login.html',error=errorinfo)
		else:
			session['zid'] = zid
			student_to_show = session['zid']
			user_post = request.form.get('User_post', '')

			if user_post != '':
				existed_post = extract_post(student_to_show)
				num = len(existed_post)
				new_file = str(num) + ".txt"
				now = datetime.utcnow()
				now = re.sub('\.[0-9]*','',str(now))
				filename = os.path.join(students_dir, student_to_show, new_file)
				with open(filename, 'w+') as f:
					f.write("from: "+ student_to_show+ "\n")
					f.write("message: "+user_post+"\n")
					f.write("time:" + now + "\n")
					f.close
			details_filename = os.path.join(students_dir, student_to_show, "student.txt") 
			img_filename = os.path.join(students_dir, student_to_show, "img.jpg") # dataset-medium/z5555555/student.txt
			post_filename = os.path.join(students_dir, student_to_show) 
	
			person = extract_user_personal_info(student_to_show)
			friends = extract_user_friends_info(student_to_show)
			post = extract_post(student_to_show)
			post_with_comment = extract_one_user_post_comment(student_to_show)
			time = time_order()
			return render_template('first.html', person = person, friends = friends, time = time, time_key = reversed(sorted(time)))
	else:	                     
		errorinfo = "unknown zid - are you enrolled in UNSW?"
		return render_template('login.html',error=errorinfo)

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
	student_to_show = session['zid']
	user_post = request.form.get('User_post', '')
	comment = request.form.get('comment', '')
	student = request.form.get('zid_name', '')
	filename = request.form.get('filename', '')
	postlist = extract_one_user_post_comment(student)
	if comment != '':
		num = int(re.sub('.txt','',filename))
		length = len(postlist[num]['comment'])
		new_file = str(num)+"-"+str(length)+".txt"
		now = datetime.utcnow()
		now = re.sub('\.[0-9]*','',str(now))
		filename = os.path.join(students_dir, student, new_file)
		with open(filename, 'w+') as f:
			f.write("from: "+ student_to_show+ "\n")
			f.write("message: "+comment+"\n")
			f.write("time:" + now + "\n")
			f.close
	if user_post != '':
		existed_post = extract_post(student_to_show)
		num = len(existed_post)
		new_file = str(num) + ".txt"
		now = datetime.utcnow()
		now = re.sub('\.[0-9]*','',str(now))
		filename = os.path.join(students_dir, student_to_show, new_file)
		with open(filename, 'w+') as f:
			f.write("from: "+ student_to_show+ "\n")
			f.write("message: "+user_post+"\n")
			f.write("time:" + now + "\n")
			f.close
	details_filename = os.path.join(students_dir, student_to_show, "student.txt") 
	img_filename = os.path.join(students_dir, student_to_show, "img.jpg") 
	post_filename = os.path.join(students_dir, student_to_show) 
	
	person = extract_user_personal_info(student_to_show)
	friends = extract_user_friends_info(student_to_show)
	post = extract_post(student_to_show)
	post_with_comment = extract_one_user_post_comment(student_to_show)
	time = time_order()
	return render_template('first.html', person = person, friends = friends, time = time, time_key = reversed(sorted(time)))


@app.route('/mention', methods=['GET','POST'])
def mention():
	student_to_show = session['zid']
	comment = request.form.get('comment', '')
	student = request.form.get('zid_name', '')
	filename = request.form.get('filename', '')
	postlist = extract_one_user_post_comment(student)
	if comment != '':
		num = int(re.sub('.txt','',filename))
		length = len(postlist[num]['comment'])
		new_file = str(num)+"-"+str(length)+".txt"
		now = datetime.utcnow()
		now = re.sub('\.[0-9]*','',str(now))
		filename = os.path.join(students_dir, student, new_file)
		with open(filename, 'w+') as f:
			f.write("from: "+ student_to_show+ "\n")
			f.write("message: "+comment+"\n")
			f.write("time:" + now + "\n")
			f.close
	mention = search_mention_me()
	person = extract_user_personal_info(student_to_show)
	friends = extract_user_friends_info(student_to_show)
	return render_template('mention.html', person = person, friends = friends, time = mention, time_key = reversed(sorted(mention)))


@app.route('/start', methods=['GET','POST'])
def start():	
	student_to_show = session['zid']
	user_post = request.form.get('User_post', '')
	comment = request.form.get('comment', '')
	filename = request.form.get('filename', '')
	new_friend = request.form.get('new_friend', '')
	postlist = extract_one_user_post_comment(student_to_show)
	if comment != '':
		num = int(re.sub('.txt','',filename))
		length = len(postlist[num]['comment'])
		new_file = str(num)+"-"+str(length)+".txt"
		now = datetime.utcnow()
		now = re.sub('\.[0-9]*','',str(now))
		filename = os.path.join(students_dir, student_to_show, new_file)
		with open(filename, 'w+') as f:
			f.write("from: "+ student_to_show+ "\n")
			f.write("message: "+comment+"\n")
			f.write("time:" + now + "\n")
			f.close
	if user_post != '':
		existed_post = extract_post(student_to_show)
		num = len(existed_post)
		new_file = str(num) + ".txt"
		now = datetime.utcnow()
		now = re.sub('\.[0-9]*','',str(now))
		filename = os.path.join(students_dir, student_to_show, new_file)
		with open(filename, 'w+') as f:
			f.write("from: "+ student_to_show+ "\n")
			f.write("message: "+user_post+"\n")
			f.write("time:" + now + "\n")
			f.close
	details_filename = os.path.join(students_dir, student_to_show, "student.txt")
	img_filename = os.path.join(students_dir, student_to_show, "img.jpg") 
	post_filename = os.path.join(students_dir, student_to_show) 
	
	personal = extract_user_personal_info(student_to_show)
	friends = extract_user_friends_info(student_to_show)
	#if new_friend not in friends:
	#	add_new_friends(new_friend)
	friends = extract_user_friends_info(student_to_show)
	post = extract_post(student_to_show)
	post_with_comment = extract_one_user_post_comment(student_to_show)
	p = defaultdict(dict)
	return render_template('start.html', person = personal, friends = friends, post_comment = post_with_comment, order_comment = reversed(sorted(post_with_comment.keys())), path = p)

@app.route('/search', methods=['GET','POST'])
def search():
	result_user=defaultdict(dict)
	result_post=defaultdict(dict)
	keyword = request.form.get('keyword', '')
	keyword = keyword.lower()
	my_regex = r"\b(?=\w)" + re.escape(keyword) + r"\b(?!\w)"
	student_to_show = session['zid']
	############################# name
	all_zid = [dI for dI in os.listdir(students_dir) if os.path.isdir(os.path.join(students_dir,dI))]    #????????????????????????????????
	for ids in all_zid:
		flag = 0
		img_filename = os.path.join(students_dir, ids, "img.jpg")
		filename = os.path.join(students_dir, ids, "student.txt")
		with open(filename) as f:
			for line in f:
				if re.search("full_name",line):
					line = re.sub('.*: *','',line)
					copy = line.lower()
					if re.search(keyword,copy):
						flag = 1
						result_user[ids]['full_name'] = line
						break
		if flag:
			if os.path.exists(img_filename):
				result_user[ids]['img_path'] = img_filename
			else:
				result_user[ids]['img_path'] = "static/images.png"
		else:
			continue	
	################################### post
	for ids in all_zid:
		for files in glob.glob(os.path.join(students_dir, ids,'[0-9]*.txt')):
			with open(files) as f:
				for line in f:
					if re.search("^message:",line):
						line = re.sub('^message: *','',line)
						copy = line.lower()
						if re.search(my_regex,copy):
							path = os.path.join(files)
							index = re.sub('.*/', '', files)
							p = find_one_post(path)
							result_post[line]['time'] = p['time'] 
							result_post[line]['zid'] = ids
							info = extract_user_personal_info(ids)
							result_post[line]['full_name'] = info['full_name']
							result_post[line]['img_path'] = info['img_path']			
	personal = extract_user_personal_info(student_to_show)
	return render_template('search.html',person = personal, result_user = result_user, result_post = result_post)



def read_student_password(znum):
	filename = os.path.join(students_dir, znum, "student.txt") 
	with open(filename) as f:
		for line in f:
			if re.search("password",line):
				password = re.sub('password: *','',line)
				password = re.sub('\n','',password)
	return password

def extract_user_personal_info(student_to_show):
	personal=defaultdict(dict)
	details_filename = os.path.join(students_dir, student_to_show, "student.txt") # dataset-medium/z5555555/student.txt
	img_filename = os.path.join(students_dir, student_to_show, "img.jpg") # dataset-medium/z5555555/student.txt
	with open(details_filename) as f:
		personal['birthday'] = ""
		personal['program'] = ""
		personal['home'] = ""
		for line in f:
			if re.search("full_name",line):
				personal['full_name'] = re.sub('.*: *','',line)
			elif re.search("birthday",line):
				personal['birthday'] = re.sub('.*: *','',line)
			elif re.search("zid",line):
				line = re.sub('.*: *','',line)
				personal['zid'] = re.sub('\n','',line)
			elif re.search("program",line):
				personal['program'] = re.sub('.*: *','',line)
			elif re.search("home_suburb",line):
				personal['home'] = re.sub('.*: *','',line)
	if os.path.exists(img_filename):
		personal['img_path'] = img_filename
	else:
		personal['img_path'] = "static/images.png"		
	
	return personal

def extract_user_friends_info(student_to_show):
	friends_info=defaultdict(dict)
	details_filename = os.path.join(students_dir, student_to_show, "student.txt") 
	with open(details_filename) as f:
		for line in f:
			if re.search("friends",line):
				line = re.sub('.*: *','',line)
				line = re.sub('[()]*','',line)
				line = re.sub('\n','',line)
				friends = line.split(", ")	
	for id in friends:
		id_filename = os.path.join(students_dir, id, "student.txt") 
		id_img = os.path.join(students_dir, id, "img.jpg") 
		with open(id_filename) as d:
			for line in d:
				if re.search("full_name",line):
					fullname = re.sub('.*: *','',line)
		if os.path.exists(id_img):
			img = id_img
		else:
			img = "static/images.png"
		friends_info[id] = {'name':fullname, 'img':img }
	return friends_info

def extract_post(student_to_show):
	post=defaultdict(dict)
	count = 0
	files = str(count) + ".txt"
	post_filename = os.path.join(students_dir, student_to_show, files) 
	while os.path.exists(post_filename):
		with open(post_filename) as f:
			for line in f:
				if re.search("^message",line):
					line = re.sub("^message: *",'',line)
					message = re.sub('\\n','\n',line)
				if re.search("^time",line):
					line = re.sub("^time: *",'',line)
					line = re.sub('T',' ',line)
					time = re.sub('\+.*','',line)
		post[count] = { 'message': message, 'time': time }
		count += 1
		files = str(count) + ".txt"
		post_filename = os.path.join(students_dir, student_to_show, files) 
	return post

def find_one_post(path):
	post=defaultdict(dict)
	with open(path) as f:
		for line in f:
			if re.search("^message",line):
				line = re.sub("^message: *",'',line)
				message = re.sub('\\n','\n',line)
				post['message'] = message
			if re.search("^time",line):
				line = re.sub("^time: *",'',line)
				line = re.sub('T',' ',line)
				time = re.sub('\+.*','',line)
				post['time'] = time	
	return post

def extract_comment(path):
	post=defaultdict(dict)
	with open(path) as f:
		for line in f:
			if re.search("^message",line):
				line = re.sub("^message: *",'',line)
				message = re.sub('\\n','\n',line)
				post['message'] = message
			if re.search("^time",line):
				line = re.sub("^time: *",'',line)
				line = re.sub('T',' ',line)
				time = re.sub('\+.*','',line)
				post['time'] = time
			if re.search("^from",line):
				line = re.sub("^from: *",'',line)
				line = re.sub('\n','',line)
				post['zid'] = line	
	return post

def extract_one_user_post_comment(student_to_show):
	post=defaultdict(dict)
	for files in glob.glob(os.path.join(students_dir, student_to_show,'*.txt')):
		name = re.sub('.*/','',files)
		if re.search('^[0-9]+.txt',name):
			index1 = re.sub('.txt','',name)	
			index1 = int(index1)			
			p =find_one_post(files)
			e = extract_user_personal_info(student_to_show)
			post[index1] = { 'zid':student_to_show ,'message':p['message'], 'time':p['time'], 'full_name':e['full_name'], 'img_path': e['img_path'], 'file':name, 'comment':{}} 
	for files in glob.glob(os.path.join(students_dir, student_to_show,'*.txt')):
		name = re.sub('.*/','',files)
		if re.search('^[0-9]+-[0-9]+.txt',name):
			newlist = []
			sur = re.sub('.txt','',name)
			newlist = sur.split("-")
			index1 = int(newlist[0])
			index2 = newlist[1]
			c = extract_comment(files)
			user = c['zid']
			e = extract_user_personal_info(user)
			post[index1]['comment'][index2]= {'message':c['message'],'time':c['time'], 'zid':c['zid'], 'full_name':e['full_name'], 'file':name, 'reply':{}}
	for files in glob.glob(os.path.join(students_dir, student_to_show,'*.txt')):
		name = re.sub('.*/','',files)
		if re.search('^[0-9]+-[0-9]+-[0-9]+.txt',name):
			newlist = []
			sur = re.sub('.txt','',name)
			newlist = sur.split("-")
			index1 = int(newlist[0])
			index2 = newlist[1]
			index3 = newlist[2]
			c = extract_comment(files)
			user = c['zid']
			e = extract_user_personal_info(user)
			post[index1]['comment'][index2]['reply'][index3] = { 'message':c['message'], 'time':c['time'], 'zid':c['zid'], 'file':name, 'full_name':e['full_name']}
	return post

def extract_all_post_comment():
	post=defaultdict(dict)
	all_zid = [dI for dI in os.listdir(students_dir) if os.path.isdir(os.path.join(students_dir,dI))]
	for ids in all_zid:
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			if re.search('^[0-9]+.txt',name):
				index1 = re.sub('.txt','',name)
				p =find_one_post(files)
				e = extract_user_personal_info(ids)
				post[ids][index1] = { 'zid':ids, 'message':p['message'], 'time':p['time'], 'full_name':e['full_name'], 'img_path': e['img_path'], 'file':name, 'comment':{}} 
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			if re.search('^[0-9]+-[0-9]+.txt',name):
				newlist = []
				sur = re.sub('.txt','',name)
				newlist = sur.split("-")
				index1 = newlist[0]
				index2 = newlist[1]
				c = extract_comment(files)
				user = c['zid']
				e = extract_user_personal_info(user)
				post[ids][index1]['comment'][index2]= {'message':c['message'],'time':c['time'], 'zid':c['zid'], 'full_name':e['full_name'], 'file':name, 'reply':{}}
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			if re.search('^[0-9]+-[0-9]+-[0-9]+.txt',name):
				newlist = []
				sur = re.sub('.txt','',name)
				newlist = sur.split("-")
				index1 = newlist[0]
				index2 = newlist[1]
				index3 = newlist[2]
				c = extract_comment(files)
				user = c['zid']
				e = extract_user_personal_info(user)
				post[ids][index1]['comment'][index2]['reply'][index3] = { 'message':c['message'], 'time':c['time'], 'zid':c['zid'], 'file':name, 'full_name':e['full_name']}
	return post
def time_order():
	post=defaultdict(dict)
	timelist=defaultdict(dict)
	all_zid = [dI for dI in os.listdir(students_dir) if os.path.isdir(os.path.join(students_dir,dI))]
	for ids in all_zid:
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			if re.search('^[0-9]+.txt',name):
				index1 = re.sub('.txt','',name)
				p =find_one_post(files)
				e = extract_user_personal_info(ids)
				time = p['time']
				timelist[time] = { 'zid':ids, 'message':p['message'], 'time':p['time'], 'full_name':e['full_name'], 'img_path': e['img_path'], 'file':name, 'comment':{}} 
				post[ids][index1] = { 'zid':ids, 'message':p['message'], 'time':p['time'], 'full_name':e['full_name'], 'img_path': e['img_path'], 'file':name, 'comment':{}} 
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			if re.search('^[0-9]+-[0-9]+.txt',name):
				newlist = []
				sur = re.sub('.txt','',name)
				newlist = sur.split("-")
				index1 = newlist[0]
				index2 = newlist[1]
				c = extract_comment(files)
				user = c['zid']
				e = extract_user_personal_info(user)
				post[ids][index1]['comment'][index2]= {'message':c['message'],'time':c['time'], 'zid':c['zid'], 'full_name':e['full_name'], 'file':name, 'reply':{}}
				time = post[ids][index1]['time']
				timelist[time]['comment'][index2]= {'message':c['message'],'time':c['time'], 'zid':c['zid'], 'full_name':e['full_name'], 'file':name, 'reply':{}}
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			if re.search('^[0-9]+-[0-9]+-[0-9]+.txt',name):
				newlist = []
				sur = re.sub('.txt','',name)
				newlist = sur.split("-")
				index1 = newlist[0]
				index2 = newlist[1]
				index3 = newlist[2]
				c = extract_comment(files)
				user = c['zid']
				e = extract_user_personal_info(user)
				post[ids][index1]['comment'][index2]['reply'][index3] = { 'message':c['message'], 'time':c['time'], 'zid':c['zid'], 'file':name, 'full_name':e['full_name']}
				time = post[ids][index1]['time']
				timelist[time]['comment'][index2]['reply'][index3] = { 'message':c['message'], 'time':c['time'], 'zid':c['zid'],'file':name,  'full_name':e['full_name']}
	return timelist
def search_mention_me():
	post=defaultdict(dict)
	keyword = session['zid']
	k = r"\b(?=\w)" + re.escape(keyword) + r"\b(?!\w)"
	allpost = extract_all_post_comment()
	all_zid = [dI for dI in os.listdir(students_dir) if os.path.isdir(os.path.join(students_dir,dI))]
	for ids in all_zid:
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			with open(files) as f:
				for line in f:
					if re.search("^message",line):
						if re.search(k,line):
							name = re.sub('.txt','',name)		
							index1 = re.sub('-.*','',name)
							time = allpost[ids][index1]['time']
							post[time]= allpost[ids][index1]
							break
	return post

#def add_new_friends(new_friend):
#	user = session['zid']
#	newline = ", "+ str(new_friend)+ ")\n"
#	details_filename = os.path.join(students_dir, user, "student.txt")
#	with open(details_filename,'r') as f:
#		lines = f.readlines()
#	f = open(details_filename,"w")
#	for line in lines:
#		if re.search("^friends:",line):
#			line = re.sub(r')\n',newline,line)
#		f.write(line)
#	f.close()



if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True, port=2424)   #Ive change from 5000 to 2424

