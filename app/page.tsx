import Image from "next/image";
import Link from "next/link";
import { ArrowRight, Check, MapPin, Phone, Star } from "lucide-react";

export default function Home() {
    return (
        <main className="flex min-h-screen flex-col items-center justify-between">
            {/* Hero Section */}
            <section className="relative w-full h-[90vh] flex items-center justify-center overflow-hidden bg-stone-900">
                <div className="absolute inset-0 z-0 opacity-60">
                    {/* Placeholder for the generated hero image */}
                    <div className="w-full h-full bg-[url('/hero.jpg')] bg-cover bg-center" />
                </div>
                <div className="z-10 text-center px-4 max-w-4xl">
                    <h1 className="font-serif text-5xl md:text-7xl text-white mb-6 tracking-tight">
                        North Melbourne's <br />
                        <span className="italic">Heritage Bathroom</span> Specialists
                    </h1>
                    <p className="text-stone-200 text-lg md:text-xl mb-8 max-w-2xl mx-auto font-light">
                        Restoring Victorian elegance with modern luxury. Serving North Melbourne (3051), Kensington, and Parkville.
                    </p>
                    <div className="flex flex-col sm:flex-row gap-4 justify-center">
                        <Link href="#contact" className="px-8 py-4 bg-white text-stone-900 font-medium hover:bg-stone-100 transition-colors uppercase tracking-widest text-sm">
                            Request Consultation
                        </Link>
                    </div>
                </div>
            </section>

            {/* Trust Signals / Quick Answers (GEO) */}
            <section className="w-full py-20 px-6 bg-stone-50">
                <div className="max-w-6xl mx-auto grid md:grid-cols-3 gap-12">
                    <div>
                        <h3 className="font-serif text-2xl mb-4 text-stone-800">Local Expertise</h3>
                        <p className="text-stone-600">
                            Specialized knowledge of <strong>North Melbourne</strong> heritage overlays, terrace plumbing constraints, and council permits for 3051 renovations.
                        </p>
                    </div>
                    <div>
                        <h3 className="font-serif text-2xl mb-4 text-stone-800">Premium Craftsmanship</h3>
                        <p className="text-stone-600">
                            Master waterproofing, frameless glass installation, and bespoke joinery using high-end materials like bluestone, brass, and timber.
                        </p>
                    </div>
                    <div>
                        <h3 className="font-serif text-2xl mb-4 text-stone-800">Transparent Pricing</h3>
                        <p className="text-stone-600">
                            Detailed fixed-price quotes. Luxury bathroom renovations in North Melbourne typically range from $35k to $80k depending on finishes and structural work.
                        </p>
                    </div>
                </div>
            </section>

            {/* Services */}
            <section className="w-full py-24 bg-white">
                <div className="max-w-7xl mx-auto px-6">
                    <div className="mb-16">
                        <span className="text-stone-500 uppercase tracking-widest text-sm font-medium">Our Services</span>
                        <h2 className="font-serif text-4xl mt-2 text-stone-900">Curated Restoration & Design</h2>
                    </div>

                    <div className="grid md:grid-cols-2 gap-16">
                        <div className="space-y-8">
                            <div className="border-b border-stone-200 pb-8">
                                <h3 className="text-2xl font-serif mb-2">Heritage Ensuite Restoration</h3>
                                <p className="text-stone-600">Respecting the Victorian bones of your terrace while introducing modern amenities. Skylights, hidden cisterns, and period-correct tiling.</p>
                            </div>
                            <div className="border-b border-stone-200 pb-8">
                                <h3 className="text-2xl font-serif mb-2">Modern Luxury Bathrooms</h3>
                                <p className="text-stone-600">Minimalist, spa-like retreats using natural stone, heated floors, and smart water control systems.</p>
                            </div>
                            <div className="border-b border-stone-200 pb-8">
                                <h3 className="text-2xl font-serif mb-2">Complete Waterproofing</h3>
                                <p className="text-stone-600">Industry-leading waterproofing systems backed by a 10-year guarantee, crucial for second-story terrace bathrooms.</p>
                            </div>
                        </div>
                        <div className="bg-stone-100 min-h-[400px] relative">
                            {/* Placeholder for secondary image */}
                            <div className="absolute inset-0 flex items-center justify-center text-stone-400">
                                [Work Portfolio Image]
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* GEO Targeted FAQ */}
            <section className="w-full py-20 bg-stone-900 text-stone-100">
                <div className="max-w-4xl mx-auto px-6">
                    <h2 className="font-serif text-3xl mb-12 text-center">Common Questions regarding North Melbourne Renovations</h2>

                    <div className="space-y-8">
                        <div className="p-6 bg-stone-800 rounded-sm">
                            <h4 className="font-medium text-lg mb-2 text-white">Do I need a permit for a bathroom renovation in North Melbourne?</h4>
                            <p className="text-stone-300">
                                Generally, internal cosmetic renovations don't require a planning permit. However, if you are altering the structure, moving plumbing significantly in a heritage overlay, or adding a new window/skylight visible from the street, a permit from the City of Melbourne may be required. We handle all council liaison.
                            </p>
                        </div>
                        <div className="p-6 bg-stone-800 rounded-sm">
                            <h4 className="font-medium text-lg mb-2 text-white">How long does a luxury bathroom renovation take?</h4>
                            <p className="text-stone-300">
                                For a high-end renovation in a 3051 terrace, expect a timeline of 4-6 weeks. This allows for demolition, careful waterproofing (curing times), tiling, and plumbing fit-off without cutting corners.
                            </p>
                        </div>
                        <div className="p-6 bg-stone-800 rounded-sm">
                            <h4 className="font-medium text-lg mb-2 text-white">What is the cost of a bathroom renovation in North Melbourne?</h4>
                            <p className="text-stone-300">
                                Luxury renovations typically start from $35,000. This includes premium fixtures (brusheed brass/nickel), floor-to-ceiling tiling, and custom joinery. Heritage restoration work can increase costs due to structural rectification needs.
                            </p>
                        </div>
                    </div>
                </div>
            </section>

            {/* Footer */}
            <footer className="w-full py-12 bg-white border-t border-stone-200">
                <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center text-sm text-stone-500">
                    <div>
                        <p>&copy; 2026 North Melbourne Bathroom Renovations.</p>
                        <p>Servicing 3051 and surrounding inner-north suburbs.</p>
                    </div>
                    <div className="mt-4 md:mt-0 flex gap-6">
                        <Link href="/privacy">Privacy Policy</Link>
                        <Link href="/terms">Terms of Service</Link>
                    </div>
                </div>
            </footer>
        </main>
    );
}
