from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def customsort(log):
            identifier, log = log.split(" ", 1)
            # if letter log
            if log[0].isalpha():
                return (0, log, identifier)
            return (1,)

        logs.sort(key=customsort)
        return logs
