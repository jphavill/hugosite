var searchPairs = {
    'about': '/about',
    'homepage': '/',
    'if-else': '/articles/if-else',
    'math': '/articles/math',
    'strings': '/articles/strings',
    'print': '/articles/print',
    'tuples': '/articles/tuples',
    'articles': '/articles'
}


function searchArticles(event, input) {
    var code = event.keyCode
    // if the escape key is pressed
    if (code === 27) {
        // clear the serach box
        input.value=''
    }
    searchTerm = input.value.toLowerCase()
    let searchResultsBox = findElement('searchResults')
    searchResultsBox.innerHTML = ''
    searchResultsBox.classList.add('jsHidden')
    if (searchTerm != ''){
        var searchResults = []
        for (var key in searchPairs) {
            if (key.toLowerCase().includes(searchTerm)){
                searchResults.push(key)
            }

        }

        let resultsBox = document.createElement('ul')
        if (searchResults.length > 0){
            searchResultsBox.classList.remove('jsHidden')
        }
        for (let i = 0; i<Math.min(searchResults.length, 5); i++){
            console.log(i)
            var entry = document.createElement('li')
            var entryLink = document.createElement('a')
            entryLink.innerText = searchResults[i]
            entryLink.setAttribute('href', searchPairs[searchResults[i]])
            entry.appendChild(entryLink)
            resultsBox.appendChild(entry)
        }
        searchResultsBox.appendChild(resultsBox)
    }
    //todo add arrow keys to select between results and enter to go to that link
    // if the enter key is pressed
    if (code === 13) {
        // go to the top result 

    }


}

function findElement(identifier){
    // returns the element using the identifier checking if it is an id, name, class and finally an element type.
    var element = document.getElementById(identifier);
    if (element == null){
        element = document.getElementsByTagName(identifier)[0];
    }
    if (element == null){
        element = document.getElementsByClassName(identifier)[0];
    }
    if (element == null){
        element = document.getElementsByName(identifier)[0];
    }
    if (element == null){
        element = document.getElementsByTagName(identifier)[0];
    }
    return element;

}

// when parsing content for search, ignore code multiline blocks, delete words than occur most commonly, such as "the"
// requires two passes, fine because that only happens when i generate a new page
// os.walks through all files in the content section
//