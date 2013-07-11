# Using the Unbounded Spigot Algorithm to find Digits of Pi
# www.cs.ox.ac.uk/people/jermy.gibbons/publications/spigot.pdf

def pi_digits(n):
	q, r, t, j = 1, 180, 60, 2
	for i in range(n):
		u, y = 3*(3*j+1)*(3*j+2), (q*(27*j-12)+5*r)//(5*t)
		yield y
		q, r, t, j = 10*q*j*(2*j-1), 10*u*(q*(5*j-2)+r-y*t), t*u, j+1

def print_pi(n=16):
	pi_temp = [i for i in pi_digits(n)]
	pi = ""

	pi_temp.insert(1,'.')

	for i in pi_temp:
		pi += str(i)

	return pi