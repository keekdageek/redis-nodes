import logging
logger = logging.getLogger(__name__)

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
        :return:
        """
        return self.parser.ip_hosts.get(self.row.ip, self.row.ip)