# redis-nodes

Simple CLI that parses 'redis cluster nodes' input and a ip address to hostname map.

* [redis\-nodes](#redis-nodes)
  * [Install](#install)
  * [Execution](#execution)
    * [Poetry execution](#poetry-execution)
    * [Native python 3\.7](#native-python-37)
  * [Test](#test)

## Install

Requires python ^3.7

The [poetry](https://python-poetry.org/) package manager manages the projects virutalenv and dependencies.  If poetry is installed the following commands can be used to execute the CLI. A requirements.txt is provided if you want to manage your own virtualenv and run with native python instead. 

After installing poetry  this command will install a virtualenv w/ the respective dependencies.

    poetry install
    
To update dependencies

    poetry update
    
## Execution

The redis-nodes CLI has a single CLI entrypoint that takes the `redis cluster nodes` input and hostname to ip mapping as CLI parameters.

    poetry run redis-nodes -h                                                                               
        usage: redis-nodes [-h] -n NODES -H HOSTS
        
        Parses 'redis-cli cluster nodes' input and dumps master slave relationships
        
        optional arguments:
          -h, --help            show this help message and exit
          -n NODES, --nodes NODES
                                Path to file w/ `redis-cli cluster nodes` output,
                                assumes space deliminated csv
          -H HOSTS, --hosts HOSTS
                                Hostname to ip map, assumes space deliminated csv
     
### Poetry execution

Executing the CLI with `poetry run` will ensure the command is run in the correct virutalenv.  The following is an example w/ CLI executable.

    poetry run redis-nodes -H tests/fixtures/hosts.csv -n tests/fixtures/nodes.csv
        0-3276
        	master: redis-cluster001:7001
        	slaves: redis-cluster004:7002, redis-cluster003:7004
        
        
        3277-6554
        	master: redis-cluster002:7004
        	slaves: redis-cluster004:7001, redis-cluster001:7002
        
        .
        .
        . 	

Alternatively the `__main__.py` can be executed

    poetry run redis_nodes/__main__.py -H tests/fixtures/hosts.csv -n tests/fixtures/nodes.csv
    
If you'd rather run within virtual env.

    source ~/.virtualenvs/redis-nodes-qA0ThxLa-py3.7/bin/activate
    python redis_nodes/__main__.py -H tests/fixtures/hosts.csv -n tests/fixtures/nodes.csv
    
### Native python 3.7

Poetry is able to export a requirements.txt, if you wish to use native python instead.  NOTE: it's including the dev dependencies so pytest will also work.

    poetry export --dev -f requirements.txt > requirements.txt
    
Then to execute w/ requirements.txt
    
    python -m virtualenv ~/.virtualenvs/redis-nodes
    source /Users/fmarin/.virtualenvs/redis-nodes/bin/activate.fish
    pip install -r requirements.txt
    export PYTHONPATH=$PWD
    python redis_nodes/__main__.py -H tests/fixtures/hosts.csv -n tests/fixtures/nodes.csv
    .
    .
    .
    pytest
    
## Test    

Testing with pytest should also be executed with `poetry run` wrapper

    poetry run pytest                                                
        ====== test session starts =====================================================================================
        platform darwin -- Python 3.7.5, pytest-5.4.1, py-1.8.1, pluggy-0.13.1
        rootdir: /Users/fmarin/keekdageek/redis-nodes, inifile: pytest.ini
        plugins: mock-3.1.0, notifier-1.0.3
        collected 3 items                                                                                                                                                                                                                      
        
        tests/test_parser.py ...
        
        ======= 3 passed in 1.89s ======================================================================================
    
To run an autotester daemon using pytest watch

    poetry run ptw
    
