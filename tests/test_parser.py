# Seeded with devops-scaffold/roles/project by fmarin at 03/09/2020, 13:14:43 
import pytest
from redis_nodes.parser import Parser
import ipdb

@pytest.fixture
def parser():
    host_ips = {}
    with open('./tests/fixtures/hosts.csv') as fp:
        line = fp.readline()
        while line:
            host_ip = line.split()
            host_ips[host_ip[0]] = host_ip[1]
            line = fp.readline()
    return Parser(host_ips, "./tests/fixtures/nodes.csv")


def test_parser_columns(parser):
    assert len(parser.df.columns) == 8




