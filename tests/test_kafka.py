import testing.zookeeper
import testing.kafka
import unittest
import time
import os


class TestKafka(unittest.TestCase):

    def test_basic(self):
        try:
            # start postgresql server
            zookeeper = testing.zookeeper.ZookeeperServer()
            self.assertIsNotNone(zookeeper)
            kafka = testing.kafka.KafkaServer(zookeeper_url=zookeeper.url())

        finally:
            # shutting down
            pid = zookeeper.server_pid
            self.assertTrue(zookeeper.is_alive())

            zookeeper.stop()
            time.sleep(1)

            self.assertFalse(zookeeper.is_alive())
            with self.assertRaises(OSError):
                os.kill(pid, 0) # process is down
