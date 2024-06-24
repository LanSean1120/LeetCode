int minKBitFlips(int* nums, int numsSize, int k) {
    int flip_count = 0;
    int flips[numsSize];
    int ans =0;
    for(int i=0; i<numsSize; i++){
        flips[i] = 0;
        if(i>=k){
            flip_count ^= flips[i-k];
        }
        if(nums[i]^flip_count == 0){
            if(i>numsSize-k) return -1;
            flip_count ^=1;
            flips[i] = 1;
            ans ++;
        }
    }
    return ans;
}