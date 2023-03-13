<template>
<div class="keypad">
    <div class="keypad-row">
      <div class="keypad-key" @click="preventInput(index, $event, '1')">1</div>
      <div class="keypad-key" @click="inputKey(index, '2')">2</div>
      <div class="keypad-key" @click="inputKey(index, '3')">3</div>
    </div>
    <div class="keypad-row">
      <div class="keypad-key" @click="inputKey(index, '4')">4</div>
      <div class="keypad-key" @click="inputKey(index, '5')">5</div>
      <div class="keypad-key" @click="inputKey(index, '6')">6</div>
    </div>
    <div class="keypad-row">
      <div class="keypad-key" @click="inputKey(index, '7')">7</div>
      <div class="keypad-key" @click="inputKey(index, '8')">8</div>
      <div class="keypad-key" @click="inputKey(index, '9')">9</div>
    </div>
    <div class="keypad-row">
      <div class="keypad-empty"></div>
      <div class="keypad-key" @click="inputKey(index, '0')">0</div>
      <div class="keypad-key" @click="deleteDigit()">Backspace</div>
    </div>
</div>
</template>


<style scoped>

.keypad {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 24px;
}

.keypad-row {
  display: flex;
  justify-content: center;
}

.keypad-key {
  width: 80px;
  height: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid #ccc;
  margin: 5px;
  cursor: pointer;
}

.keypad-empty {
  width: 40px;
  height: 40px;
  margin: 5px;
}

</style>