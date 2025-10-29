#include "bits/stdc++.h"
using namespace std;

#define PR(a) a.weight << "/" << a.height

struct person {
  int id;
  int weight;
  int height;
} typedef person_t;

int comp(person_t a, person_t b) {
  if (a.weight > b.weight && a.height > b.height) return 1;
  if (a.weight < b.weight && a.height < b.height) return -1;
  return 0;
}

int main() {
  int N;
  cin >> N;
  person_t people[N];
  for (int i = 0; i < N; i++) {
    people[i].id = i;
    cin >> people[i].weight >> people[i].height;
  }

  int biggers[N];
  for (int i = 0; i < N; i++) biggers[i] = 0;
  
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (i == j) continue;
      if (comp(people[i], people[j]) > 0) biggers[j]++;
    }
  }

  for (int i = 0; i < N; i++) cout << biggers[i] + 1 << ' ';
  cout << endl;

  return 0;
}
