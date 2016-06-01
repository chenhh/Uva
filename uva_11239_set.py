# -*- coding: utf-8 -*-
"""
Authors: Hung-Hsin Chen <chenhh@par.cse.nsysu.edu.tw>
License: GPL v2

status: AC
difficulty: 1

https://uva.onlinejudge.org/external/112/11239.pdf
"""

from collections import defaultdict


def main():
    projects, students = {}, defaultdict(set)
    project_get = projects.get
    proj = None

    while 1:
        data = input().strip()
        if data == '0':
            break
        elif data != '1':
            if data.isupper():
                # project, the same project may show many times
                proj = data
                projects[proj] = project_get(proj, 0)
            else:
                # student
                students[data].add(proj)
        else:
            # end of test cases
            for k, project_set in students.items():
                if len(project_set) == 1:
                    for name in project_set:
                        projects[name] += 1

            # sort by value first (descending) then by project name
            sorted_data = sorted(projects.items(), key=lambda k: (-k[1], k[0]))
            for name, cnt in sorted_data:
                print(name, cnt)
            projects.clear()
            students.clear()


if __name__ == '__main__':
    main()
