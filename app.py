from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def list_service():

    service_list = {"services":[
        "service-list":"/services/list",
        "rollback_service":"/rollback_service'",
        "/users/<user>":"/users/<user>",
        "/servers/json":"/servers/json",
    ]
     }
    return service_list

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

if __name__ == '__main__':
    app.run()
