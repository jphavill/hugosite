// {
//
// }

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

// when parsing content for search, ignore code multiline blocks, delete words than occur most commonly, such as "the"
// requires two passes, fine because that only happens when i generate a new page
// os.walks through all files in the content section
//