from flask import Flask, request, render_template, jsonify, session, url_for
from functools import wraps
# from flask.ext.bcrypt import Bcrypt
# from wtforms.fields import SelectField
from db import Mdb
# import jwt
# import datetime
import json
import traceback

app = Flask(__name__)
# bcrypt = Bcrypt(app)
mdb = Mdb()

app.config['secretkey'] = 'some-strong+secret#key'
app.secret_key = 'F12Zr47j\3yX R~X@H!jmM]Lwf/,?KT'


def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'missing token!'})

        try:
            data = jwt.decode(token, app.config['secretkey'])
        except:
            return jsonify({'message': 'invalid token!'})

        return f(*args, **kwargs)

    return decorated


##############################################################################
#                                                                            #
#                                   bootstrap                                #
#                                                                            #
##############################################################################
##################################
#           step 1-4             #
##################################
@app.route('/bootstrap')
@app.route('/')
def bootstrap():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/login.html', **templateData)


@app.route('/grid')
def grid():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/grid.html', **templateData)


@app.route('/image')
def image():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/image.html', **templateData)


@app.route('/typography')
def typography():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/typography.html', **templateData)


@app.route('/table')
def table():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/table.html', **templateData)


##################################
#           step 5-8             #
##################################
@app.route('/jumbotrom')
def jumbotrom():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/jumbotrom.html', **templateData)


@app.route('/well')
def well():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/well.html', **templateData)


@app.route('/alert')
def alert():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/alert.html', **templateData)


@app.route('/button')
def button():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/button.html', **templateData)


##################################
#           step 9-12            #
##################################
@app.route('/buttons')
def buttons():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/buttons.html', **templateData)


@app.route('/glyphicons')
def glyphicons():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/glyphicons.html', **templateData)


@app.route('/lable')
def lable():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/lable.html', **templateData)


@app.route('/progress')
def progress():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/progress.html', **templateData)


##################################
#           step 13-16           #
##################################
@app.route('/pagination')
def pagination():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/pagination.html', **templateData)


@app.route('/pager')
def pager():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/pager.html', **templateData)


@app.route('/list')
def list():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/list.html', **templateData)


@app.route('/panel')
def panel():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/panel.html', **templateData)


##################################
#           step 17-20           #
##################################
@app.route('/dropdown')
def dropdown():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/dropdown.html', **templateData)


@app.route('/collapse')
def collapse():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/collapse.html', **templateData)


@app.route('/tab')
def tabs():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/tabs.html', **templateData)


@app.route('/navbar')
def navbar():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/navbar.html', **templateData)


##################################
#           step 21-24           #
##################################
@app.route('/form')
def form():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/form.html', **templateData)


@app.route('/input')
def input():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/input.html', **templateData)


@app.route('/input2')
def input2():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/input2.html', **templateData)


@app.route('/sizing')
def sizing():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/sizing.html', **templateData)


##################################
#           step 25-28           #
##################################
@app.route('/media')
def media():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/media.html', **templateData)


@app.route('/carousel')
def carousel():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/carousel.html', **templateData)


@app.route('/model')
def model():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/model.html', **templateData)


@app.route('/tooltip')
def tooltip():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/tooltip.html', **templateData)


##################################
#           step 29-31           #
##################################
@app.route('/popover')
def popover():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/popover.html', **templateData)


@app.route('/scrollspy')
def scrollspy():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/scrollspy.html', **templateData)


@app.route('/affix')
def affix():
    templateData = {'title': 'Bootstrap Page'}
    return render_template('bootstrap/affix.html', **templateData)


@app.route('/registration', methods=['POST'])
def registration():
    try:
        name = request.form['name']
        email = request.form['email']
        type = request.form['type']
        password = request.form['password']

        mdb.register(name, email, type, password)
        print('Registration is successfully')

    except Exception as exp:
        print(traceback.format_exc())
    return render_template('home.html', session=session)


##############################################################################
#                                                                            #
#                                  EMPLOYEE                                  #
#                                                                            #
##############################################################################
@app.route('/employee')
def employee():
    templateData = {'title': 'Home Page'}
    return render_template('employee/signin.html', **templateData)


@app.route('/clear1')
def clearsession1():
    session.clear()
    return render_template('employee/signin.html', session=session)


##############################################################################
#                                                                            #
#                                INTERVIEWER                                 #
#                                                                            #
##############################################################################
@app.route('/interviewer')
def interviewer():
    templateData = {'title': 'Home Page'}
    return render_template('interviewer/signin.html', **templateData)


@app.route('/clear2')
def clearsession2():
    session.clear()
    return render_template('interviewer/signin.html', session=session)


##############################################################################
#                                                                            #
#                                  TRAINEE                                   #
#                                                                            #
##############################################################################
@app.route('/trainee')
def trainee():
    templateData = {'title': 'Home Page'}
    return render_template('trainee/signin.html', **templateData)


@app.route('/clear3')
def clearsession3():
    session.clear()
    return render_template('trainee/signin.html', session=session)

# its for testing

@app.route('/admin_login')
def admin_login():
    templateData = {'title': 'Login Page'}
    return render_template('admin/login.html', **templateData)


@app.route('/signin')
def signin():
    templateData = {'title': 'Signin Page'}
    return render_template('signin.html', **templateData)


@app.route('/protected')
@token_required
def protected():
    return 'protected'


@app.route('/unprotected')
def unprotected():
    return 'unprotected'


@app.route('/login', methods=['POST'])
def login():
    ret = {}
    try:
        sumSessionCounter()
        company_email = request.form['company_email']
        password = request.form['password']
        if mdb.user_exists(company_email, password):
            # mdb.get_data(company_email)
            session['name'] = company_email
            # mdb.get_data(company_email)

            # login successfully

            expiry = datetime.datetime.utcnow() + datetime.\
                timedelta(minutes=30)
            token = jwt.encode({'company_email': company_email, 'exp': expiry},
                               app.config['secretkey'], algorithm='HS256')

            ret['msg'] = 'Login Successfull'
            ret['error'] = 0
            ret['token'] = token.decode('UTF-8')
            templateData = {'title': 'singin page'}
        else:
            return render_template('index.html', session=session)
    except Exception as exp:
        ret['msg'] = '%s' % exp
        ret['error'] = 1
        print(traceback.format_exc())
    # return jsonify(ret)
    return render_template('home.html', session=session)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
