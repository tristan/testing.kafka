import testing.zookeeper
import unittest
import time
import os


class TestZookeeper(unittest.TestCase):

    def test_basic(self):
        try:
            # start postgresql server
            zookeeper = testing.zookeeper.ZookeeperServer()
            self.assertIsNotNone(zookeeper)

        finally:
            # shutting down
            pid = zookeeper.server_pid
            self.assertTrue(zookeeper.is_alive())

            zookeeper.stop()
            time.sleep(1)

            self.assertFalse(zookeeper.is_alive())
            with self.assertRaises(OSError):
                os.kill(pid, 0) # process is down
