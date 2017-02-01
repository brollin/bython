"""
Given a list of clock times, find the pair which has the smallest duration between them. 
For instance, if given 03:03, 02:15, 07:42, and 10:23, you should return the pair 02:15 and 03:03. 
Print out the number of minutes between and the two times in any order. For instance, the above set should return (48, 02:15, 03:03)
"""


def shortest_duration(list_of_times):
    if not list_of_times:
        return None
    
    minutes = []
    for time in list_of_times:
        times = time.split(':')
        minutes.append(int(times[0])*60 + int(times[1]))
    
    sorted_minutes = sorted(minutes)
    
    shortest_duration = sorted_minutes[1] - sorted_minutes[0]
    candidate_times = [sorted_minutes[0], sorted_minutes[1]]
    for i in xrange(2,len(sorted_minutes)-1):
        duration = sorted_minutes[i] - sorted_minutes[i-1]
        if duration < shortest_duration:
            shortest_duration = duration
            candidate_times = [sorted_minutes[i-1], sorted_minutes[i]]
    
    first_time = sorted_minutes[0] + 60*24
    duration = first_time - sorted_minutes[-1]
    if duration < shortest_duration:
        shortest_duration = duration
        candidate_times = [sorted_minutes[-1], sorted_minutes[0]]
    
    return (shortest_duration, convert_minutes_to_time(candidate_times[0]), convert_minutes_to_time(candidate_times[1]))

def convert_minutes_to_time(minutes):
    hours = minutes / 60
    minutes = minutes % 60
    
    return ":".join(["%02d" % hours, "%02d" % minutes])


list_of_times = ["17:21", "23:50", "04:01", "07:07", "03:03", "00:01", "12:42", "16:03"]
print(shortest_duration(list_of_times))

list_of_times = ["17:21", "23:50", "04:01", "07:07", "03:03", "12:42", "16:03"]
print(shortest_duration(list_of_times))
