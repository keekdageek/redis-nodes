import logging
logger = logging.getLogger(__name__)
from cached_property import threaded_cached_property

class Master:
    """
    Parses redis-cli nodes output and dumps ordered master and slave topology
    """
    def __init__(self, parser, row, idx):
        self.parser = parser
        self.row = row
        self.idx = idx

    @property
    def hostname(self):
        """
        Master hostname based on ip_hosts mapped from ipaddress
        :return: hostname string
        """
        return self.parser.ip_hosts.get(self.row.ip, self.row.ip)

    @threaded_cached_property
    def slaves(self):
        """
        The masters slaves based on the parser dataframe
        :return: array of slave w/ hostname & port
        """
        ret = []
        sframe = self.parser.df.loc[self.parser.df['master'] == self.row.name]
        for idx, row in sframe.iterrows():
            ret.append(f"{self.parser.ip_hosts.get(row.ip, row.ip)}:{row.port}")
        return ret
