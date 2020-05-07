# redis-nodes

Simple CLI that parses 'redis cluster nodes' input and a ip address to hostname map.

## Install

After installing [poetry](https://python-poetry.org/) this command will install a virtualenv w/ the respective dependencies.

    poetry install
    
To update dependencies

    poetry update    
    
## Exec

Executing the CLI with `poetry run` will ensure the command is run in the correct virutalenv

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
    
