import en from './en/global.json'; // This import style requires "esModuleInterop", see "side notes"
import es from './es/global.json'; // This import style requires "esModuleInterop", see "side notes"
import ca from './ca/global.json'; // This import style requires "esModuleInterop", see "side notes"
import it from './it/global.json'; // This import style requires "esModuleInterop", see "side notes"

export const languages = {
  en: 'English',
  es: 'Español',
  it: 'Italiano',
  ca: 'Catalan',
};

export const defaultLang = 'en';

export const ui = {
  en: en,
  es: es,
  it: it,
  ca: ca,
} as any;