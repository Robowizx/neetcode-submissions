class Solution {
public:
    char get_open_bracket(char bracket){
        switch(bracket){
            case ')':
                return '(';
            case '}':
                return '{';
            case ']':
                return '[';
            default:
                return '0';            
        }
    }
    bool isValid(string s) {
        vector<char> stack;

        for (char i:s){
            if (i == '(' || i == '{' || i == '['){
                stack.push_back(i);
            }
            else if (stack.size() > 0){
                if (this->get_open_bracket(i) == stack.back()){
                    stack.pop_back();
                }
                else{
                    return false;
                }
            }
            else{
                return false;
            }
        }

        if (stack.size() != 0){
            return false;
        }  

        return true;
    }
};
