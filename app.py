from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

import random
character_map = {
    "ash": {
        "image": "ash.jpg",
        "lines": ["jivan ki lanka lgi hui hai, bhaii ke paas kam se kam pikachu tohh tha, terepe tohh vohh bhi nhi hai."]
},
    "bhochan": {
        "image": "bhochan.jpg",
        "lines": ["aadha jeevan toh naak saaf krne mein hi nikal gya, ab khud bhi duniya se saaf krne ka time aa gya bhaii. Krr de😊"]
},
    "bubbles": {
        "image": "bhondu.jpg",
        "lines": ["bubbles jaise bhondu ho tum, log fyada utha lenge tumhara😭. Lekin hai kya kuch tumhara fyada??"]
},
    "blossom": {
        "image": "blossom.jpg",
        "lines": ["leader ban na tha didi/bhaiji ko. Lekin sunta kon hai tumhari bhaii??? "]
},
    "buttercup": {
        "image": "chidchidi.jpg",
        "lines": ["inti chidhan ho gyi hai tumko logo se, abb toh tum duniya hi chhod do bhaii😭"]
},
    "brock": {
        "image": "brock.jpg",
        "lines": ["bhai ab toh londiya baazi chhod de, one woman man bannja suar😒"]
},
    "chhota bheem": {
        "image": "chhota bheem.jpg",
        "lines": ["bhaii kitna bda playboy hai re tu, khud pe dhyaan de, padhai likhai karo ias wiyas bano aur dekh ko sambhalo"]
},
    "chutki": {
        "image": "chutki.jpg",
        "lines": ["kya hua bhaii?? chala gya bheem chhor ke?? aur padh mardjaat ke peeche🫡"]
},
    "courage": {
        "image": "courage.jpg",
        "lines": ["fattu kahin ka, kabhi tohh apne uss supercomputer ko hta ke dimag lga le, ghee khatam hai bhaii tera na ho payega terse😒"]
},
    "dekisugi": {
        "image": "dekisugi.jpg",
        "lines": ["bhaii tu iss duniya ke liye jyada hi achcha hai bhaii, bura bann thoda....yahan log achche nhi hain😭😭"]
},
    "doraemon": {
        "image": "doraemon.jpg",
        "lines": ["bhaii tu bigad rha hai logo ki zindagi😭....paltu kahin ka itne gadget hone ke baad bhi jyada bhav khata hai, rakoon!!"]
},
    "gian": {
        "image": "gian.jpg",
        "lines": ["besure aadmi, chupp hoja tu, jyada na bona... tere bolne se chidan machti hai, CHUPP!! BILKUL CHUPP!!"]
},
    "hiroshi": {
        "image": "hiroshi.jpg",
        "lines": ["bin kuch kare bhi thak gya tu??? kya aalsi aadmi hai re...CHIIII!!"]
},
    "indraverma": {
        "image": "indraverma.jpg",
        "lines": ["Bhaii, matlabi suar...jabtak kaam hai tabtak devta hai koi, vrna nikal ja...heinn???"]
},
    "james": {
        "image": "james.jpg",
        "lines": ["bande ka facecard toh achcha hai, style bhi hai...phir bhi jivan ki lanka lgi hui hai😭 "]
},
    "jessie": {
        "image": "jessie.jpg",
        "lines": ["baddie toh hai tu but bhaii jab logo ki baaton mein aa jati hai tuu, sudharr ja baddieee😭"]
},
    "kai": {
        "image": "kai.jpg",
        "lines": ["og face card, nonchalant....kitni tarif karun bhaii, perfect hai tuu😭🩷"]
},
    "kalia": {
        "image": "kalia.jpg",
        "lines": ["MOTE kalia, jyada gunda bnta hai, ek repte mein ghoomta phirega, laadleeee "]
},
    "kasama": {
        "image": "kasama.jpg",
        "lines": ["feku!! Suneo ke bhaiii, mana ki terko angrezi aati hai, lekin phir bhi kitna show off krega bhaiii??"]
},
    "masao": {
        "image": "masao.jpg",
        "lines": ["kya re desperate aadmi, kuch kaam dham nhi hai terko?? jab koi terko bhav nhi derha toh kyun pda hai uske peeche...koi self respect hai teri???"]
},
    "matsuzaka": {
        "image": "matsuzaka.jpg",
        "lines": ["Areee ma'am pta hai baddie ho aap, lekin itna bhi nahh feko bhaii, apki baato ka sar hota hai na per😭"]
},
    "meowth": {
        "image": "meowth.jpg",
        "lines": ["HTTT BILLE!!! terse jyada tohh psyduck mein buddhi hai😒"]
},
    "misty": {
        "image": "misty.jpg",
        "lines": ["Baddie ma'am, Aap toh achchi ho😍"]
},
    "mitsi": {
        "image": "mitsi.jpg",
        "lines": ["Aalsii!!! Sote reh tu, aur logo se bolna bhaii kaam kar kar ke thak gyi hu🤨"]
},
    "muriel": {
        "image": "muriel.jpg",
        "lines": ["Aap tohh achchi ho, lekin thoda apne aadmi pe dhyaan do, bhot dushtt aadmi hai"]
},
    "nanny": {
        "image": "nanny.jpg",
        "lines": ["Lady Don!! Bhai koi self respect hai, jab tere dosto ko tera office office nhi khelna hai tohh kyun jaati hai unke paas, burai krte hain teri peeth piche, sudhar ja, naye dost bna le"]
},
    "nobita": {
        "image": "nobita.jpg",
        "lines": ["Fattu!! Tere jivan ka kya aim hai bhaii, din raat rota reh tu, complain krta hreh bss, na ldki bhav deri, na tera future bann rha hai, sharam krr le"]
},
    "oldman": {
        "image": "oldman.jpg",
        "lines": ["Akdu, terko kisi din mai ki khatm krr du, DUSHTTT AADMI, BUDDHEE!!!🤬"]
},
    "pikachu": {
        "image": "pikachu.jpg",
        "lines": ["aap tohh pookie ho🥰"]
},
    "principal": {
        "image": "principal.jpg",
        "lines": ["GANGLEADER!!!!!! eklauta mard"]
},
    "psyduck": {
        "image": "psyduck.jpg",
        "lines": ["Bhondu bachchha meraa😭😭, kitna pyara hai tuu!!"]
},
    "raju": {
        "image": "raju.jpg",
        "lines": ["TAKLE!!! do baal toh hain sar mein, 3 footiya toh tu hai, bheem ki chamchagiri krta hai, kuch hai khudka bhaii???"]
},
    "shinchan": {
        "image": "shinchan.jpg",
        "lines": ["AREYYY SIRRR🫡🫡 apki tohh baat hi kuch aur hai!!!"]
},
    "shiro": {
        "image": "shiro.jpg",
        "lines": ["CHADDDD!!!!!"]
},
    "shizuka": {
        "image": "shizuka.jpg",
        "lines": ["khud bhi kuch krr le kaamchor, vaise tohh buri nhi hai tu, lein jyada nahh helpless hone ki acting nahh krr, nautanki"]
},
    "suneo": {
        "image": "suneo.jpg",
        "lines": ["FEKUUUUUU, tu ekk kaam krr, doob ja"]
},
    "togepi": {
        "image": "togepi.jpg",
        "lines": ["CUTIEE hain aap🥰"]
},
    "tuntun": {
        "image": "tuntun.jpg",
        "lines": ["EMPOWERD LADYYY!!!🔥🔥"]
},
}
@app.route('/get_character')
def get_character():
    char = random.choice(list(character_map.keys()))
    data = character_map[char]

    line = random.choice(data["lines"])

    return jsonify({
        "image": data["image"],
        "line": line
    })


@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    image_data = data['image']  # we are not using it yet

    # just return random for now
    char = random.choice(list(character_map.keys()))
    data = character_map[char]

    line = random.choice(data["lines"])

    return jsonify({
        "image": data["image"],
        "line": line
    })

from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)