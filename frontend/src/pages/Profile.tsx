interface Order {
  id: number;
  products: string[];
  status: 'pending' | 'processing' | 'shipped' | 'delivered';
  total: number;
  date: string;
}

const SAMPLE_ORDERS: Order[] = [
  {
    id: 1,
    products: ['Product 1', 'Product 2'],
    status: 'processing',
    total: 4998,
    date: '2024-02-15'
  },
  {
    id: 2,
    products: ['Product 3'],
    status: 'delivered',
    total: 1999,
    date: '2024-02-10'
  }
];

export default function Profile() {
  return (
    <div className="space-y-6">
      {/* User Info */}
      <div className="bg-gray-800 rounded-lg p-6">
        <div className="flex items-center space-x-4">
          <img
            src="https://via.placeholder.com/80"
            alt="User Avatar"
            className="w-20 h-20 rounded-full"
          />
          <div>
            <h2 className="text-2xl font-bold">@username</h2>
            <p className="text-gray-400">Joined February 2024</p>
          </div>
        </div>
      </div>

      {/* Orders */}
      <div className="space-y-4">
        <h3 className="text-xl font-semibold">Orders</h3>
        {SAMPLE_ORDERS.map((order) => (
          <div key={order.id} className="bg-gray-800 rounded-lg p-4">
            <div className="flex justify-between items-start">
              <div>
                <p className="text-sm text-gray-400">Order #{order.id}</p>
                <p className="mt-1">{order.products.join(', ')}</p>
                <p className="text-sm text-gray-400 mt-2">{order.date}</p>
              </div>
              <div className="text-right">
                <span className={`
                  px-2 py-1 rounded text-sm
                  ${order.status === 'delivered' ? 'bg-green-500' : 'bg-blue-500'}
                `}>
                  {order.status}
                </span>
                <p className="mt-2 text-blue-400">{order.total} ₽</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
} 