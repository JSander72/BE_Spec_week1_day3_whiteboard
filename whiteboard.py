# **WHITEBOARD STEPS:

# 1.) Read the prompt out loud, verbalize and key points you take note of, and conclude this step with a clarifying statement on what the prompt is asking you to do.

# 2.) The Planning Phase: This is the phase you will probably spend the most time in, and is where you lay down your logic in pseudocode (Optional: Highlight you Point A and B)

# 3.) Code Phase: This phase is where you will translate your pseudo code into actual code. Be sure to test things out as you go to ensure that what you expect to be happening at each step, is what is actually happening.

# 4.) Refactoring Phase: Handle any edge cases you may not have considered, and express considerations for time complexity**


#==================================================================================================

# Create a function that given a list which represents street lights given as a 
#parameter, determine if an outage has occurred. A street with a total 
#number of "F" greater than or equal to 2 returns "Outage", anything below returns "Power"
# Example Input: [ 'T', 'F', 'F', 'F' ]				
# Example Output: "Outage"

# first thing i will be creating a function
# look thorugh the given list
# Iterate thorugh the list to determine if there are 2 or more "F"
# This will bbe done per list provided
# Once it is determined there are 2 or more "F" 
# Create a collection that will act as our bucket
# taking in value and check content of bucket to see if value is unique 
# Continue chekcing each value until alll values have bee checkd and confirmed unique 
# Or if we connfirm value is not longer unique 
# Return "outage"
# If list is completed return "Power" 

def solution(power_status):
    
    
    F_count = power_status.count("F")
    if F_count >= 2:
        return "Outage"
    else:
        return "Power"
        
    




    
    




