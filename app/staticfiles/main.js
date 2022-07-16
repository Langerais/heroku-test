var hiddenClass = 'hidden';
var shownClass = 'toggled-from-hidden';

function propertySectionHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === hiddenClass) {
            child.className = shownClass;
        }
    }
    console.log("HOVER")
}

function propertySectionEndHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === shownClass) {
            child.className = hiddenClass;
        }
    }
}

(function() {
    var propertySections = document.getElementsByClassName('property-name');
    for(var i = 0; i < petSections.length; i++) {
        propertySections[i].addEventListener('mouseover', propertySectionHover);
        propertySections[i].addEventListener('mouseout', propertySectionEndHover);
    }
}());
