from flask import Flask

app = Flask(__name__)

@app.route('/list_services')
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

if __name__ == '__main__':
    app.run()
