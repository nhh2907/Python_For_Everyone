#include <stdio.h>

// \n is just one character, not two characters
int main()
{
	int i;
	int j;
	char string[] =  "this is the world";
	char string2[] = "this is \nthe world";

	i = 0;
	while(string[i] != '\0')
	{
		i++;
	}

	j = 0;
	while(string2[j] != '\0')
	{
		j++;
	}

	printf("this is the world = %d\n", i);
	printf("this is \\nthe world = %d\n", j);
}
