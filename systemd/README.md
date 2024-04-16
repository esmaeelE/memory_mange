# Manage memroy with systemd services

## make python program a systemd service

```
sudo cp memeater.service /lib/systemd/system/

# after all changes we need
sudo systemctl daemon-reload

```

## Service Management

```
sudo systemctl start memeater.service
sudo systemctl stop memeater.service
sudo systemctl cat memeater.service
sudo systemctl stop memeater.service
sudo systemctl status memeater.service
```

## Monitoring

```
htop
free -hm
```

## Notes

Systemd manage restriction with **cgroup** in GNU/Linux.

Control Groups. The control groups, abbreviated as cgroups in this guide, are a **Linux kernel feature** that allows you to allocate resources — such as **CPU** time, system **memory**, **network** bandwidth, or combinations of these resources — among hierarchically ordered groups of processes running on a system.

In the other hand docker itself use this feaure of Kernel to mange restriction on containers.
(podman?)

