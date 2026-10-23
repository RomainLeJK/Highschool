function afficher_resultat() {
    let tableau_etapes = document.getElementById("tableau_etapes"); 
    let temp_tableau_etapes = document.getElementById("temp_tableau_etapes");

    tableau_etapes.style.opacity = 0; // Rendre le texte transparent avant le changement
    tableau_etapes.innerText = temp_tableau_etapes.innerText; // Changer le texte immédiatement
    tableau_etapes.style.transition = "opacity 3.5s"; // Régler la durée de l'animation
    tableau_etapes.style.opacity = 1; // Faire réapparaître progressivement
   
}