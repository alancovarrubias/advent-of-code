const FILENAME = 'files/10.txt';
const fs = require('fs');

class Asteroid {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.primeFactors = [2, 3, 5, 7, 11, 13]
  }

  simplifyDistance(x, y) {
    this.primeFactors.forEach(factor => {
      if (x%factor == 0 && y%factor == 0) {
        [x, y] = this.simplifyDistance(x/factor, y/factor);
      }
    });
    return [x, y];
  }

  isDetectable(monitor, detected) {
    let detectable = true;
    const [x_dist, y_dist] = this.simplifyDistance(this.x - monitor.x, this.y - monitor.y);
    detected.forEach(asteroid => {
      const [d_x_dist, d_y_dist] = this.simplifyDistance(asteroid.x - monitor.x, asteroid.y - monitor.y);
      if (x_dist == d_x_dist && y_dist == d_y_dist) {
        detectable = false;
      }
    });
    return detectable;
  }
}

class AsteroidMap {
  constructor() {
    const mapString = fs.readFileSync(FILENAME).toString().trim();
    this.data = mapString.split('\n').map(row => row.split(''));
    let asteroidCount = 0;
    this.data = this.data.map((row, y) => row.map((elem, x) => {
      if (elem == '#') {
        asteroidCount += 1;
        return new Asteroid(x, y);
      } else {
        return elem;
      }
    }));
    this.asteroidCount = asteroidCount;
    this.height = this.data.length;
    this.width = this.data[0].length;
  }

  detectAsteroid(x, y) {
    if (x >= 0 && x < this.width && y >= 0 && y < this.height) {
      const elem = this.data[y][x];
      if (elem != '.') {
        this.asteroidsChecked += 1;
        if (elem.isDetectable(this.monitor, this.asteroidsDetected)) {
          this.asteroidsDetected.push(elem);
        }
      }
    }
  }

  countDetectableAsteroids(asteroid) {
    let ringSize = 1;
    this.monitor = asteroid
    this.asteroidsChecked = 0;
    this.asteroidsDetected = [];
    while (this.asteroidsChecked < this.asteroidCount - 1) {
      let x = asteroid.x - ringSize;
      let y = asteroid.y - ringSize;
      while (x <= asteroid.x + ringSize) {
        this.detectAsteroid(x, y);
        x += 1;
      }
      x -= 1;
      while (y <= asteroid.y + ringSize) {
        this.detectAsteroid(x, y);
        y += 1;
      }
      y -= 1;
      while (x >= asteroid.x - ringSize) {
        this.detectAsteroid(x, y);
        x -= 1;
      }
      x += 1;
      while (y > asteroid.y - ringSize) {
        this.detectAsteroid(x, y);
        y -= 1;
      }
      ringSize += 1
    }
    return this.asteroidsDetected.length;
  }

  buildDetectCountMap() {
    const countMap = [];
    this.data.forEach(row => {
      const countRow = [];
      row.forEach(elem => {
        if (elem != '.') {
          countRow.push(this.countDetectableAsteroids(elem));
        } else {
          countRow.push('.');
        }
      });
      countMap.push(countRow);
    });
    return countMap;
  }
}

const map = new AsteroidMap();
const detectMap = map.buildDetectCountMap();
const numberMap = detectMap.map(row => row.filter(elem => typeof(elem) == 'number'));
const maxNumber = Math.max(...numberMap.map(row => Math.max(...row)));
console.log(maxNumber);
