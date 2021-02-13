from flask import Flask, render_tempelate, request, redirect, url_for
from flask import send_file
from flask import send_from_directory
import os
import shutil
import util as utils

isLoggedIn = False
isAuthRequired = True # ===> pick this from config

@app.route('/server',methods=['GET','POST'])  # writing it for both get and post
def serverMain():
	global isLoggedIn
	global isAuthRequired
	#first check fro config whether auth is enabled or not 
	#if login is required and 
	#render login page if not logged in
	if isLoggedIn == False and isAuthRequired == True:
		render_tempelate("serverLogin.html")
	else:
		#TODO: call the rbac server next layer 

@app.route('/login',methods=[POST])
def loginServer():
	global isLoggedIn
	global isAuthRequired
	userName = ""
	passWord = ""
	authSuccess = False
	uUid = utils.getuUid()
    #print"UUid is "
	#if already logged in or if auth is not required we need to proceed to next page 
	if isLoggedIn == False and isAuthRequired == True:
		userName = str(request.form.get('Username'))
		passWord = str(request.form.get('Password'))
		print userName
		print passWord
		#TODO: call post sql query with given username and password
		#like 
		#authSuccess = sqlQuery()
		authSuccess = True
		if authSuccess == True:
			#TODO: call the rbac server next layer i.e resource page 


portNum = 8001  #TODO: get it from config

if __name__ == '__main__':
	 app.run(host=='0.0.0.0', port = portNum, debug=True, threaded=True)

