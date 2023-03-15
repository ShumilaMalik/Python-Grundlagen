package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter message: ")
	message, _ := reader.ReadString('\n')
	message = strings.TrimSpace(message)
	
	cow := `
 _________
< ` + message + ` >
 ---------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
`
	fmt.Println(strings.TrimSpace(cow))
}