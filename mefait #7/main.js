console.log(1 == "1"); // Don't touch it

const canvas = document.getElementById("game");
const context = canvas.getContext("2d");
const spanScore = document.getElementById("score");
const spanVie = document.getElementById("vie");
var width = window.innerWidth;
var height = window.innerHeight;
const tps = 12; // nombre de frames entre chaque tir
const speed = 10;
const bulletSpeed = 16;
const alexisSpeed = 1.6;
const oliviSpeed = 1;
let zic = new Audio("le-sanglier-qui-court-instrumentale.ogg");
let alex = new Image();
alex.src = "alexis.bmp";

let megalex = new Image();
megalex.src = "megaalexis.bmp";

let rayan = new Image();
let nayar = new Image();
let dieu = new Image();
dieu.src = "olivi-sec.png";

let sldwks = new Image();
sldwks.src = "sldwks.jpg";

let py = new Image();
py.src = "py.png";

selection = 0;
img = document.getElementById("img");
img.src = selection + ".png";

function droite() {
    selection += 1;
    selection = selection % 4;
    img.src = selection + ".png";
}

function gauche() {
    selection -= 1;
    if (selection < 0)
        selection = 3;
    img.src = selection + ".png";
}

class Entity {
    constructor(x, y, sx, sy, image) {
        this.x = x;
        this.y = y;
        this.vx = 0;
        this.vy = 0;
        this.sx = sx;
        this.sy = sy;
        this.aaron = false;
        this.image = image;
        this.collision = [];
    }

    draw() {
        context.drawImage(this.image, this.x - this.sx / 2, this.y - this.sy / 2, this.sx, this.sy);
    }

    update() {
        this.x += this.vx;
        this.y += this.vy;
        if (this.y - this.sy / 2 >= height || this.y + this.sx / 2 <= 0) {
            this.aaron = true;
        }
    }
    collide(mdrsman, truc) {
        if (!(this.x - this.sx / 2 > mdrsman.x + mdrsman.sx / 2 ||
                this.y - this.sy / 2 > mdrsman.y + mdrsman.sy / 2 ||
                this.x + this.sx / 2 < mdrsman.x - mdrsman.sx / 2 ||
                this.y + this.sy / 2 < mdrsman.y - mdrsman.sy / 2)) {
            truc(this, mdrsman);
        }
    }
}

class Alexis extends Entity {
    constructor() {
        super(Math.random() * width, 0, 60, 60, alex)
        this.vy = alexisSpeed;
        this.collision = [Joseph];
    }

    update() {
        this.vx = (joseph.x - this.x) / 700
        super.update();
    }
    collide(mdrsman) {
        super.collide(mdrsman, (yes, no) => {
            yes.aaron = true;
            vie--;
            if (vie == 0) {
                end()
            }
        })
    }
}

class MegaAlexis extends Entity {
    constructor() {
        super(Math.random() * width, 0, 230, 100, megalex)
        this.vy = alexisSpeed;
        this.dir = 3;
        this.time = 70;
        this.ctime = 0;
        this.life = 6;
        this.collision = [Vincent];
    }

    update() {
        if (Math.random() < 0.01) {
            this.dir *= -1
        }
        if (this.ctime < 0) {
            entities.push(new VincentCaniballe(this.x, this.y, joseph.x, joseph.y));
            this.ctime = this.time;
        }
        this.ctime -= 1;
        this.vx = this.dir;
        this.vy = (100 - this.y) / 100;
        super.update();
        this.x = ((this.x % width) + width) % width;
        if (this.life < 0) {
            this.aaron = true;
        }
    }
    collide(vincent) {
        super.collide(vincent, (yes, no) => {
            no.aaron = true;
            this.life--;
            this.sx *= 0.9;
            this.sy *= 0.9;
            if (this.life < 0) {
                this.aaron = true;
                for (let i = 0; i < 50; i++) {
                    entities.push(new mor(no.x, no.y));
                }
                lpet = new Pet(lpet);
                entities.push(lpet);
            }
        })
    }
}

class Olivi extends Entity {
    constructor() {
        super(Math.random() * width, 0, 60, 60, dieu);
    }
    update() {
        this.y += oliviSpeed;
        if (this.y >= height + this.sy) {
            this.aaron = true;
        }
    }

}

class Vincent extends Entity {
    // les tirs de joseph
    constructor(x, y) {
        super(x, y, 5, 10, null);
        this.vy = -bulletSpeed;
        this.collision = [Alexis, Olivi];
    }

    draw() {
        context.fillStyle = "#6174ee";
        context.fillRect(this.x - this.sx / 2, this.y - this.sy / 2, this.sx, this.sy);
    }
    collide(alex) {
        super.collide(alex, (yes, no) => {
            yes.aaron = true;
            no.aaron = true;
            if (no instanceof Alexis) {
                score += 1;
                for (let i = 0; i < 50; i++) {
                    entities.push(new mor(no.x, no.y));
                }
                if (score % 30 == 0 && Math.ceil(score/30)>boss && score != 0) {
                    boss++;
                    for(let i = 0; i < Math.ceil(score/30); i++){
                      entities.push(new MegaAlexis());
                    }
                }
            } else if (no instanceof Olivi) {
                score -= 1;
                if (score < -10 && !mmmmmmm) {
                  mmmmmmm = true;
                  for(let i = 0; i < 50; i++){
                    entities.push(new MegaAlexis());
                  }
                }
            }
        })
    }
}

class VincentCaniballe extends Entity {
    // Les tirs de megalexis
    constructor(x, y, px, py) {
        super(x, y, 50, 50, sldwks);
        let dist = Math.sqrt(Math.pow(px - x, 2) + Math.pow(py - y, 2));
        this.vx = 3 * (px - x) / dist;
        this.vy = 3 * (py - y) / dist;
        this.collision = [Joseph];
    }

    /*draw() {
        context.fillStyle = "#9e8b11";
        context.fillRect(this.x - this.sx / 2, this.y - this.sy / 2, this.sx, this.sy);
    }*/
    collide(jof) {
        super.collide(jof, (yes, no) => {
            yes.aaron = true;
            vie--;
            if (vie == 0) {
                end()
            }
        })
    }
}

class VincentLeBg extends Entity {
    // les tirs de joseph
    constructor(x, y) {
        super(x, y, 20, 20, null);
        this.vy = -2.1;
        this.collision = [Alexis];
    }

    draw() {
        context.fillStyle = "#6174ee";
        context.fillRect(this.x - this.sx / 2, this.y - this.sy / 2, this.sx, this.sy);
    }
    collide(alex) {
        super.collide(alex, (yes, no) => {
            yes.aaron = true;
            no.aaron = true;
            if (no instanceof Alexis) {
                score += 1;
                for (let i = 0; i < 50; i++) {
                    entities.push(new mor(no.x, no.y));
                }
                if (score % 30 == 0 && Math.ceil(score/30)>boss && score != 0) {
                    boss++;
                    for(let i = 0; i < Math.ceil(score/30); i++){
                      entities.push(new MegaAlexis());
                    }
                }
            }
        })
    }
}

class Joseph extends Entity {
    constructor() {
        super(width / 2, height - 50, 90, 90, rayan);
    }
    update() {
        if (left) {
            this.vx -= 2;
            entities.push(new paillette(joseph.x + joseph.sx / 2, height, Math.PI * 3 / 2, Math.PI / 16));
            this.image = rayan;
        }
        if (right) {
            this.vx += 2;
            entities.push(new paillette(joseph.x - joseph.sx / 2, height, -Math.PI / 2, Math.PI / 16));
            this.image = nayar;
        }
        this.vx *= 0.8;
        super.update();
        this.x = ((this.x % width) + width) % width;
    }
}

class paillette extends Entity {
    constructor(x, y, angle = 0, ouverture = Math.PI * 2) {
        super(x, y, 10, null, null);
        this.angle = angle + ouverture * (Math.random() * 2 - 1);
        this.forse = Math.random() * 4 + 2;
        this.vx = Math.cos(this.angle) * this.forse;
        this.vy = Math.sin(this.angle) * this.forse;
        this.color = "rgb(255, 255, 255)";
    }
    update() {
        this.vy += .2;
        super.update();
    }

    draw() {
        context.fillStyle = this.color;
        context.beginPath();
        context.arc(this.x, this.y, 5, 0, Math.PI * 2);
        context.fill();
        context.closePath();
    }
}

class mor extends Entity {
    // Les paillettes d'Alexis
    constructor(x, y) {
        super(x, y, 10, null, null);
        this.angle = Math.random() * Math.PI * 2;
        this.forse = Math.random() * 4 + 2;
        this.vx = Math.cos(this.angle) * this.forse;
        this.vy = Math.sin(this.angle) * this.forse;
        this.color = "rgb(247, 255, 106)";
        this.alpha = 1;
    }
    update() {
        this.vy += .2;
        this.alpha -= 0.04;
        if (this.alpha <= 0) {
            this.aaron = true;
        }
        super.update();
    }

    draw() {
        context.beginPath();
        context.fillStyle = this.color;
        context.globalAlpha = this.alpha;
        context.arc(this.x, this.y, 5, 0, Math.PI * 2);
        context.fill();
        context.closePath();
        context.globalAlpha = 1;
    }
}

class Pet extends Entity{
    constructor(f){
      super(0, height - 30, 50, 50, py);
      this.dist = 200;
      this.follower = f;
      this.time = 700;
      this.ctime = Math.floor(Math.random()*this.time);
    }
    update() {
        if (this.ctime < 0) {
            entities.push(new VincentLeBg(this.x, height - 50));
            this.ctime = this.time;
        }
        this.ctime -= 1;
        if (this.follower.x - this.dist < this.x) {
          this.vx -= 0.5;
        }
        if (this.follower.x + this.dist > this.x) {
          this.vx += 0.5;
        }
        this.vx *= 0.95;
        super.update();
    }
}

function resize() {
    width = window.innerWidth,
        height = window.innerHeight,
        ratio = window.devicePixelRatio;
    canvas.width = width * ratio;
    canvas.height = height * ratio;
    canvas.style.width = width + "px";
    canvas.style.height = height + "px";
    context.scale(ratio, ratio);
}

window.onresize = function() {
    resize();
};

window.onload = function() {
    resize();
    //window.requestAnimationFrame(boucle);
};

document.addEventListener("keydown", (e) => {
    if (e.repeat) return;
    if (e.keyCode == 37 || e.keyCode == 81) {
        left = true;

    } else if (e.keyCode == 39 || e.keyCode == 68) {
        right = true;

    } else if (e.keyCode == 38 || e.keyCode == 90) {
        up = true;
    }
}, false);

document.addEventListener('keyup', (e) => {
    if (e.keyCode == 37 || e.keyCode == 81) {
        left = false;
    } else if (e.keyCode == 39 || e.keyCode == 68) {
        right = false;
    } else if (e.keyCode == 38 || e.keyCode == 90) {
        up = false;
    }
}, false);
document.onmousedown = function(e) {
    if (e.clientX > width / 2) {
        right = true;
    }
    if (e.clientX < width / 2) {
        left = true;
    }
    if (e.clientY < height / 2) {
        up = true;
    }
}
document.onmouseup = function(e) {
    if (e.clientX > width / 2) {
        right = false;
    }
    if (e.clientX < width / 2) {
        left = false;
    }
    if (e.clientY < height / 2) {
        up = false;
    }
}

let joseph = new Joseph();
let lpet = joseph;
let direc = 0;
let entities = [joseph];
let left = false;
let right = false;
let up = false;
let shoot = 0;
let score = 0;
let vie = 3;
let boss = 0;
let mmmmmmm = false;


function boucle() {
    context.clearRect(0, 0, width, height);
    context.beginPath();
    context.fillStyle = "rgba(0, 0, 0, 0.5)";
    context.rect(0, 0, width, height);
    context.fill();
    context.closePath();


    if (up && shoot == 0) {
        entities.push(new Vincent(joseph.x, height - 50));
        shoot = tps;
    }
    shoot = Math.max(0, shoot - 1);

    if (Math.random() > .98) {
        entities.push(new Alexis())
    }
    if (Math.random() > .99) {
        entities.push(new Olivi())
    }

    for (const entity of entities) {
        entity.update();
        if (entity.collide.length != 0) {
            for (const otherEntity of entities) {
                for (type of entity.collision) {
                    if (otherEntity instanceof type) {
                        entity.collide(otherEntity);
                    }
                }
            }
        }
    }
    entities = entities.filter((entity) => !entity.aaron);
    for (const entity of entities) {
        entity.draw();
    }

    spanScore.innerHTML = score;
    spanVie.innerHTML = "💖".repeat(vie);
    window.requestAnimationFrame(boucle);
}

function start() {
    rayan.onload = function() {
        try {
            // essayer de renverser verticalement RAYAN
            let c = document.createElement('canvas');
            c.width = rayan.width;
            c.height = rayan.height;
            let ctx = c.getContext('2d');
            ctx.scale(-1, 1);
            ctx.drawImage(rayan, -rayan.width, 0);
            rayan.onload = undefined;
            nayar.src = c.toDataURL();
            delete c, ctx;
        } catch (e) {
            console.log(e);
            nayar.src = rayan.src;
        }

    }
    rayan.src = selection + ".png";

    zic.play();
    document.getElementById("menu").style.display = "none";
    document.getElementById("LEJEU").style.display = "block";
    window.requestAnimationFrame(boucle);
}

function end() {
    zic.pause();
    document.getElementById("LEJEU").style.display = "none";
    document.getElementById("menu").style.display = "block";
    document.getElementById("menu").innerHTML = `<h1>t'as perdu espèce de SI</h1><h2>Score : ${score}</h2><button onclick="location.reload()">Retenter ma chance wlh</button>`;
}
