import logging
logger = logging.getLogger(__name__)
from cached_property import threaded_cached_property


class Parser:
    """
    Parses redis-cli nodes output and dumps ordered master and slave topology
    """
    def __init__(self, host_ips, nodes):
        self.host_ips = host_ips
        self.nodes = nodes

    @threaded_cached_property
    def df(self):
        """
        Pandas Dataframe customized for redis nodes output
        :return: pandas dataframe
        """
        import pandas as pd
        return pd.read_csv(self.nodes,
                           sep='\s+',
                           header=None,
                           index_col='id',
                           names=["id", "ip_port", "flags", "master", "ping", 'pong', 'epoc', 'state', 'range'],
                           engine='python')




    def dump_nodes(self):
        print(self.df)
