#include <stdio.h>
#include <string.h>
int main(){
	char str[100];
	int result;
	char flag1[] = "STRT{s";
	char distract3[] = "flagflagflag"; 
	char flag2[] = "Tr1ngs_4";
	char distract4[] = "asfndasdvcnkasd";
	char flag3[] = "re_gr34t}";
	printf("Enter the password: ");
	scanf("%s",str);
	char distract1[] = "918374";
	char distract2[] = "1389273";
	if(!strcmp(str,"364929")){
		printf("%s%s%s",flag1,flag2,flag3);
		return 0;
	}
	printf("lol good try tho");
	return 0;
}
