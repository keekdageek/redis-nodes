import logging
log = logging.getLogger(__name__)
from cached_property import threaded_cached_property
import ipdb
import pandas as pd
from .master import Master

class Parser:
    """
    Parses redis-cli nodes output and dumps ordered master and slave topology
    """
    def __init__(self, ip_hosts, nodes):
        self.ip_hosts = ip_hosts
        self.nodes = nodes

    @threaded_cached_property
    def df(self):
        """
        Pandas Dataframe customized for redis nodes output
        :return: pandas dataframe
        """
        pd.options.mode.chained_assignment = None
        dframe = pd.read_csv(self.nodes,
                           sep='\\s+',
                           header=None,
                           index_col='id',
                           names=["id", "ip_port", "flags", "master", "ping", 'pong', 'epoc', 'state', 'range'],
                           engine='python')
        dframe[['ip','port']] = dframe.ip_port.str.split(":",expand=True)
        # print(dframe)
        return dframe

    def masters(self):
        master_df = self.df.loc[self.df['flags'] == 'master']
        master_df[['range_start','range_end']] = master_df.range.str.split("-",expand=True)
        master_df[["range_start", "range_end"]] = master_df[["range_start", "range_end"]].apply(pd.to_numeric)
        master_df = master_df.sort_values(by=['range_start'])
        ret = []
        # print(master_df)
        for idx, row in master_df.iterrows():
            ret.append(Master(self, row, idx))
        log.info(f"Found {len(ret)} master rows")
        return ret


    def dump_nodes(self):
        for master in self.masters():
            print(master.row['range'])
            print(f"\tmaster: {master.hostname}:{master.row['port']}")
            print(f"\tslaves: {', '.join(master.slaves)}")
            print("\n")
