from flask import Flask, render_template
from flask import jsonify
from test import context



app = Flask(__name__)

@app.route('/services/list')
def list_service():

    service_list = {"services":[
        "cart","demo","extra","cheddar"
    ]
     }
    return service_list

@app.route('/rollback_service')
def rollback_service():
    rollback_result = {"rollback":"cheddar", "version":"v2.2.3"}
    return rollback_result

@app.route('/users/<user>')
def users(user):
   return render_template('user.html', name = user)

@app.route('/servers/json/<server>')
def servers(server):
   return render_template('servers.json', name = server)

@app.route('/welcome/<country>/<username>', methods=['GET','POST'])
def welcome(country, username):
        return jsonify({'name': username, 'country': country}), 200



if __name__ == '__main__':
    app.run()
