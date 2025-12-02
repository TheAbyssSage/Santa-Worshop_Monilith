// src/types.ts
export type Product = {
  id: string;
  name: string;
  price: number;
  stock: number;
  category: 'transport' | 'clothing' | 'food' | 'tech' | 'crafts';
  description: string;
};

// src/api.ts
const BASE_URL = 'http://localhost:3000';

export async function fetchProducts(params: { q?: string; category?: string }) {
  const url = new URL(`${BASE_URL}/products`);
  if (params.q && params.q.trim()) url.searchParams.set('q', params.q.trim());
  if (params.category && params.category !== 'all') url.searchParams.set('category', params.category);
  const res = await fetch(url);
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return (await res.json()) as unknown[];
}
