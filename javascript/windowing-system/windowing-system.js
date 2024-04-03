// @ts-check

/**
 * Implement the classes etc. that are needed to solve the
 * exercise in this file. Do not forget to export the entities
 * you defined so they are available for the tests.
 */

export class Size {
  /**
   * Constructor for creating a new instance of the Size class.
   *
   * @param {number} width - the width of the instance
   * @param {number} height - the height of the instance
   */
  constructor(width = 80, height = 60) {
    this.width = width;
    this.height = height;
  }

  set width(value) {
    this._width = value < 1 ? 1 : value;
  }

  get width() {
    return this._width;
  }

  set height(value) {
    this._height = value < 1 ? 1 : value;
  }

  get height() {
    return this._height;
  }

  /**
   * resize the width and height of the object
   *
   * @param {number} width - the new width
   * @param {number} height - the new height
   */
  resize(width, height) {
    this.width = width;
    this.height = height;
  }
}

export class Position {
  /**
   * Constructor for creating a new instance of the Position class.
   *
   * @param {number} x - the x coordinate
   * @param {number} y - the y coordinate
   */
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
  }
  set x(value) {
    this._x = value < 0 ? 0 : value;
  }

  get x() {
    return this._x;
  }

  set y(value) {
    this._y = value < 0 ? 0 : value;
  }

  get y() {
    return this._y;
  }

  /**
   * Set the x and y coordinates of the object.
   *
   * @param {number} x - the x coordinate
   * @param {number} y - the y coordinate
   */
  move(x, y) {
    this.x = x;
    this.y = y;
  }
}

export class ProgramWindow {
  /**
   * Constructor for setting up the initial screen size, size, and position of the Program Window class.
   */
  constructor() {
    this.screenSize = new Size(800, 600);
    this.size = new Size();
    this.position = new Position();
  }
  /**
   * Set the size of the object.
   *
   * @param {Size} size - the new size to set
   */
  resize(size) {
    const maxWidth = this.screenSize.width - this.position.x;
    const maxHeight = this.screenSize.height - this.position.y;
    this.size.height = size.height > maxHeight ? maxHeight : size.height;
    this.size.width = size.width > maxWidth ? maxWidth : size.width;
  }

  /**
   * Setter for updating the position.
   *
   * @param {Position} position - the new position to set
   */
  move(position) {
    const maxX = this.screenSize.width - this.size.width;
    const maxY = this.screenSize.height - this.size.height;
    this.position.x = position.x > maxX ? maxX : position.x;
    this.position.y = position.y > maxY ? maxY : position.y;
  }
}

/**
 * Change the window.
 *
 * @param {ProgramWindow} window - the window to be changed
 * @return {ProgramWindow} the updated window
 */
export function changeWindow(window) {
  window.size = new Size(400, 300);
  window.position = new Position(100, 150);
  return window;
}
