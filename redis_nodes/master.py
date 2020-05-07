import logging
logger = logging.getLogger(__name__)
from cached_property import threaded_cached_property

class Master:
    """
    Parses redis-cli nodes output and dumps ordered master and slave topology
    """
    def __init__(self, topology, row, idx):
        self.topology = topology
        self.row = row
        self.idx = idx

    @property
    def hostname(self):
        """
        Master hostname
        :return: hostname string
        """
        return self._ip_host(self.row.ip)

    @threaded_cached_property
    def slaves(self):
        """
        The masters slaves based on the parser dataframe
        :return: array of slave w/ hostname & port
        """
        ret = []
        sframe = self.topology.df.loc[self.topology.df['master'] == self.row.name]
        for idx, row in sframe.iterrows():
            ret.append(f"{self._ip_host(row.ip)}:{row.port}")
        return ret

    def _ip_host(self, ip):
        """
        Simple hostname lookup based on ip, if not found returns ip
        :param ip:
        :return: hostname
        """
        return self.topology.ip_hosts.get(ip, ip)
