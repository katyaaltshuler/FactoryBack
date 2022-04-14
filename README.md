# FactoryBack
<h2>An automatic production line of foobar.</h2> <p><i>The goal is to reach automatically 30 robots by assigning tasks to Robots randomly. 
  Starts from 2 Robots and zero resources.</i></p>

> Instructions:
> <p>At the beginning, we have 2 robots, each of which is able to perform several actions:</p>
> 
> <ul>
> <li> Moving to change activity: occupy the robot for 5 seconds.
> <li> Mining foo: occupies the robot for 1 second.
> <li> Mining bar: keeps the robot busy for a random time between 0.5 and 2 seconds.
> <li> Assembling a foobar from a foo and a bar: keeps the robot busy for 2 seconds. The operation has a 60% chance of success; in case of failure the bar can be reused, the foo is lost.
> <li> Sell foobar: 10s to sell from 1 to 5 foobar, we earn €1 per foobar sold
> <li> Buy a new robot for €3 and 6 foo, 0s
> </ul>
  
  
<h2>Installing Factory</h2>


To start game from console you should clone this repository first:

> <code>$ git clone https://github.com/katyaaltshuler/FactoryBack </code>

And satisfy all requirements indicated.
> 
**<h2>To be improved</h2>**
<ul>
 <li> Write unittests
 <li> The robot should not repeat the previous random action when "change_activity" appears to be True. Solution might be in tracking the ID of called function.
 <li> Test the parallel executions of processes
 <li> Split the main.py into additional functions
 <li> Make console messages more detailed and user-friendly.
 </ul>
