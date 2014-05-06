// append new tile to section
function createTile(identifier, name, image, vt, vg, section) {
    var new_tile = document.createElement('div');

    $(new_tile).addClass("result ui dimmable");

    // identifier and link
    var link = '/vsafe/';
    if (identifier[0] == "I") {
        link = '/vsafe/browse/ingredient/' + identifier.substring(1);
    } else if (identifier[0] == "D") {
        link = '/vsafe/browse/dish/' + identifier.substring(1);
    }
    $(new_tile).html('<a href=' + link + ' class="ui dimmer"><div class="content"><div class="center"><div class="ui button">More Info</div></div></div></a>');

    $(new_tile).attr('id',identifier);

    // image
    var new_img = document.createElement('div');
    $(new_img).addClass("result-img");
    var item_img_url = 'url(\'/vsafe/img/' + image + '\')';
    $(new_img).css('background-image', item_img_url);
    $(new_tile).append(new_img);


    var new_info = document.createElement('div');
    $(new_info).addClass("result-info");
    var new_title = document.createElement('h3');
    $(new_title).addClass("result-title");
    $(new_title).html(name);
    $(new_info).append(new_title);
    var is_vt = document.createElement('div');
    $(is_vt).html("Vegetarian");
    $(is_vt).addClass("ui label");
    if (vt === true){
        $(is_vt).addClass("green");
    } else{
        $(is_vt).addClass("red");
    }
    $(new_info).append(is_vt);
    var is_vg = document.createElement('div');
    $(is_vg).html("Vegan");
    $(is_vg).addClass("ui label");
    if (vg === true) {
        $(is_vg).addClass("green");
    } else{
        $(is_vg).addClass("red");
    }
    $(new_info).append(is_vg);
    $(new_tile).append(new_info);

    $(section).append(new_tile);
}

// previously
// var all_tiles = [
//     {
//         "title":   'Apple',
//         "image":   '/vsafe/img/apple.jpg',
//         "link":    '/vsafe/browse/ingredient/',
//         "tags":    ['ingredient','fruit'],
//         "vt":      true,
//         "vg":      true
//     },
// ]
