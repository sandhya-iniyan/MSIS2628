import re
input_file = open('fb_sub.csv', 'r')
input = input_file.read()
input_file.close()
output = re.search('[^,]*INC', input)
output_file = open('company.txt', 'w')
output_file.write(output[0])
output_file.close()


