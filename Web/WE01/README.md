# WE01 - 100pts

## Briefing

> View the page at <https://cfta-we01.allyourbases.co> and try to get the flag.

## Solution

1. Looking at the source code for the website shows that all we have to work with is this: `ロ='',コ=!ロ+ロ,Y=!コ+ロ,ㅣ=ロ+{},ᗐ=コ[ロ++],Ξ=コ[Δ=ロ],ᐳ=++Δ+ロ,ㅡ=ㅣ[Δ+ᐳ],ウ="+=*:.",コ[ㅡ+=ㅣ[ロ]+(コ.Y+ㅣ)[ロ]+Y[ᐳ]+ᗐ+Ξ+コ[Δ]+ㅡ+ᗐ+ㅣ[ロ]+Ξ][ㅡ](ㅣ[Δ+ᐳ]+ㅣ[ロ]+(コ.Y+ㅣ)[ロ]+Y[ᐳ]+ㅣ[ロ]+Y[Δ]+コ[ᐳ]+ウ[ᐳ+ロ]+Y[Δ]+ㅣ[ロ]+(([]+([]+[])[ㅡ])[ᐳ*(ᐳ+ロ)+Δ])+"(Y[Δ-Δ]+Y[Δ]+Y[ロ]+(([]+([]+[])[ㅡ])[ᐳ*(ᐳ+ロ)+Δ])+ウ[ᐳ]+ㅣ[(ᐳ+ロ)*ロ+ᐳ]+コ[Δ]+(コ.Y+ㅣ)[ロ]+(コ.Y+ㅣ)[ᐳ*Δ-ロ]+ㅡ[ロ-ロ]+ㅡ[ロ]+(コ.Y+ㅣ)[ᐳ-ロ]+コ[ᐳ]+ウ[ロ-ロ]+ㅣ[ロ]+ㅣ[Δ]+Y[Δ-Δ]+コ[Δ]+Y[ᐳ]+ㅡ[ᐳ-ᐳ]+Y[ロ]+ᗐ+(コ.Y+ㅣ)[ᐳ*Δ-ロ]+ㅣ[ロ]+(コ.Y+ㅣ)[ロ]+ウ[ロ]+ㅣ[ᐳ]+Y[ᐳ]+ウ[Δ]+Y[Δ-Δ]+コ[Δ]+(コ.Y+ㅣ)[ロ] )")()`

2. The brackets make it seem like a programming language. Searching the beginning new characters finds [aurebesh.js](http://aem1k.com/aurebesh.js/), which says this is executable JavaScript code.

3. Sure enough, running the snippet in the JS console gives the flag.

### Flag

`unicode+obfuscation=js*fun`
