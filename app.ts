// types
export type Product = {
    id: string;
    name: string;
    price: number;
    stock: number;
    category: 'transport' | 'clothing' | 'food' | 'tech' | 'crafts';
    description: string;
};

// api
const BASE_URL = 'http://localhost:3000';

export async function fetchProducts(params: { q?: string; category?: string }) {
  const url = new URL(`${BASE_URL}/products`);
  if (params.q && params.q.trim()) url.searchParams.set('q', params.q.trim());
  if (params.category && params.category !== 'all') url.searchParams.set('category', params.category);

  const res = await fetch(url.toString(), {
    headers: { 'Accept': 'application/json' },
  });
  if (!res.ok) throw new Error(`API error: ${res.status} ${res.statusText}`);
  return (await res.json()) as unknown[];
}




// src/hooks/useProducts.ts
import { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { fetchProducts } from '../api';
import type { Product } from '../types';

const RATINGS = ['😇 Nice', '😈 Naughty', '🌟 Super Nice'] as const;

export function useProducts() {
  const [params] = useSearchParams();
  const q = params.get('q') ?? '';
  const category = params.get('category') ?? 'all';

  const [data, setData] = useState<(Product & { rating?: string })[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);

    fetchProducts({ q, category })
      .then((raw) => {
        const products = raw as Product[];
        const withRatings = products.map((p) => ({
          ...p,
          rating: RATINGS[Math.floor(Math.random() * RATINGS.length)],
        }));
        if (!cancelled) setData(withRatings);
      })
      .catch((e) => {
        if (!cancelled) setError(e?.message ?? 'Unknown error');
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });

    return () => {
      cancelled = true;
    };
  }, [q, category]);

  return { data, loading, error, q, category };
}



// src/components/Controls.tsx
import { useSearchParams } from 'react-router-dom';

const categories = ['all', 'transport', 'clothing', 'food', 'tech', 'crafts'] as const;

export function Controls() {
  const [params, setParams] = useSearchParams();
  const q = params.get('q') ?? '';
  const category = params.get('category') ?? 'all';

  function updateParam(key: string, value: string) {
    const next = new URLSearchParams(params);
    if (value) next.set(key, value);
    else next.delete(key);
    setParams(next);
  }

  return (
    <div className="controls">
      <label>🔍 Search:</label>
      <input
        type="text"
        value={q}
        placeholder="Search toys..."
        onChange={(e) => updateParam('q', e.target.value)}
      />

      <label>📂 Category:</label>
      <select
        value={category}
        onChange={(e) => updateParam('category', e.target.value)}
      >
        {categories.map((c) => (
          <option key={c} value={c}>
            {c === 'all' ? 'All Categories' : c[0].toUpperCase() + c.slice(1)}
          </option>
        ))}
      </select>
    </div>
  );
}

// src/components/ProductCard.tsx
import type { Product } from '../types';

type Props = Product & { rating?: string };

export function ProductCard({ name, description, price, stock, category, rating }: Props) {
  return (
    <div className="card">
      <div className="card-header">
        <span className="category-tag">{category}</span>
        <span className="stock-tag">📦 {stock} left</span>
      </div>
      <h2>{name}</h2>
      <p className="description">{description}</p>
      <div className="price-row">
        <span className="price">${price}</span>
        {rating && <span className="rating">{rating}</span>}
      </div>
      <button className="buy-btn">Add to Sleigh 🛷</button>
    </div>
  );
}
