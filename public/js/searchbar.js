// import { findElement } from "/js/lookup.js";

var searchPairs = {
    'about': '/about',
    'homepage': '/',
    'if-else': '/articles/if-else',
    'math': '/articles/mathematics',
    'strings': '/articles/strings',
    'print': '/articles/print',
    'tuples': '/articles/tuples',
    'articles': '/articles'
}

var highlighted = 0
console.log('test')
function searchArticles(event, input) {
    var code = event.keyCode
    var maxResults = 5
    // if the escape key is pressed
    if (code === 27) {
        // clear the serach box
        input.value=''
    }
    let searchTerm = input.value.toLowerCase()
    let searchResultsBox = findElement('searchResults')
    searchResultsBox.innerHTML = ''
    if (searchTerm !== ''){
        var searchResults = []
        for (var key in searchPairs) {
            if (key.toLowerCase().includes(searchTerm)){
                searchResults.push(key)
            }

        }

        if (code === 40) {
            highlighted = Math.min(highlighted+1, searchResults.length-1, maxResults-1)
            console.log(highlighted)
        }
        if (code === 38) {
            highlighted = Math.max(highlighted-1, 0)
        }
        let resultsBox = document.createElement('ul')
        if (searchResults.length > 0){
            searchResultsBox.classList.remove('jsHidden')
        }
        for (let i = 0; i<Math.min(searchResults.length, maxResults); i++){
            var entry = document.createElement('li')
            var entryLink = document.createElement('a')
            entryLink.innerText = searchResults[i]
            entryLink.setAttribute('href', searchPairs[searchResults[i]])
            if (i === highlighted){
                entry.classList.add('jsSearchHighlighted')
            }
            if (i !== highlighted){
                entry.classList.remove('jsSearchHighlighted')
            }
            entry.appendChild(entryLink)
            resultsBox.appendChild(entry)
        }
        searchResultsBox.appendChild(resultsBox)
    }
    if (code === 13) {
        window.location.href = searchPairs[searchResults[highlighted]]

    }
    if (input.value === ''){
        highlighted = 0
        searchResultsBox.classList.add('jsHidden')
    }


}



// when parsing content for search, ignore code multiline blocks, delete words than occur most commonly, such as "the"
// requires two passes, fine because that only happens when i generate a new page
// os.walks through all files in the content section
//

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
