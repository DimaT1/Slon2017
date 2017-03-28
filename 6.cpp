#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>

#define len(A, B) abs(A.first - B.first) + abs(A.second - B.second)
typedef unsigned long long ull;

std::string IntToString(ull a) { // У меня не хотело работать std::to_string(), я не стал разбираться, всё из-за винды
    std::ostringstream temp;
    temp << a;
    return temp.str();
}


ull N;


int main() {
    std::cin >> N;
    std::vector<ull> trip(N);
    std::vector<std::pair<ull, ull>> cost(N);

    for (ull i = 0; i < N; i++) {
        ull x, y;

        trip[i] = i;
        std::cin >> x >> y;
        cost[i] = {x, y};
    }

    ull min_len = (ull) 1e8;
    std::string answ = "";

    do {
        ull trip_len = 0;

        for (ull i = 0; i < N - 1; i++) {
            trip_len += len(cost[trip[i]], cost[trip[i + 1]]);
        }
        trip_len += len(cost[trip[N - 1]], cost[trip[0]]);

        if (trip_len < min_len) {
            min_len = trip_len;
            answ = "";
            for (auto i : trip) {
                answ += IntToString(i + 1);//std::to_string(i);
            }
            answ += '\n';

        } else if (trip_len == min_len) {
            for (auto i : trip) {
                answ += IntToString(i + 1);//std::to_string(i);
            }
            answ += '\n';
        }

    } while (std::next_permutation(trip.begin() + 1, trip.end()));

    std::cout << min_len << std::endl << answ;
    return 0;
}
