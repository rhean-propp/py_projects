//- ssize_t read(int fd, void *buf, size_t count);
//- ssize_t write(int fd, const void *buf, size_t count);
//- void exit(int status);

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

int main() {
	
	//FILE *fd;
	int fd = open ("test.txt", O_RDONLY, 0);

	read(fd, 0, 20);
	
	write(fd, 0, 20);

	close(fd);

	
	
	//write(fd, 0, 20);

	exit(1);

	return 0;
}
