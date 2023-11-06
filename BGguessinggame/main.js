let IMAGEDISPLAY = 5000

class imagepulling{
    constructor(directory, name)
    {
        this.directory = directory;
        this.name = name;
    }
    
    dataopenfile(filelocation){
        fetch("AnimeBG//BGguessinggame//atabase.txt")
        .then(response => {
            if (!response.ok) {
              throw new Error("File invalid");
            }
            // Parse the response as JSON
            return response.json();
          })


    }
}


function greet(){
    return "Hello, World"
}

console.log(greet());