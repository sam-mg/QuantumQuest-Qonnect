Java.perform(function () {
    var MainActivity = Java.use('com.example.angler.MainActivity');
    MainActivity.getInfo.implementation = function (str) {
        var result = this.getInfo(str);
        console.log("getInfo result: " + result);
        return result;
    };
});