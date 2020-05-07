
import argparse
import logging
logger = logging.getLogger(__name__)
from .parser import Parser

class RedisNodes:
    def __init__(self):
        self._parser = argparse.ArgumentParser(prog='redis-nodes', description="Parses 'redis-cli cluster nodes' input and dumps master slave relationships")
        self._parser.add_argument(
            '-n', '--nodes',
            required=True,
            help="Path to file w/ `redis-cli cluster nodes` output, assumes space deliminated csv")

        self._parser.add_argument(
            '-H', '--hosts',
            required=True,
            help="Hostname to ip map, assumes space deliminated csv")


    def main(self):
        cli_args = self._parser.parse_args()

        ip_hosts = {}
        with open(cli_args.hosts) as fp:
            line = fp.readline()
            while line:
                host_ip = line.split()
                ip_hosts[host_ip[1]] = host_ip[0]
                line = fp.readline()
        parser = Parser(ip_hosts, cli_args.nodes)
        parser.dump_nodes()

def main():
    return RedisNodes().main()

if __name__ == '__main__':
    RedisNodes().main()