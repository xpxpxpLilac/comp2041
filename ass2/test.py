#!/usr/bin/python3
from collections import defaultdict
from datetime import datetime
import re,os,glob
students_dir = "static/dataset-medium"
post=defaultdict(dict)








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
	#student_to_show = session['zid']
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
	#student_to_show = session['zid']
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
	#if os.path.exists(path):
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
			p =find_one_post(files)
			e = extract_user_personal_info(student_to_show)
			post[index1] = { 'message':p['message'], 'time':p['time'], 'full_name':e['full_name'], 'img_path': e['img_path'], 'comment':{}} 
	for files in glob.glob(os.path.join(students_dir, student_to_show,'*.txt')):
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
			post[index1]['comment'][index2]= {'message':c['message'],'time':c['time'], 'zid':c['zid'], 'full_name':e['full_name'], 'reply':{}}
	for files in glob.glob(os.path.join(students_dir, student_to_show,'*.txt')):
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
			post[index1]['comment'][index2]['reply'][index3] = { 'message':c['message'], 'time':c['time'], 'zid':c['zid'], 'full_name':e['full_name']}
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
				post[ids][index1] = { 'message':p['message'], 'time':p['time'], 'full_name':e['full_name'], 'img_path': e['img_path'], 'comment':{}} 
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			if re.search('^[0-9]+-[0-9]+.txt',name):
				newlist = []
				#print(name)
				sur = re.sub('.txt','',name)
				newlist = sur.split("-")
				index1 = newlist[0]
				index2 = newlist[1]
				c = extract_comment(files)
				user = c['zid']
				e = extract_user_personal_info(user)
				#post[ids][index1][index2] = "intersting"
				post[ids][index1]['comment'][index2]= {'message':c['message'],'time':c['time'], 'zid':c['zid'], 'full_name':e['full_name'], 'reply':{}}
		for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
			name = re.sub('.*/','',files)
			if re.search('^[0-9]+-[0-9]+-[0-9]+.txt',name):
				newlist = []
				print("now is "+ids +" name: "+name)
				sur = re.sub('.txt','',name)
				newlist = sur.split("-")
				index1 = newlist[0]
				index2 = newlist[1]
				index3 = newlist[2]
				c = extract_comment(files)
				user = c['zid']
				e = extract_user_personal_info(user)
				post[ids][index1]['comment'][index2]['reply'][index3] = { 'message':c['message'], 'time':c['time'], 'zid':c['zid'], 'full_name':e['full_name']}
	return post
def add_new_friends(new_friend):
	user = "z5190009"
	newline = ", "+ str(new_friend)+ ")\n"
	details_filename = os.path.join(students_dir, user, "student.txt")
	with open(details_filename,'r') as f:
		lines = f.readlines()
	f = open(details_filename,"w")
	for line in lines:
		if re.search("^friends:",line):
			line = re.sub('\)\n',newline,line)
		f.write(line)
	f.close()
	print("finish")


student_to_show = "z5190009"
post = extract_one_user_post_comment(student_to_show)

add_new_friends("z5193755")

#all_zid = [dI for dI in os.listdir(students_dir) if os.path.isdir(os.path.join(students_dir,dI))]
#for ids in all_zid:
#	for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
#		name = re.sub('.*/','',files)
#		if re.search('^[0-9]+.txt',name):
#			#print(name)
#			index1 = re.sub('.txt','',name)
#			p =find_one_post(files)
#			e = extract_user_personal_info(ids)	
#			post[ids][index1] = { 'message':p['message'], 'time':p['time'], 'full_name':e['full_name'], 'img_path': e['img_path'], 'comment':{}} 
#	for files in glob.glob(os.path.join(students_dir, ids,'*.txt')):
#		name = re.sub('.*/','',files)
#		if re.search('^[0-9]+-[0-9]+.txt',name):
#			newlist = []
#			print(name)
#			sur = re.sub('.txt','',name)
#			newlist = sur.split("-")
			




