module.exports = {
    register: function(koRef) {
        koRef.bindingHandlers.truncatedText = {
            update: function(element, valueAccessor, allBindingsAccessor) {
                var originalText = koRef.utils.unwrapObservable(valueAccessor());
                var length = koRef.utils.unwrapObservable(allBindingsAccessor().maxTextLength);
                var truncatedText = originalText.length > length ? originalText.substring(0, length) + "..." : originalText;

                koRef.bindingHandlers.text.update(element, function() {
                    return truncatedText;
                });
            }
        };
    }
};