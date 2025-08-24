##include <iostream>
#include <vector>
#include <numeric>

const int MAX_SCORE = 500000;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);


    int n, m;
    std::cin >> n >> m;
    std::vector<int> freq(MAX_SCORE+1, 0);
    for (int i = 0; i < n; i++) {
        int score;
        std::cin >> score;
        freq[score]++;
    }

    std::vector<int> divisors_count(MAX_SCORE+1, 0);
    for (int k = 1; k <= MAX_SCORE; ++k) {
        if (freq[k] > 0) {
            for (int j = k; j <= MAX_SCORE; j += k) {
                divisors_count[j] += freq[k];
            }
        }
    }

    std::vector<int> multiples_count(MAX_SCORE+1, 0);
    for (int k = 1; k <= MAX_SCORE; ++k) {
        for (int j = k; j <= MAX_SCORE; j += k) {
            multiples_count[k] += freq[j];
        }
    }

   for (int q_idx = 0; q_idx < m; ++q_idx) {
        int x;
        std::cin >> x;
        int current_compatibles = multiples_count[x] + divisors_count[x];
        if (freq[x] > 0) {
            current_compatibles -= freq[x];
        }
        std::cout << current_compatibles << std::endl;
   }

   return 0;
}