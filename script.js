// Fonction pour gérer les clics sur les boutons et afficher une réponse
function selectService(service) {
    let message = '';

    // Logique de réponse selon le service choisi
    if (service === 'Meetup') {
        message = "Vous avez choisi l'option Meetup.";
    } else if (service === 'Potato') {
        message = "Vous avez choisi l'option Potato.";
    } else if (service === 'Delivery') {
        message = "Vous avez choisi l'option Delivery.";
    } else if (service === 'Linktree') {
        message = "Vous avez choisi Linktree.";
    }

    // Mettre à jour la réponse sur la page
    document.getElementById('response-message').textContent = message;
}
