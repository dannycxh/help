

## Grafana
sudo apt-get install -y adduser libfontconfig1 musl
wget https://dl.grafana.com/enterprise/release/grafana-enterprise_10.4.1_amd64.deb
sudo dpkg -i grafana-enterprise_10.4.1_amd64.deb

 sudo /bin/systemctl daemon-reload
 sudo /bin/systemctl enable grafana-server
### You can start grafana-server by executing
 sudo /bin/systemctl start grafana-server



## prometheus
nohup /home/ubuntu/prometheus-2.51.0.linux-386/node_exporter-1.7.0.linux-386/node_exporter &
 ./prometheus --config.file=prometheus.yml


CREATE USER 'exporter'@'%' IDENTIFIED BY '********' WITH MAX_USER_CONNECTIONS 3;
GRANT PROCESS, REPLICATION CLIENT, SELECT ON *.* TO 'exporter'@'%';

nohup ./mysqld_exporter --config.my-cnf="/home/ubuntu/prometheus-2.51.0.linux-386/mysqld_exporter-0.15.1.linux-386/my.cnf" &


nohup ./mysqld_exporter --config.my-cnf=cache.my.cnf --web.listen-address=":9104" &
nohup ./mysqld_exporter --config.my-cnf=test.my.cnf --web.listen-address=":9105" &




###################################################################
# my global config
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).
  
# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
          # - alertmanager:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  # - "first_rules.yml"
  # - "second_rules.yml"     


# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  #在 Prometheus 中添加一个新的 job，指向 Node Exporter 的地址
  - job_name: node
    static_configs:
      - targets: ['localhost:9100']

  - job_name: 'mysql-cache'
    static_configs:
    - targets:
      - 'localhost:9104'

  - job_name: 'mysql-test'
    static_configs:
    - targets:
      - 'localhost:9105'    





#############################################################################
## for track user token and diamonds
export JAVA_HOME=/home/ubuntu/canal.1.1.7/jdk-22/  #echo $JAVA_HOME
mvn clean install -Denv=release -Dmaven.test.skip=true

## tips:
tar -zxvf canal-1.1.7.tar.gz
tar -zxvf canal.adapter-1.1.7.tar.gz -C canal.adapter-1.1.7
tar -zxvf canal.deployer-1.1.7.tar.gz -C canal.deployer-1.1.7
tar -zxvf jdk-22_linux-x64_bin.tar.gz -C jdk-22

mkdir target/canal.adapter-1.1.7 && tar -zxvf  target/canal.adapter-1.1.7.tar.gz -C target/canal.adapter-1.1.7 && cp  target/canal.adapter-1.1.7/plugin/client-adapter.logger-1.1.7-jar-with-dependencies.jar  /home/ubuntu/canal.1.1.7/canal.adapter-1.1.7/plugin/

/home/ubuntu/canal.1.1.7/canal.adapter-1.1.7/bin/startup.sh
/home/ubuntu/canal.1.1.7/canal.adapter-1.1.7/bin/stop.sh

/home/ubuntu/canal.1.1.7/canal.adapter-1.1.7/bin/stop.sh



[Unit]
Description=Canal Service
After=network.target

[Service]
Type=simple
User=root
Group=root
ExecStart=/home/ubuntu/startup.sh
ExecStop=/home/ubuntu/stop.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target


#!/bin/bash

export JAVA_HOME=/home/ubuntu/canal.1.1.7/jdk-22/
# 启动 Deploy
nohup /home/ubuntu/canal.1.1.7/canal.deployer-1.1.7/bin/startup.sh &
# 等待Deploy完成启动
sleep 5
# 启动adapter
nohup /home/ubuntu/canal.1.1.7/canal.adapter-1.1.7/bin/startup.sh &




