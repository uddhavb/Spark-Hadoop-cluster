Digital ocean: guide

https://www.digitalocean.com/community/tutorials/how-to-spin-up-a-hadoop-cluster-with-digitalocean-droplets?comment=75609

( https://www.linode.com/docs/databases/hadoop/how-to-install-and-set-up-hadoop-cluster/ )

wget https://archive.apache.org/dist/hadoop/core/hadoop-3.0.1/hadoop-3.0.1.tar.gz


New username: ‘hadoop’

COMMON FILES

Core-site.xml:

<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://MASTER_IP:9000</value>
    </property>
</configuration>

Mapred-site.xml:

<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>

Hdfs-site.xml:

NAMENODE
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>3</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/usr/local/hadoop/hdfs/data</value>
    </property>
</configuration>
DATANODE
    <property>
        <name>dfs.replication</name>
        <value>3</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>/usr/local/hadoop/hdfs/data</value>
    </property>
<property> <name>dfs.namenode.datanode.registration.ip-hostname-check</name> <value>false</value> </property>


Yarn-site.xml:
NAMENODE:
<configuration>

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>204.48.21.134</value>
    </property>
</configuration>

DATANODE:
<configuration>

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
</configuration>
 /etc/environment:

ADD these lines:
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
HDFS_NAMENODE_USER="hadoop"
HDFS_DATANODE_USER="hadoop"
HDFS_SECONDARYNAMENODE_USER="hadoop"
YARN_RESOURCEMANAGER_USER="hadoop"
YARN_NODEMANAGER_USER="hadoop"
/etc/hosts:
NAMENODE
204.48.21.134 hadoop-master hadoop-master
167.99.231.17 hadoop-worker-01
68.183.22.107 hadoop-worker-02
127.0.0.1 localhost
DATANODE
		204.48.21.134 hadoop-master
68.183.22.107 hadoop-worker-02
167.99.231.17 hadoop-worker-01 hadoop-worker-01
127.0.0.1 localhost
