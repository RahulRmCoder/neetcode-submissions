class Solution {
    public int uniquePaths(int m, int n) {
        int rows[] = new int[n];
        Arrays.fill(rows,1);

        for(int i=m-2; i>=0; i--){
            int newRows[] = new int[n];
            Arrays.fill(newRows,1);

            for(int j=n-2;j>=0;j--){
                newRows[j] = newRows[j+1] + rows[j];
            }
            rows= newRows;
        }
        return rows[0];
    }
}
