#include <stdio.h>
#include <string.h>

#include <algorithm>
#include <bitset>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <memory>
#include <mutex>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
// #include <unordered_map> // NEVER USE THOSE IN CP
// #include <unordered_set> // NEVER USE THOSE IN CP

#define int long long  // Because i'm so done with integer overflow mistakes

using namespace std;

signed main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int l, r;
  vector<int> a;
  vector<int> b;
  while (cin >> l >> r) {
    a.push_back(l);
    b.push_back(r);
  }
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());

  // omg C++ is so long... i give up

  return 0;
}
