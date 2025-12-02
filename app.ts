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
