int compare(const void * a, const void * b){
    return (*(int*)a - *(int*)b);
}
int minDifference(int* nums, int numsSize) {
    if(numsSize <= 4) return 0;
    qsort(nums, numsSize, sizeof(int), compare);
    int candidate[4];
    for(int i=0; i<4; i++){
        candidate[i] = nums[numsSize-1-(3-i)] - nums[i];
    }
    int ans = candidate[0];
    for(int i=1; i<4; i++){
        if(ans>candidate[i]){
            ans = candidate[i];
        }
    }
    return ans;
}