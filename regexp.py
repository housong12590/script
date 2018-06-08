import os
import re

git_branch = os.popen('git branch').read()
branch_regexp = re.compile(r'\*\s(\w+)')
result = branch_regexp.findall(git_branch)
origin_branch = result[0]

if origin_branch not in ['develop', 'master']:
    os.system('git checkout develop')
    os.system('git merge {}'.format(origin_branch))
    os.system('git push origin develop')
    os.system('git checkout master')
    os.system('git merge develop')
    os.system('git push origin master')
if origin_branch == 'develop':
    os.system('git checkout master')
    os.system('git merge develop')
    os.system('git push origin master')

os.system('git tag 1.0.2')
os.system('git push 1.0.2')
os.system('gradlew assembleRelease')

os.system('git checkout {}'.format(origin_branch))
