import ipaddress
import logging
import os

from flask import Flask, json, jsonify, render_template, request, wrappers
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from helpers.version import get_project_version


APP_DEBUG = bool(int(os.getenv('APP_DEBUG', 0)))
APP_VERSION = os.getenv('APP_VERSION', get_project_version())
APP_NAME = os.getenv('APP_NAME', f'devops-test-v{APP_VERSION}')

USER_NAME = os.getenv('USER_NAME', 'noviicee')
USER_URL = os.getenv('USER_URL', 'https://github.com/noviicee')

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://anamika:singh@localhost/mydatabase')

app = Flask(__name__)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': DATABASE_URL,
    'SQLALCHEMY_POOL_TIMEOUT': 60,
    'SQLALCHEMY_POOL_RECYCLE': 300,
})
db = SQLAlchemy(app)
migrate = Migrate(app, db)
logger = logging.getLogger(__name__)


# Health check
@app.route('/healthz')
def status() -> json:
    response = app.response_class(
        response=json.dumps({'result': 'OK - healthy'}),
        status=200,
        mimetype='application/json')
    app.logger.info('Status request successfull')
    return response


class Visitor(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(40), index=True, unique=True)
    visits = db.Column(db.Integer)


@app.route('/')
def index() -> wrappers.Response:
    data = {
        'app_name': APP_NAME,
        'app_version': APP_VERSION,

        'user_name': USER_NAME,
        'user_url': USER_URL,
    }

    if not DATABASE_URL:
        data['message'] = 'Database is not configured'
    else:
        try:
            data['db_version'] = db.engine.execute('SELECT version();').fetchone()[0]

            user_ip = 'n/a'
            try:
                x_forwarded_addrs = request.headers.getlist('x-forwarded-for')
                if x_forwarded_addrs:
                    user_ip = str(ipaddress.ip_address(x_forwarded_addrs[0]))
                else:
                    user_ip = request.remote_addr
            except ValueError as ex:
                logger.exception(f'Wrong IP address detected: {ex}')

            data['user_ip'] = user_ip

            visitor = Visitor.query.filter_by(ip=user_ip).first()
            if visitor:
                visitor.visits += 1
            else:
                visitor = Visitor(ip=user_ip, visits=1)

            db.session.add(visitor)
            db.session.commit()

            data['message'] = 'You have visited this page {visited!s} times. Total visitors: {total!s}'.format(
                visited=visitor.visits,
                total=Visitor.query.count(),
            )
        except Exception as ex:
            logger.exception(f'Query to DB failed: {ex}')
            data['message'] = 'Query to DB failed'

    return render_template('page.html', **data)


@app.route('/version')
def version() -> wrappers.Response:
    return jsonify({'version': get_project_version()})


if __name__ == '__main__':
    app.run(debug=APP_DEBUG)
