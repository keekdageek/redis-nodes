# Seeded with devops-scaffold/roles/project by fmarin at 03/09/2020, 13:14:43 
import pytest
from redis_nodes.topology import Topology
import ipdb

@pytest.fixture
def topology():
    ip_hosts = {}
    with open('./tests/fixtures/hosts.csv') as fp:
        line = fp.readline()
        while line:
            host_ip = line.split()
            ip_hosts[host_ip[1]] = host_ip[0]
            line = fp.readline()
    return Topology(ip_hosts, "./tests/fixtures/nodes.csv")


def test_parser_columns(topology):
    assert len(topology.df.columns) == 10

def test_masters(topology):
    masters = topology.masters()
    assert len(masters) == 5
    assert masters[0].row['range_start'] == 0
    assert masters[4].row['range_start'] == 13108
    assert masters[1].hostname == 'redis-cluster002'
    assert masters[2].hostname == 'redis-cluster002'

def test_slaves(topology):
    masters = topology.masters()
    assert set(masters[0].slaves) == set(['redis-cluster003:7004', 'redis-cluster004:7002'])
    assert set(masters[4].slaves) == set(['redis-cluster002:7002', 'redis-cluster003:7001', 'redis-cluster001:7003'])




