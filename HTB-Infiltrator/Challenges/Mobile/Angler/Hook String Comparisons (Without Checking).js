Interceptor.attach(Module.findExportByName(null, 'strcmp'), {
    onEnter: function (args) {
        this.str1 = Memory.readUtf8String(args[0]);
        this.str2 = Memory.readUtf8String(args[1]);
        console.log("strcmp called with arguments: '" + this.str1 + "' and '" + this.str2 + "'");
    }
});