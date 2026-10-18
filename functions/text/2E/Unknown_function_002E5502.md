# sub_002E5502

- RVA: `0x002E5502`–`0x002E5960` (길이 `1,118` bytes)
- VA: `0x00000001402E5502`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071148`
- 디코드: `307`개 명령, `1,118/1,118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **59**
  - `0x002E5505` → [sub_002E4C42 + 0x5B](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E550D` → [sub_002E4C42 + 0x75](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5515` → [sub_002E4C42 + 0x5B3](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E551D` → [sub_002E4C42 + 0x171](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5525` → [sub_002E4C42 + 0x306](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E552D` → [sub_002E4C42 + 0x33A](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5535` → [sub_002E4C42 + 0x55A](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5540` → [sub_002E4C42 + 0x14F](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5552` → [sub_002E4C42 + 0x500](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E555A` → [sub_002E4C42 + 0x92](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5562` → [sub_002E4C42 + 0x136](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E556A` → [sub_002E4C42 + 0x490](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5572` → [sub_002E4C42 + 0x4BA](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E557A` → [sub_002E4C42 + 0x402](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5582` → [sub_002E4C42 + 0x6D7](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E558A` → [sub_002E4C42 + 0x711](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5592` → [sub_002E4C42 + 0x6F1](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E559A` → [sub_002E4C42 + 0x660](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E55A2` → [sub_002E4C42 + 0x770](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E55AA` → [sub_002E4C42 + 0x796](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E55B2` → [sub_002E4C42 + 0x1AF](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E55F9` → [sub_002E4C42 + 0xFC](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5619` → [sub_002E4C42 + 0x2BC](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5627` → [sub_002E4C42 + 0x1F7](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E562F` → [sub_002E4C42 + 0x292](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5638` → [sub_002E4C42 + 0x292](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E564E` → [sub_002E4C42 + 0xFC](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5654` → [sub_002E4C42 + 0x231](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E565F` → [sub_002E4C42 + 0xFC](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E566A` → [sub_002E4C42 + 0x1F1](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5675` → [sub_002E4C42 + 0x224](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E567D` → [sub_002E4C42 + 0x24C](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5685` → [sub_002E4C42 + 0x255](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E56B7` → [sub_002E4C42 + 0x35B](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E56C7` → [sub_002E4C42 + 0x2B7](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E56DC` → [sub_002E4C42 + 0xAA](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E56E4` → [sub_002E4C42 + 0xAA](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E56FA` → [sub_002E4C42 + 0x2B7](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5713` → [sub_002E4C42 + 0x2B7](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5721` → [sub_002E4C42 + 0x2BC](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5729` → [sub_002E4C42 + 0x418](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5731` → [sub_002E4C42 + 0x5CB](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5739` → [sub_002E4C42 + 0x729](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5744` → [sub_002E4C42 + 0x6A4](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E57EF` → [sub_002E4C42 + 0x3AB](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5814` → [sub_002E4C42 + 0xFC](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5849` → [sub_002E4C42 + 0xFC](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5882` → [sub_002E4C42 + 0x3AB](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E58B6` → [sub_002E4C42 + 0x681](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E58CB` → [sub_002E4C42 + 0x7F1](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E58D3` → [sub_002E4C42 + 0x7D2](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E58DE` → [sub_002E4C42 + 0x83D](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E58FC` → [sub_002E4C42 + 0xFC](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5917` → [sub_002E4C42 + 0x83D](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5928` → [sub_002E4C42 + 0x86E](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5931` → [sub_002E4C42 + 0x816](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5943` → [sub_002E4C42 + 0x85E](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E594E` → [sub_002E4C42 + 0x819](Unknown_function_002E4C42.md) (`tail-transfer`)
  - `0x002E5956` → [sub_002E4C42 + 0x7B7](Unknown_function_002E4C42.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E5502  4D 33 CA                        xor r9, r10
002E5505  E9 93 F7 FF FF                  jmp 0x1402e4c9d
002E550A  49 33 C9                        xor rcx, r9
002E550D  E9 A5 F7 FF FF                  jmp 0x1402e4cb7
002E5512  48 33 C1                        xor rax, rcx
002E5515  E9 DB FC FF FF                  jmp 0x1402e51f5
002E551A  48 33 C8                        xor rcx, rax
002E551D  E9 91 F8 FF FF                  jmp 0x1402e4db3
002E5522  49 33 D1                        xor rdx, r9
002E5525  E9 1E FA FF FF                  jmp 0x1402e4f48
002E552A  48 33 C2                        xor rax, rdx
002E552D  E9 4A FA FF FF                  jmp 0x1402e4f7c
002E5532  49 33 D1                        xor rdx, r9
002E5535  E9 62 FC FF FF                  jmp 0x1402e519c
002E553A  48 8B CB                        mov rcx, rbx
002E553D  48 33 C8                        xor rcx, rax
002E5540  E9 4C F8 FF FF                  jmp 0x1402e4d91
002E5545  49 33 C9                        xor rcx, r9
002E5548  8B C5                           mov eax, ebp
002E554A  48 83 F0 01                     xor rax, 1
002E554E  49 89 0C C1                     mov qword ptr [r9 + rax*8], rcx
002E5552  E9 EB FB FF FF                  jmp 0x1402e5142
002E5557  49 33 C9                        xor rcx, r9
002E555A  E9 75 F7 FF FF                  jmp 0x1402e4cd4
002E555F  48 33 D9                        xor rbx, rcx
002E5562  E9 11 F8 FF FF                  jmp 0x1402e4d78
002E5567  48 33 C1                        xor rax, rcx
002E556A  E9 63 FB FF FF                  jmp 0x1402e50d2
002E556F  48 33 CA                        xor rcx, rdx
002E5572  E9 85 FB FF FF                  jmp 0x1402e50fc
002E5577  48 33 C8                        xor rcx, rax
002E557A  E9 C5 FA FF FF                  jmp 0x1402e5044
002E557F  4C 33 C8                        xor r9, rax
002E5582  E9 92 FD FF FF                  jmp 0x1402e5319
002E5587  48 33 C1                        xor rax, rcx
002E558A  E9 C4 FD FF FF                  jmp 0x1402e5353
002E558F  49 33 C1                        xor rax, r9
002E5592  E9 9C FD FF FF                  jmp 0x1402e5333
002E5597  48 33 C2                        xor rax, rdx
002E559A  E9 03 FD FF FF                  jmp 0x1402e52a2
002E559F  4C 33 D2                        xor r10, rdx
002E55A2  E9 0B FE FF FF                  jmp 0x1402e53b2
002E55A7  49 33 C2                        xor rax, r10
002E55AA  E9 29 FE FF FF                  jmp 0x1402e53d8
002E55AF  49 33 C0                        xor rax, r8
002E55B2  E9 3A F8 FF FF                  jmp 0x1402e4df1
002E55B7  45 0F B6 63 08                  movzx r12d, byte ptr [r11 + 8]
002E55BC  41 0F B6 D4                     movzx edx, r12b
002E55C0  80 E2 01                        and dl, 1
002E55C3  74 59                           je 0x1402e561e
002E55C5  49 33 FA                        xor rdi, r10
002E55C8  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
002E55CC  48 85 C9                        test rcx, rcx
002E55CF  0F 85 B5 00 00 00               jne 0x1402e568a
002E55D5  49 3B CA                        cmp rcx, r10
002E55D8  49 8B F7                        mov rsi, r15
002E55DB  41 BE 08 00 00 00               mov r14d, 8
002E55E1  49 0F 44 F6                     cmove rsi, r14
002E55E5  48 8B 0C 3E                     mov rcx, qword ptr [rsi + rdi]
002E55E9  84 D2                           test dl, dl
002E55EB  74 09                           je 0x1402e55f6
002E55ED  48 85 C9                        test rcx, rcx
002E55F0  0F 85 B6 00 00 00               jne 0x1402e56ac
002E55F6  49 3B CA                        cmp rcx, r10
002E55F9  0F 85 3F F7 FF FF               jne 0x1402e4d3e
002E55FF  48 8B D7                        mov rdx, rdi
002E5602  48 8B CB                        mov rcx, rbx
002E5605  48 33 D3                        xor rdx, rbx
002E5608  41 F6 C4 01                     test r12b, 1
002E560C  48 0F 45 CA                     cmovne rcx, rdx
002E5610  48 89 0C 3E                     mov qword ptr [rsi + rdi], rcx
002E5614  41 0F B6 53 08                  movzx edx, byte ptr [r11 + 8]
002E5619  E9 E0 F8 FF FF                  jmp 0x1402e4efe
002E561E  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
002E5622  EB B1                           jmp 0x1402e55d5
002E5624  49 8B C8                        mov rcx, r8
002E5627  E9 0D F8 FF FF                  jmp 0x1402e4e39
002E562C  48 85 FF                        test rdi, rdi
002E562F  0F 84 9F F8 FF FF               je 0x1402e4ed4
002E5635  49 33 FB                        xor rdi, r11
002E5638  E9 97 F8 FF FF                  jmp 0x1402e4ed4
002E563D  44 0F B6 C7                     movzx r8d, dil
002E5641  45 84 F6                        test r14b, r14b
002E5644  74 16                           je 0x1402e565c
002E5646  48 85 C9                        test rcx, rcx
002E5649  75 0E                           jne 0x1402e5659
002E564B  49 3B D9                        cmp rbx, r9
002E564E  0F 85 EA F6 FF FF               jne 0x1402e4d3e
002E5654  E9 1A F8 FF FF                  jmp 0x1402e4e73
002E5659  48 33 CB                        xor rcx, rbx
002E565C  48 85 C9                        test rcx, rcx
002E565F  0F 85 D9 F6 FF FF               jne 0x1402e4d3e
002E5665  EB E4                           jmp 0x1402e564b
002E5667  48 33 C3                        xor rax, rbx
002E566A  E9 C4 F7 FF FF                  jmp 0x1402e4e33
002E566F  48 8B F1                        mov rsi, rcx
002E5672  48 33 F3                        xor rsi, rbx
002E5675  E9 EC F7 FF FF                  jmp 0x1402e4e66
002E567A  49 33 CA                        xor rcx, r10
002E567D  E9 0C F8 FF FF                  jmp 0x1402e4e8e
002E5682  48 33 CB                        xor rcx, rbx
002E5685  E9 0D F8 FF FF                  jmp 0x1402e4e97
002E568A  48 8B C7                        mov rax, rdi
002E568D  49 8B F7                        mov rsi, r15
002E5690  48 33 C1                        xor rax, rcx
002E5693  41 BE 08 00 00 00               mov r14d, 8
002E5699  49 3B C2                        cmp rax, r10
002E569C  49 8B C5                        mov rax, r13
002E569F  49 0F 44 F6                     cmove rsi, r14
002E56A3  48 8B 0C 37                     mov rcx, qword ptr [rdi + rsi]
002E56A7  E9 41 FF FF FF                  jmp 0x1402e55ed
002E56AC  48 33 CF                        xor rcx, rdi
002E56AF  E9 42 FF FF FF                  jmp 0x1402e55f6
002E56B4  49 33 C9                        xor rcx, r9
002E56B7  E9 E1 F8 FF FF                  jmp 0x1402e4f9d
002E56BC  84 C9                           test cl, cl
002E56BE  75 3F                           jne 0x1402e56ff
002E56C0  49 89 43 08                     mov qword ptr [r11 + 8], rax
002E56C4  0F B6 D0                        movzx edx, al
002E56C7  E9 2D F8 FF FF                  jmp 0x1402e4ef9
002E56CC  48 83 F9 01                     cmp rcx, 1
002E56D0  74 0F                           je 0x1402e56e1
002E56D2  4D 8B C3                        mov r8, r11
002E56D5  49 83 C8 01                     or r8, 1
002E56D9  4C 33 C1                        xor r8, rcx
002E56DC  E9 0B F6 FF FF                  jmp 0x1402e4cec
002E56E1  4D 8B C7                        mov r8, r15
002E56E4  E9 03 F6 FF FF                  jmp 0x1402e4cec
002E56E9  49 8B D1                        mov rdx, r9
002E56EC  49 33 D3                        xor rdx, r11
002E56EF  49 89 53 08                     mov qword ptr [r11 + 8], rdx
002E56F3  80 CA 01                        or dl, 1
002E56F6  41 88 53 08                     mov byte ptr [r11 + 8], dl
002E56FA  E9 FA F7 FF FF                  jmp 0x1402e4ef9
002E56FF  48 8B C8                        mov rcx, rax
002E5702  49 33 CB                        xor rcx, r11
002E5705  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
002E5709  80 C9 01                        or cl, 1
002E570C  41 88 4B 08                     mov byte ptr [r11 + 8], cl
002E5710  0F B6 D1                        movzx edx, cl
002E5713  E9 E1 F7 FF FF                  jmp 0x1402e4ef9
002E5718  48 8B CB                        mov rcx, rbx
002E571B  49 33 CB                        xor rcx, r11
002E571E  49 89 0A                        mov qword ptr [r10], rcx
002E5721  E9 D8 F7 FF FF                  jmp 0x1402e4efe
002E5726  4C 33 C8                        xor r9, rax
002E5729  E9 2C F9 FF FF                  jmp 0x1402e505a
002E572E  49 8B C1                        mov rax, r9
002E5731  E9 D7 FA FF FF                  jmp 0x1402e520d
002E5736  48 8B C2                        mov rax, rdx
002E5739  E9 2D FC FF FF                  jmp 0x1402e536b
002E573E  49 33 C9                        xor rcx, r9
002E5741  48 85 C9                        test rcx, rcx
002E5744  0F 84 9C FB FF FF               je 0x1402e52e6
002E574A  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
002E574E  45 85 C0                        test r8d, r8d
002E5751  74 09                           je 0x1402e575c
002E5753  48 85 C0                        test rax, rax
002E5756  0F 85 42 01 00 00               jne 0x1402e589e
002E575C  49 3B C1                        cmp rax, r9
002E575F  0F 85 D4 00 00 00               jne 0x1402e5839
002E5765  45 85 C0                        test r8d, r8d
002E5768  0F 84 FF 00 00 00               je 0x1402e586d
002E576E  48 8B C1                        mov rax, rcx
002E5771  48 33 C2                        xor rax, rdx
002E5774  48 89 41 08                     mov qword ptr [rcx + 8], rax
002E5778  45 85 C0                        test r8d, r8d
002E577B  74 09                           je 0x1402e5786
002E577D  48 85 C9                        test rcx, rcx
002E5780  0F 85 20 01 00 00               jne 0x1402e58a6
002E5786  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
002E5789  83 E0 03                        and eax, 3
002E578C  48 0B C1                        or rax, rcx
002E578F  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
002E5793  8B C5                           mov eax, ebp
002E5795  48 8B 0C C2                     mov rcx, qword ptr [rdx + rax*8]
002E5799  45 85 C0                        test r8d, r8d
002E579C  74 59                           je 0x1402e57f7
002E579E  48 85 C9                        test rcx, rcx
002E57A1  75 51                           jne 0x1402e57f4
002E57A3  45 85 C0                        test r8d, r8d
002E57A6  74 09                           je 0x1402e57b1
002E57A8  48 85 C9                        test rcx, rcx
002E57AB  0F 85 DB 00 00 00               jne 0x1402e588c
002E57B1  8B C5                           mov eax, ebp
002E57B3  48 83 F0 01                     xor rax, 1
002E57B7  49 89 0C C1                     mov qword ptr [r9 + rax*8], rcx
002E57BB  45 85 C0                        test r8d, r8d
002E57BE  0F 84 9E 00 00 00               je 0x1402e5862
002E57C4  48 8B CA                        mov rcx, rdx
002E57C7  8B C5                           mov eax, ebp
002E57C9  49 33 C9                        xor rcx, r9
002E57CC  48 89 0C C2                     mov qword ptr [rdx + rax*8], rcx
002E57D0  49 33 D1                        xor rdx, r9
002E57D3  41 8B 41 10                     mov eax, dword ptr [r9 + 0x10]
002E57D7  83 E0 03                        and eax, 3
002E57DA  48 0B C2                        or rax, rdx
002E57DD  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
002E57E1  41 F6 43 08 01                  test byte ptr [r11 + 8], 1
002E57E6  0F 85 89 00 00 00               jne 0x1402e5875
002E57EC  4C 8B FB                        mov r15, rbx
002E57EF  E9 F9 F7 FF FF                  jmp 0x1402e4fed
002E57F4  48 33 CA                        xor rcx, rdx
002E57F7  48 85 C9                        test rcx, rcx
002E57FA  74 A7                           je 0x1402e57a3
002E57FC  4C 8B 51 10                     mov r10, qword ptr [rcx + 0x10]
002E5800  49 8B C2                        mov rax, r10
002E5803  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E5807  45 85 C0                        test r8d, r8d
002E580A  74 05                           je 0x1402e5811
002E580C  48 85 C0                        test rax, rax
002E580F  75 76                           jne 0x1402e5887
002E5811  48 3B C2                        cmp rax, rdx
002E5814  0F 85 24 F5 FF FF               jne 0x1402e4d3e
002E581A  45 85 C0                        test r8d, r8d
002E581D  0F 84 98 00 00 00               je 0x1402e58bb
002E5823  48 8B C1                        mov rax, rcx
002E5826  49 33 C1                        xor rax, r9
002E5829  41 83 E2 03                     and r10d, 3
002E582D  4C 0B D0                        or r10, rax
002E5830  4C 89 51 10                     mov qword ptr [rcx + 0x10], r10
002E5834  E9 6A FF FF FF                  jmp 0x1402e57a3
002E5839  48 8B 01                        mov rax, qword ptr [rcx]
002E583C  45 85 C0                        test r8d, r8d
002E583F  74 05                           je 0x1402e5846
002E5841  48 85 C0                        test rax, rax
002E5844  75 68                           jne 0x1402e58ae
002E5846  49 3B C1                        cmp rax, r9
002E5849  0F 85 EF F4 FF FF               jne 0x1402e4d3e
002E584F  45 85 C0                        test r8d, r8d
002E5852  74 6F                           je 0x1402e58c3
002E5854  48 8B C1                        mov rax, rcx
002E5857  48 33 C2                        xor rax, rdx
002E585A  48 89 01                        mov qword ptr [rcx], rax
002E585D  E9 16 FF FF FF                  jmp 0x1402e5778
002E5862  8B C5                           mov eax, ebp
002E5864  4C 89 0C C2                     mov qword ptr [rdx + rax*8], r9
002E5868  E9 66 FF FF FF                  jmp 0x1402e57d3
002E586D  48 8B C2                        mov rax, rdx
002E5870  E9 FF FE FF FF                  jmp 0x1402e5774
002E5875  49 8B C3                        mov rax, r11
002E5878  48 33 C3                        xor rax, rbx
002E587B  48 85 DB                        test rbx, rbx
002E587E  4C 0F 45 F8                     cmovne r15, rax
002E5882  E9 66 F7 FF FF                  jmp 0x1402e4fed
002E5887  48 33 C1                        xor rax, rcx
002E588A  EB 85                           jmp 0x1402e5811
002E588C  49 33 C9                        xor rcx, r9
002E588F  8B C5                           mov eax, ebp
002E5891  48 83 F0 01                     xor rax, 1
002E5895  49 89 0C C1                     mov qword ptr [r9 + rax*8], rcx
002E5899  E9 26 FF FF FF                  jmp 0x1402e57c4
002E589E  48 33 C1                        xor rax, rcx
002E58A1  E9 B6 FE FF FF                  jmp 0x1402e575c
002E58A6  48 33 CA                        xor rcx, rdx
002E58A9  E9 D8 FE FF FF                  jmp 0x1402e5786
002E58AE  48 33 C1                        xor rax, rcx
002E58B1  EB 93                           jmp 0x1402e5846
002E58B3  49 33 C9                        xor rcx, r9
002E58B6  E9 08 FA FF FF                  jmp 0x1402e52c3
002E58BB  49 8B C1                        mov rax, r9
002E58BE  E9 66 FF FF FF                  jmp 0x1402e5829
002E58C3  48 8B C2                        mov rax, rdx
002E58C6  EB 92                           jmp 0x1402e585a
002E58C8  48 33 C2                        xor rax, rdx
002E58CB  E9 63 FB FF FF                  jmp 0x1402e5433
002E58D0  49 33 C1                        xor rax, r9
002E58D3  E9 3C FB FF FF                  jmp 0x1402e5414
002E58D8  49 33 CA                        xor rcx, r10
002E58DB  48 85 C9                        test rcx, rcx
002E58DE  0F 84 9B FB FF FF               je 0x1402e547f
002E58E4  48 8B 79 10                     mov rdi, qword ptr [rcx + 0x10]
002E58E8  48 8B C7                        mov rax, rdi
002E58EB  48 83 E0 FC                     and rax, 0xfffffffffffffffc
002E58EF  45 85 C0                        test r8d, r8d
002E58F2  74 05                           je 0x1402e58f9
002E58F4  48 85 C0                        test rax, rax
002E58F7  75 23                           jne 0x1402e591c
002E58F9  49 3B C2                        cmp rax, r10
002E58FC  0F 85 3C F4 FF FF               jne 0x1402e4d3e
002E5902  45 85 C0                        test r8d, r8d
002E5905  74 54                           je 0x1402e595b
002E5907  48 8B C1                        mov rax, rcx
002E590A  48 33 C2                        xor rax, rdx
002E590D  83 E7 03                        and edi, 3
002E5910  48 0B F8                        or rdi, rax
002E5913  48 89 79 10                     mov qword ptr [rcx + 0x10], rdi
002E5917  E9 63 FB FF FF                  jmp 0x1402e547f
002E591C  48 33 C1                        xor rax, rcx
002E591F  EB D8                           jmp 0x1402e58f9
002E5921  49 89 14 DA                     mov qword ptr [r10 + rbx*8], rdx
002E5925  49 8B CA                        mov rcx, r10
002E5928  E9 83 FB FF FF                  jmp 0x1402e54b0
002E592D  4D 89 14 D9                     mov qword ptr [r9 + rbx*8], r10
002E5931  E9 22 FB FF FF                  jmp 0x1402e5458
002E5936  48 33 CA                        xor rcx, rdx
002E5939  8B C3                           mov eax, ebx
002E593B  48 83 F0 01                     xor rax, 1
002E593F  48 89 0C C2                     mov qword ptr [rdx + rax*8], rcx
002E5943  E9 58 FB FF FF                  jmp 0x1402e54a0
002E5948  49 8B CA                        mov rcx, r10
002E594B  49 33 C9                        xor rcx, r9
002E594E  E9 08 FB FF FF                  jmp 0x1402e545b
002E5953  48 33 CA                        xor rcx, rdx
002E5956  E9 9E FA FF FF                  jmp 0x1402e53f9
002E595B  48 8B C2                        mov rax, rdx
002E595E  EB AD                           jmp 0x1402e590d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E5502(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    a4 = (a4) ^ (v_r10);
}
```

## 5. (Beta) C Style

```c
int64_t sub_002E5502(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    Arg4 = (Arg4) ^ (local_r10);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E5502&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
