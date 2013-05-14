#!/bin/bash

function command_exists {
	type "$1" &> /dev/null ;
}

function run_process {
	my_command="$1"
	tmp=($my_command)
	process=${tmp[0]}
	if command_exists $process; then
		if [[ -z $(pidof $1) ]]; then
			printf "%s: starting\n" "$my_command"
			# Run command.
			$my_command
		else
			printf "%s: already running\n" "$my_command"
		fi
	else
		printf "%s: not in system\n" "$my_command"
	fi
}

# Check neccesary.
printf "FTF is in: %s\n" $FTF_HOME
if [[ -d "$FTF_HOME" && -f "${FTF_HOME}/dev_https" ]]; then
	
	# Move to proper directory.
	cd $FTF_HOME

	# Run stunnel if is not running.
	run_process "stunnel dev_https &"

	# Run rabbitmq-server if is not running.
	run_process "rabbitmq-server"

	# Run memcadhed.
	echo "memcached: will run if not running"
	memcached -d
else
	echo "Didn't pass neccesary check."
fi
