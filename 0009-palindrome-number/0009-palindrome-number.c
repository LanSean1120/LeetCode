bool isPalindrome(int x) {
    if(x<0) return false;
    int l[10];
    int index = 0;
    while(x!=0){
        l[index] = x%10;
        x/=10;
        index++;
    }

    int left = 0, right = index-1;
    while(left<right){
        if(l[left]!=l[right]) return false;
        left++;
        right--;
    }
    return true;
}