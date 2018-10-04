
Install
=======
Use pip::

   $ pip install testing.kafka

``testing.kafka`` requires ``zookeeper``, ``kafka`` and ``java`` to be installed.


Usage
=====
Create Kafka and Zookeeper instances::

  @pytest.fixture
  def kafka():

      zookeeper = testing.zookeeper.ZookeeperServer()
      kafka = testing.kafka.KafkaServer(zookeeper_url=zookeeper.url())

      yield kafka

      kafka.stop(_signal=signal.SIGKILL)
      zookeeper.stop(_signal=signal.SIGKILL)
