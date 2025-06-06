import React, { useState } from 'react';

interface Product {
  id: number;
  name: string;
  price: number;
  image: string;
  description: string;
}

const SAMPLE_PRODUCTS: Product[] = [
  {
    id: 1,
    name: 'Product 1',
    price: 1999,
    image: 'https://via.placeholder.com/200',
    description: 'Sample product description'
  },
  {
    id: 2,
    name: 'Product 2',
    price: 2999,
    image: 'https://via.placeholder.com/200',
    description: 'Sample product description'
  },
  // Add more sample products as needed
];

export default function Shop() {
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);

  return (
    <div className="grid grid-cols-2 gap-4">
      {SAMPLE_PRODUCTS.map((product) => (
        <div
          key={product.id}
          className="bg-gray-800 rounded-lg p-4 cursor-pointer"
          onClick={() => setSelectedProduct(product)}
        >
          <img
            src={product.image}
            alt={product.name}
            className="w-full h-32 object-cover rounded-lg mb-2"
          />
          <h3 className="text-lg font-semibold">{product.name}</h3>
          <p className="text-blue-400">{product.price} ₽</p>
        </div>
      ))}

      {/* Product Modal */}
      {selectedProduct && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4">
          <div className="bg-gray-800 rounded-lg p-6 max-w-lg w-full">
            <img
              src={selectedProduct.image}
              alt={selectedProduct.name}
              className="w-full h-48 object-cover rounded-lg mb-4"
            />
            <h2 className="text-xl font-bold mb-2">{selectedProduct.name}</h2>
            <p className="text-gray-300 mb-4">{selectedProduct.description}</p>
            <div className="flex justify-between items-center">
              <p className="text-blue-400 text-xl">{selectedProduct.price} ₽</p>
              <button
                className="bg-blue-500 text-white px-6 py-2 rounded-lg"
                onClick={() => {
                  // Add to cart logic here
                  setSelectedProduct(null);
                }}
              >
                В корзину
              </button>
            </div>
            <button
              className="mt-4 text-gray-400"
              onClick={() => setSelectedProduct(null)}
            >
              Закрыть
            </button>
          </div>
        </div>
      )}
    </div>
  );
} 