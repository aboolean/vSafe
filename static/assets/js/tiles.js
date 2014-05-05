// populate section will list of tiles
function createTiles(tileList, section) {
                        for (var j = 0; j < tileList.length; j++){
                            var item = tileList[j];

                            var new_tile = document.createElement('div');
                            $(new_tile).addClass("result ui dimmable");
                            $(new_tile).html('<a href=' + item['link'] + ' class="ui dimmer"><div class="content"><div class="center"><div class="ui button">More Info</div></div></div></a>');

                            // add tags
                            for (var i = 0; i < item['tags'].length; i++){
                                $(new_tile).addClass(item['tags'][i]);
                            }

                            var new_img = document.createElement('div');
                            $(new_img).addClass("result-img");
                            var item_img_url = 'url(' + item['image'] + ')';
                            $(new_img).css('background-image', item_img_url);
                            $(new_tile).append(new_img);

                            var new_info = document.createElement('div');
                            $(new_info).addClass("result-info");
                            var new_title = document.createElement('h3');
                            $(new_title).addClass("result-title");
                            $(new_title).html(item['title']);
                            $(new_info).append(new_title);
                            var is_vt = document.createElement('div');
                            $(is_vt).html("Vegetarian");
                            $(is_vt).addClass("ui label");
                            if (item['vt'] == true){
                                $(is_vt).addClass("green");
                            } else{
                                $(is_vt).addClass("red");
                            }
                            $(new_info).append(is_vt);
                            var is_vg = document.createElement('div');
                            $(is_vg).html("Vegan");
                            $(is_vg).addClass("ui label");
                            if (item['vg'] == true) {
                                $(is_vg).addClass("green");
                            } else{
                                $(is_vg).addClass("red");
                            }
                            $(new_info).append(is_vg);
                            $(new_tile).append(new_info);

                            $(section).append(new_tile);
                        }
                    }

// all available items
var all_tiles = [
    {
        "title":   'Apple',
        "image":   '/vsafe/img/apple.jpg',
        "link":    'apple.html',
        "tags":    ['ingredient','fruit'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Barley',
        "image":   '/vsafe/img/barley.jpg',
        "link":    'barley.html',
        "tags":    ['ingredient','grain'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Basil',
        "image":   '/vsafe/img/basil.jpg',
        "link":    'basil.html',
        "tags":    ['ingredient','other'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Butter',
        "image":   '/vsafe/img/butter.jpg',
        "link":    'butter.html',
        "tags":    ['ingredient','dairy'],
        "vt":      true,
        "vg":      false
    },
    {
        "title":   'Cheese',
        "image":   '/vsafe/img/cheese.jpg',
        "link":    'cheese.html',
        "tags":    ['ingredient','dairy'],
        "vt":      true,
        "vg":      false
    },
    {
        "title":   'Chickpeas',
        "image":   '/vsafe/img/chickpeas.jpg',
        "link":    'chickpeas.html',
        "tags":    ['ingredient','protein'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Eggs',
        "image":   '/vsafe/img/eggs.jpg',
        "link":    'eggs.html',
        "tags":    ['ingredient','protein'],
        "vt":      true,
        "vg":      false
    },
    {
        "title":   'Flour',
        "image":   '/vsafe/img/flour.jpg',
        "link":    'flour.html',
        "tags":    ['ingredient','grain'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Green Pepper',
        "image":   '/vsafe/img/greenPepper.jpg',
        "link":    'green_pepper.html',
        "tags":    ['ingredient','vegetable'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Beef',
        "image":   '/vsafe/img/groundBeef.jpg',
        "link":    'beef.html',
        "tags":    ['ingredient','protein'],
        "vt":      false,
        "vg":      false
    },
    {
        "title":   'Hamburger',
        "image":   '/vsafe/img/hamburger.jpg',
        "link":    'hamburger.html',
        "tags":    ['dish','entree'],
        "vt":      false,
        "vg":      false
    },
    {
        "title":   'Hummus',
        "image":   '/vsafe/img/hummus.jpg',
        "link":    'hummus.html',
        "tags":    ['dish','appetizer','snack'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Margherita Pizza',
        "image":   '/vsafe/img/margheritaPizza.jpg',
        "link":    'margherita_pizza.html',
        "tags":    ['dish','entree'],
        "vt":      true,
        "vg":      false
    },
    {
        "title":   'Milk',
        "image":   '/vsafe/img/milk.jpg',
        "link":    'milk.html',
        "tags":    ['ingredient','dairy'],
        "vt":      true,
        "vg":      false
    },
    {
        "title":   'Mushrooms',
        "image":   '/vsafe/img/mushroom.jpg',
        "link":    'mushrooms.html',
        "tags":    ['ingredient','vegetable'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Mushroom Souffle',
        "image":   '/vsafe/img/mushroomSouffle.jpg',
        "link":    'mushroom_souffle.html',
        "tags":    ['dish','entree'],
        "vt":      true,
        "vg":      false
    },
    {
        "title":   'Olive Oil',
        "image":   '/vsafe/img/oliveOil.jpg',
        "link":    'olive_oil.html',
        "tags":    ['ingredient','condiment','other'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Onion',
        "image":   '/vsafe/img/onion.jpg',
        "link":    'onion.html',
        "tags":    ['ingredient','vegetable'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Peanut Butter',
        "image":   '/vsafe/img/peanutButter.jpg',
        "link":    'peanut_butter.html',
        "tags":    ['ingredient','protein','condiment'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Apple Wedges and Peanut Butter',
        "image":   '/vsafe/img/peanutButterApple.jpg',
        "link":    'apple_wedges_and_peanut_butter.html',
        "tags":    ['dish','snack'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Quinoa',
        "image":   '/vsafe/img/quinoa.jpg',
        "link":    'quinoa.html',
        "tags":    ['ingredient','grain'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Sriracha',
        "image":   '/vsafe/img/sriracha.jpg',
        "link":    'sriracha.html',
        "tags":    ['ingredient','condiment'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Spicy Stir Fry',
        "image":   '/vsafe/img/srirachaStirFry.jpg',
        "link":    'spicy_stir_fry.html',
        "tags":    ['dish','entree'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Sugar',
        "image":   '/vsafe/img/sugar.jpg',
        "link":    'sugar.html',
        "tags":    ['ingredient','other'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Sugar Cookies',
        "image":   '/vsafe/img/sugarCookies.jpg',
        "link":    'sugar_cookies.html',
        "tags":    ['dish','snack'],
        "vt":      true,
        "vg":      false
    },
    {
        "title":   'Tofu',
        "image":   '/vsafe/img/tofu.jpg',
        "link":    'tofu.html',
        "tags":    ['ingredient','protein'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Tomato',
        "image":   '/vsafe/img/tomato.jpg',
        "link":    'tomato.html',
        "tags":    ['ingredient','fruit','vegetable'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Vegan Cheese',
        "image":   '/vsafe/img/veganCheese.jpg',
        "link":    'vegan_cheese.html',
        "tags":    ['ingredient','dairy'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Vegetable Medley',
        "image":   '/vsafe/img/vegetableMedley.jpg',
        "link":    'vegetable_medly.html',
        "tags":    ['dish','entree'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Wheat Bread',
        "image":   '/vsafe/img/wheatBread.jpg',
        "link":    'wheat_bread.html',
        "tags":    ['ingredient','grain'],
        "vt":      true,
        "vg":      true
    },
    {
        "title":   'Zucchini',
        "image":   '/vsafe/img/zucchini.jpg',
        "link":    'zucchini.html',
        "tags":    ['ingredient','vegetable'],
        "vt":      true,
        "vg":      true
    },
];

// create mapping between title and item info
var map_tiles = Array();
for (var u = 0; u < all_tiles.length; u++) {
    var item = all_tiles[u];
    map_tiles[item['title']] = item;
}
