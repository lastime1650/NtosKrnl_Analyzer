# KiDoesHeteroSoftParkElectionHaveWinner

- RVA: `0x0039E7A0`–`0x0039ECC3` (길이 `1,315` bytes)
- VA: `0x000000014039E7A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00081BE8`
- 디코드: `307`개 명령, `1,315/1,315` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiPerformHeteroSoftParkElection](KiPerformHeteroSoftParkElection_function_0039E490.md) at `0x0039E554`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0039E7A0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0039E7A5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0039E7AA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0039E7AF  49 8B F8                        mov rdi, r8
0039E7B2  48 8B F1                        mov rsi, rcx
0039E7B5  33 DB                           xor ebx, ebx
0039E7B7  B8 02 00 00 00                  mov eax, 2
0039E7BC  0F 1F 40 00                     nop dword ptr [rax]
0039E7C0  44 8D 58 FE                     lea r11d, [rax - 2]
0039E7C4  45 8B D3                        mov r10d, r11d
0039E7C7  4C 0F A3 D2                     bt rdx, r10
0039E7CB  0F 82 33 02 00 00               jb 0x14039ea04
0039E7D1  44 8D 40 FF                     lea r8d, [rax - 1]
0039E7D5  41 8B C8                        mov ecx, r8d
0039E7D8  48 0F A3 CA                     bt rdx, rcx
0039E7DC  0F 82 38 02 00 00               jb 0x14039ea1a
0039E7E2  8B C8                           mov ecx, eax
0039E7E4  48 0F A3 CA                     bt rdx, rcx
0039E7E8  0F 82 42 02 00 00               jb 0x14039ea30
0039E7EE  44 8D 40 01                     lea r8d, [rax + 1]
0039E7F2  41 8B C8                        mov ecx, r8d
0039E7F5  48 0F A3 CA                     bt rdx, rcx
0039E7F9  0F 82 46 02 00 00               jb 0x14039ea45
0039E7FF  44 8D 40 02                     lea r8d, [rax + 2]
0039E803  41 8B C8                        mov ecx, r8d
0039E806  48 0F A3 CA                     bt rdx, rcx
0039E80A  0F 82 4B 02 00 00               jb 0x14039ea5b
0039E810  44 8D 40 03                     lea r8d, [rax + 3]
0039E814  41 8B C8                        mov ecx, r8d
0039E817  48 0F A3 CA                     bt rdx, rcx
0039E81B  0F 82 50 02 00 00               jb 0x14039ea71
0039E821  44 8D 40 04                     lea r8d, [rax + 4]
0039E825  41 8B C8                        mov ecx, r8d
0039E828  48 0F A3 CA                     bt rdx, rcx
0039E82C  0F 82 55 02 00 00               jb 0x14039ea87
0039E832  44 8D 40 05                     lea r8d, [rax + 5]
0039E836  41 8B C8                        mov ecx, r8d
0039E839  48 0F A3 CA                     bt rdx, rcx
0039E83D  0F 82 5A 02 00 00               jb 0x14039ea9d
0039E843  44 8D 40 06                     lea r8d, [rax + 6]
0039E847  41 8B C8                        mov ecx, r8d
0039E84A  48 0F A3 CA                     bt rdx, rcx
0039E84E  0F 82 5F 02 00 00               jb 0x14039eab3
0039E854  44 8D 40 07                     lea r8d, [rax + 7]
0039E858  41 8B C8                        mov ecx, r8d
0039E85B  48 0F A3 CA                     bt rdx, rcx
0039E85F  0F 82 64 02 00 00               jb 0x14039eac9
0039E865  44 8D 40 08                     lea r8d, [rax + 8]
0039E869  41 8B C8                        mov ecx, r8d
0039E86C  48 0F A3 CA                     bt rdx, rcx
0039E870  0F 82 69 02 00 00               jb 0x14039eadf
0039E876  44 8D 40 09                     lea r8d, [rax + 9]
0039E87A  41 8B C8                        mov ecx, r8d
0039E87D  48 0F A3 CA                     bt rdx, rcx
0039E881  0F 82 6E 02 00 00               jb 0x14039eaf5
0039E887  44 8D 40 0A                     lea r8d, [rax + 0xa]
0039E88B  41 8B C8                        mov ecx, r8d
0039E88E  48 0F A3 CA                     bt rdx, rcx
0039E892  0F 82 73 02 00 00               jb 0x14039eb0b
0039E898  44 8D 40 0B                     lea r8d, [rax + 0xb]
0039E89C  41 8B C8                        mov ecx, r8d
0039E89F  48 0F A3 CA                     bt rdx, rcx
0039E8A3  0F 82 78 02 00 00               jb 0x14039eb21
0039E8A9  44 8D 40 0C                     lea r8d, [rax + 0xc]
0039E8AD  41 8B C8                        mov ecx, r8d
0039E8B0  48 0F A3 CA                     bt rdx, rcx
0039E8B4  0F 82 7D 02 00 00               jb 0x14039eb37
0039E8BA  44 8D 40 0D                     lea r8d, [rax + 0xd]
0039E8BE  41 8B C8                        mov ecx, r8d
0039E8C1  48 0F A3 CA                     bt rdx, rcx
0039E8C5  0F 82 82 02 00 00               jb 0x14039eb4d
0039E8CB  44 8D 40 0E                     lea r8d, [rax + 0xe]
0039E8CF  41 8B C8                        mov ecx, r8d
0039E8D2  48 0F A3 CA                     bt rdx, rcx
0039E8D6  0F 82 87 02 00 00               jb 0x14039eb63
0039E8DC  44 8D 40 0F                     lea r8d, [rax + 0xf]
0039E8E0  41 8B C8                        mov ecx, r8d
0039E8E3  48 0F A3 CA                     bt rdx, rcx
0039E8E7  0F 82 8C 02 00 00               jb 0x14039eb79
0039E8ED  44 8D 40 10                     lea r8d, [rax + 0x10]
0039E8F1  41 8B C8                        mov ecx, r8d
0039E8F4  48 0F A3 CA                     bt rdx, rcx
0039E8F8  0F 82 91 02 00 00               jb 0x14039eb8f
0039E8FE  44 8D 40 11                     lea r8d, [rax + 0x11]
0039E902  41 8B C8                        mov ecx, r8d
0039E905  48 0F A3 CA                     bt rdx, rcx
0039E909  0F 82 96 02 00 00               jb 0x14039eba5
0039E90F  44 8D 40 12                     lea r8d, [rax + 0x12]
0039E913  41 8B C8                        mov ecx, r8d
0039E916  48 0F A3 CA                     bt rdx, rcx
0039E91A  0F 82 9B 02 00 00               jb 0x14039ebbb
0039E920  44 8D 40 13                     lea r8d, [rax + 0x13]
0039E924  41 8B C8                        mov ecx, r8d
0039E927  48 0F A3 CA                     bt rdx, rcx
0039E92B  0F 82 A0 02 00 00               jb 0x14039ebd1
0039E931  44 8D 40 14                     lea r8d, [rax + 0x14]
0039E935  41 8B C8                        mov ecx, r8d
0039E938  48 0F A3 CA                     bt rdx, rcx
0039E93C  0F 82 A5 02 00 00               jb 0x14039ebe7
0039E942  44 8D 40 15                     lea r8d, [rax + 0x15]
0039E946  41 8B C8                        mov ecx, r8d
0039E949  48 0F A3 CA                     bt rdx, rcx
0039E94D  0F 82 AA 02 00 00               jb 0x14039ebfd
0039E953  44 8D 40 16                     lea r8d, [rax + 0x16]
0039E957  41 8B C8                        mov ecx, r8d
0039E95A  48 0F A3 CA                     bt rdx, rcx
0039E95E  0F 82 AF 02 00 00               jb 0x14039ec13
0039E964  44 8D 40 17                     lea r8d, [rax + 0x17]
0039E968  41 8B C8                        mov ecx, r8d
0039E96B  48 0F A3 CA                     bt rdx, rcx
0039E96F  0F 82 B4 02 00 00               jb 0x14039ec29
0039E975  44 8D 40 18                     lea r8d, [rax + 0x18]
0039E979  41 8B C8                        mov ecx, r8d
0039E97C  48 0F A3 CA                     bt rdx, rcx
0039E980  0F 82 B9 02 00 00               jb 0x14039ec3f
0039E986  44 8D 40 19                     lea r8d, [rax + 0x19]
0039E98A  41 8B C8                        mov ecx, r8d
0039E98D  48 0F A3 CA                     bt rdx, rcx
0039E991  0F 82 BE 02 00 00               jb 0x14039ec55
0039E997  44 8D 40 1A                     lea r8d, [rax + 0x1a]
0039E99B  41 8B C8                        mov ecx, r8d
0039E99E  48 0F A3 CA                     bt rdx, rcx
0039E9A2  0F 82 C3 02 00 00               jb 0x14039ec6b
0039E9A8  44 8D 40 1B                     lea r8d, [rax + 0x1b]
0039E9AC  41 8B C8                        mov ecx, r8d
0039E9AF  48 0F A3 CA                     bt rdx, rcx
0039E9B3  0F 82 C8 02 00 00               jb 0x14039ec81
0039E9B9  44 8D 40 1C                     lea r8d, [rax + 0x1c]
0039E9BD  41 8B C8                        mov ecx, r8d
0039E9C0  48 0F A3 CA                     bt rdx, rcx
0039E9C4  0F 82 CD 02 00 00               jb 0x14039ec97
0039E9CA  44 8D 40 1D                     lea r8d, [rax + 0x1d]
0039E9CE  41 8B C8                        mov ecx, r8d
0039E9D1  48 0F A3 CA                     bt rdx, rcx
0039E9D5  0F 82 D2 02 00 00               jb 0x14039ecad
0039E9DB  83 C0 20                        add eax, 0x20
0039E9DE  8D 48 FE                        lea ecx, [rax - 2]
0039E9E1  83 F9 40                        cmp ecx, 0x40
0039E9E4  0F 82 D6 FD FF FF               jb 0x14039e7c0
0039E9EA  48 8B 74 24 10                  mov rsi, qword ptr [rsp + 0x10]
0039E9EF  48 85 DB                        test rbx, rbx
0039E9F2  48 8B 7C 24 18                  mov rdi, qword ptr [rsp + 0x18]
0039E9F7  49 89 19                        mov qword ptr [r9], rbx
0039E9FA  0F 95 C0                        setne al
0039E9FD  48 8B 5C 24 08                  mov rbx, qword ptr [rsp + 8]
0039EA02  C3                              ret
0039EA03  CC                              int3
0039EA04  45 8B C3                        mov r8d, r11d
0039EA07  4A 39 34 DF                     cmp qword ptr [rdi + r11*8], rsi
0039EA0B  0F 85 C0 FD FF FF               jne 0x14039e7d1
0039EA11  4C 0F AB C3                     bts rbx, r8
0039EA15  E9 B7 FD FF FF                  jmp 0x14039e7d1
0039EA1A  41 8B C8                        mov ecx, r8d
0039EA1D  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EA21  0F 85 BB FD FF FF               jne 0x14039e7e2
0039EA27  48 0F AB CB                     bts rbx, rcx
0039EA2B  E9 B2 FD FF FF                  jmp 0x14039e7e2
0039EA30  8B C8                           mov ecx, eax
0039EA32  48 39 34 CF                     cmp qword ptr [rdi + rcx*8], rsi
0039EA36  0F 85 B2 FD FF FF               jne 0x14039e7ee
0039EA3C  48 0F AB CB                     bts rbx, rcx
0039EA40  E9 A9 FD FF FF                  jmp 0x14039e7ee
0039EA45  41 8B C8                        mov ecx, r8d
0039EA48  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EA4C  0F 85 AD FD FF FF               jne 0x14039e7ff
0039EA52  48 0F AB CB                     bts rbx, rcx
0039EA56  E9 A4 FD FF FF                  jmp 0x14039e7ff
0039EA5B  41 8B C8                        mov ecx, r8d
0039EA5E  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EA62  0F 85 A8 FD FF FF               jne 0x14039e810
0039EA68  48 0F AB CB                     bts rbx, rcx
0039EA6C  E9 9F FD FF FF                  jmp 0x14039e810
0039EA71  41 8B C8                        mov ecx, r8d
0039EA74  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EA78  0F 85 A3 FD FF FF               jne 0x14039e821
0039EA7E  48 0F AB CB                     bts rbx, rcx
0039EA82  E9 9A FD FF FF                  jmp 0x14039e821
0039EA87  41 8B C8                        mov ecx, r8d
0039EA8A  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EA8E  0F 85 9E FD FF FF               jne 0x14039e832
0039EA94  48 0F AB CB                     bts rbx, rcx
0039EA98  E9 95 FD FF FF                  jmp 0x14039e832
0039EA9D  41 8B C8                        mov ecx, r8d
0039EAA0  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EAA4  0F 85 99 FD FF FF               jne 0x14039e843
0039EAAA  48 0F AB CB                     bts rbx, rcx
0039EAAE  E9 90 FD FF FF                  jmp 0x14039e843
0039EAB3  41 8B C8                        mov ecx, r8d
0039EAB6  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EABA  0F 85 94 FD FF FF               jne 0x14039e854
0039EAC0  48 0F AB CB                     bts rbx, rcx
0039EAC4  E9 8B FD FF FF                  jmp 0x14039e854
0039EAC9  41 8B C8                        mov ecx, r8d
0039EACC  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EAD0  0F 85 8F FD FF FF               jne 0x14039e865
0039EAD6  48 0F AB CB                     bts rbx, rcx
0039EADA  E9 86 FD FF FF                  jmp 0x14039e865
0039EADF  41 8B C8                        mov ecx, r8d
0039EAE2  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EAE6  0F 85 8A FD FF FF               jne 0x14039e876
0039EAEC  48 0F AB CB                     bts rbx, rcx
0039EAF0  E9 81 FD FF FF                  jmp 0x14039e876
0039EAF5  41 8B C8                        mov ecx, r8d
0039EAF8  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EAFC  0F 85 85 FD FF FF               jne 0x14039e887
0039EB02  48 0F AB CB                     bts rbx, rcx
0039EB06  E9 7C FD FF FF                  jmp 0x14039e887
0039EB0B  41 8B C8                        mov ecx, r8d
0039EB0E  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EB12  0F 85 80 FD FF FF               jne 0x14039e898
0039EB18  48 0F AB CB                     bts rbx, rcx
0039EB1C  E9 77 FD FF FF                  jmp 0x14039e898
0039EB21  41 8B C8                        mov ecx, r8d
0039EB24  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EB28  0F 85 7B FD FF FF               jne 0x14039e8a9
0039EB2E  48 0F AB CB                     bts rbx, rcx
0039EB32  E9 72 FD FF FF                  jmp 0x14039e8a9
0039EB37  41 8B C8                        mov ecx, r8d
0039EB3A  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EB3E  0F 85 76 FD FF FF               jne 0x14039e8ba
0039EB44  48 0F AB CB                     bts rbx, rcx
0039EB48  E9 6D FD FF FF                  jmp 0x14039e8ba
0039EB4D  41 8B C8                        mov ecx, r8d
0039EB50  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EB54  0F 85 71 FD FF FF               jne 0x14039e8cb
0039EB5A  48 0F AB CB                     bts rbx, rcx
0039EB5E  E9 68 FD FF FF                  jmp 0x14039e8cb
0039EB63  41 8B C8                        mov ecx, r8d
0039EB66  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EB6A  0F 85 6C FD FF FF               jne 0x14039e8dc
0039EB70  48 0F AB CB                     bts rbx, rcx
0039EB74  E9 63 FD FF FF                  jmp 0x14039e8dc
0039EB79  41 8B C8                        mov ecx, r8d
0039EB7C  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EB80  0F 85 67 FD FF FF               jne 0x14039e8ed
0039EB86  48 0F AB CB                     bts rbx, rcx
0039EB8A  E9 5E FD FF FF                  jmp 0x14039e8ed
0039EB8F  41 8B C8                        mov ecx, r8d
0039EB92  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EB96  0F 85 62 FD FF FF               jne 0x14039e8fe
0039EB9C  48 0F AB CB                     bts rbx, rcx
0039EBA0  E9 59 FD FF FF                  jmp 0x14039e8fe
0039EBA5  41 8B C8                        mov ecx, r8d
0039EBA8  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EBAC  0F 85 5D FD FF FF               jne 0x14039e90f
0039EBB2  48 0F AB CB                     bts rbx, rcx
0039EBB6  E9 54 FD FF FF                  jmp 0x14039e90f
0039EBBB  41 8B C8                        mov ecx, r8d
0039EBBE  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EBC2  0F 85 58 FD FF FF               jne 0x14039e920
0039EBC8  48 0F AB CB                     bts rbx, rcx
0039EBCC  E9 4F FD FF FF                  jmp 0x14039e920
0039EBD1  41 8B C8                        mov ecx, r8d
0039EBD4  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EBD8  0F 85 53 FD FF FF               jne 0x14039e931
0039EBDE  48 0F AB CB                     bts rbx, rcx
0039EBE2  E9 4A FD FF FF                  jmp 0x14039e931
0039EBE7  41 8B C8                        mov ecx, r8d
0039EBEA  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EBEE  0F 85 4E FD FF FF               jne 0x14039e942
0039EBF4  48 0F AB CB                     bts rbx, rcx
0039EBF8  E9 45 FD FF FF                  jmp 0x14039e942
0039EBFD  41 8B C8                        mov ecx, r8d
0039EC00  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EC04  0F 85 49 FD FF FF               jne 0x14039e953
0039EC0A  48 0F AB CB                     bts rbx, rcx
0039EC0E  E9 40 FD FF FF                  jmp 0x14039e953
0039EC13  41 8B C8                        mov ecx, r8d
0039EC16  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EC1A  0F 85 44 FD FF FF               jne 0x14039e964
0039EC20  48 0F AB CB                     bts rbx, rcx
0039EC24  E9 3B FD FF FF                  jmp 0x14039e964
0039EC29  41 8B C8                        mov ecx, r8d
0039EC2C  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EC30  0F 85 3F FD FF FF               jne 0x14039e975
0039EC36  48 0F AB CB                     bts rbx, rcx
0039EC3A  E9 36 FD FF FF                  jmp 0x14039e975
0039EC3F  41 8B C8                        mov ecx, r8d
0039EC42  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EC46  0F 85 3A FD FF FF               jne 0x14039e986
0039EC4C  48 0F AB CB                     bts rbx, rcx
0039EC50  E9 31 FD FF FF                  jmp 0x14039e986
0039EC55  41 8B C8                        mov ecx, r8d
0039EC58  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EC5C  0F 85 35 FD FF FF               jne 0x14039e997
0039EC62  48 0F AB CB                     bts rbx, rcx
0039EC66  E9 2C FD FF FF                  jmp 0x14039e997
0039EC6B  41 8B C8                        mov ecx, r8d
0039EC6E  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EC72  0F 85 30 FD FF FF               jne 0x14039e9a8
0039EC78  48 0F AB CB                     bts rbx, rcx
0039EC7C  E9 27 FD FF FF                  jmp 0x14039e9a8
0039EC81  41 8B C8                        mov ecx, r8d
0039EC84  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EC88  0F 85 2B FD FF FF               jne 0x14039e9b9
0039EC8E  48 0F AB CB                     bts rbx, rcx
0039EC92  E9 22 FD FF FF                  jmp 0x14039e9b9
0039EC97  41 8B C8                        mov ecx, r8d
0039EC9A  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039EC9E  0F 85 26 FD FF FF               jne 0x14039e9ca
0039ECA4  48 0F AB CB                     bts rbx, rcx
0039ECA8  E9 1D FD FF FF                  jmp 0x14039e9ca
0039ECAD  41 8B C8                        mov ecx, r8d
0039ECB0  4A 39 34 C7                     cmp qword ptr [rdi + r8*8], rsi
0039ECB4  0F 85 21 FD FF FF               jne 0x14039e9db
0039ECBA  48 0F AB CB                     bts rbx, rcx
0039ECBE  E9 18 FD FF FF                  jmp 0x14039e9db
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiDoesHeteroSoftParkElectionHaveWinner(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rbx;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rbx = 0;
loc_0039E7C0:
    if (condition_is_below) goto loc_0039EA04;
loc_0039E7D1:
    if (condition_is_below) goto loc_0039EA1A;
loc_0039E7E2:
    if (condition_is_below) goto loc_0039EA30;
loc_0039E7EE:
    if (condition_is_below) goto loc_0039EA45;
loc_0039E7FF:
    if (condition_is_below) goto loc_0039EA5B;
loc_0039E810:
    if (condition_is_below) goto loc_0039EA71;
loc_0039E821:
    if (condition_is_below) goto loc_0039EA87;
loc_0039E832:
    if (condition_is_below) goto loc_0039EA9D;
loc_0039E843:
    if (condition_is_below) goto loc_0039EAB3;
loc_0039E854:
    if (condition_is_below) goto loc_0039EAC9;
loc_0039E865:
    if (condition_is_below) goto loc_0039EADF;
loc_0039E876:
    if (condition_is_below) goto loc_0039EAF5;
loc_0039E887:
    if (condition_is_below) goto loc_0039EB0B;
loc_0039E898:
    if (condition_is_below) goto loc_0039EB21;
loc_0039E8A9:
    if (condition_is_below) goto loc_0039EB37;
loc_0039E8BA:
    if (condition_is_below) goto loc_0039EB4D;
loc_0039E8CB:
    if (condition_is_below) goto loc_0039EB63;
loc_0039E8DC:
    if (condition_is_below) goto loc_0039EB79;
loc_0039E8ED:
    if (condition_is_below) goto loc_0039EB8F;
loc_0039E8FE:
    if (condition_is_below) goto loc_0039EBA5;
loc_0039E90F:
    if (condition_is_below) goto loc_0039EBBB;
loc_0039E920:
    if (condition_is_below) goto loc_0039EBD1;
loc_0039E931:
    if (condition_is_below) goto loc_0039EBE7;
loc_0039E942:
    if (condition_is_below) goto loc_0039EBFD;
loc_0039E953:
    if (condition_is_below) goto loc_0039EC13;
loc_0039E964:
    if (condition_is_below) goto loc_0039EC29;
loc_0039E975:
    if (condition_is_below) goto loc_0039EC3F;
loc_0039E986:
    if (condition_is_below) goto loc_0039EC55;
loc_0039E997:
    if (condition_is_below) goto loc_0039EC6B;
loc_0039E9A8:
    if (condition_is_below) goto loc_0039EC81;
loc_0039E9B9:
    if (condition_is_below) goto loc_0039EC97;
loc_0039E9CA:
    if (condition_is_below) goto loc_0039ECAD;
loc_0039E9DB:
    result = (unsigned int)((2) + (32));
    if (((unsigned int)(result - 2)) < 64) goto loc_0039E7C0;
    *(unsigned __int64 *)(a4) = 0;
    result = (0 != 0) ? 1 : 0;
    return result;
loc_0039EA04:
    if ((*(unsigned __int64 *)(v_stack_p18 + 2 - 2 * 8)) != v_stack_p10) goto loc_0039E7D1;
    goto loc_0039E7D1;
loc_0039EA1A:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E7E2;
    goto loc_0039E7E2;
loc_0039EA30:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(result)) * 8)) != v_stack_p10) goto loc_0039E7EE;
    goto loc_0039E7EE;
loc_0039EA45:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E7FF;
    goto loc_0039E7FF;
loc_0039EA5B:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E810;
    goto loc_0039E810;
loc_0039EA71:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E821;
    goto loc_0039E821;
loc_0039EA87:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E832;
    goto loc_0039E832;
loc_0039EA9D:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E843;
    goto loc_0039E843;
loc_0039EAB3:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E854;
    goto loc_0039E854;
loc_0039EAC9:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E865;
    goto loc_0039E865;
loc_0039EADF:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E876;
    goto loc_0039E876;
loc_0039EAF5:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E887;
    goto loc_0039E887;
loc_0039EB0B:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E898;
    goto loc_0039E898;
loc_0039EB21:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E8A9;
    goto loc_0039E8A9;
loc_0039EB37:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E8BA;
    goto loc_0039E8BA;
loc_0039EB4D:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E8CB;
    goto loc_0039E8CB;
loc_0039EB63:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E8DC;
    goto loc_0039E8DC;
loc_0039EB79:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E8ED;
    goto loc_0039E8ED;
loc_0039EB8F:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E8FE;
    goto loc_0039E8FE;
loc_0039EBA5:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E90F;
    goto loc_0039E90F;
loc_0039EBBB:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E920;
    goto loc_0039E920;
loc_0039EBD1:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E931;
    goto loc_0039E931;
loc_0039EBE7:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E942;
    goto loc_0039E942;
loc_0039EBFD:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E953;
    goto loc_0039E953;
loc_0039EC13:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E964;
    goto loc_0039E964;
loc_0039EC29:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E975;
    goto loc_0039E975;
loc_0039EC3F:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E986;
    goto loc_0039E986;
loc_0039EC55:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E997;
    goto loc_0039E997;
loc_0039EC6B:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E9A8;
    goto loc_0039E9A8;
loc_0039EC81:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E9B9;
    goto loc_0039E9B9;
loc_0039EC97:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E9CA;
    goto loc_0039E9CA;
loc_0039ECAD:
    if ((*(unsigned __int64 *)(v_stack_p18 + (unsigned int)((unsigned int)(2 - 2)) * 8)) != v_stack_p10) goto loc_0039E9DB;
    goto loc_0039E9DB;
}
```

## 5. (Beta) C Style

```c
int64_t KiDoesHeteroSoftParkElectionHaveWinner(int64_t Arg1, int64_t Arg2, void *Arg3, void *Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rbx;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rbx = 0;
loc_0039E7C0:
    if (condition_is_below) goto loc_0039EA04;
loc_0039E7D1:
    if (condition_is_below) goto loc_0039EA1A;
loc_0039E7E2:
    if (condition_is_below) goto loc_0039EA30;
loc_0039E7EE:
    if (condition_is_below) goto loc_0039EA45;
loc_0039E7FF:
    if (condition_is_below) goto loc_0039EA5B;
loc_0039E810:
    if (condition_is_below) goto loc_0039EA71;
loc_0039E821:
    if (condition_is_below) goto loc_0039EA87;
loc_0039E832:
    if (condition_is_below) goto loc_0039EA9D;
loc_0039E843:
    if (condition_is_below) goto loc_0039EAB3;
loc_0039E854:
    if (condition_is_below) goto loc_0039EAC9;
loc_0039E865:
    if (condition_is_below) goto loc_0039EADF;
loc_0039E876:
    if (condition_is_below) goto loc_0039EAF5;
loc_0039E887:
    if (condition_is_below) goto loc_0039EB0B;
loc_0039E898:
    if (condition_is_below) goto loc_0039EB21;
loc_0039E8A9:
    if (condition_is_below) goto loc_0039EB37;
loc_0039E8BA:
    if (condition_is_below) goto loc_0039EB4D;
loc_0039E8CB:
    if (condition_is_below) goto loc_0039EB63;
loc_0039E8DC:
    if (condition_is_below) goto loc_0039EB79;
loc_0039E8ED:
    if (condition_is_below) goto loc_0039EB8F;
loc_0039E8FE:
    if (condition_is_below) goto loc_0039EBA5;
loc_0039E90F:
    if (condition_is_below) goto loc_0039EBBB;
loc_0039E920:
    if (condition_is_below) goto loc_0039EBD1;
loc_0039E931:
    if (condition_is_below) goto loc_0039EBE7;
loc_0039E942:
    if (condition_is_below) goto loc_0039EBFD;
loc_0039E953:
    if (condition_is_below) goto loc_0039EC13;
loc_0039E964:
    if (condition_is_below) goto loc_0039EC29;
loc_0039E975:
    if (condition_is_below) goto loc_0039EC3F;
loc_0039E986:
    if (condition_is_below) goto loc_0039EC55;
loc_0039E997:
    if (condition_is_below) goto loc_0039EC6B;
loc_0039E9A8:
    if (condition_is_below) goto loc_0039EC81;
loc_0039E9B9:
    if (condition_is_below) goto loc_0039EC97;
loc_0039E9CA:
    if (condition_is_below) goto loc_0039ECAD;
loc_0039E9DB:
    result = (uint32_t)((2) + (32));
    if (((uint32_t)(result - 2)) < 64) goto loc_0039E7C0;
    *(uint64_t *)(arg4) = 0;
    result = (0 != 0) ? 1 : 0;
    return result;
loc_0039EA04:
    if ((*(uint64_t *)(v_stack_p18 + 0x2 - 0x2 * 8)) != v_stack_p10) goto loc_0039E7D1;
    goto loc_0039E7D1;
loc_0039EA1A:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E7E2;
    goto loc_0039E7E2;
loc_0039EA30:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(result)) * 8)) != v_stack_p10) goto loc_0039E7EE;
    goto loc_0039E7EE;
loc_0039EA45:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E7FF;
    goto loc_0039E7FF;
loc_0039EA5B:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E810;
    goto loc_0039E810;
loc_0039EA71:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E821;
    goto loc_0039E821;
loc_0039EA87:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E832;
    goto loc_0039E832;
loc_0039EA9D:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E843;
    goto loc_0039E843;
loc_0039EAB3:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E854;
    goto loc_0039E854;
loc_0039EAC9:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E865;
    goto loc_0039E865;
loc_0039EADF:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E876;
    goto loc_0039E876;
loc_0039EAF5:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E887;
    goto loc_0039E887;
loc_0039EB0B:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E898;
    goto loc_0039E898;
loc_0039EB21:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E8A9;
    goto loc_0039E8A9;
loc_0039EB37:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E8BA;
    goto loc_0039E8BA;
loc_0039EB4D:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E8CB;
    goto loc_0039E8CB;
loc_0039EB63:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E8DC;
    goto loc_0039E8DC;
loc_0039EB79:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E8ED;
    goto loc_0039E8ED;
loc_0039EB8F:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E8FE;
    goto loc_0039E8FE;
loc_0039EBA5:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E90F;
    goto loc_0039E90F;
loc_0039EBBB:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E920;
    goto loc_0039E920;
loc_0039EBD1:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E931;
    goto loc_0039E931;
loc_0039EBE7:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E942;
    goto loc_0039E942;
loc_0039EBFD:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E953;
    goto loc_0039E953;
loc_0039EC13:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E964;
    goto loc_0039E964;
loc_0039EC29:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E975;
    goto loc_0039E975;
loc_0039EC3F:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E986;
    goto loc_0039E986;
loc_0039EC55:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E997;
    goto loc_0039E997;
loc_0039EC6B:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E9A8;
    goto loc_0039E9A8;
loc_0039EC81:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E9B9;
    goto loc_0039E9B9;
loc_0039EC97:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E9CA;
    goto loc_0039E9CA;
loc_0039ECAD:
    if ((*(uint64_t *)(v_stack_p18 + (uint32_t)((uint32_t)(2 - 0x2)) * 8)) != v_stack_p10) goto loc_0039E9DB;
    goto loc_0039E9DB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + r11*8` | `64` | `R` |
| `Arg3` | `+ 0x0 + r8*8` | `64` | `R` |
| `Arg3` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039E7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
