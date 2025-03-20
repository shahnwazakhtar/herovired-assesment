#!/bin/bash

logfile="usage.log"

echo "Starting CPU and Memory monitoring..."
echo "Time, CPU Usage (%), Memory Usage (%)" > $logfile

while true; do
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')
    mem_usage=$(free -m | grep Mem | awk '{print ($3/$2)*100}')
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    echo "$timestamp, $cpu_usage, $mem_usage" >> $logfile
    sleep 5
done