#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
        if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
            // Create an empty object if w or h is not a positive integer or equal to 0
            return {};
        }

        this.width = w;
        this.height = h;
    }

    print () {
        for(let i = 0; i < this.height; i++) {
            let str = '';
            for (let j = 0; j < this.width; j++)
                str += 'x';
            console.log(str);
        }     
    }
}
