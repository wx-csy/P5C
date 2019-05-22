#include <iostream>
#include <cmath>
#include <utility>
#include <algorithm>
using namespace std;

#define rep(i, n) for (int i = 0; i < int(n); i++)
#define Rep(i, n) for (int i = 1; i <=int(n); i++)
#define range(x) begin(x), end(x)
#ifdef __LOCAL_DEBUG__
# define _debug(fmt, ...) fprintf(stderr, "[%s] " fmt "\n", __func__, \
  ##__VA_ARGS__)
#else
# define _debug(...) ((void) 0)
#endif

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<LL, LL> point;

inline istream& operator >> (istream& is, point& pt) {
  is >> pt.first >> pt.second;
  return is;
}

inline point operator - (point lhs, point rhs) {
  return point(lhs.first - rhs.first, lhs.second - rhs.second);
}

inline LL dist(point pt) {
  return pt.first * pt.first + pt.second * pt.second;
}

inline LL dist(point pt1, point pt2) {
  return dist(pt1 - pt2);
}

int n;
point poly[200005];

int main() {
  cin >> n;
  rep (i, n) cin >> poly[i];
  copy(poly, poly + n, poly + n);
  poly[n + n] = poly[0];
  LL maxdis = 0;
  int rptr = 0;
  rep (lptr, n) {
    while (dist(poly[rptr], poly[lptr]) < dist(poly[rptr + 1], poly[lptr]))
      rptr++;
    maxdis = dist(poly[rptr], poly[lptr]);
  }
  printf("%.15f\n", sqrt(maxdis));
  return 0;
}
