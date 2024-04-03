/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

/**
 * Determines the cooking status based on the given time.
 *
 * @param {number} time - The time in minutes for cooking
 * @return {string} The cooking status message
 */
export function cookingStatus(time) {
  if (time == undefined) return "You forgot to set the timer.";
  return time > 0 ? "Not done, please wait." : "Lasagna is done.";
}

/**
 * Calculates the preparation time based on the number of layers and the time per layer.
 *
 * @param {Array<Number>} layers - the array of layers
 * @param {number} timePerLayer - the time taken per layer, defaults to 2 if not provided
 * @return {number} the total preparation time
 */
export function preparationTime(layers, timePerLayer) {
  return layers.length * (timePerLayer ?? 2);
}

/**
 * Calculates the quantities of noodles and sauce for a given number of layers.
 *
 * @param {Array<String>} layers - the array of layers
 * @return {Object} the quantities of noodles and sauce
 */
export function quantities(layers) {
  return {
    noodles: layers.filter((layer) => layer === "noodles").length * 50,
    sauce: layers.filter((layer) => layer === "sauce").length * 0.2,
  };
}

/**
 * Adds the last element from friendsList to myList.
 *
 * @param {Array} friendsList - The list of friend's ingredients.
 * @param {Array} myList - The list to which the secret ingredient will be added.
 * @return {undefined}
 */
export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length - 1]);
}

/**
 * Scales a recipe by the given factor.
 *
 * @param {Object} recipe - The original recipe to be scaled
 * @param {number} scaleFactor - The factor by which the recipe should be scaled
 * @return {Object} The scaled recipe
 */
export function scaleRecipe(recipe, scaleFactor) {
  return Object.fromEntries(
    Object.entries(recipe).map(([key, value]) => [
      key,
      (value / 2) * scaleFactor,
    ])
  );
}
