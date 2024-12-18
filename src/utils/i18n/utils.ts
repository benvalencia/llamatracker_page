import { ui, defaultLang } from './ui';

export function getLangFromUrl(url: URL) {
  const [, lang] = url.pathname.split('/');
  if (lang in ui) return lang as keyof typeof ui;
  return defaultLang;
}

export function getIsInBase(url: URL) {
  const [, lang] = url.pathname.split('/');
  const isSupported = ['es', 'it', 'ca'].find((i) => lang === i)
  return isSupported ? url.pathname.split('/').length === 3 : url.pathname.split('/').length === 2 ;
}

export function useTranslations(lang: keyof typeof ui) {
  return function t(key: keyof typeof ui[typeof defaultLang]): string{
    const [section, element, translation] = (key as string).split('.');
    return ui[lang][section][element][translation] || ui[defaultLang][section][element][translation];
  }
}