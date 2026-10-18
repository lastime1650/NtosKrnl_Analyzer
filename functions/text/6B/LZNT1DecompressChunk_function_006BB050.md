# LZNT1DecompressChunk

- RVA: `0x006BB050`–`0x006BBBB6` (길이 `2,918` bytes)
- VA: `0x00000001406BB050`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C25E0`
- 디코드: `849`개 명령, `2,918/2,918` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [LZNT1DecompressChunkNewThread](../38/LZNT1DecompressChunkNewThread_function_0038F3F8.md) at `0x0038F4D8`
- [LZNT1DecompressChunkWorkItem](../44/LZNT1DecompressChunkWorkItem_function_00448A20.md) at `0x00448A42`
- [sub_00AEC8DA](../../page/AE/Unknown_function_00AEC8DA.md) at `0x00AEC95F`
- [RtlDecompressFragmentLZNT1](../../page/AE/RtlDecompressFragmentLZNT1_function_00AECAF0.md) at `0x00AECC51`
- [RtlDecompressFragmentLZNT1](../../page/AE/RtlDecompressFragmentLZNT1_function_00AECAF0.md) at `0x00AECC90`

### Static image references
- `0x006BB119` → RVA `0x0001EF44` (`.rdata`; read)
- `0x006BB1C7` → RVA `0x0001EF00` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006BB050  41 54                           push r12
006BB052  55                              push rbp
006BB053  53                              push rbx
006BB054  57                              push rdi
006BB055  56                              push rsi
006BB056  48 8B F9                        mov rdi, rcx
006BB059  4C 8B D1                        mov r10, rcx
006BB05C  49 8B F0                        mov rsi, r8
006BB05F  4C 8B C2                        mov r8, rdx
006BB062  49 83 E9 11                     sub r9, 0x11
006BB066  48 83 EA 08                     sub rdx, 8
006BB06A  4C 8B DA                        mov r11, rdx
006BB06D  48 8B EF                        mov rbp, rdi
006BB070  BB 0D 00 00 00                  mov ebx, 0xd
006BB075  49 3B F1                        cmp rsi, r9
006BB078  0F 83 C1 05 00 00               jae 0x1406bb63f
006BB07E  49 3B FB                        cmp rdi, r11
006BB081  0F 83 B8 05 00 00               jae 0x1406bb63f
006BB087  8A 06                           mov al, byte ptr [rsi]
006BB089  A8 01                           test al, 1
006BB08B  75 74                           jne 0x1406bb101
006BB08D  8A 56 01                        mov dl, byte ptr [rsi + 1]
006BB090  88 17                           mov byte ptr [rdi], dl
006BB092  A8 02                           test al, 2
006BB094  0F 85 42 01 00 00               jne 0x1406bb1dc
006BB09A  8A 56 02                        mov dl, byte ptr [rsi + 2]
006BB09D  88 57 01                        mov byte ptr [rdi + 1], dl
006BB0A0  A8 04                           test al, 4
006BB0A2  0F 85 01 02 00 00               jne 0x1406bb2a9
006BB0A8  8A 56 03                        mov dl, byte ptr [rsi + 3]
006BB0AB  88 57 02                        mov byte ptr [rdi + 2], dl
006BB0AE  A8 08                           test al, 8
006BB0B0  0F 85 B2 02 00 00               jne 0x1406bb368
006BB0B6  8A 56 04                        mov dl, byte ptr [rsi + 4]
006BB0B9  88 57 03                        mov byte ptr [rdi + 3], dl
006BB0BC  A8 10                           test al, 0x10
006BB0BE  0F 85 55 03 00 00               jne 0x1406bb419
006BB0C4  8A 56 05                        mov dl, byte ptr [rsi + 5]
006BB0C7  88 57 04                        mov byte ptr [rdi + 4], dl
006BB0CA  A8 20                           test al, 0x20
006BB0CC  0F 85 E6 03 00 00               jne 0x1406bb4b8
006BB0D2  8A 56 06                        mov dl, byte ptr [rsi + 6]
006BB0D5  88 57 05                        mov byte ptr [rdi + 5], dl
006BB0D8  A8 40                           test al, 0x40
006BB0DA  0F 85 69 04 00 00               jne 0x1406bb549
006BB0E0  8A 56 07                        mov dl, byte ptr [rsi + 7]
006BB0E3  88 57 06                        mov byte ptr [rdi + 6], dl
006BB0E6  A8 80                           test al, 0x80
006BB0E8  0F 85 DB 04 00 00               jne 0x1406bb5c9
006BB0EE  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BB0F1  88 57 07                        mov byte ptr [rdi + 7], dl
006BB0F4  48 83 C6 09                     add rsi, 9
006BB0F8  48 83 C7 08                     add rdi, 8
006BB0FC  E9 74 FF FF FF                  jmp 0x1406bb075
006BB101  48 3B FD                        cmp rdi, rbp
006BB104  0F 87 B8 00 00 00               ja 0x1406bb1c2
006BB10A  48 8D 56 01                     lea rdx, [rsi + 1]
006BB10E  4C 8B E2                        mov r12, rdx
006BB111  33 C9                           xor ecx, ecx
006BB113  66 8B 4E 01                     mov cx, word ptr [rsi + 1]
006BB117  8B F1                           mov esi, ecx
006BB119  48 8D 15 24 3E 96 FF            lea rdx, [rip - 0x69c1dc]
006BB120  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB123  87 D9                           xchg ecx, ebx
006BB125  D3 EE                           shr esi, cl
006BB127  87 D9                           xchg ecx, ebx
006BB129  48 F7 DE                        neg rsi
006BB12C  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB131  49 3B F2                        cmp rsi, r10
006BB134  0F 82 5F 0A 00 00               jb 0x1406bbb99
006BB13A  83 C1 03                        add ecx, 3
006BB13D  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB141  49 3B D3                        cmp rdx, r11
006BB144  0F 83 06 05 00 00               jae 0x1406bb650
006BB14A  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB14C  49 8B F4                        mov rsi, r12
006BB14F  48 83 EF 01                     sub rdi, 1
006BB153  A8 02                           test al, 2
006BB155  0F 85 81 00 00 00               jne 0x1406bb1dc
006BB15B  8A 56 02                        mov dl, byte ptr [rsi + 2]
006BB15E  88 57 01                        mov byte ptr [rdi + 1], dl
006BB161  A8 04                           test al, 4
006BB163  0F 85 40 01 00 00               jne 0x1406bb2a9
006BB169  8A 56 03                        mov dl, byte ptr [rsi + 3]
006BB16C  88 57 02                        mov byte ptr [rdi + 2], dl
006BB16F  A8 08                           test al, 8
006BB171  0F 85 F1 01 00 00               jne 0x1406bb368
006BB177  8A 56 04                        mov dl, byte ptr [rsi + 4]
006BB17A  88 57 03                        mov byte ptr [rdi + 3], dl
006BB17D  A8 10                           test al, 0x10
006BB17F  0F 85 94 02 00 00               jne 0x1406bb419
006BB185  8A 56 05                        mov dl, byte ptr [rsi + 5]
006BB188  88 57 04                        mov byte ptr [rdi + 4], dl
006BB18B  A8 20                           test al, 0x20
006BB18D  0F 85 25 03 00 00               jne 0x1406bb4b8
006BB193  8A 56 06                        mov dl, byte ptr [rsi + 6]
006BB196  88 57 05                        mov byte ptr [rdi + 5], dl
006BB199  A8 40                           test al, 0x40
006BB19B  0F 85 A8 03 00 00               jne 0x1406bb549
006BB1A1  8A 56 07                        mov dl, byte ptr [rsi + 7]
006BB1A4  88 57 06                        mov byte ptr [rdi + 6], dl
006BB1A7  A8 80                           test al, 0x80
006BB1A9  0F 85 1A 04 00 00               jne 0x1406bb5c9
006BB1AF  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BB1B2  88 57 07                        mov byte ptr [rdi + 7], dl
006BB1B5  48 83 C6 09                     add rsi, 9
006BB1B9  48 83 C7 08                     add rdi, 8
006BB1BD  E9 B3 FE FF FF                  jmp 0x1406bb075
006BB1C2  FF CB                           dec ebx
006BB1C4  49 8B D2                        mov rdx, r10
006BB1C7  48 8D 0D 32 3D 96 FF            lea rcx, [rip - 0x69c2ce]
006BB1CE  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB1D1  48 03 D1                        add rdx, rcx
006BB1D4  48 8B EA                        mov rbp, rdx
006BB1D7  E9 25 FF FF FF                  jmp 0x1406bb101
006BB1DC  48 83 C7 01                     add rdi, 1
006BB1E0  48 3B FD                        cmp rdi, rbp
006BB1E3  0F 87 A6 00 00 00               ja 0x1406bb28f
006BB1E9  48 8D 56 01                     lea rdx, [rsi + 1]
006BB1ED  4C 8B E2                        mov r12, rdx
006BB1F0  33 C9                           xor ecx, ecx
006BB1F2  66 8B 4E 02                     mov cx, word ptr [rsi + 2]
006BB1F6  8B F1                           mov esi, ecx
006BB1F8  48 8D 15 45 3D 96 FF            lea rdx, [rip - 0x69c2bb]
006BB1FF  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB202  87 D9                           xchg ecx, ebx
006BB204  D3 EE                           shr esi, cl
006BB206  87 D9                           xchg ecx, ebx
006BB208  48 F7 DE                        neg rsi
006BB20B  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB210  49 3B F2                        cmp rsi, r10
006BB213  0F 82 80 09 00 00               jb 0x1406bbb99
006BB219  83 C1 03                        add ecx, 3
006BB21C  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB220  49 3B D3                        cmp rdx, r11
006BB223  0F 83 D1 04 00 00               jae 0x1406bb6fa
006BB229  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB22B  49 8B F4                        mov rsi, r12
006BB22E  48 83 EF 02                     sub rdi, 2
006BB232  A8 04                           test al, 4
006BB234  75 73                           jne 0x1406bb2a9
006BB236  8A 56 03                        mov dl, byte ptr [rsi + 3]
006BB239  88 57 02                        mov byte ptr [rdi + 2], dl
006BB23C  A8 08                           test al, 8
006BB23E  0F 85 24 01 00 00               jne 0x1406bb368
006BB244  8A 56 04                        mov dl, byte ptr [rsi + 4]
006BB247  88 57 03                        mov byte ptr [rdi + 3], dl
006BB24A  A8 10                           test al, 0x10
006BB24C  0F 85 C7 01 00 00               jne 0x1406bb419
006BB252  8A 56 05                        mov dl, byte ptr [rsi + 5]
006BB255  88 57 04                        mov byte ptr [rdi + 4], dl
006BB258  A8 20                           test al, 0x20
006BB25A  0F 85 58 02 00 00               jne 0x1406bb4b8
006BB260  8A 56 06                        mov dl, byte ptr [rsi + 6]
006BB263  88 57 05                        mov byte ptr [rdi + 5], dl
006BB266  A8 40                           test al, 0x40
006BB268  0F 85 DB 02 00 00               jne 0x1406bb549
006BB26E  8A 56 07                        mov dl, byte ptr [rsi + 7]
006BB271  88 57 06                        mov byte ptr [rdi + 6], dl
006BB274  A8 80                           test al, 0x80
006BB276  0F 85 4D 03 00 00               jne 0x1406bb5c9
006BB27C  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BB27F  88 57 07                        mov byte ptr [rdi + 7], dl
006BB282  48 83 C6 09                     add rsi, 9
006BB286  48 83 C7 08                     add rdi, 8
006BB28A  E9 E6 FD FF FF                  jmp 0x1406bb075
006BB28F  FF CB                           dec ebx
006BB291  49 8B D2                        mov rdx, r10
006BB294  48 8D 0D 65 3C 96 FF            lea rcx, [rip - 0x69c39b]
006BB29B  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB29E  48 03 D1                        add rdx, rcx
006BB2A1  48 8B EA                        mov rbp, rdx
006BB2A4  E9 37 FF FF FF                  jmp 0x1406bb1e0
006BB2A9  48 83 C7 02                     add rdi, 2
006BB2AD  48 3B FD                        cmp rdi, rbp
006BB2B0  0F 87 98 00 00 00               ja 0x1406bb34e
006BB2B6  48 8D 56 01                     lea rdx, [rsi + 1]
006BB2BA  4C 8B E2                        mov r12, rdx
006BB2BD  33 C9                           xor ecx, ecx
006BB2BF  66 8B 4E 03                     mov cx, word ptr [rsi + 3]
006BB2C3  8B F1                           mov esi, ecx
006BB2C5  48 8D 15 78 3C 96 FF            lea rdx, [rip - 0x69c388]
006BB2CC  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB2CF  87 D9                           xchg ecx, ebx
006BB2D1  D3 EE                           shr esi, cl
006BB2D3  87 D9                           xchg ecx, ebx
006BB2D5  48 F7 DE                        neg rsi
006BB2D8  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB2DD  49 3B F2                        cmp rsi, r10
006BB2E0  0F 82 B3 08 00 00               jb 0x1406bbb99
006BB2E6  83 C1 03                        add ecx, 3
006BB2E9  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB2ED  49 3B D3                        cmp rdx, r11
006BB2F0  0F 83 AE 04 00 00               jae 0x1406bb7a4
006BB2F6  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB2F8  49 8B F4                        mov rsi, r12
006BB2FB  48 83 EF 03                     sub rdi, 3
006BB2FF  A8 08                           test al, 8
006BB301  75 65                           jne 0x1406bb368
006BB303  8A 56 04                        mov dl, byte ptr [rsi + 4]
006BB306  88 57 03                        mov byte ptr [rdi + 3], dl
006BB309  A8 10                           test al, 0x10
006BB30B  0F 85 08 01 00 00               jne 0x1406bb419
006BB311  8A 56 05                        mov dl, byte ptr [rsi + 5]
006BB314  88 57 04                        mov byte ptr [rdi + 4], dl
006BB317  A8 20                           test al, 0x20
006BB319  0F 85 99 01 00 00               jne 0x1406bb4b8
006BB31F  8A 56 06                        mov dl, byte ptr [rsi + 6]
006BB322  88 57 05                        mov byte ptr [rdi + 5], dl
006BB325  A8 40                           test al, 0x40
006BB327  0F 85 1C 02 00 00               jne 0x1406bb549
006BB32D  8A 56 07                        mov dl, byte ptr [rsi + 7]
006BB330  88 57 06                        mov byte ptr [rdi + 6], dl
006BB333  A8 80                           test al, 0x80
006BB335  0F 85 8E 02 00 00               jne 0x1406bb5c9
006BB33B  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BB33E  88 57 07                        mov byte ptr [rdi + 7], dl
006BB341  48 83 C6 09                     add rsi, 9
006BB345  48 83 C7 08                     add rdi, 8
006BB349  E9 27 FD FF FF                  jmp 0x1406bb075
006BB34E  FF CB                           dec ebx
006BB350  49 8B D2                        mov rdx, r10
006BB353  48 8D 0D A6 3B 96 FF            lea rcx, [rip - 0x69c45a]
006BB35A  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB35D  48 03 D1                        add rdx, rcx
006BB360  48 8B EA                        mov rbp, rdx
006BB363  E9 45 FF FF FF                  jmp 0x1406bb2ad
006BB368  48 83 C7 03                     add rdi, 3
006BB36C  48 3B FD                        cmp rdi, rbp
006BB36F  0F 87 8A 00 00 00               ja 0x1406bb3ff
006BB375  48 8D 56 01                     lea rdx, [rsi + 1]
006BB379  4C 8B E2                        mov r12, rdx
006BB37C  33 C9                           xor ecx, ecx
006BB37E  66 8B 4E 04                     mov cx, word ptr [rsi + 4]
006BB382  8B F1                           mov esi, ecx
006BB384  48 8D 15 B9 3B 96 FF            lea rdx, [rip - 0x69c447]
006BB38B  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB38E  87 D9                           xchg ecx, ebx
006BB390  D3 EE                           shr esi, cl
006BB392  87 D9                           xchg ecx, ebx
006BB394  48 F7 DE                        neg rsi
006BB397  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB39C  49 3B F2                        cmp rsi, r10
006BB39F  0F 82 F4 07 00 00               jb 0x1406bbb99
006BB3A5  83 C1 03                        add ecx, 3
006BB3A8  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB3AC  49 3B D3                        cmp rdx, r11
006BB3AF  0F 83 99 04 00 00               jae 0x1406bb84e
006BB3B5  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB3B7  49 8B F4                        mov rsi, r12
006BB3BA  48 83 EF 04                     sub rdi, 4
006BB3BE  A8 10                           test al, 0x10
006BB3C0  75 57                           jne 0x1406bb419
006BB3C2  8A 56 05                        mov dl, byte ptr [rsi + 5]
006BB3C5  88 57 04                        mov byte ptr [rdi + 4], dl
006BB3C8  A8 20                           test al, 0x20
006BB3CA  0F 85 E8 00 00 00               jne 0x1406bb4b8
006BB3D0  8A 56 06                        mov dl, byte ptr [rsi + 6]
006BB3D3  88 57 05                        mov byte ptr [rdi + 5], dl
006BB3D6  A8 40                           test al, 0x40
006BB3D8  0F 85 6B 01 00 00               jne 0x1406bb549
006BB3DE  8A 56 07                        mov dl, byte ptr [rsi + 7]
006BB3E1  88 57 06                        mov byte ptr [rdi + 6], dl
006BB3E4  A8 80                           test al, 0x80
006BB3E6  0F 85 DD 01 00 00               jne 0x1406bb5c9
006BB3EC  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BB3EF  88 57 07                        mov byte ptr [rdi + 7], dl
006BB3F2  48 83 C6 09                     add rsi, 9
006BB3F6  48 83 C7 08                     add rdi, 8
006BB3FA  E9 76 FC FF FF                  jmp 0x1406bb075
006BB3FF  FF CB                           dec ebx
006BB401  49 8B D2                        mov rdx, r10
006BB404  48 8D 0D F5 3A 96 FF            lea rcx, [rip - 0x69c50b]
006BB40B  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB40E  48 03 D1                        add rdx, rcx
006BB411  48 8B EA                        mov rbp, rdx
006BB414  E9 53 FF FF FF                  jmp 0x1406bb36c
006BB419  48 83 C7 04                     add rdi, 4
006BB41D  48 3B FD                        cmp rdi, rbp
006BB420  77 7C                           ja 0x1406bb49e
006BB422  48 8D 56 01                     lea rdx, [rsi + 1]
006BB426  4C 8B E2                        mov r12, rdx
006BB429  33 C9                           xor ecx, ecx
006BB42B  66 8B 4E 05                     mov cx, word ptr [rsi + 5]
006BB42F  8B F1                           mov esi, ecx
006BB431  48 8D 15 0C 3B 96 FF            lea rdx, [rip - 0x69c4f4]
006BB438  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB43B  87 D9                           xchg ecx, ebx
006BB43D  D3 EE                           shr esi, cl
006BB43F  87 D9                           xchg ecx, ebx
006BB441  48 F7 DE                        neg rsi
006BB444  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB449  49 3B F2                        cmp rsi, r10
006BB44C  0F 82 47 07 00 00               jb 0x1406bbb99
006BB452  83 C1 03                        add ecx, 3
006BB455  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB459  49 3B D3                        cmp rdx, r11
006BB45C  0F 83 96 04 00 00               jae 0x1406bb8f8
006BB462  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB464  49 8B F4                        mov rsi, r12
006BB467  48 83 EF 05                     sub rdi, 5
006BB46B  A8 20                           test al, 0x20
006BB46D  75 49                           jne 0x1406bb4b8
006BB46F  8A 56 06                        mov dl, byte ptr [rsi + 6]
006BB472  88 57 05                        mov byte ptr [rdi + 5], dl
006BB475  A8 40                           test al, 0x40
006BB477  0F 85 CC 00 00 00               jne 0x1406bb549
006BB47D  8A 56 07                        mov dl, byte ptr [rsi + 7]
006BB480  88 57 06                        mov byte ptr [rdi + 6], dl
006BB483  A8 80                           test al, 0x80
006BB485  0F 85 3E 01 00 00               jne 0x1406bb5c9
006BB48B  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BB48E  88 57 07                        mov byte ptr [rdi + 7], dl
006BB491  48 83 C6 09                     add rsi, 9
006BB495  48 83 C7 08                     add rdi, 8
006BB499  E9 D7 FB FF FF                  jmp 0x1406bb075
006BB49E  FF CB                           dec ebx
006BB4A0  49 8B D2                        mov rdx, r10
006BB4A3  48 8D 0D 56 3A 96 FF            lea rcx, [rip - 0x69c5aa]
006BB4AA  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB4AD  48 03 D1                        add rdx, rcx
006BB4B0  48 8B EA                        mov rbp, rdx
006BB4B3  E9 65 FF FF FF                  jmp 0x1406bb41d
006BB4B8  48 83 C7 05                     add rdi, 5
006BB4BC  48 3B FD                        cmp rdi, rbp
006BB4BF  77 6E                           ja 0x1406bb52f
006BB4C1  48 8D 56 01                     lea rdx, [rsi + 1]
006BB4C5  4C 8B E2                        mov r12, rdx
006BB4C8  33 C9                           xor ecx, ecx
006BB4CA  66 8B 4E 06                     mov cx, word ptr [rsi + 6]
006BB4CE  8B F1                           mov esi, ecx
006BB4D0  48 8D 15 6D 3A 96 FF            lea rdx, [rip - 0x69c593]
006BB4D7  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB4DA  87 D9                           xchg ecx, ebx
006BB4DC  D3 EE                           shr esi, cl
006BB4DE  87 D9                           xchg ecx, ebx
006BB4E0  48 F7 DE                        neg rsi
006BB4E3  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB4E8  49 3B F2                        cmp rsi, r10
006BB4EB  0F 82 A8 06 00 00               jb 0x1406bbb99
006BB4F1  83 C1 03                        add ecx, 3
006BB4F4  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB4F8  49 3B D3                        cmp rdx, r11
006BB4FB  0F 83 A1 04 00 00               jae 0x1406bb9a2
006BB501  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB503  49 8B F4                        mov rsi, r12
006BB506  48 83 EF 06                     sub rdi, 6
006BB50A  A8 40                           test al, 0x40
006BB50C  75 3B                           jne 0x1406bb549
006BB50E  8A 56 07                        mov dl, byte ptr [rsi + 7]
006BB511  88 57 06                        mov byte ptr [rdi + 6], dl
006BB514  A8 80                           test al, 0x80
006BB516  0F 85 AD 00 00 00               jne 0x1406bb5c9
006BB51C  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BB51F  88 57 07                        mov byte ptr [rdi + 7], dl
006BB522  48 83 C6 09                     add rsi, 9
006BB526  48 83 C7 08                     add rdi, 8
006BB52A  E9 46 FB FF FF                  jmp 0x1406bb075
006BB52F  FF CB                           dec ebx
006BB531  49 8B D2                        mov rdx, r10
006BB534  48 8D 0D C5 39 96 FF            lea rcx, [rip - 0x69c63b]
006BB53B  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB53E  48 03 D1                        add rdx, rcx
006BB541  48 8B EA                        mov rbp, rdx
006BB544  E9 73 FF FF FF                  jmp 0x1406bb4bc
006BB549  48 83 C7 06                     add rdi, 6
006BB54D  48 3B FD                        cmp rdi, rbp
006BB550  77 60                           ja 0x1406bb5b2
006BB552  48 8D 56 01                     lea rdx, [rsi + 1]
006BB556  4C 8B E2                        mov r12, rdx
006BB559  33 C9                           xor ecx, ecx
006BB55B  66 8B 4E 07                     mov cx, word ptr [rsi + 7]
006BB55F  8B F1                           mov esi, ecx
006BB561  48 8D 15 DC 39 96 FF            lea rdx, [rip - 0x69c624]
006BB568  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB56B  87 D9                           xchg ecx, ebx
006BB56D  D3 EE                           shr esi, cl
006BB56F  87 D9                           xchg ecx, ebx
006BB571  48 F7 DE                        neg rsi
006BB574  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB579  49 3B F2                        cmp rsi, r10
006BB57C  0F 82 17 06 00 00               jb 0x1406bbb99
006BB582  83 C1 03                        add ecx, 3
006BB585  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB589  49 3B D3                        cmp rdx, r11
006BB58C  0F 83 BA 04 00 00               jae 0x1406bba4c
006BB592  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB594  49 8B F4                        mov rsi, r12
006BB597  48 83 EF 07                     sub rdi, 7
006BB59B  A8 80                           test al, 0x80
006BB59D  75 2A                           jne 0x1406bb5c9
006BB59F  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BB5A2  88 57 07                        mov byte ptr [rdi + 7], dl
006BB5A5  48 83 C6 09                     add rsi, 9
006BB5A9  48 83 C7 08                     add rdi, 8
006BB5AD  E9 C3 FA FF FF                  jmp 0x1406bb075
006BB5B2  FF CB                           dec ebx
006BB5B4  49 8B D2                        mov rdx, r10
006BB5B7  48 8D 0D 42 39 96 FF            lea rcx, [rip - 0x69c6be]
006BB5BE  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB5C1  48 03 D1                        add rdx, rcx
006BB5C4  48 8B EA                        mov rbp, rdx
006BB5C7  EB 84                           jmp 0x1406bb54d
006BB5C9  48 83 C7 07                     add rdi, 7
006BB5CD  48 3B FD                        cmp rdi, rbp
006BB5D0  77 56                           ja 0x1406bb628
006BB5D2  48 8D 56 01                     lea rdx, [rsi + 1]
006BB5D6  4C 8B E2                        mov r12, rdx
006BB5D9  33 C9                           xor ecx, ecx
006BB5DB  66 8B 4E 08                     mov cx, word ptr [rsi + 8]
006BB5DF  8B F1                           mov esi, ecx
006BB5E1  48 8D 15 5C 39 96 FF            lea rdx, [rip - 0x69c6a4]
006BB5E8  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB5EB  87 D9                           xchg ecx, ebx
006BB5ED  D3 EE                           shr esi, cl
006BB5EF  87 D9                           xchg ecx, ebx
006BB5F1  48 F7 DE                        neg rsi
006BB5F4  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB5F9  49 3B F2                        cmp rsi, r10
006BB5FC  0F 82 97 05 00 00               jb 0x1406bbb99
006BB602  83 C1 03                        add ecx, 3
006BB605  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB609  49 3B D3                        cmp rdx, r11
006BB60C  0F 83 E4 04 00 00               jae 0x1406bbaf6
006BB612  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB614  49 8B F4                        mov rsi, r12
006BB617  48 83 EF 08                     sub rdi, 8
006BB61B  48 83 C6 09                     add rsi, 9
006BB61F  48 83 C7 08                     add rdi, 8
006BB623  E9 4D FA FF FF                  jmp 0x1406bb075
006BB628  FF CB                           dec ebx
006BB62A  49 8B D2                        mov rdx, r10
006BB62D  48 8D 0D CC 38 96 FF            lea rcx, [rip - 0x69c734]
006BB634  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB637  48 03 D1                        add rdx, rcx
006BB63A  48 8B EA                        mov rbp, rdx
006BB63D  EB 8E                           jmp 0x1406bb5cd
006BB63F  49 83 C1 11                     add r9, 0x11
006BB643  49 3B F1                        cmp rsi, r9
006BB646  0F 84 54 05 00 00               je 0x1406bbba0
006BB64C  8A 06                           mov al, byte ptr [rsi]
006BB64E  EB 0A                           jmp 0x1406bb65a
006BB650  49 83 C1 11                     add r9, 0x11
006BB654  49 8B F4                        mov rsi, r12
006BB657  48 FF CE                        dec rsi
006BB65A  48 8D 4E 01                     lea rcx, [rsi + 1]
006BB65E  49 3B C9                        cmp rcx, r9
006BB661  0F 84 39 05 00 00               je 0x1406bbba0
006BB667  0F 87 2C 05 00 00               ja 0x1406bbb99
006BB66D  49 3B F8                        cmp rdi, r8
006BB670  0F 84 2A 05 00 00               je 0x1406bbba0
006BB676  0F 87 1D 05 00 00               ja 0x1406bbb99
006BB67C  A8 01                           test al, 1
006BB67E  75 0A                           jne 0x1406bb68a
006BB680  8A 56 01                        mov dl, byte ptr [rsi + 1]
006BB683  88 17                           mov byte ptr [rdi], dl
006BB685  48 FF C7                        inc rdi
006BB688  EB 7A                           jmp 0x1406bb704
006BB68A  48 8D 4E 03                     lea rcx, [rsi + 3]
006BB68E  49 3B C9                        cmp rcx, r9
006BB691  0F 87 02 05 00 00               ja 0x1406bbb99
006BB697  48 3B FD                        cmp rdi, rbp
006BB69A  77 47                           ja 0x1406bb6e3
006BB69C  48 8D 56 01                     lea rdx, [rsi + 1]
006BB6A0  4C 8B E2                        mov r12, rdx
006BB6A3  33 C9                           xor ecx, ecx
006BB6A5  66 8B 4E 01                     mov cx, word ptr [rsi + 1]
006BB6A9  8B F1                           mov esi, ecx
006BB6AB  48 8D 15 92 38 96 FF            lea rdx, [rip - 0x69c76e]
006BB6B2  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB6B5  87 D9                           xchg ecx, ebx
006BB6B7  D3 EE                           shr esi, cl
006BB6B9  87 D9                           xchg ecx, ebx
006BB6BB  48 F7 DE                        neg rsi
006BB6BE  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB6C3  49 3B F2                        cmp rsi, r10
006BB6C6  0F 82 CD 04 00 00               jb 0x1406bbb99
006BB6CC  83 C1 03                        add ecx, 3
006BB6CF  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB6D3  49 3B D0                        cmp rdx, r8
006BB6D6  0F 87 BD 04 00 00               ja 0x1406bbb99
006BB6DC  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB6DE  49 8B F4                        mov rsi, r12
006BB6E1  EB 21                           jmp 0x1406bb704
006BB6E3  FF CB                           dec ebx
006BB6E5  49 8B D2                        mov rdx, r10
006BB6E8  48 8D 0D 11 38 96 FF            lea rcx, [rip - 0x69c7ef]
006BB6EF  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB6F2  48 03 D1                        add rdx, rcx
006BB6F5  48 8B EA                        mov rbp, rdx
006BB6F8  EB 9D                           jmp 0x1406bb697
006BB6FA  49 83 C1 11                     add r9, 0x11
006BB6FE  49 8B F4                        mov rsi, r12
006BB701  48 FF CE                        dec rsi
006BB704  48 8D 4E 02                     lea rcx, [rsi + 2]
006BB708  49 3B C9                        cmp rcx, r9
006BB70B  0F 84 8F 04 00 00               je 0x1406bbba0
006BB711  0F 87 82 04 00 00               ja 0x1406bbb99
006BB717  49 3B F8                        cmp rdi, r8
006BB71A  0F 84 80 04 00 00               je 0x1406bbba0
006BB720  0F 87 73 04 00 00               ja 0x1406bbb99
006BB726  A8 02                           test al, 2
006BB728  75 0A                           jne 0x1406bb734
006BB72A  8A 56 02                        mov dl, byte ptr [rsi + 2]
006BB72D  88 17                           mov byte ptr [rdi], dl
006BB72F  48 FF C7                        inc rdi
006BB732  EB 7A                           jmp 0x1406bb7ae
006BB734  48 8D 4E 04                     lea rcx, [rsi + 4]
006BB738  49 3B C9                        cmp rcx, r9
006BB73B  0F 87 58 04 00 00               ja 0x1406bbb99
006BB741  48 3B FD                        cmp rdi, rbp
006BB744  77 47                           ja 0x1406bb78d
006BB746  48 8D 56 01                     lea rdx, [rsi + 1]
006BB74A  4C 8B E2                        mov r12, rdx
006BB74D  33 C9                           xor ecx, ecx
006BB74F  66 8B 4E 02                     mov cx, word ptr [rsi + 2]
006BB753  8B F1                           mov esi, ecx
006BB755  48 8D 15 E8 37 96 FF            lea rdx, [rip - 0x69c818]
006BB75C  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB75F  87 D9                           xchg ecx, ebx
006BB761  D3 EE                           shr esi, cl
006BB763  87 D9                           xchg ecx, ebx
006BB765  48 F7 DE                        neg rsi
006BB768  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB76D  49 3B F2                        cmp rsi, r10
006BB770  0F 82 23 04 00 00               jb 0x1406bbb99
006BB776  83 C1 03                        add ecx, 3
006BB779  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB77D  49 3B D0                        cmp rdx, r8
006BB780  0F 87 13 04 00 00               ja 0x1406bbb99
006BB786  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB788  49 8B F4                        mov rsi, r12
006BB78B  EB 21                           jmp 0x1406bb7ae
006BB78D  FF CB                           dec ebx
006BB78F  49 8B D2                        mov rdx, r10
006BB792  48 8D 0D 67 37 96 FF            lea rcx, [rip - 0x69c899]
006BB799  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB79C  48 03 D1                        add rdx, rcx
006BB79F  48 8B EA                        mov rbp, rdx
006BB7A2  EB 9D                           jmp 0x1406bb741
006BB7A4  49 83 C1 11                     add r9, 0x11
006BB7A8  49 8B F4                        mov rsi, r12
006BB7AB  48 FF CE                        dec rsi
006BB7AE  48 8D 4E 03                     lea rcx, [rsi + 3]
006BB7B2  49 3B C9                        cmp rcx, r9
006BB7B5  0F 84 E5 03 00 00               je 0x1406bbba0
006BB7BB  0F 87 D8 03 00 00               ja 0x1406bbb99
006BB7C1  49 3B F8                        cmp rdi, r8
006BB7C4  0F 84 D6 03 00 00               je 0x1406bbba0
006BB7CA  0F 87 C9 03 00 00               ja 0x1406bbb99
006BB7D0  A8 04                           test al, 4
006BB7D2  75 0A                           jne 0x1406bb7de
006BB7D4  8A 56 03                        mov dl, byte ptr [rsi + 3]
006BB7D7  88 17                           mov byte ptr [rdi], dl
006BB7D9  48 FF C7                        inc rdi
006BB7DC  EB 7A                           jmp 0x1406bb858
006BB7DE  48 8D 4E 05                     lea rcx, [rsi + 5]
006BB7E2  49 3B C9                        cmp rcx, r9
006BB7E5  0F 87 AE 03 00 00               ja 0x1406bbb99
006BB7EB  48 3B FD                        cmp rdi, rbp
006BB7EE  77 47                           ja 0x1406bb837
006BB7F0  48 8D 56 01                     lea rdx, [rsi + 1]
006BB7F4  4C 8B E2                        mov r12, rdx
006BB7F7  33 C9                           xor ecx, ecx
006BB7F9  66 8B 4E 03                     mov cx, word ptr [rsi + 3]
006BB7FD  8B F1                           mov esi, ecx
006BB7FF  48 8D 15 3E 37 96 FF            lea rdx, [rip - 0x69c8c2]
006BB806  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB809  87 D9                           xchg ecx, ebx
006BB80B  D3 EE                           shr esi, cl
006BB80D  87 D9                           xchg ecx, ebx
006BB80F  48 F7 DE                        neg rsi
006BB812  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB817  49 3B F2                        cmp rsi, r10
006BB81A  0F 82 79 03 00 00               jb 0x1406bbb99
006BB820  83 C1 03                        add ecx, 3
006BB823  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB827  49 3B D0                        cmp rdx, r8
006BB82A  0F 87 69 03 00 00               ja 0x1406bbb99
006BB830  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB832  49 8B F4                        mov rsi, r12
006BB835  EB 21                           jmp 0x1406bb858
006BB837  FF CB                           dec ebx
006BB839  49 8B D2                        mov rdx, r10
006BB83C  48 8D 0D BD 36 96 FF            lea rcx, [rip - 0x69c943]
006BB843  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB846  48 03 D1                        add rdx, rcx
006BB849  48 8B EA                        mov rbp, rdx
006BB84C  EB 9D                           jmp 0x1406bb7eb
006BB84E  49 83 C1 11                     add r9, 0x11
006BB852  49 8B F4                        mov rsi, r12
006BB855  48 FF CE                        dec rsi
006BB858  48 8D 4E 04                     lea rcx, [rsi + 4]
006BB85C  49 3B C9                        cmp rcx, r9
006BB85F  0F 84 3B 03 00 00               je 0x1406bbba0
006BB865  0F 87 2E 03 00 00               ja 0x1406bbb99
006BB86B  49 3B F8                        cmp rdi, r8
006BB86E  0F 84 2C 03 00 00               je 0x1406bbba0
006BB874  0F 87 1F 03 00 00               ja 0x1406bbb99
006BB87A  A8 08                           test al, 8
006BB87C  75 0A                           jne 0x1406bb888
006BB87E  8A 56 04                        mov dl, byte ptr [rsi + 4]
006BB881  88 17                           mov byte ptr [rdi], dl
006BB883  48 FF C7                        inc rdi
006BB886  EB 7A                           jmp 0x1406bb902
006BB888  48 8D 4E 06                     lea rcx, [rsi + 6]
006BB88C  49 3B C9                        cmp rcx, r9
006BB88F  0F 87 04 03 00 00               ja 0x1406bbb99
006BB895  48 3B FD                        cmp rdi, rbp
006BB898  77 47                           ja 0x1406bb8e1
006BB89A  48 8D 56 01                     lea rdx, [rsi + 1]
006BB89E  4C 8B E2                        mov r12, rdx
006BB8A1  33 C9                           xor ecx, ecx
006BB8A3  66 8B 4E 04                     mov cx, word ptr [rsi + 4]
006BB8A7  8B F1                           mov esi, ecx
006BB8A9  48 8D 15 94 36 96 FF            lea rdx, [rip - 0x69c96c]
006BB8B0  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB8B3  87 D9                           xchg ecx, ebx
006BB8B5  D3 EE                           shr esi, cl
006BB8B7  87 D9                           xchg ecx, ebx
006BB8B9  48 F7 DE                        neg rsi
006BB8BC  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB8C1  49 3B F2                        cmp rsi, r10
006BB8C4  0F 82 CF 02 00 00               jb 0x1406bbb99
006BB8CA  83 C1 03                        add ecx, 3
006BB8CD  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB8D1  49 3B D0                        cmp rdx, r8
006BB8D4  0F 87 BF 02 00 00               ja 0x1406bbb99
006BB8DA  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB8DC  49 8B F4                        mov rsi, r12
006BB8DF  EB 21                           jmp 0x1406bb902
006BB8E1  FF CB                           dec ebx
006BB8E3  49 8B D2                        mov rdx, r10
006BB8E6  48 8D 0D 13 36 96 FF            lea rcx, [rip - 0x69c9ed]
006BB8ED  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB8F0  48 03 D1                        add rdx, rcx
006BB8F3  48 8B EA                        mov rbp, rdx
006BB8F6  EB 9D                           jmp 0x1406bb895
006BB8F8  49 83 C1 11                     add r9, 0x11
006BB8FC  49 8B F4                        mov rsi, r12
006BB8FF  48 FF CE                        dec rsi
006BB902  48 8D 4E 05                     lea rcx, [rsi + 5]
006BB906  49 3B C9                        cmp rcx, r9
006BB909  0F 84 91 02 00 00               je 0x1406bbba0
006BB90F  0F 87 84 02 00 00               ja 0x1406bbb99
006BB915  49 3B F8                        cmp rdi, r8
006BB918  0F 84 82 02 00 00               je 0x1406bbba0
006BB91E  0F 87 75 02 00 00               ja 0x1406bbb99
006BB924  A8 10                           test al, 0x10
006BB926  75 0A                           jne 0x1406bb932
006BB928  8A 56 05                        mov dl, byte ptr [rsi + 5]
006BB92B  88 17                           mov byte ptr [rdi], dl
006BB92D  48 FF C7                        inc rdi
006BB930  EB 7A                           jmp 0x1406bb9ac
006BB932  48 8D 4E 07                     lea rcx, [rsi + 7]
006BB936  49 3B C9                        cmp rcx, r9
006BB939  0F 87 5A 02 00 00               ja 0x1406bbb99
006BB93F  48 3B FD                        cmp rdi, rbp
006BB942  77 47                           ja 0x1406bb98b
006BB944  48 8D 56 01                     lea rdx, [rsi + 1]
006BB948  4C 8B E2                        mov r12, rdx
006BB94B  33 C9                           xor ecx, ecx
006BB94D  66 8B 4E 05                     mov cx, word ptr [rsi + 5]
006BB951  8B F1                           mov esi, ecx
006BB953  48 8D 15 EA 35 96 FF            lea rdx, [rip - 0x69ca16]
006BB95A  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BB95D  87 D9                           xchg ecx, ebx
006BB95F  D3 EE                           shr esi, cl
006BB961  87 D9                           xchg ecx, ebx
006BB963  48 F7 DE                        neg rsi
006BB966  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BB96B  49 3B F2                        cmp rsi, r10
006BB96E  0F 82 25 02 00 00               jb 0x1406bbb99
006BB974  83 C1 03                        add ecx, 3
006BB977  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BB97B  49 3B D0                        cmp rdx, r8
006BB97E  0F 87 15 02 00 00               ja 0x1406bbb99
006BB984  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BB986  49 8B F4                        mov rsi, r12
006BB989  EB 21                           jmp 0x1406bb9ac
006BB98B  FF CB                           dec ebx
006BB98D  49 8B D2                        mov rdx, r10
006BB990  48 8D 0D 69 35 96 FF            lea rcx, [rip - 0x69ca97]
006BB997  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BB99A  48 03 D1                        add rdx, rcx
006BB99D  48 8B EA                        mov rbp, rdx
006BB9A0  EB 9D                           jmp 0x1406bb93f
006BB9A2  49 83 C1 11                     add r9, 0x11
006BB9A6  49 8B F4                        mov rsi, r12
006BB9A9  48 FF CE                        dec rsi
006BB9AC  48 8D 4E 06                     lea rcx, [rsi + 6]
006BB9B0  49 3B C9                        cmp rcx, r9
006BB9B3  0F 84 E7 01 00 00               je 0x1406bbba0
006BB9B9  0F 87 DA 01 00 00               ja 0x1406bbb99
006BB9BF  49 3B F8                        cmp rdi, r8
006BB9C2  0F 84 D8 01 00 00               je 0x1406bbba0
006BB9C8  0F 87 CB 01 00 00               ja 0x1406bbb99
006BB9CE  A8 20                           test al, 0x20
006BB9D0  75 0A                           jne 0x1406bb9dc
006BB9D2  8A 56 06                        mov dl, byte ptr [rsi + 6]
006BB9D5  88 17                           mov byte ptr [rdi], dl
006BB9D7  48 FF C7                        inc rdi
006BB9DA  EB 7A                           jmp 0x1406bba56
006BB9DC  48 8D 4E 08                     lea rcx, [rsi + 8]
006BB9E0  49 3B C9                        cmp rcx, r9
006BB9E3  0F 87 B0 01 00 00               ja 0x1406bbb99
006BB9E9  48 3B FD                        cmp rdi, rbp
006BB9EC  77 47                           ja 0x1406bba35
006BB9EE  48 8D 56 01                     lea rdx, [rsi + 1]
006BB9F2  4C 8B E2                        mov r12, rdx
006BB9F5  33 C9                           xor ecx, ecx
006BB9F7  66 8B 4E 06                     mov cx, word ptr [rsi + 6]
006BB9FB  8B F1                           mov esi, ecx
006BB9FD  48 8D 15 40 35 96 FF            lea rdx, [rip - 0x69cac0]
006BBA04  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BBA07  87 D9                           xchg ecx, ebx
006BBA09  D3 EE                           shr esi, cl
006BBA0B  87 D9                           xchg ecx, ebx
006BBA0D  48 F7 DE                        neg rsi
006BBA10  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BBA15  49 3B F2                        cmp rsi, r10
006BBA18  0F 82 7B 01 00 00               jb 0x1406bbb99
006BBA1E  83 C1 03                        add ecx, 3
006BBA21  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BBA25  49 3B D0                        cmp rdx, r8
006BBA28  0F 87 6B 01 00 00               ja 0x1406bbb99
006BBA2E  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BBA30  49 8B F4                        mov rsi, r12
006BBA33  EB 21                           jmp 0x1406bba56
006BBA35  FF CB                           dec ebx
006BBA37  49 8B D2                        mov rdx, r10
006BBA3A  48 8D 0D BF 34 96 FF            lea rcx, [rip - 0x69cb41]
006BBA41  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BBA44  48 03 D1                        add rdx, rcx
006BBA47  48 8B EA                        mov rbp, rdx
006BBA4A  EB 9D                           jmp 0x1406bb9e9
006BBA4C  49 83 C1 11                     add r9, 0x11
006BBA50  49 8B F4                        mov rsi, r12
006BBA53  48 FF CE                        dec rsi
006BBA56  48 8D 4E 07                     lea rcx, [rsi + 7]
006BBA5A  49 3B C9                        cmp rcx, r9
006BBA5D  0F 84 3D 01 00 00               je 0x1406bbba0
006BBA63  0F 87 30 01 00 00               ja 0x1406bbb99
006BBA69  49 3B F8                        cmp rdi, r8
006BBA6C  0F 84 2E 01 00 00               je 0x1406bbba0
006BBA72  0F 87 21 01 00 00               ja 0x1406bbb99
006BBA78  A8 40                           test al, 0x40
006BBA7A  75 0A                           jne 0x1406bba86
006BBA7C  8A 56 07                        mov dl, byte ptr [rsi + 7]
006BBA7F  88 17                           mov byte ptr [rdi], dl
006BBA81  48 FF C7                        inc rdi
006BBA84  EB 7A                           jmp 0x1406bbb00
006BBA86  48 8D 4E 09                     lea rcx, [rsi + 9]
006BBA8A  49 3B C9                        cmp rcx, r9
006BBA8D  0F 87 06 01 00 00               ja 0x1406bbb99
006BBA93  48 3B FD                        cmp rdi, rbp
006BBA96  77 47                           ja 0x1406bbadf
006BBA98  48 8D 56 01                     lea rdx, [rsi + 1]
006BBA9C  4C 8B E2                        mov r12, rdx
006BBA9F  33 C9                           xor ecx, ecx
006BBAA1  66 8B 4E 07                     mov cx, word ptr [rsi + 7]
006BBAA5  8B F1                           mov esi, ecx
006BBAA7  48 8D 15 96 34 96 FF            lea rdx, [rip - 0x69cb6a]
006BBAAE  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BBAB1  87 D9                           xchg ecx, ebx
006BBAB3  D3 EE                           shr esi, cl
006BBAB5  87 D9                           xchg ecx, ebx
006BBAB7  48 F7 DE                        neg rsi
006BBABA  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BBABF  49 3B F2                        cmp rsi, r10
006BBAC2  0F 82 D1 00 00 00               jb 0x1406bbb99
006BBAC8  83 C1 03                        add ecx, 3
006BBACB  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BBACF  49 3B D0                        cmp rdx, r8
006BBAD2  0F 87 C1 00 00 00               ja 0x1406bbb99
006BBAD8  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BBADA  49 8B F4                        mov rsi, r12
006BBADD  EB 21                           jmp 0x1406bbb00
006BBADF  FF CB                           dec ebx
006BBAE1  49 8B D2                        mov rdx, r10
006BBAE4  48 8D 0D 15 34 96 FF            lea rcx, [rip - 0x69cbeb]
006BBAEB  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BBAEE  48 03 D1                        add rdx, rcx
006BBAF1  48 8B EA                        mov rbp, rdx
006BBAF4  EB 9D                           jmp 0x1406bba93
006BBAF6  49 83 C1 11                     add r9, 0x11
006BBAFA  49 8B F4                        mov rsi, r12
006BBAFD  48 FF CE                        dec rsi
006BBB00  48 8D 4E 08                     lea rcx, [rsi + 8]
006BBB04  49 3B C9                        cmp rcx, r9
006BBB07  0F 84 93 00 00 00               je 0x1406bbba0
006BBB0D  0F 87 86 00 00 00               ja 0x1406bbb99
006BBB13  49 3B F8                        cmp rdi, r8
006BBB16  0F 84 84 00 00 00               je 0x1406bbba0
006BBB1C  77 7B                           ja 0x1406bbb99
006BBB1E  A8 80                           test al, 0x80
006BBB20  75 0A                           jne 0x1406bbb2c
006BBB22  8A 56 08                        mov dl, byte ptr [rsi + 8]
006BBB25  88 17                           mov byte ptr [rdi], dl
006BBB27  48 FF C7                        inc rdi
006BBB2A  EB 64                           jmp 0x1406bbb90
006BBB2C  48 8D 4E 0A                     lea rcx, [rsi + 0xa]
006BBB30  49 3B C9                        cmp rcx, r9
006BBB33  77 64                           ja 0x1406bbb99
006BBB35  48 3B FD                        cmp rdi, rbp
006BBB38  77 3F                           ja 0x1406bbb79
006BBB3A  48 8D 56 01                     lea rdx, [rsi + 1]
006BBB3E  4C 8B E2                        mov r12, rdx
006BBB41  33 C9                           xor ecx, ecx
006BBB43  66 8B 4E 08                     mov cx, word ptr [rsi + 8]
006BBB47  8B F1                           mov esi, ecx
006BBB49  48 8D 15 F4 33 96 FF            lea rdx, [rip - 0x69cc0c]
006BBB50  23 0C 9A                        and ecx, dword ptr [rdx + rbx*4]
006BBB53  87 D9                           xchg ecx, ebx
006BBB55  D3 EE                           shr esi, cl
006BBB57  87 D9                           xchg ecx, ebx
006BBB59  48 F7 DE                        neg rsi
006BBB5C  48 8D 74 3E FF                  lea rsi, [rsi + rdi - 1]
006BBB61  49 3B F2                        cmp rsi, r10
006BBB64  72 33                           jb 0x1406bbb99
006BBB66  83 C1 03                        add ecx, 3
006BBB69  48 8D 14 0F                     lea rdx, [rdi + rcx]
006BBB6D  49 3B D0                        cmp rdx, r8
006BBB70  77 27                           ja 0x1406bbb99
006BBB72  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
006BBB74  49 8B F4                        mov rsi, r12
006BBB77  EB 17                           jmp 0x1406bbb90
006BBB79  FF CB                           dec ebx
006BBB7B  49 8B D2                        mov rdx, r10
006BBB7E  48 8D 0D 7B 33 96 FF            lea rcx, [rip - 0x69cc85]
006BBB85  8B 0C 99                        mov ecx, dword ptr [rcx + rbx*4]
006BBB88  48 03 D1                        add rdx, rcx
006BBB8B  48 8B EA                        mov rbp, rdx
006BBB8E  EB A5                           jmp 0x1406bbb35
006BBB90  48 83 C6 09                     add rsi, 9
006BBB94  E9 AA FA FF FF                  jmp 0x1406bb643
006BBB99  B8 42 02 00 C0                  mov eax, 0xc0000242
006BBB9E  EB 0F                           jmp 0x1406bbbaf
006BBBA0  48 8B C7                        mov rax, rdi
006BBBA3  49 2B C2                        sub rax, r10
006BBBA6  48 8B 7C 24 50                  mov rdi, qword ptr [rsp + 0x50]
006BBBAB  89 07                           mov dword ptr [rdi], eax
006BBBAD  33 C0                           xor eax, eax
006BBBAF  5E                              pop rsi
006BBBB0  5F                              pop rdi
006BBBB1  5B                              pop rbx
006BBBB2  5D                              pop rbp
006BBBB3  41 5C                           pop r12
006BBBB5  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LZNT1DecompressChunk(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;

    a4 = (a4) - (17);
    a2 = (a2) - (8);
loc_006BB075:
    if (a3 >= a4) goto loc_006BB63F;
    if (a1 >= a2) goto loc_006BB63F;
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (1)) != 0) goto loc_006BB101;
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 1));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (2)) != 0) goto loc_006BB1DC;
    *(unsigned __int8 *)(a1 + 1) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 2));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (4)) != 0) goto loc_006BB2A9;
    *(unsigned __int8 *)(a1 + 2) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 3));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (8)) != 0) goto loc_006BB368;
    *(unsigned __int8 *)(a1 + 3) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 4));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (16)) != 0) goto loc_006BB419;
    *(unsigned __int8 *)(a1 + 4) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 5));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (32)) != 0) goto loc_006BB4B8;
    *(unsigned __int8 *)(a1 + 5) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 6));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (64)) != 0) goto loc_006BB549;
    *(unsigned __int8 *)(a1 + 6) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 7));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (128)) != 0) goto loc_006BB5C9;
    *(unsigned __int8 *)(a1 + 7) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 8));
    v_rsi = (a3) + (9);
    v_rdi = (a1) + (8);
    goto loc_006BB075;
loc_006BB101:
    if (v_rdi > a1) goto loc_006BB1C2;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 1)) & (*(unsigned int *)(v_rip - 6930908 + 13 * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 1)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) >= a2) goto loc_006BB650;
    v_rdi = (v_rdi) - (1);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (2)) != 0) goto loc_006BB1DC;
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 2));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (4)) != 0) goto loc_006BB2A9;
    *(unsigned __int8 *)(v_rdi + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 3));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (8)) != 0) goto loc_006BB368;
    *(unsigned __int8 *)(v_rdi + 3) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 4));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (16)) != 0) goto loc_006BB419;
    *(unsigned __int8 *)(v_rdi + 4) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 5));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (32)) != 0) goto loc_006BB4B8;
    *(unsigned __int8 *)(v_rdi + 5) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 6));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (64)) != 0) goto loc_006BB549;
    *(unsigned __int8 *)(v_rdi + 6) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 7));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (128)) != 0) goto loc_006BB5C9;
    *(unsigned __int8 *)(v_rdi + 7) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 8));
    v_rsi = (v_rsi + 1) + (9);
    v_rdi = (v_rdi) + (8);
    goto loc_006BB075;
loc_006BB1C2:
    v_rbx = (unsigned int)((13) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6931150 + v_rbx * 4)));
    goto loc_006BB101;
loc_006BB1DC:
    v_rdi = (v_rdi) + (1);
loc_006BB1E0:
    if (v_rdi > a2) goto loc_006BB28F;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 2)) & (*(unsigned int *)(v_rip - 6931131 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 2)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) >= a2) goto loc_006BB6FA;
    v_rdi = (v_rdi) - (2);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (4)) != 0) goto loc_006BB2A9;
    *(unsigned __int8 *)(v_rdi + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 3));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (8)) != 0) goto loc_006BB368;
    *(unsigned __int8 *)(v_rdi + 3) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 4));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (16)) != 0) goto loc_006BB419;
    *(unsigned __int8 *)(v_rdi + 4) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 5));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (32)) != 0) goto loc_006BB4B8;
    *(unsigned __int8 *)(v_rdi + 5) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 6));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (64)) != 0) goto loc_006BB549;
    *(unsigned __int8 *)(v_rdi + 6) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 7));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (128)) != 0) goto loc_006BB5C9;
    *(unsigned __int8 *)(v_rdi + 7) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 8));
    v_rsi = (v_rsi + 1) + (9);
    v_rdi = (v_rdi) + (8);
    goto loc_006BB075;
loc_006BB28F:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6931355 + v_rbx * 4)));
    goto loc_006BB1E0;
loc_006BB2A9:
    v_rdi = (v_rdi) + (2);
loc_006BB2AD:
    if (v_rdi > a2) goto loc_006BB34E;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 3)) & (*(unsigned int *)(v_rip - 6931336 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 3)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) >= a2) goto loc_006BB7A4;
    v_rdi = (v_rdi) - (3);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (8)) != 0) goto loc_006BB368;
    *(unsigned __int8 *)(v_rdi + 3) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 4));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (16)) != 0) goto loc_006BB419;
    *(unsigned __int8 *)(v_rdi + 4) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 5));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (32)) != 0) goto loc_006BB4B8;
    *(unsigned __int8 *)(v_rdi + 5) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 6));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (64)) != 0) goto loc_006BB549;
    *(unsigned __int8 *)(v_rdi + 6) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 7));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (128)) != 0) goto loc_006BB5C9;
    *(unsigned __int8 *)(v_rdi + 7) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 8));
    v_rsi = (v_rsi + 1) + (9);
    v_rdi = (v_rdi) + (8);
    goto loc_006BB075;
loc_006BB34E:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6931546 + v_rbx * 4)));
    goto loc_006BB2AD;
loc_006BB368:
    v_rdi = (v_rdi) + (3);
loc_006BB36C:
    if (v_rdi > a2) goto loc_006BB3FF;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 4)) & (*(unsigned int *)(v_rip - 6931527 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 4)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) >= a2) goto loc_006BB84E;
    v_rdi = (v_rdi) - (4);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (16)) != 0) goto loc_006BB419;
    *(unsigned __int8 *)(v_rdi + 4) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 5));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (32)) != 0) goto loc_006BB4B8;
    *(unsigned __int8 *)(v_rdi + 5) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 6));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (64)) != 0) goto loc_006BB549;
    *(unsigned __int8 *)(v_rdi + 6) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 7));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (128)) != 0) goto loc_006BB5C9;
    *(unsigned __int8 *)(v_rdi + 7) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 8));
    v_rsi = (v_rsi + 1) + (9);
    v_rdi = (v_rdi) + (8);
    goto loc_006BB075;
loc_006BB3FF:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6931723 + v_rbx * 4)));
    goto loc_006BB36C;
loc_006BB419:
    v_rdi = (v_rdi) + (4);
loc_006BB41D:
    if (v_rdi > a2) goto loc_006BB49E;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 5)) & (*(unsigned int *)(v_rip - 6931700 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 5)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) >= a2) goto loc_006BB8F8;
    v_rdi = (v_rdi) - (5);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (32)) != 0) goto loc_006BB4B8;
    *(unsigned __int8 *)(v_rdi + 5) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 6));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (64)) != 0) goto loc_006BB549;
    *(unsigned __int8 *)(v_rdi + 6) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 7));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (128)) != 0) goto loc_006BB5C9;
    *(unsigned __int8 *)(v_rdi + 7) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 8));
    v_rsi = (v_rsi + 1) + (9);
    v_rdi = (v_rdi) + (8);
    goto loc_006BB075;
loc_006BB49E:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6931882 + v_rbx * 4)));
    goto loc_006BB41D;
loc_006BB4B8:
    v_rdi = (v_rdi) + (5);
loc_006BB4BC:
    if (v_rdi > a2) goto loc_006BB52F;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 6)) & (*(unsigned int *)(v_rip - 6931859 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 6)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) >= a2) goto loc_006BB9A2;
    v_rdi = (v_rdi) - (6);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (64)) != 0) goto loc_006BB549;
    *(unsigned __int8 *)(v_rdi + 6) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 7));
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (128)) != 0) goto loc_006BB5C9;
    *(unsigned __int8 *)(v_rdi + 7) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 8));
    v_rsi = (v_rsi + 1) + (9);
    v_rdi = (v_rdi) + (8);
    goto loc_006BB075;
loc_006BB52F:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6932027 + v_rbx * 4)));
    goto loc_006BB4BC;
loc_006BB549:
    v_rdi = (v_rdi) + (6);
loc_006BB54D:
    if (v_rdi > a2) goto loc_006BB5B2;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 7)) & (*(unsigned int *)(v_rip - 6932004 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 7)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) >= a2) goto loc_006BBA4C;
    v_rdi = (v_rdi) - (7);
    if ((((unsigned __int8)(*(unsigned __int8 *)(a3))) & (128)) != 0) goto loc_006BB5C9;
    *(unsigned __int8 *)(v_rdi + 7) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1 + 8));
    v_rsi = (v_rsi + 1) + (9);
    v_rdi = (v_rdi) + (8);
    goto loc_006BB075;
loc_006BB5B2:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6932158 + v_rbx * 4)));
    goto loc_006BB54D;
loc_006BB5C9:
    v_rdi = (v_rdi) + (7);
loc_006BB5CD:
    if (v_rdi > a2) goto loc_006BB628;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 8)) & (*(unsigned int *)(v_rip - 6932132 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 8)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) >= a2) goto loc_006BBAF6;
    v_rdi = (v_rdi) - (8);
    v_rsi = (v_rsi + 1) + (9);
    v_rdi = (v_rdi) + (8);
    goto loc_006BB075;
loc_006BB628:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6932276 + v_rbx * 4)));
    goto loc_006BB5CD;
loc_006BB63F:
    a4 = (a4) + (17);
loc_006BB643:
    if (v_rsi == a4) goto loc_006BBBA0;
    goto loc_006BB65A;
loc_006BB650:
    a4 = (a4) + (17);
    v_rsi = (v_rsi + 1) - 1;
loc_006BB65A:
    if ((v_rsi + 1) == a4) goto loc_006BBBA0;
    if ((v_rsi + 1) > a4) goto loc_006BBB99;
    if (v_rdi == a2) goto loc_006BBBA0;
    if (v_rdi > a2) goto loc_006BBB99;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi))) & (1)) != 0) goto loc_006BB68A;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 1));
    v_rdi = (v_rdi) + 1;
    goto loc_006BB704;
loc_006BB68A:
    if ((v_rsi + 3) > a4) goto loc_006BBB99;
loc_006BB697:
    if (v_rdi > a2) goto loc_006BB6E3;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 1)) & (*(unsigned int *)(v_rip - 6932334 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 1)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) > a2) goto loc_006BBB99;
    goto loc_006BB704;
loc_006BB6E3:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6932463 + v_rbx * 4)));
    goto loc_006BB697;
loc_006BB6FA:
    a4 = (a4) + (17);
    v_rsi = (v_rsi + 1) - 1;
loc_006BB704:
    if ((v_rsi + 2) == a4) goto loc_006BBBA0;
    if ((v_rsi + 2) > a4) goto loc_006BBB99;
    if (v_rdi == a2) goto loc_006BBBA0;
    if (v_rdi > a2) goto loc_006BBB99;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi))) & (2)) != 0) goto loc_006BB734;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 2));
    v_rdi = (v_rdi) + 1;
    goto loc_006BB7AE;
loc_006BB734:
    if ((v_rsi + 4) > a4) goto loc_006BBB99;
loc_006BB741:
    if (v_rdi > a2) goto loc_006BB78D;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 2)) & (*(unsigned int *)(v_rip - 6932504 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 2)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) > a2) goto loc_006BBB99;
    goto loc_006BB7AE;
loc_006BB78D:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6932633 + v_rbx * 4)));
    goto loc_006BB741;
loc_006BB7A4:
    a4 = (a4) + (17);
    v_rsi = (v_rsi + 1) - 1;
loc_006BB7AE:
    if ((v_rsi + 3) == a4) goto loc_006BBBA0;
    if ((v_rsi + 3) > a4) goto loc_006BBB99;
    if (v_rdi == a2) goto loc_006BBBA0;
    if (v_rdi > a2) goto loc_006BBB99;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi))) & (4)) != 0) goto loc_006BB7DE;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 3));
    v_rdi = (v_rdi) + 1;
    goto loc_006BB858;
loc_006BB7DE:
    if ((v_rsi + 5) > a4) goto loc_006BBB99;
loc_006BB7EB:
    if (v_rdi > a2) goto loc_006BB837;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 3)) & (*(unsigned int *)(v_rip - 6932674 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 3)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) > a2) goto loc_006BBB99;
    goto loc_006BB858;
loc_006BB837:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6932803 + v_rbx * 4)));
    goto loc_006BB7EB;
loc_006BB84E:
    a4 = (a4) + (17);
    v_rsi = (v_rsi + 1) - 1;
loc_006BB858:
    if ((v_rsi + 4) == a4) goto loc_006BBBA0;
    if ((v_rsi + 4) > a4) goto loc_006BBB99;
    if (v_rdi == a2) goto loc_006BBBA0;
    if (v_rdi > a2) goto loc_006BBB99;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi))) & (8)) != 0) goto loc_006BB888;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 4));
    v_rdi = (v_rdi) + 1;
    goto loc_006BB902;
loc_006BB888:
    if ((v_rsi + 6) > a4) goto loc_006BBB99;
loc_006BB895:
    if (v_rdi > a2) goto loc_006BB8E1;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 4)) & (*(unsigned int *)(v_rip - 6932844 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 4)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) > a2) goto loc_006BBB99;
    goto loc_006BB902;
loc_006BB8E1:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6932973 + v_rbx * 4)));
    goto loc_006BB895;
loc_006BB8F8:
    a4 = (a4) + (17);
    v_rsi = (v_rsi + 1) - 1;
loc_006BB902:
    if ((v_rsi + 5) == a4) goto loc_006BBBA0;
    if ((v_rsi + 5) > a4) goto loc_006BBB99;
    if (v_rdi == a2) goto loc_006BBBA0;
    if (v_rdi > a2) goto loc_006BBB99;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi))) & (16)) != 0) goto loc_006BB932;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 5));
    v_rdi = (v_rdi) + 1;
    goto loc_006BB9AC;
loc_006BB932:
    if ((v_rsi + 7) > a4) goto loc_006BBB99;
loc_006BB93F:
    if (v_rdi > a2) goto loc_006BB98B;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 5)) & (*(unsigned int *)(v_rip - 6933014 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 5)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) > a2) goto loc_006BBB99;
    goto loc_006BB9AC;
loc_006BB98B:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6933143 + v_rbx * 4)));
    goto loc_006BB93F;
loc_006BB9A2:
    a4 = (a4) + (17);
    v_rsi = (v_rsi + 1) - 1;
loc_006BB9AC:
    if ((v_rsi + 6) == a4) goto loc_006BBBA0;
    if ((v_rsi + 6) > a4) goto loc_006BBB99;
    if (v_rdi == a2) goto loc_006BBBA0;
    if (v_rdi > a2) goto loc_006BBB99;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi))) & (32)) != 0) goto loc_006BB9DC;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 6));
    v_rdi = (v_rdi) + 1;
    goto loc_006BBA56;
loc_006BB9DC:
    if ((v_rsi + 8) > a4) goto loc_006BBB99;
loc_006BB9E9:
    if (v_rdi > a2) goto loc_006BBA35;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 6)) & (*(unsigned int *)(v_rip - 6933184 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 6)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) > a2) goto loc_006BBB99;
    goto loc_006BBA56;
loc_006BBA35:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6933313 + v_rbx * 4)));
    goto loc_006BB9E9;
loc_006BBA4C:
    a4 = (a4) + (17);
    v_rsi = (v_rsi + 1) - 1;
loc_006BBA56:
    if ((v_rsi + 7) == a4) goto loc_006BBBA0;
    if ((v_rsi + 7) > a4) goto loc_006BBB99;
    if (v_rdi == a2) goto loc_006BBBA0;
    if (v_rdi > a2) goto loc_006BBB99;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi))) & (64)) != 0) goto loc_006BBA86;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 7));
    v_rdi = (v_rdi) + 1;
    goto loc_006BBB00;
loc_006BBA86:
    if ((v_rsi + 9) > a4) goto loc_006BBB99;
loc_006BBA93:
    if (v_rdi > a2) goto loc_006BBADF;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 7)) & (*(unsigned int *)(v_rip - 6933354 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 7)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) > a2) goto loc_006BBB99;
    goto loc_006BBB00;
loc_006BBADF:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6933483 + v_rbx * 4)));
    goto loc_006BBA93;
loc_006BBAF6:
    a4 = (a4) + (17);
    v_rsi = (v_rsi + 1) - 1;
loc_006BBB00:
    if ((v_rsi + 8) == a4) goto loc_006BBBA0;
    if ((v_rsi + 8) > a4) goto loc_006BBB99;
    if (v_rdi == a2) goto loc_006BBBA0;
    if (v_rdi > a2) goto loc_006BBB99;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_rsi))) & (128)) != 0) goto loc_006BBB2C;
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsi + 8));
    v_rdi = (v_rdi) + 1;
    goto loc_006BBB90;
loc_006BBB2C:
    if ((v_rsi + 10) > a4) goto loc_006BBB99;
loc_006BBB35:
    if (v_rdi > a2) goto loc_006BBB79;
    a1 = 0;
    a1 = (unsigned int)((*(unsigned __int16 *)(v_rsi + 8)) & (*(unsigned int *)(v_rip - 6933516 + v_rbx * 4)));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rsi + 8)))) >> ((unsigned __int8)(a1)));
    v_rsi = -(v_rsi);
    if ((v_rsi + v_rdi * 1 - 1) < a1) goto loc_006BBB99;
    a1 = (unsigned int)((a1) + (3));
    if ((v_rdi + a1 * 1) > a2) goto loc_006BBB99;
    goto loc_006BBB90;
loc_006BBB79:
    v_rbx = (unsigned int)((v_rbx) - 1);
    a2 = (a1) + ((unsigned int)(*(unsigned int *)(v_rip - 6933637 + v_rbx * 4)));
    goto loc_006BBB35;
loc_006BBB90:
    v_rsi = (v_rsi + 1) + (9);
    goto loc_006BB643;
loc_006BBB99:
    goto loc_006BBBAF;
loc_006BBBA0:
    result = (v_rdi) - (a1);
    *(unsigned int *)(a5) = (unsigned int)(result);
    result = 0;
loc_006BBBAF:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t LZNT1DecompressChunk(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;

    Arg4 = (Arg4) - (17);
    Arg2 = (Arg2) - (8);
loc_006BB075:
    if (Arg3 >= Arg4) goto loc_006BB63F;
    if (Arg1 >= Arg2) goto loc_006BB63F;
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (1)) != 0) goto loc_006BB101;
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(Arg3 + 0x1));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (2)) != 0) goto loc_006BB1DC;
    *(uint8_t *)(Arg1 + 0x1) = (uint8_t)(*(uint8_t *)(Arg3 + 0x2));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (4)) != 0) goto loc_006BB2A9;
    *(uint8_t *)(Arg1 + 0x2) = (uint8_t)(*(uint8_t *)(Arg3 + 0x3));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (8)) != 0) goto loc_006BB368;
    *(uint8_t *)(Arg1 + 0x3) = (uint8_t)(*(uint8_t *)(Arg3 + 0x4));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (16)) != 0) goto loc_006BB419;
    *(uint8_t *)(Arg1 + 0x4) = (uint8_t)(*(uint8_t *)(Arg3 + 0x5));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (32)) != 0) goto loc_006BB4B8;
    *(uint8_t *)(Arg1 + 0x5) = (uint8_t)(*(uint8_t *)(Arg3 + 0x6));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (64)) != 0) goto loc_006BB549;
    *(uint8_t *)(Arg1 + 0x6) = (uint8_t)(*(uint8_t *)(Arg3 + 0x7));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (128)) != 0) goto loc_006BB5C9;
    *(uint8_t *)(Arg1 + 0x7) = (uint8_t)(*(uint8_t *)(Arg3 + 0x8));
    local_rsi = (Arg3) + (9);
    local_rdi = (Arg1) + (8);
    goto loc_006BB075;
loc_006BB101:
    if (local_rdi > Arg1) goto loc_006BB1C2;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x1)) & (*(uint32_t *)(v_rip - 0x69C1DC + 0xD * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x1)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) >= Arg2) goto loc_006BB650;
    local_rdi = (local_rdi) - (1);
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (2)) != 0) goto loc_006BB1DC;
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x2));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (4)) != 0) goto loc_006BB2A9;
    *(uint8_t *)(local_rdi + 0x2) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x3));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (8)) != 0) goto loc_006BB368;
    *(uint8_t *)(local_rdi + 0x3) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x4));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (16)) != 0) goto loc_006BB419;
    *(uint8_t *)(local_rdi + 0x4) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x5));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (32)) != 0) goto loc_006BB4B8;
    *(uint8_t *)(local_rdi + 0x5) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x6));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (64)) != 0) goto loc_006BB549;
    *(uint8_t *)(local_rdi + 0x6) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x7));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (128)) != 0) goto loc_006BB5C9;
    *(uint8_t *)(local_rdi + 0x7) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x8));
    local_rsi = (local_rsi + 1) + (9);
    local_rdi = (local_rdi) + (8);
    goto loc_006BB075;
loc_006BB1C2:
    local_rbx = (uint32_t)((13) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C2CE + local_rbx * 4)));
    goto loc_006BB101;
loc_006BB1DC:
    local_rdi = (local_rdi) + (1);
loc_006BB1E0:
    if (local_rdi > Arg2) goto loc_006BB28F;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x2)) & (*(uint32_t *)(v_rip - 0x69C2BB + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x2)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) >= Arg2) goto loc_006BB6FA;
    local_rdi = (local_rdi) - (2);
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (4)) != 0) goto loc_006BB2A9;
    *(uint8_t *)(local_rdi + 0x2) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x3));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (8)) != 0) goto loc_006BB368;
    *(uint8_t *)(local_rdi + 0x3) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x4));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (16)) != 0) goto loc_006BB419;
    *(uint8_t *)(local_rdi + 0x4) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x5));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (32)) != 0) goto loc_006BB4B8;
    *(uint8_t *)(local_rdi + 0x5) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x6));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (64)) != 0) goto loc_006BB549;
    *(uint8_t *)(local_rdi + 0x6) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x7));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (128)) != 0) goto loc_006BB5C9;
    *(uint8_t *)(local_rdi + 0x7) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x8));
    local_rsi = (local_rsi + 1) + (9);
    local_rdi = (local_rdi) + (8);
    goto loc_006BB075;
loc_006BB28F:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C39B + local_rbx * 4)));
    goto loc_006BB1E0;
loc_006BB2A9:
    local_rdi = (local_rdi) + (2);
loc_006BB2AD:
    if (local_rdi > Arg2) goto loc_006BB34E;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x3)) & (*(uint32_t *)(v_rip - 0x69C388 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x3)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) >= Arg2) goto loc_006BB7A4;
    local_rdi = (local_rdi) - (3);
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (8)) != 0) goto loc_006BB368;
    *(uint8_t *)(local_rdi + 0x3) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x4));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (16)) != 0) goto loc_006BB419;
    *(uint8_t *)(local_rdi + 0x4) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x5));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (32)) != 0) goto loc_006BB4B8;
    *(uint8_t *)(local_rdi + 0x5) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x6));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (64)) != 0) goto loc_006BB549;
    *(uint8_t *)(local_rdi + 0x6) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x7));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (128)) != 0) goto loc_006BB5C9;
    *(uint8_t *)(local_rdi + 0x7) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x8));
    local_rsi = (local_rsi + 1) + (9);
    local_rdi = (local_rdi) + (8);
    goto loc_006BB075;
loc_006BB34E:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C45A + local_rbx * 4)));
    goto loc_006BB2AD;
loc_006BB368:
    local_rdi = (local_rdi) + (3);
loc_006BB36C:
    if (local_rdi > Arg2) goto loc_006BB3FF;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x4)) & (*(uint32_t *)(v_rip - 0x69C447 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x4)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) >= Arg2) goto loc_006BB84E;
    local_rdi = (local_rdi) - (4);
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (16)) != 0) goto loc_006BB419;
    *(uint8_t *)(local_rdi + 0x4) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x5));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (32)) != 0) goto loc_006BB4B8;
    *(uint8_t *)(local_rdi + 0x5) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x6));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (64)) != 0) goto loc_006BB549;
    *(uint8_t *)(local_rdi + 0x6) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x7));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (128)) != 0) goto loc_006BB5C9;
    *(uint8_t *)(local_rdi + 0x7) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x8));
    local_rsi = (local_rsi + 1) + (9);
    local_rdi = (local_rdi) + (8);
    goto loc_006BB075;
loc_006BB3FF:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C50B + local_rbx * 4)));
    goto loc_006BB36C;
loc_006BB419:
    local_rdi = (local_rdi) + (4);
loc_006BB41D:
    if (local_rdi > Arg2) goto loc_006BB49E;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x5)) & (*(uint32_t *)(v_rip - 0x69C4F4 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x5)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) >= Arg2) goto loc_006BB8F8;
    local_rdi = (local_rdi) - (5);
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (32)) != 0) goto loc_006BB4B8;
    *(uint8_t *)(local_rdi + 0x5) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x6));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (64)) != 0) goto loc_006BB549;
    *(uint8_t *)(local_rdi + 0x6) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x7));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (128)) != 0) goto loc_006BB5C9;
    *(uint8_t *)(local_rdi + 0x7) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x8));
    local_rsi = (local_rsi + 1) + (9);
    local_rdi = (local_rdi) + (8);
    goto loc_006BB075;
loc_006BB49E:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C5AA + local_rbx * 4)));
    goto loc_006BB41D;
loc_006BB4B8:
    local_rdi = (local_rdi) + (5);
loc_006BB4BC:
    if (local_rdi > Arg2) goto loc_006BB52F;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x6)) & (*(uint32_t *)(v_rip - 0x69C593 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x6)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) >= Arg2) goto loc_006BB9A2;
    local_rdi = (local_rdi) - (6);
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (64)) != 0) goto loc_006BB549;
    *(uint8_t *)(local_rdi + 0x6) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x7));
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (128)) != 0) goto loc_006BB5C9;
    *(uint8_t *)(local_rdi + 0x7) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x8));
    local_rsi = (local_rsi + 1) + (9);
    local_rdi = (local_rdi) + (8);
    goto loc_006BB075;
loc_006BB52F:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C63B + local_rbx * 4)));
    goto loc_006BB4BC;
loc_006BB549:
    local_rdi = (local_rdi) + (6);
loc_006BB54D:
    if (local_rdi > Arg2) goto loc_006BB5B2;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x7)) & (*(uint32_t *)(v_rip - 0x69C624 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x7)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) >= Arg2) goto loc_006BBA4C;
    local_rdi = (local_rdi) - (7);
    if ((((uint8_t)(*(uint8_t *)(Arg3))) & (128)) != 0) goto loc_006BB5C9;
    *(uint8_t *)(local_rdi + 0x7) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1 + 0x8));
    local_rsi = (local_rsi + 1) + (9);
    local_rdi = (local_rdi) + (8);
    goto loc_006BB075;
loc_006BB5B2:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C6BE + local_rbx * 4)));
    goto loc_006BB54D;
loc_006BB5C9:
    local_rdi = (local_rdi) + (7);
loc_006BB5CD:
    if (local_rdi > Arg2) goto loc_006BB628;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x8)) & (*(uint32_t *)(v_rip - 0x69C6A4 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x8)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) >= Arg2) goto loc_006BBAF6;
    local_rdi = (local_rdi) - (8);
    local_rsi = (local_rsi + 1) + (9);
    local_rdi = (local_rdi) + (8);
    goto loc_006BB075;
loc_006BB628:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C734 + local_rbx * 4)));
    goto loc_006BB5CD;
loc_006BB63F:
    Arg4 = (Arg4) + (17);
loc_006BB643:
    if (local_rsi == Arg4) goto loc_006BBBA0;
    goto loc_006BB65A;
loc_006BB650:
    Arg4 = (Arg4) + (17);
    local_rsi = (local_rsi + 1) - 1;
loc_006BB65A:
    if ((local_rsi + 1) == Arg4) goto loc_006BBBA0;
    if ((local_rsi + 1) > Arg4) goto loc_006BBB99;
    if (local_rdi == Arg2) goto loc_006BBBA0;
    if (local_rdi > Arg2) goto loc_006BBB99;
    if ((((uint8_t)(*(uint8_t *)(local_rsi))) & (1)) != 0) goto loc_006BB68A;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi + 0x1));
    local_rdi = (local_rdi) + 1;
    goto loc_006BB704;
loc_006BB68A:
    if ((local_rsi + 3) > Arg4) goto loc_006BBB99;
loc_006BB697:
    if (local_rdi > Arg2) goto loc_006BB6E3;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x1)) & (*(uint32_t *)(v_rip - 0x69C76E + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x1)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) > Arg2) goto loc_006BBB99;
    goto loc_006BB704;
loc_006BB6E3:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C7EF + local_rbx * 4)));
    goto loc_006BB697;
loc_006BB6FA:
    Arg4 = (Arg4) + (17);
    local_rsi = (local_rsi + 1) - 1;
loc_006BB704:
    if ((local_rsi + 2) == Arg4) goto loc_006BBBA0;
    if ((local_rsi + 2) > Arg4) goto loc_006BBB99;
    if (local_rdi == Arg2) goto loc_006BBBA0;
    if (local_rdi > Arg2) goto loc_006BBB99;
    if ((((uint8_t)(*(uint8_t *)(local_rsi))) & (2)) != 0) goto loc_006BB734;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi + 0x2));
    local_rdi = (local_rdi) + 1;
    goto loc_006BB7AE;
loc_006BB734:
    if ((local_rsi + 4) > Arg4) goto loc_006BBB99;
loc_006BB741:
    if (local_rdi > Arg2) goto loc_006BB78D;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x2)) & (*(uint32_t *)(v_rip - 0x69C818 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x2)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) > Arg2) goto loc_006BBB99;
    goto loc_006BB7AE;
loc_006BB78D:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C899 + local_rbx * 4)));
    goto loc_006BB741;
loc_006BB7A4:
    Arg4 = (Arg4) + (17);
    local_rsi = (local_rsi + 1) - 1;
loc_006BB7AE:
    if ((local_rsi + 3) == Arg4) goto loc_006BBBA0;
    if ((local_rsi + 3) > Arg4) goto loc_006BBB99;
    if (local_rdi == Arg2) goto loc_006BBBA0;
    if (local_rdi > Arg2) goto loc_006BBB99;
    if ((((uint8_t)(*(uint8_t *)(local_rsi))) & (4)) != 0) goto loc_006BB7DE;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi + 0x3));
    local_rdi = (local_rdi) + 1;
    goto loc_006BB858;
loc_006BB7DE:
    if ((local_rsi + 5) > Arg4) goto loc_006BBB99;
loc_006BB7EB:
    if (local_rdi > Arg2) goto loc_006BB837;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x3)) & (*(uint32_t *)(v_rip - 0x69C8C2 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x3)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) > Arg2) goto loc_006BBB99;
    goto loc_006BB858;
loc_006BB837:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C943 + local_rbx * 4)));
    goto loc_006BB7EB;
loc_006BB84E:
    Arg4 = (Arg4) + (17);
    local_rsi = (local_rsi + 1) - 1;
loc_006BB858:
    if ((local_rsi + 4) == Arg4) goto loc_006BBBA0;
    if ((local_rsi + 4) > Arg4) goto loc_006BBB99;
    if (local_rdi == Arg2) goto loc_006BBBA0;
    if (local_rdi > Arg2) goto loc_006BBB99;
    if ((((uint8_t)(*(uint8_t *)(local_rsi))) & (8)) != 0) goto loc_006BB888;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi + 0x4));
    local_rdi = (local_rdi) + 1;
    goto loc_006BB902;
loc_006BB888:
    if ((local_rsi + 6) > Arg4) goto loc_006BBB99;
loc_006BB895:
    if (local_rdi > Arg2) goto loc_006BB8E1;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x4)) & (*(uint32_t *)(v_rip - 0x69C96C + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x4)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) > Arg2) goto loc_006BBB99;
    goto loc_006BB902;
loc_006BB8E1:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69C9ED + local_rbx * 4)));
    goto loc_006BB895;
loc_006BB8F8:
    Arg4 = (Arg4) + (17);
    local_rsi = (local_rsi + 1) - 1;
loc_006BB902:
    if ((local_rsi + 5) == Arg4) goto loc_006BBBA0;
    if ((local_rsi + 5) > Arg4) goto loc_006BBB99;
    if (local_rdi == Arg2) goto loc_006BBBA0;
    if (local_rdi > Arg2) goto loc_006BBB99;
    if ((((uint8_t)(*(uint8_t *)(local_rsi))) & (16)) != 0) goto loc_006BB932;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi + 0x5));
    local_rdi = (local_rdi) + 1;
    goto loc_006BB9AC;
loc_006BB932:
    if ((local_rsi + 7) > Arg4) goto loc_006BBB99;
loc_006BB93F:
    if (local_rdi > Arg2) goto loc_006BB98B;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x5)) & (*(uint32_t *)(v_rip - 0x69CA16 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x5)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) > Arg2) goto loc_006BBB99;
    goto loc_006BB9AC;
loc_006BB98B:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69CA97 + local_rbx * 4)));
    goto loc_006BB93F;
loc_006BB9A2:
    Arg4 = (Arg4) + (17);
    local_rsi = (local_rsi + 1) - 1;
loc_006BB9AC:
    if ((local_rsi + 6) == Arg4) goto loc_006BBBA0;
    if ((local_rsi + 6) > Arg4) goto loc_006BBB99;
    if (local_rdi == Arg2) goto loc_006BBBA0;
    if (local_rdi > Arg2) goto loc_006BBB99;
    if ((((uint8_t)(*(uint8_t *)(local_rsi))) & (32)) != 0) goto loc_006BB9DC;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi + 0x6));
    local_rdi = (local_rdi) + 1;
    goto loc_006BBA56;
loc_006BB9DC:
    if ((local_rsi + 8) > Arg4) goto loc_006BBB99;
loc_006BB9E9:
    if (local_rdi > Arg2) goto loc_006BBA35;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x6)) & (*(uint32_t *)(v_rip - 0x69CAC0 + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x6)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) > Arg2) goto loc_006BBB99;
    goto loc_006BBA56;
loc_006BBA35:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69CB41 + local_rbx * 4)));
    goto loc_006BB9E9;
loc_006BBA4C:
    Arg4 = (Arg4) + (17);
    local_rsi = (local_rsi + 1) - 1;
loc_006BBA56:
    if ((local_rsi + 7) == Arg4) goto loc_006BBBA0;
    if ((local_rsi + 7) > Arg4) goto loc_006BBB99;
    if (local_rdi == Arg2) goto loc_006BBBA0;
    if (local_rdi > Arg2) goto loc_006BBB99;
    if ((((uint8_t)(*(uint8_t *)(local_rsi))) & (64)) != 0) goto loc_006BBA86;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi + 0x7));
    local_rdi = (local_rdi) + 1;
    goto loc_006BBB00;
loc_006BBA86:
    if ((local_rsi + 9) > Arg4) goto loc_006BBB99;
loc_006BBA93:
    if (local_rdi > Arg2) goto loc_006BBADF;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x7)) & (*(uint32_t *)(v_rip - 0x69CB6A + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x7)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) > Arg2) goto loc_006BBB99;
    goto loc_006BBB00;
loc_006BBADF:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69CBEB + local_rbx * 4)));
    goto loc_006BBA93;
loc_006BBAF6:
    Arg4 = (Arg4) + (17);
    local_rsi = (local_rsi + 1) - 1;
loc_006BBB00:
    if ((local_rsi + 8) == Arg4) goto loc_006BBBA0;
    if ((local_rsi + 8) > Arg4) goto loc_006BBB99;
    if (local_rdi == Arg2) goto loc_006BBBA0;
    if (local_rdi > Arg2) goto loc_006BBB99;
    if ((((uint8_t)(*(uint8_t *)(local_rsi))) & (128)) != 0) goto loc_006BBB2C;
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(local_rsi + 0x8));
    local_rdi = (local_rdi) + 1;
    goto loc_006BBB90;
loc_006BBB2C:
    if ((local_rsi + 10) > Arg4) goto loc_006BBB99;
loc_006BBB35:
    if (local_rdi > Arg2) goto loc_006BBB79;
    Arg1 = 0;
    Arg1 = (uint32_t)((*(uint16_t *)(local_rsi + 0x8)) & (*(uint32_t *)(v_rip - 0x69CC0C + local_rbx * 4)));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_rsi + 0x8)))) >> ((uint8_t)(Arg1)));
    local_rsi = -(local_rsi);
    if ((local_rsi + local_rdi * 1 - 1) < Arg1) goto loc_006BBB99;
    Arg1 = (uint32_t)((Arg1) + (3));
    if ((local_rdi + Arg1 * 1) > Arg2) goto loc_006BBB99;
    goto loc_006BBB90;
loc_006BBB79:
    local_rbx = (uint32_t)((local_rbx) - 1);
    Arg2 = (Arg1) + ((uint32_t)(*(uint32_t *)(v_rip - 0x69CC85 + local_rbx * 4)));
    goto loc_006BBB35;
loc_006BBB90:
    local_rsi = (local_rsi + 1) + (9);
    goto loc_006BB643;
loc_006BBB99:
    goto loc_006BBBAF;
loc_006BBBA0:
    result = (local_rdi) - (Arg1);
    *(uint32_t *)(arg5) = (uint32_t)(result);
    result = 0;
loc_006BBBAF:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006BB050&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
