import { useEffect, useState } from "react";
import axios from "axios";

const ImageGallery = () => {
    const [images, setImages] = useState([]);

    useEffect(() => {
        axios.get("http://localhost:5000/images")
            .then(res => setImages(res.data))
            .catch(err => console.error("Error fetching images:", err));
    }, []);

    return (
        <div>
            <h1>Gallery</h1>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap: "10px" }}>
                {images.map((img, index) => (
                    <img key={index} src={img.url} alt="Processed" width="200" />
                ))}
            </div>
        </div>
    );
};

export default ImageGallery;
