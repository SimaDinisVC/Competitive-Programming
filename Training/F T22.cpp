#include <iostream>

using namespace std;

int seq1[100], seq2[100]; // Duas arrays para guardar as sequencias

int par(int numero) {
  return numero % 2 == 0;
}

int main() {
  int n1, n2;

  cin >> n1;                    // Vamos ler a primeira sequencia
  for (int i = 0; i < n1; i++)
  cin >> seq1[i];

  cin >> n2;                    // Vamos ler a segunda sequencia
  for (int i = 0; i < n2; i++)
  cin >> seq2[i];

  int npares = 0, nimpares = 0; // Os contadores de pares e impares
  for (int i = 0; i < n1; i++) // Para cada par de numeros possivel
    for (int j = 0; j < n2; j++)
      if (par(seq1[i] + seq2[j])) // Verificar se a soma e par
        npares++;
      else
        nimpares++;

  cout << npares << " " << nimpares << endl;

  return 0;
}