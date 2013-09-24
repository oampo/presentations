var Presentation = function() {
    this.slides = $('section');
    this.index = parseInt(window.location.hash.slice(1)) || 0;

    this.disableContextMenu();

    $(document).keydown(this.onKeyDown.bind(this));
    $(document).mousedown(this.onMouseClick.bind(this));

    this.move();
};

Presentation.prototype.move = function() {
    this.slides.filter(":visible").fadeOut("fast", function() {
        $(this.slides[this.index]).fadeIn("fast");
    }.bind(this));
};

Presentation.prototype.next = function() {
    if (this.index == this.slides.length - 1) {
        return;
    }
    this.index += 1;
    this.move();
    this.setHash();
};

Presentation.prototype.prev = function() {
    if (this.index == 0) {
        return;
    }
    this.index -= 1;
    this.move();
    this.setHash();
};

Presentation.prototype.setHash = function() {
    window.location.hash = "#" + this.index.toString();
};

Presentation.prototype.onKeyDown = function(event) {
    if (event.keyCode == 37) {
        this.prev();
    }
    else if (event.keyCode == 32 || event.keyCode == 39) {
        this.next();
    }
};

Presentation.prototype.onMouseClick = function(event) {
    if (event.which == 1) {
        this.next();
    }
    else if (event.which == 3) {
        this.prev();
    }
};

Presentation.prototype.disableContextMenu = function() {
    $(document).bind("contextmenu", function(event) {
        return false;
    });
};

$(document).ready(function() {
    var presentation = new Presentation();
})
