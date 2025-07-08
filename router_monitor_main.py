#router_monitor_main driver program
from pynetgear import Netgear
import configparser

config = configparser.ConfigParser()

config.read ('router_config.ini')

print(config.get('ServerPass'))

    #netgear = Netgear(password='pass')
