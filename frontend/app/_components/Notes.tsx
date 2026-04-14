"use client";

import axios from "axios";
import { useEffect, useState } from "react";

function Notes() {
  const [notes, setNotes] = useState();

  useEffect(() => {
    const fetchNotes = async () => {
      try {
        const res = await axios.get("http://127.0.0.1:8000/api/notes/");
        console.log(res);
        setNotes(res.data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchNotes();
  }, []);
  return <div></div>;
}

export default Notes;
