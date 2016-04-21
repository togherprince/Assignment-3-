import os
import json
import requests
from flask import Flask, render_template


app = Flask(__name__)

app.config.update(
    DEBUG=True,
)
# connect the app with cloudant
def confdb():
    try:
        vcap = json.loads(os.getenv("VCAP_SERVICES"))['cloudantNoSQLDB']

        cl_username = vcap[0]['credentials']['username']
        cl_password = vcap[0]['credentials']['password']

        url         = vcap[0]['credentials']['url']
        auth        = ( cl_username, cl_password )
		

    except:
        return 'A Cloudant service is not bound to the application.  Please bind a Cloudant service and try again.'
    return auth

# go to UI page
@app.route('/')
def welcome():
      return render_template('home.html')

@app.route('/Amsterdam')
def stata():
    # call the DB connection + request 4 queries and send them to second.html
    auth=confdb()
    r1 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/type?limit=100&group=true',auth=auth)
    data= r1.json()
    r2 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/policy-view?limit=100&group=true',auth=auth)
    data2=r2.json()
    r3 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/availablity-view?limit=100&group=true',auth=auth)
    data3=r3.json()
    r4 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/new-view?limit=300&group=true',auth=auth)
    data4=r4.json()
    return render_template('second.html', data=data,data2=data2,data3=data3,data4=data4)

@app.route('/Dublin')
def statd():
    auth=confdb()
    r1 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/type?limit=100&group=true',auth=auth)
    data= r1.json()
    r2 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/policy-view?limit=100&group=true',auth=auth)
    data2=r2.json()
    r3 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/availablity-view?limit=100&group=true',auth=auth)
    data3=r3.json()
    r4 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/new-view?limit=300&group=true',auth=auth)
    data4=r4.json()
    return render_template('second.html', data=data,data2=data2,data3=data3,data4=data4)

	
@app.route('/London')
def statl():
    auth=confdb()
    r1 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/type?limit=100&group=true',auth=auth)
    data= r1.json()
    r2 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/policy-view?limit=100&group=true',auth=auth)
    data2=r2.json()
    r3 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/availablity-view?limit=100&group=true',auth=auth)
    data3=r3.json()
    r4 = requests.get('https://214362f6-399d-4bda-a371-5dbbb848161c-bluemix.cloudant.com/airbnbt/_design/D1/_view/new-view?limit=300&group=true',auth=auth)
    data4=r4.json()
    return render_template('second.html', data=data,data2=data2,data3=data3,data4=data4)

	
    
port = os.getenv('VCAP_APP_PORT', '5000')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
