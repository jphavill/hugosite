// import {findElement, createButton} from "/js/lookup.js";
console.log('test3')
var visible = true
var refEl = findElement('practiceProblem').parentNode
var toggleButton = createButton(toggleVisible, refEl, 'Show Solution', 'toggleButton', 'practiceButton', true)
toggleVisible()
console.log('after creating button')
function toggleVisible(){
    visible = !visible
    let solution = findElement('practiceProblem')
    if (visible){
        solution.classList.remove('hiddencode')
        toggleButton.textContent = 'Hide Solution'
    } else {
        solution.classList.add('hiddencode')
        toggleButton.textContent = 'Show Solution'
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

function createButton(func, referenceElement, textContent, className=null, id=null, previousIdentifier=false){
    var tempButton = document.createElement("button");

    // sets all passed attributes
    var params = [className, id];
    var attributes = ["className", "id"];
    for (var i=0; i<params.length; i++){
        if (params[i] !== null){
            tempButton.setAttribute(attributes[i], params[i]);
        }
    }

    //sets the text of the button
    tempButton.textContent = textContent;

    if (!previousIdentifier){
        referenceElement.appendChild(tempButton);
    } else{
        referenceElement.parentNode.insertBefore(tempButton, referenceElement.nextSibling)
    }
    // sets the parent of the button, checking if it is an id, name, class and finally an element type. defaults to body

    tempButton.addEventListener("click", func);
    return tempButton;
}