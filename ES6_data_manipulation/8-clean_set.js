export default function cleanSet(set, stratString) {
    if (!stratString) {
        return '';
    }
    let myString = "";

    for(const item of set) {
        if (item.startsWith(stratString)) {
            if (myString !== '') {
                myString += '-';
            }
            myString += item.slice(stratString.length);
        }
    }

    return myString;
};
