function searchArticles(event, input) {
    var code = event.keyCode
    // if the escape key is pressed
    if (code === 27) {
        // clear the serach box
        input.value=''
        return
    }
    searchTerm = input.value.toLowerCase()
    console.log(searchTerm)
    // if the enter key is pressed
    if (code === 13) {
        // go to the top result 

    }

}