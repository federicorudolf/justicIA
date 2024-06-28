#!/bin/zsh
LOG_FILE="/Users/federico.launchpadlab/Documents/Proyectos/justicIA/justicIA/logs.txt"
cd /Users/federico.launchpadlab/Documents/Proyectos/justicIA/justicIA/
source bin/activate
python_exec_path=$(which python)
env_python_exec_path="/Users/federico.launchpadlab/Documents/Proyectos/justicIA/justicIA/bin/python"

if [ "$python_exec_path" = "$env_python_exec_path" ]; then
  echo "Virtual environment is activated."
  python3 -m pip install -r ./requirements.txt
  python3 app.py
  if [ $? -eq 0 ]; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Script ejecutado correctamente" >> $LOG_FILE
  else
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Error ejecutando el script" >> $LOG_FILE
  fi
  deactivate
else
  echo "Virtual environment is not activated."
  echo "$(date '+%Y-%m-%d %H:%M:%S') - Error: Virtual environment not activated" >> $LOG_FILE
fi
