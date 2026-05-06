## Promises (how, why, and what)  
    A promise is an object that represent the eventual completion, or failure, of an asynchronous operation and its resulting value.
    It can exists in 3 states:
        - pending: initial state
        - fulfilled: the operation was a success
        - rejected: the operation as failed
    It is used to avoid the callback hell and make asynchrone code more lisible.

## How to use the then, resolve, catch methods  
    maPromise
  .then(result => console.log(result))      // call if resolve()
  .catch(error => console.error(error))     // call if reject()
  .finally(() => console.log("Finish !"))   // Always called

## How to use every method of the Promise object  
    // Promise.resolve / Promise.reject — créer une promise déjà résolue/rejetée
    Promise.resolve(42).then(v => console.log(v)); // 42
    Promise.reject("oops").catch(e => console.log(e)); // "oops"

    // Promise.all — attend TOUTES les promises (échoue si l'une échoue)
    Promise.all([p1, p2, p3]).then(([r1, r2, r3]) => console.log(r1, r2, r3));

    // Promise.allSettled — attend toutes, sans échouer (donne le statut de chacune)
    Promise.allSettled([p1, p2]).then(results => {
    results.forEach(r => console.log(r.status, r.value ?? r.reason));
    });

    // Promise.race — retourne la PREMIÈRE promise qui se termine (résolue ou rejetée)
    Promise.race([p1, p2]).then(v => console.log("Gagnant :", v));

    // Promise.any — retourne la première promise RÉSOLUE (ignore les rejets)
    Promise.any([p1, p2]).then(v => console.log("Premier succès :", v));

## Throw / Try  
    function risqué() {
    throw new Error("Quelque chose a mal tourné !");
    }

    try {
    risqué();
    } catch (e) {
    console.error(e.message); // "Quelque chose a mal tourné !"
    } finally {
    console.log("Bloc finally toujours exécuté");
    }

## The await operator  
    async function fetchData() {
    try {
        const response = await fetch("https://api.exemple.com/data"); // attend la Promise
        const data = await response.json();
        console.log(data);
    } catch (e) {
        console.error("Erreur :", e.message);
    }
    }

    fetchData();

## How to use an async function  
    await ne peut s'utiliser que dans une fonction async
    Une fonction async retourne toujours une Promise
    await suspend l'exécution de la fonction jusqu'à la résolution de la Promise

    jsasync function exemple() {
    return 42; // équivalent à : return Promise.resolve(42)
    }

    exemple().then(v => console.log(v)); // 42
