$("input[name='content']").keyup(function (event) {
    if (event.keyCode === 13) {
        $("#myButton").click();
    }
});


function likePost(postId) {
    fetch(`/post/${postId}/like/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`likes-count-${postId}`).textContent = data.likes_count;
        document.getElementById(`dislikes-count-${postId}`).textContent = data.dislikes_count;
    });
}

function dislikePost(postId) {
    fetch(`/post/${postId}/dislike/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`likes-count-${postId}`).textContent = data.likes_count;
        document.getElementById(`dislikes-count-${postId}`).textContent = data.dislikes_count;
    });
}

function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}