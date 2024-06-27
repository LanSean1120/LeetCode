int lengthOfLastWord(char* s) {
    int count = 0;
    int ans = 0;
    for(int i=0; i < strlen(s); i++){
        if(s[i] != ' '){
            count++;
        }
        else{
            if(count > 0 ){
                ans = count;
                count = 0;
            }
        }
    }
    if(count>0) ans = count;
    return ans;
}