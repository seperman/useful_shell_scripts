#sets the BG color of terminal when SSH to the terminal
#it sets it to black when you exit the SSH
#to use: run: ssh_box.sh [name or IP of the box]
set_bg () {
  osascript -e "tell application \"Terminal\" to set background color of window 1 to $1"
}

set_bg "{9000, 3000, 1000, 50000}";

#vagrant ssh;
ssh $1;

set_bg "{0, 0, 0, 50000}";
