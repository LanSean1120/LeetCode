int mySqrt(int x) {
    if(x==1) return 1;
    int left = 0, right = x;
    int mid = 0;
    while(left+1 < right){
        mid = (left+right)/2;
        if(mid > x/mid) right = mid;
        else if(mid < x/mid) left = mid;
        else left = right = mid;
    }
    
    return left;
}