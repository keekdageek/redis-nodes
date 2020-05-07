
import argparse
import logging
logger = logging.getLogger(__name__)
from redis_nodes.topology import Topology

class RedisNodes:
    """
    Main CLI executable using python argparse.  Requires a nodes and hosts parameter to space deliminated files and dumps the topology.
    """
    def __init__(self):
        """
        Defines the CLI parameters
        """
        self._parser = argparse.ArgumentParser(
            prog='redis-nodes',
            description="Parses 'redis-cli cluster nodes' input and dumps master slave relationships")
        self._parser.add_argument(
            '-n', '--nodes',
            required=True,
            help="Path to file w/ `redis-cli cluster nodes` output, assumes space deliminated csv")

        self._parser.add_argument(
            '-H', '--hosts',
            required=True,
            help="Hostname to ip map, assumes space deliminated csv")


    def exec(self):
        """
        Runs the main application by instantiating a Topology and dumping the output
        :return:
        """
        cli_args = self._parser.parse_args()

        ip_hosts = {}
        with open(cli_args.hosts) as fp:
            line = fp.readline()
            while line:
                host_ip = line.split()
                ip_hosts[host_ip[1]] = host_ip[0]
                line = fp.readline()
        top = Topology(ip_hosts, cli_args.nodes)
        top.dump_nodes()

# executable pip package referenced by poetry.toml
# > redis-nodes
def main():
    return RedisNodes().exec()

# executed w/ native python
# > python redis_nodes/__main__.py
if __name__ == '__main__':
    RedisNodes().exec()