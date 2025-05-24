import logging
import coloredlogs

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

coloredlogs.install(
    level='DEBUG',
    logger=logger,
    fmt='%(asctime)s %(levelname)s [%(name)s] %(message)s',
    level_styles={
        'debug': {'color': 'blue', 'bold': True},
        'info': {'color': 'green'},
        'warning': {'color': 'yellow'},
        'error': {'color': 'red', 'bold': True},
        'critical': {'color': 'red', 'bold': True, 'background': 'white'},
    },
    field_styles={
        'asctime': {'color': 'cyan'},
        'levelname': {'bold': True},
        'name': {'color': 'cyan'},
    }
)
