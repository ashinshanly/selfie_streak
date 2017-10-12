import os
import libs

libs.setup()
# This file indicates that the environment is development
# This file should not be tracked using version control.
if os.path.exists(os.path.join(os.path.dirname(__file__), '.dev')):
    #noinspection PyUnresolvedReferences
    from dev_settings import *
elif os.path.exists(os.path.join(os.path.dirname(__file__), '.stage')):
    #noinspection PyUnresolvedReferences
    from staging_settings import *
else:
    #noinspection PyUnresolvedReferences
    from prod_settings import *