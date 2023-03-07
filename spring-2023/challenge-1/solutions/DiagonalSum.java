/**
 * Diagonal Sum
 */
class DiagonalSum {
    /**
     * diagonalSum - returns the sum of the diagonal elements of a matrix
     * @param matrix
     * @return diagonalSum
     */
    public int diagonalSum(int[][] matrix) {
        int pd_ptr = 0;
        int sd_ptr = matrix[0].length - 1;
        int diagonalSum = 0;

        for (int i = 0; i < matrix.length; i++) {
            diagonalSum += matrix[i][pd_ptr];

            if(pd_ptr != sd_ptr)
                diagonalSum += matrix[i][sd_ptr];

            pd_ptr += 1;
            sd_ptr -= 1;
        }
        
        return diagonalSum;
    }
}