from flask import jsonify, request
from . import api, app
import requests

LISTENER = app.config['LISTENER']


@api.route('/salt-state/events/push', methods=['POST'])
def process_push_event_from_salt_state_repo():
    app.logger.info('Push event notification from salt-state')
    data = request.get_json()
    app.logger.info('{}'.format(data))
    ref = data['ref']
    branch = ref.split('/')[-1]
    r = requests.put('{}/states/{0}'.format(LISTENER, branch), json=data)
    app.logger.info('Forwarded to salt proxy listener with status: {}'.format(r.status))
    return '', 204


@api.route('/salt-pillar/events/push', methods=['POST'])
def process_push_event_from_salt_pillar_repo():
    app.logger.info('Push event notification from salt-pillar')
    data = request.get_json()
    app.logger.info('{}'.format(data))
    ref = data['ref']
    branch = ref.split('/')[-1]
    r = requests.put('{}/pillars/{0}'.format(LISTENER, branch), json=data)
    app.logger.info('Forwarded to salt proxy listener with status: {}'.format(r.status))
    return '', 204


@api.route('/events/tag', methods=['POST'])
def process_tag_event():
    app.logger.info('Tag event notification')
    data = request.get_json()
    app.logger.info('{}'.format(data))
    #name = data['name']
    return jsonify(data)
