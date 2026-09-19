# Install your GitHub profile

## 1. Create or open the special repository
Your username, taken from your resume links, is PRATIK0SHARMA.

Your profile README belongs in a PUBLIC repository called exactly:
PRATIK0SHARMA

Its address should be:
https://github.com/PRATIK0SHARMA/PRATIK0SHARMA

If it already exists, back up its README and assets before replacing them. This package has not modified your account. The live profile could not be fetched during preparation, so no assumptions were made about existing profile content.

This is different from pratik0sharma.github.io, which is a portfolio hosting repository.

## 2. Upload the files
1. Extract the ZIP on your laptop.
2. Create the repository above (Public), or open the existing one.
3. Choose Add file > Upload files.
4. Upload README.md and the complete assets folder together. Keep assets as a folder; do not flatten it.
5. Commit the changes.
6. Open https://github.com/PRATIK0SHARMA to see the result.

README.md must be at the root of the repository, not inside another folder. You do not need to upload SETUP.md or build_assets.py, although retaining the generator is useful if you want to update images later.

Official instructions:
https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme

## 3. Update your sidebar
Suggested bio:
CSE '28 | Python, AI agents & backend development | Building practical systems with guardrails and verification | Open to internships

Set the website field only when your portfolio is publicly accessible. Your current Sites portfolio is private, so its URL is deliberately omitted from this README. When your custom domain or public GitHub Pages address is live, add it to the top link row too.

## 4. Pin your best repositories
Use Customize your pins on your profile. Prioritise:
1. RESOLVE_AI
2. MORTAL-FI
3. The actual FastAPI Blogs repository
4. The actual AGRI AI repository
5. Your portfolio source repository once it exists

Only pin repositories that actually exist and show work you are ready to discuss. The exact Blogs and AGRI repository URLs were not provided, so the README links to your repository list instead of inventing URLs.

For project repository descriptions:
RESOLVE_AI: Customer resolution AI agent with policy guardrails, duplicate-action prevention, recovery and independent verification. Simulated transactions.
MORTAL-FI: Financial reconciliation prototype with exception detection, guarded resolution and an audit trail on synthetic transaction data.

## 5. Included visuals and interactions
- assets/banner.gif: custom rotating geometric network and personal banner. It loops automatically in supported image viewers; visitors' reduced-motion/browser preferences can affect playback.
- assets/banner.png: static alternative. Change the README image source from banner.gif to banner.png if you prefer no motion.
- assets/resolve.png and assets/mortal-fi.png: matching project headers.
- Skill strips: local PNG images, not a third-party badge service.
- Project headers link to repositories; demo and contact links are clickable.
- Details/summary sections expand to reveal extra information.

GitHub READMEs cannot run your website's JavaScript or Canvas. The banner is an animated image, not a live 3D scene. The contribution calendar is GitHub's own data and is not modified or fabricated here. No fake counters, invented streaks, tokens, API keys or scheduled workflows are included.

## 6. Maintenance
Update achievements and metrics when your resume changes. Metrics inside banner/project graphics must be regenerated as well as editing README text. Project figures currently match the resume you supplied. Courses are described as coursework, not unverified certifications.

build_assets.py recreates the assets using Python and Pillow:
python -m pip install pillow
python build_assets.py

The script uses Linux DejaVu font paths by default. On Windows change the font, bold and mono paths near its start to installed fonts, for example C:/Windows/Fonts/arial.ttf, arialbd.ttf and consola.ttf. Different fonts will alter the appearance; you do not need to run this script to use the included assets.

Asset verification: images were generated locally; the static banner and project card were visually inspected, GIF frame count and every local README image path were checked. GitHub's actual final layout can vary by screen width and theme; a live GitHub-rendered preview was not available in this environment.
