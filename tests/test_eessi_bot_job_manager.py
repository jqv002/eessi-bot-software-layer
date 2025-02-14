# Tests for 'job managaer' task of the EESSI build-and-deploy bot,
# see https://github.com/EESSI/eessi-bot-software-layer
#
# The bot helps with requests to add software installations to the
# EESSI software layer, see https://github.com/EESSI/software-layer
#
# author: Kenneth Hoste (@boegel)
# author: Hafsa Naeem (@hafsa-naeem)
#
# license: GPLv2
#
import os
import shutil

from eessi_bot_job_manager import EESSIBotSoftwareLayerJobManager


def test_read_job_pr_metadata(tmpdir):
    # copy needed app.cfg from tests directory
    shutil.copyfile("tests/test_app.cfg", "app.cfg")

    # if metadata file does not exist, we should get None as return value
    job_manager = EESSIBotSoftwareLayerJobManager()
    path = os.path.join(tmpdir, 'test.metadata')
    assert job_manager.read_job_pr_metadata(path) is None

    with open(path, 'w') as fp:
        fp.write('''[PR]
        repo=test
        pr_number=12345''')

    metadata_pr = job_manager.read_job_pr_metadata(path)
    expected = {
        "repo": "test",
        "pr_number": "12345",
    }
    assert metadata_pr == expected
