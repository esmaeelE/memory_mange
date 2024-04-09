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


