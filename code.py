import subprocess
import ast
import re

batcmd="aws s3api list-buckets"
result = subprocess.check_output(batcmd, shell=True)
arr = ast.literal_eval(result.decode('utf-8'))

for i in arr['Buckets']:
    batcmd = "aws s3 ls s3://" + i['Name'] + " --recursive --human-readable --summarize"
    result = subprocess.check_output(batcmd, shell=True).decode("utf-8")
    demo = re.findall(r'Total Size: (\d+)',result)

    if int(demo[0]) == 0:
        print(i['Name'])
