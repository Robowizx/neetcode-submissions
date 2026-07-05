class Solution {
public:

    string encode(vector<string>& strs) {

        string out = "";

        for (string i : strs){
            out += (to_string(i.size()) + "#" + i);
        }

        return out;
    }

    vector<string> decode(string s) {
        vector<string> out;
        string buffer = "";
        int i = 0;
        while(i < s.size()){
            if (s[i] != '#'){
                buffer += s[i];
                i++;
            }
            else{
                out.push_back(s.substr(i+1,stoi(buffer)));
                i+=stoi(buffer)+1;
                buffer = "";
            }
        }

        return out;
    }
};
