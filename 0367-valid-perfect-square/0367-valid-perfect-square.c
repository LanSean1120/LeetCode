bool isPerfectSquare(int num) {
    if(num == 1) return true;
    int left = 0, right = num;
    int mid;
    while(left+1<right){
        mid = (right+left)/2;
        if(mid == (double)num/mid){
            return true;
        }else if(mid >= (double)num/mid){
            right = mid;
        }else{
            left = mid;
        }
    }
    if(left == (double)num/left) return true;
    return false;
}