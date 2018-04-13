from flask import Flask,render_template,request
from difflib import SequenceMatcher
import os
app=Flask(__name__)
@app.route('/')
def display():
	return render_template('plag.html')
@app.route('/',methods=['POST'])
def plagarism():
	inputtxt=request.form['inputtext']
	similarity=[]
	for i in range(1,5):
		with open(os.path.join("Path of direcory where files are stored",str(i))) as ifile:
			givenfile=ifile.read()
		s=SequenceMatcher(None,inputtxt,givenfile)
		similarity.append(s.ratio())
	return render_template('result.html',inputtext=max(similarity)*100)
if __name__=="__main__":
	app.run("localhost",debug=True)
