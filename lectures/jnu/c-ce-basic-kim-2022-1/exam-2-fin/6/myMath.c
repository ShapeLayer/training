#define swap(a, b) int c = a; a = b; b = c

double add(double a, double b)
{
	return a + b;
}

double sub(double a, double b)
{
	return a - b;
}

double mul(double a, double b)
{
	return a * b;
}

double divs(double a, double b)
{
	return a / b;
}

double spr(double a, double b)
{
	int x = (int)a;
	int y = (int)b;
	y--;
	if (y == 0) return x;
	return spr(x, y) * x;
}
double gcd(double a, double b)
{
	/*
	* 유클리드 호제법: 두 수의 나머지로 나눌 수 있을 때까지 나누기
	* 간단한 코드 까먹었으니 일단 작성하고 일반화시키기
	*/
	int x = (int)a;
	int y = (int)b;
	if (x > y) { swap(x, y); }
	if (y / x == y || y % x == 1) { return 1; }
	int z = y % x;
	if (z == 0) z = x;
	if (x % z != 0 || y % z != 0) { return 1; }
	return gcd(x / z, y / z) * z;
}
