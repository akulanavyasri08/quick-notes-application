// Save note
async function saveNote() {

    const noteInput = document.getElementById("noteInput");
    const noteText = noteInput.value;

    if (noteText.trim() === "") {
        alert("Please write a note");
        return;
    }

    await fetch('/add_note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ note: noteText })
    });

    noteInput.value = "";

    loadNotes();
}

// Load notes
async function loadNotes() {

    const response = await fetch('/get_notes');
    const notes = await response.json();

    const notesContainer = document.getElementById("notesContainer");

    notesContainer.innerHTML = "";

    notes.forEach(note => {

        const div = document.createElement("div");

        div.className = "note";

        div.innerHTML = note.content;

        notesContainer.appendChild(div);
    });
}

loadNotes();