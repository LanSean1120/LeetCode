int countSeniors(char ** details, int detailsSize){
int ans = 0;

for(int i = 0; i<detailsSize; i++){
    if((int*) (details[i][11]-'0') > 6){
        ans++;
    }
    else if ((int*)(details[i][11]-'0') == 6 && (int*)(details[i][12]-'0') > 0){
        ans++;
    }
}
return ans;
}