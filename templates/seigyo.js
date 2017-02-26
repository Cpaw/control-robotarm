//初期化
webiopi().ready(
    function(){
	all_off(); //全モーター,LEDをOFFにする
	all_duty(80); //全モーター,LEDのduty比を初期化(引数はパーセンテージ)
    }
);

//モーター制御。2桁の数を1桁ずつに分けてマクロ関数に渡す
//2桁目:どのモーターか 1桁目:モーターのモード
function motor_mode(num){
    webiopi().callMacro("motorChangemode", [Math.floor(num/10), num%10]);
}

/*
//モーターのduty比変更。2桁の数を1桁ずつに分けてマクロ関数に渡す
//2桁目:どのモーターか 1桁目:PWMのduty比
function motor_duty(num){
    webiopi().callMacro("motorChangeduty",  [Math.floor(num/10), num%10])
}*/

//LEDの制御。電気つけるか消すか
function led_mode(mode){
    webiopi().callMacro("ledChangemode", mode);
}

/*
//LEDのduty比変更
function led_duty(level){
    webiopi().callMacro("ledChangeduty", level);
}*/

//全モーター,LEDをOFFにする
function all_off(){
    webiopi().callMacro("allOff");
}

//全モーター,LEDのduty比を変更
function all_duty(level){
    webiopi().callMacro("allChangeduty",level)
}
