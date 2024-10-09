Java.perform(function () {
    var MainActivity = Java.use('com.example.apkrypt.MainActivity');
    MainActivity.decrypt.implementation = function (encryptedString) {
        var decrypted = this.decrypt(encryptedString);
        return decrypted;
    };
    var result = MainActivity.decrypt("k+RLD5J86JRYnluaZLF3Zs/yJrVdVfGo1CQy5k0+tCZDJZTozBWPn2lExQYDHH1l");
    console.log("Result: " + result);
});