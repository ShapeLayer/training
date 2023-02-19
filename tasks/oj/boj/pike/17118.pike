int main()
{
  int a = 860798509;
  int b = 198609463;
  int p = 1000000007;
  write("%d\n", 
    (a * (int)Stdio.stdin->gets() + b) % p
  );
  return 0;
}