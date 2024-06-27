int findCenter(int** edges, int edgesSize, int* edgesColSize) {
    int ans = edges[0][0];
    for(int i = 0; i <= 1; i++){
        if(ans == edges[1][i]) return ans;
    }
    return edges[0][1];
}