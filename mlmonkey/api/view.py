import flask
import json
from flask import make_response
#from mlmonkey.status import Status
#from status import Status
# ref https://github.com/Alwayswithme/sysinfo

#from mlmonkey import constants
import constants
from utils import sysinfo
#import scenario
#import scheduler
#from mlmonkey.utils import sysinfo
#from mlmonkey import scenario
#from mlmonkey import scheduler

blueprint = flask.Blueprint(__name__, __name__)


@blueprint.route('/', methods=['GET'])
def home():
    return "homepage"


@blueprint.route('/system', methods=['GET'])
def show_hw_info():
    file = constants.SYSTEM_JSON
    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
        return flask.jsonify(data)
    except FileNotFoundError:
        return "System information file not found, generate it with a POST request with {action:detect}"

@blueprint.route('/system', methods=['POST'])
def get_hw_info():
    file = constants.SYSTEM_JSON
    if flask.request.args['action'] == 'detect':
        gpus = sysinfo.get_graphics_card_info()
        cpu = sysinfo.get_cpu_hwinfo()
        memory = sysinfo.get_mem_info()
        disk = sysinfo.get_disk_info()

        data = {
            'cpu': cpu,
            'memory': memory,
            'disk': disk,
            'gpu': gpus
        }
        with open(file, 'w') as json_file:
            json.dump(data, json_file)
            
    elif flask.request.args['action'] == 'setup':
        return "Setup CUDA & nvidia-docker"
    elif flask.request.args['action'] == 'verify':
        return "Verify that the number of gpus"
    else:
        return "Unnkown action requested"
    with open(file, 'r') as json_file:
        data = json.load(json_file)
    return flask.jsonify(data)


@blueprint.route('/datasets', methods=['GET'])
def show_dataset_info():
    return "Show dataset info"
      
      
@blueprint.route('/datasets/<id>', methods=['POST'])
def dataset_action(id):
    
    if flask.request.args['action'] == 'detect':
        return "Detect dataset with id "+str(id)
    elif flask.request.args['action'] == 'download':
        return "Download dataset with id "+str(id)
    elif flask.request.args['action'] == 'verify':
        return "Verify dataset with id "+str(id)
    elif flask.request.args['action'] == 'process':
        return "Process dataset with id "+str(id)    
    else:
      return "Unnkown action requested"
      
@blueprint.route('/benchmarks', methods=['GET'])
def show_benchmark_info():
    return "Show benchmark info"
      
      
@blueprint.route('/benchmarks/<id>', methods=['POST'])
def benchmark_action(id):
    
    if flask.request.args['action'] == 'build':
        return "Build benchmark with id "+str(id)
    elif flask.request.args['action'] == 'train':
        return "Train benchmark with id "+str(id)
    elif flask.request.args['action'] == 'stop':
        return "Stop benchmark with id "+str(id)
    else:
      return "Unnkown action requested"
#@blueprint.route('/scenario', methods=['POST'])
#def create_scenario():
#    # Get data from the scenario form
#    name = flask.request.form.get('name')
#    data_dir = flask.request.form.get('data_dir')
#    num_gpus = flask.request.form.get('num_gpus')
#    batch_size = flask.request.form.get('batch_size')
#    model = flask.request.form.get('model')
#    variable_update = flask.request.form.get('variable_update')
#    fp16 = flask.request.form.get('fp16')
#    optimizer = flask.request.form.get('optimizer')
#    data_format = flask.request.form.get('data_format')
#    num_epochs = flask.request.form.get('num_epochs')
#    status = Status.INIT
#    task = scenario.Scenario(
#        name = name,
#        data_dir=data_dir,
#        num_gpus=num_gpus,
#        batch_size=batch_size,
#        model=model,
#        variable_update=variable_update,
#        fp16=fp16,
#        optimizer=optimizer,
#        data_format=data_format,
#        num_epochs=num_epochs,
#        status = status
#    )
#    scheduler.add_task(task)
#
#    return flask.jsonify({'id': task.id()})
#
#
#@blueprint.route('/scenario/', methods=['GET'])
#def show_all_scenario():
#    tasks = scheduler.get_tasks()
#    response = []
#    for task in tasks:
#        response.append(task.json_dict())
#
#    return flask.jsonify(response)
#
#
#@blueprint.route('/scenario/result', methods=['GET'])
#def show_all_scenario_result():
#    tasks = scheduler.get_tasks()
#    response = []
#    for task in tasks:
#        if task.status is Status.DONE:
#            response.append(task.json_dict())
#    return flask.jsonify(response)
#
#
#@blueprint.route('/scenario/abort', methods=['POST'])
#def abort_all_scenario():
#    pass
#
#
#@blueprint.route('/scenario/run', methods=['POST'])
#def run_all_scenario():
#    pass
#
#
#@blueprint.route('/scenario/<job_id>', methods=['DELETE'])
#def delete_scenario(job_id):
#    scheduler.delete_task(job_id)
#    return True
#
#
#@blueprint.route('/scenario/<job_id>', methods=['GET'])
#def show_scenario(job_id):
#    task = scheduler.get_task(job_id)
#    response = task.json_dict()
#    return flask.jsonify(response)
#
#
#@blueprint.route('/bandwidth', methods=['POST', 'GET'])
#def run_bandwidth():
#    file_path = constants.BANDWIDTH_TXT
#    if flask.request.method == 'POST':
#        info = sysinfo.init_bandwidth()
#        with open(file_path, 'w') as file:
#            file.write(info)
#
#    with open(file_path, 'r') as file:
#        info = file.read()
#    return make_response(info)
#
#
#
#
#
#@blueprint.route('/topology', methods=['POST', 'GET'])
#def run_topology():
#    # get folder or filepath by config
#    file_path = constants.TOPOLOGY_TXT
#    if flask.request.method == 'POST':
#        info = sysinfo.init_topology()
#        with open(file_path, 'w') as file:
#            file.write(info)
#
#    with open(file_path, 'r') as file:
#        info = file.read()
#    return make_response(info)
#
#
#@blueprint.errorhandler(401)
#def unauthorized():
#    pass
#
#
#@blueprint.errorhandler(403)
#def forbidden():
#    pass
#
#
#@blueprint.errorhandler(404)
#def item_not_found():
#    pass
#
#
#@blueprint.errorhandler(409)
#def conflict():
#    pass
