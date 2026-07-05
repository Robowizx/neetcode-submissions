class Solution {
public:
    bool isPresent(int num, int val){
        int flag = num & (int(pow(2,val)));
        
        if (flag){
            return true;
        }

        return false;
    }

    bool valCheck(int val, int acc){ 

        if (acc == (int(pow(2,val)))){
            return false;
        }
        else if ( (acc > int(pow(2,val))) ){
            if (this->isPresent(acc,val)){
                return false;
            }
            
        }

        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {

        for(int i=0;i<9;i++){
            int row_acc=0, col_acc=0, grid_acc=0;
            for(int j=0;j<9;j++){
                int digit;

                //row check
                if (board[i][j] != '.'){
                    digit = int(board[i][j] - '0');
                    if (this->valCheck(digit,row_acc)){
                        row_acc += int(pow(2,digit));
                    }
                    else{
                        cout <<"Row = "<< i+1 << "\nval = " << digit << "\n Acc = " << row_acc;
                        return false;
                    }
                }
                
                //col check
                if (board[j][i] != '.'){
                    digit = int(board[j][i] - '0');
                    if (this->valCheck(digit,col_acc)){
                        col_acc += int(pow(2,digit));
                    }
                    else{
                        cout << "col = "<< i+1 << "\nval = " << digit << "\n Acc = " << col_acc;
                        return false;
                    }
                }

                //grid check
                int row = ((i/3)*3) + (j/3);
                int col = ((i%3)*3) + (j%3);
                if (board[row][col] != '.'){
                    digit = int(board[row][col] - '0');
                    if (this->valCheck(digit,grid_acc)){
                        grid_acc += int(pow(2,digit));
                    }
                    else{
                        cout <<"grid = "<< i+1 << "\nPos = "<< j+1 <<"\ntranslate = ("<< row <<","<< col <<")"<< "\nval = " << digit << "\n Acc = " << grid_acc;
                        return false;
                    }
                }
            }
        }

        return true;
    }
};
