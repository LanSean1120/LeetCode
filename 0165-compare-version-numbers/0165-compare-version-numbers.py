class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1=version1+"."
        v1={}
        i=0
        start1=0
        end1=0
        while end1<len(version1):
            if version1[end1] != ".":
                end1+=1
            elif version1[end1] == ".":
                if end1-start1==1:
                    v1[i] = int(version1[start1])
                    start1=end1+1
                    end1=start1+1
                    i+=1
                else:
                    while start1<end1-1:
                        if version1[start1]=="0":
                            start1+=1
                        else:
                            break
                    v1[i] = int(version1[start1:end1])
                    start1=end1+1
                    end1=start1+1
                    i+=1
        '''
        for version2
        '''            
        version2=version2+"."
        v2={}
        i=0
        start2=0
        end2=0
        while end2<len(version2):
            if version2[end2] != ".":
                end2+=1
            elif version2[end2] == ".":
                if end2-start2==1:
                    v2[i] = int(version2[start2])
                    start2=end2+1
                    end2=start2+1
                    i+=1
                else:
                    while start2<end2-1:
                        if version2[start2]=="0":
                            start2+=1
                        else:
                            break
                    v2[i] = int(version2[start2:end2])
                    start2=end2+1
                    end2=start2+1
                    i+=1

        for i in range(min(len(v1), len(v2))):
            if v1[i]>v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
            else:
                continue
        
        if len(v1)>len(v2):
            for i in range(len(v2), len(v1)):
                if v1[i]!=0:
                    return 1
            return 0
        elif len(v1)==len(v2):
            return 0
        else:
            for i in range(len(v1), len(v2)):
                if v2[i]!=0:
                    return -1
            return 0

        