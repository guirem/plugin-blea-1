import time
CURRENT_DIVOOM_TEXT={}
CURRENT_DIVOOM_SCROLL={}
DAEMON_VERSION = '2.7'
BLUEPY_VERSION = '1.0'
SCAN_MODE = 'passive'
JEEDOM_COM = ''
SCAN_INTERVAL = 29
NOSEEN_NUMBER = 4
START_TIME = int(time.time())
KNOWN_DEVICES = {}
SEEN_DEVICES = {}
LEARN_MODE = False
LEARN_TYPE = ''
READY = False
LEARN_MODE_ALL = 0
LAST_BLUEPY = int(time.time())
LAST_VIRTUAL = int(time.time())
LAST_BEAT = int(time.time())
LEARN_BEGIN = int(time.time())
LEARN_END = int(time.time())
LAST_CLEAR = int(time.time())
COMPATIBILITY = []
LAST_STATE={}
PRESENT={}
IGNORE=[]
KEEPED_CONNECTION={}
LAST_STORAGE={}
LAST_TIME_READ = {}
IFACE_DEVICE = 0
SCAN_ERRORS = 0
SCANNER = ''
PENDING_ACTION = False
PENDING_TIME = int(time.time())
log_level = "error"
pidfile = '/tmp/blead.pid'
apikey = ''
callback = ''
cycle = 0.3
daemonname=''
socketport=''
sockethost=''
