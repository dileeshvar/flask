from flask import Flask
from flask import request,redirect,render_template

import urllib
import re
import json as simplejson


app = Flask(__name__)

client_id = 'daeb516e46690f8013f0'
client_secret = '4c463b6d0ea65382ea6eb91d5ba86906788e6311'
github_url = 'https://github.com/login/oauth/'
redirect_uri = 'http://127.0.0.1:5000/user'


@app.route('/')
def index():
 return redirect('%sauthorize?client_id=%s&redirect_uri=%s' %(github_url,client_id,redirect_uri))


@app.route('/user', methods=['GET'])
def gitHub_userData():
 code = request.args.get('code')
 
 resp = urllib.urlopen('%saccess_token?client_id=%s&client_secret=%s&code=%s' %(github_url,client_id,client_secret,code))
 output = re.search('access_token=([0-9a-f]+)',resp.read()).group()
 
 resp1 = urllib.urlopen('https://github.com/api/v2/json/user/show?%s' %output)
 user_data = simplejson.loads(resp1.read())
 
 return render_template("user.html", user=user_data["user"])

if __name__ == '__main__':
 app.run(debug=True)

