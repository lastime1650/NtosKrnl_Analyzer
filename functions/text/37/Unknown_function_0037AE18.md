# sub_0037AE18

- RVA: `0x0037AE18`–`0x0037B34E` (길이 `1,334` bytes)
- VA: `0x000000014037AE18`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007B0D8`
- 디코드: `297`개 명령, `1,334/1,334` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **14**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x0037AF31` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0037AFED` → [HalpTimerScaleCounter](HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x0037B028` → [HalpTimerScaleCounter](HalpTimerScaleCounter_function_0037B354.md) (function, `0x0037B354`)
- `0x0037B04D` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0037B062` → [HalpHpetQueryCounter](HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x0037B17F` → [HvlpGetRegister64](HvlpGetRegister64_function_00379050.md) (function, `0x00379050`)
- `0x0037B1CB` → [HalpTimerGetInternalData](../20/HalpTimerGetInternalData_function_00209500.md) (function, `0x00209500`)
- `0x0037B1E0` → [HalpHpetQueryCounter](HalpHpetQueryCounter_function_00379660.md) (function, `0x00379660`)
- `0x0037B2E6` → [HvlpGetRegister64](HvlpGetRegister64_function_00379050.md) (function, `0x00379050`)
- `0x0037B306` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0037B312` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0037B31F` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0037B335` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0037B341` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0037AE20` → RVA `0x0041FD10` (`HalpTscQueryCounterOrdered`; read)
- `0x0037AE31` → RVA `0x002DDBC0` (`HvlGetReferenceTimeUsingTscPage`; read)
- `0x0037AE69` → RVA `0x00378F50` (`HalpHvCounterQueryCounter`; read)
- `0x0037AE79` → RVA `0x00E11760` (`.data`; read)
- `0x0037AE9B` → RVA `0x00FC6D88` (`ALMOSTRO`; read)
- `0x0037B035` → RVA `0x00379660` (`HalpHpetQueryCounter`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **7**
  - `0x0037AE38` → [sub_0037AC2F + 0x68](Unknown_function_0037AC2F.md) (`tail-transfer`)
  - `0x0037AF1C` → [sub_0037AC2F + 0x10B](Unknown_function_0037AC2F.md) (`tail-transfer`)
  - `0x0037B002` → [sub_0037AC2F + 0x10B](Unknown_function_0037AC2F.md) (`tail-transfer`)
  - `0x0037B00A` → [sub_0037AC2F + 0x11B](Unknown_function_0037AC2F.md) (`tail-transfer`)
  - `0x0037B030` → [sub_0037AC2F + 0x11B](Unknown_function_0037AC2F.md) (`tail-transfer`)
  - `0x0037B0D3` → [sub_0037AC2F + 0xCB](Unknown_function_0037AC2F.md) (`tail-transfer`)
  - `0x0037B32D` → [sub_0037AC2F + 0xED](Unknown_function_0037AC2F.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0037AE18  F3 90                           pause
0037AE1A  41 B9 80 96 98 00               mov r9d, 0x989680
0037AE20  48 8D 15 E9 4E 0A 00            lea rdx, [rip + 0xa4ee9]
0037AE27  49 BA 94 02 00 00 80 F7 FF FF   movabs r10, 0xfffff78000000294
0037AE31  4C 8D 1D 88 2D F6 FF            lea r11, [rip - 0x9d278]
0037AE38  E9 5A FE FF FF                  jmp 0x14037ac97
0037AE3D  83 BD DC 00 00 00 40            cmp dword ptr [rbp + 0xdc], 0x40
0037AE44  48 8B B5 C0 00 00 00            mov rsi, qword ptr [rbp + 0xc0]
0037AE4B  0F 85 E4 01 00 00               jne 0x14037b035
0037AE51  F7 85 E0 00 00 00 00 00 01 00   test dword ptr [rbp + 0xe0], 0x10000
0037AE5B  0F 85 E1 02 00 00               jne 0x14037b142
0037AE61  48 8B 4D 48                     mov rcx, qword ptr [rbp + 0x48]
0037AE65  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
0037AE69  48 8D 15 E0 E0 FF FF            lea rdx, [rip - 0x1f20]
0037AE70  48 3B C2                        cmp rax, rdx
0037AE73  0F 85 C8 04 00 00               jne 0x14037b341
0037AE79  48 8B 05 E0 68 A9 00            mov rax, qword ptr [rip + 0xa968e0]
0037AE80  48 85 C0                        test rax, rax
0037AE83  0F 84 17 03 00 00               je 0x14037b1a0
0037AE89  49 3B C3                        cmp rax, r11
0037AE8C  0F 85 AD 04 00 00               jne 0x14037b33f
0037AE92  48 C7 44 24 28 00 00 00 00      mov qword ptr [rsp + 0x28], 0
0037AE9B  48 8B 05 E6 BE C4 00            mov rax, qword ptr [rip + 0xc4bee6]
0037AEA2  44 8B 08                        mov r9d, dword ptr [rax]
0037AEA5  45 85 C9                        test r9d, r9d
0037AEA8  0F 84 C7 02 00 00               je 0x14037b175
0037AEAE  41 80 3A 00                     cmp byte ptr [r10], 0
0037AEB2  0F 84 A1 02 00 00               je 0x14037b159
0037AEB8  0F 01 F9                        rdtscp
0037AEBB  4C 8D 84 24 B8 00 00 00         lea r8, [rsp + 0xb8]
0037AEC3  41 89 08                        mov dword ptr [r8], ecx
0037AEC6  48 C1 E2 20                     shl rdx, 0x20
0037AECA  48 0B D0                        or rdx, rax
0037AECD  48 8B 05 B4 BE C4 00            mov rax, qword ptr [rip + 0xc4beb4]
0037AED4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0037AED8  48 8B 0D A9 BE C4 00            mov rcx, qword ptr [rip + 0xc4bea9]
0037AEDF  48 F7 E2                        mul rdx
0037AEE2  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
0037AEE6  48 8B 05 9B BE C4 00            mov rax, qword ptr [rip + 0xc4be9b]
0037AEED  49 03 D0                        add rdx, r8
0037AEF0  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
0037AEF5  8B 08                           mov ecx, dword ptr [rax]
0037AEF7  41 3B C9                        cmp ecx, r9d
0037AEFA  75 9F                           jne 0x14037ae9b
0037AEFC  48 8B 54 24 28                  mov rdx, qword ptr [rsp + 0x28]
0037AF01  4C 8B B5 D0 00 00 00            mov r14, qword ptr [rbp + 0xd0]
0037AF08  4D 8D 1C 16                     lea r11, [r14 + rdx]
0037AF0C  41 B9 80 96 98 00               mov r9d, 0x989680
0037AF12  49 BE 40 03 00 00 80 F7 FF FF   movabs r14, 0xfffff78000000340
0037AF1C  E9 19 FE FF FF                  jmp 0x14037ad3a
0037AF21  83 BD DC 00 00 00 40            cmp dword ptr [rbp + 0xdc], 0x40
0037AF28  0F 85 85 02 00 00               jne 0x14037b1b3
0037AF2E  48 8B CD                        mov rcx, rbp
0037AF31  E8 CA E5 E8 FF                  call 0x140209500
0037AF36  48 8B C8                        mov rcx, rax
0037AF39  48 8D 15 10 E0 FF FF            lea rdx, [rip - 0x1ff0]
0037AF40  48 8B 45 70                     mov rax, qword ptr [rbp + 0x70]
0037AF44  48 3B C2                        cmp rax, rdx
0037AF47  0F 85 C5 03 00 00               jne 0x14037b312
0037AF4D  48 8B 05 0C 68 A9 00            mov rax, qword ptr [rip + 0xa9680c]
0037AF54  48 85 C0                        test rax, rax
0037AF57  0F 84 93 03 00 00               je 0x14037b2f0
0037AF5D  49 3B C3                        cmp rax, r11
0037AF60  0F 85 AA 03 00 00               jne 0x14037b310
0037AF66  48 C7 44 24 20 00 00 00 00      mov qword ptr [rsp + 0x20], 0
0037AF6F  48 8B 05 12 BE C4 00            mov rax, qword ptr [rip + 0xc4be12]
0037AF76  44 8B 08                        mov r9d, dword ptr [rax]
0037AF79  45 85 C9                        test r9d, r9d
0037AF7C  0F 84 5A 03 00 00               je 0x14037b2dc
0037AF82  41 80 3A 00                     cmp byte ptr [r10], 0
0037AF86  0F 84 1D 03 00 00               je 0x14037b2a9
0037AF8C  0F 01 F9                        rdtscp
0037AF8F  4C 8D 84 24 A8 00 00 00         lea r8, [rsp + 0xa8]
0037AF97  41 89 08                        mov dword ptr [r8], ecx
0037AF9A  48 C1 E2 20                     shl rdx, 0x20
0037AF9E  48 0B D0                        or rdx, rax
0037AFA1  48 8B 05 E0 BD C4 00            mov rax, qword ptr [rip + 0xc4bde0]
0037AFA8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0037AFAC  48 8B 0D D5 BD C4 00            mov rcx, qword ptr [rip + 0xc4bdd5]
0037AFB3  48 F7 E2                        mul rdx
0037AFB6  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
0037AFBA  48 8B 05 C7 BD C4 00            mov rax, qword ptr [rip + 0xc4bdc7]
0037AFC1  49 03 D0                        add rdx, r8
0037AFC4  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0037AFC9  8B 08                           mov ecx, dword ptr [rax]
0037AFCB  41 3B C9                        cmp ecx, r9d
0037AFCE  75 9F                           jne 0x14037af6f
0037AFD0  48 8B 54 24 20                  mov rdx, qword ptr [rsp + 0x20]
0037AFD5  4C 8B B5 D0 00 00 00            mov r14, qword ptr [rbp + 0xd0]
0037AFDC  49 8D 0C 16                     lea rcx, [r14 + rdx]
0037AFE0  41 B8 80 96 98 00               mov r8d, 0x989680
0037AFE6  48 8B 95 C0 00 00 00            mov rdx, qword ptr [rbp + 0xc0]
0037AFED  E8 62 03 00 00                  call 0x14037b354
0037AFF2  4C 8B D8                        mov r11, rax
0037AFF5  45 8B C8                        mov r9d, r8d
0037AFF8  49 BE 40 03 00 00 80 F7 FF FF   movabs r14, 0xfffff78000000340
0037B002  E9 33 FD FF FF                  jmp 0x14037ad3a
0037B007  48 85 C0                        test rax, rax
0037B00A  0F 84 3A FD FF FF               je 0x14037ad4a
0037B010  83 B8 E4 00 00 00 05            cmp dword ptr [rax + 0xe4], 5
0037B017  48 8B D6                        mov rdx, rsi
0037B01A  4C 8B 80 C0 00 00 00            mov r8, qword ptr [rax + 0xc0]
0037B021  49 8B CB                        mov rcx, r11
0037B024  4D 0F 44 C1                     cmove r8, r9
0037B028  E8 27 03 00 00                  call 0x14037b354
0037B02D  4C 8B D8                        mov r11, rax
0037B030  E9 15 FD FF FF                  jmp 0x14037ad4a
0037B035  4C 8D 2D 24 E6 FF FF            lea r13, [rip - 0x19dc]
0037B03C  4C 8B B5 D0 00 00 00            mov r14, qword ptr [rbp + 0xd0]
0037B043  48 8B BD C8 00 00 00            mov rdi, qword ptr [rbp + 0xc8]
0037B04A  48 8B CD                        mov rcx, rbp
0037B04D  E8 AE E4 E8 FF                  call 0x140209500
0037B052  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
0037B056  48 8B C8                        mov rcx, rax
0037B059  49 3B D5                        cmp rdx, r13
0037B05C  0F 85 D0 02 00 00               jne 0x14037b332
0037B062  E8 F9 E5 FF FF                  call 0x140379660
0037B067  4C 8B D0                        mov r10, rax
0037B06A  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0037B06F  48 8B 85 C8 00 00 00            mov rax, qword ptr [rbp + 0xc8]
0037B076  48 3B F8                        cmp rdi, rax
0037B079  75 C8                           jne 0x14037b043
0037B07B  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
0037B082  4C 3B F1                        cmp r14, rcx
0037B085  75 B5                           jne 0x14037b03c
0037B087  44 8B 8D DC 00 00 00            mov r9d, dword ptr [rbp + 0xdc]
0037B08E  49 BD 50 03 00 00 80 F7 FF FF   movabs r13, 0xfffff78000000350
0037B098  41 8D 49 FF                     lea ecx, [r9 - 1]
0037B09C  0F B6 D1                        movzx edx, cl
0037B09F  49 8B CA                        mov rcx, r10
0037B0A2  48 33 CF                        xor rcx, rdi
0037B0A5  48 0F A3 D1                     bt rcx, rdx
0037B0A9  72 2D                           jb 0x14037b0d8
0037B0AB  41 83 F9 40                     cmp r9d, 0x40
0037B0AF  74 6B                           je 0x14037b11c
0037B0B1  41 8B C9                        mov ecx, r9d
0037B0B4  BA 01 00 00 00                  mov edx, 1
0037B0B9  48 D3 E2                        shl rdx, cl
0037B0BC  48 FF CA                        dec rdx
0037B0BF  EB 62                           jmp 0x14037b123
0037B0C1  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0037B0C9  0F AF 45 50                     imul eax, dword ptr [rbp + 0x50]
0037B0CD  8B C8                           mov ecx, eax
0037B0CF  48 03 4D 48                     add rcx, qword ptr [rbp + 0x48]
0037B0D3  E9 22 FC FF FF                  jmp 0x14037acfa
0037B0D8  41 83 F9 40                     cmp r9d, 0x40
0037B0DC  75 53                           jne 0x14037b131
0037B0DE  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
0037B0E5  41 8B C9                        mov ecx, r9d
0037B0E8  BA 01 00 00 00                  mov edx, 1
0037B0ED  48 D3 E2                        shl rdx, cl
0037B0F0  33 C9                           xor ecx, ecx
0037B0F2  41 83 F9 40                     cmp r9d, 0x40
0037B0F6  48 0F 45 CA                     cmovne rcx, rdx
0037B0FA  4C 23 C7                        and r8, rdi
0037B0FD  49 8B D0                        mov rdx, r8
0037B100  48 33 D7                        xor rdx, rdi
0037B103  49 0B D2                        or rdx, r10
0037B106  4D 3B D0                        cmp r10, r8
0037B109  73 03                           jae 0x14037b10e
0037B10B  48 03 D1                        add rdx, rcx
0037B10E  F0 48 0F B1 95 C8 00 00 00      lock cmpxchg qword ptr [rbp + 0xc8], rdx
0037B117  E9 EC FD FF FF                  jmp 0x14037af08
0037B11C  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0037B123  48 F7 D2                        not rdx
0037B126  48 23 D7                        and rdx, rdi
0037B129  49 0B D2                        or rdx, r10
0037B12C  E9 D7 FD FF FF                  jmp 0x14037af08
0037B131  41 8B C9                        mov ecx, r9d
0037B134  41 B8 01 00 00 00               mov r8d, 1
0037B13A  49 D3 E0                        shl r8, cl
0037B13D  49 FF C8                        dec r8
0037B140  EB A3                           jmp 0x14037b0e5
0037B142  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0037B14A  0F AF 45 50                     imul eax, dword ptr [rbp + 0x50]
0037B14E  8B C8                           mov ecx, eax
0037B150  48 03 4D 48                     add rcx, qword ptr [rbp + 0x48]
0037B154  E9 0C FD FF FF                  jmp 0x14037ae65
0037B159  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0037B162  80 B8 8D 00 00 00 02            cmp byte ptr [rax + 0x8d], 2
0037B169  75 1E                           jne 0x14037b189
0037B16B  0F AE E8                        lfence
0037B16E  0F 31                           rdtsc
0037B170  E9 51 FD FF FF                  jmp 0x14037aec6
0037B175  48 8D 54 24 28                  lea rdx, [rsp + 0x28]
0037B17A  B9 04 00 09 00                  mov ecx, 0x90004
0037B17F  E8 CC DE FF FF                  call 0x140379050
0037B184  E9 73 FD FF FF                  jmp 0x14037aefc
0037B189  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0037B192  80 B8 8D 00 00 00 01            cmp byte ptr [rax + 0x8d], 1
0037B199  75 D3                           jne 0x14037b16e
0037B19B  0F AE F0                        mfence
0037B19E  EB CE                           jmp 0x14037b16e
0037B1A0  B9 20 00 00 40                  mov ecx, 0x40000020
0037B1A5  0F 32                           rdmsr
0037B1A7  48 C1 E2 20                     shl rdx, 0x20
0037B1AB  48 0B D0                        or rdx, rax
0037B1AE  E9 4E FD FF FF                  jmp 0x14037af01
0037B1B3  4C 8D 2D A6 E4 FF FF            lea r13, [rip - 0x1b5a]
0037B1BA  4C 8B B5 D0 00 00 00            mov r14, qword ptr [rbp + 0xd0]
0037B1C1  48 8B BD C8 00 00 00            mov rdi, qword ptr [rbp + 0xc8]
0037B1C8  48 8B CD                        mov rcx, rbp
0037B1CB  E8 30 E3 E8 FF                  call 0x140209500
0037B1D0  48 8B 55 70                     mov rdx, qword ptr [rbp + 0x70]
0037B1D4  48 8B C8                        mov rcx, rax
0037B1D7  49 3B D5                        cmp rdx, r13
0037B1DA  0F 85 23 01 00 00               jne 0x14037b303
0037B1E0  E8 7B E4 FF FF                  call 0x140379660
0037B1E5  4C 8B D0                        mov r10, rax
0037B1E8  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0037B1ED  48 8B 85 C8 00 00 00            mov rax, qword ptr [rbp + 0xc8]
0037B1F4  48 3B F8                        cmp rdi, rax
0037B1F7  75 C8                           jne 0x14037b1c1
0037B1F9  48 8B 8D D0 00 00 00            mov rcx, qword ptr [rbp + 0xd0]
0037B200  4C 3B F1                        cmp r14, rcx
0037B203  75 B5                           jne 0x14037b1ba
0037B205  44 8B 8D DC 00 00 00            mov r9d, dword ptr [rbp + 0xdc]
0037B20C  49 BD 50 03 00 00 80 F7 FF FF   movabs r13, 0xfffff78000000350
0037B216  41 8D 49 FF                     lea ecx, [r9 - 1]
0037B21A  0F B6 D1                        movzx edx, cl
0037B21D  49 8B CA                        mov rcx, r10
0037B220  48 33 CF                        xor rcx, rdi
0037B223  48 0F A3 D1                     bt rcx, rdx
0037B227  72 1B                           jb 0x14037b244
0037B229  41 83 F9 40                     cmp r9d, 0x40
0037B22D  75 59                           jne 0x14037b288
0037B22F  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0037B236  48 F7 D2                        not rdx
0037B239  48 23 D7                        and rdx, rdi
0037B23C  49 0B D2                        or rdx, r10
0037B23F  E9 98 FD FF FF                  jmp 0x14037afdc
0037B244  41 83 F9 40                     cmp r9d, 0x40
0037B248  75 4E                           jne 0x14037b298
0037B24A  49 C7 C0 FF FF FF FF            mov r8, 0xffffffffffffffff
0037B251  41 8B C9                        mov ecx, r9d
0037B254  BA 01 00 00 00                  mov edx, 1
0037B259  48 D3 E2                        shl rdx, cl
0037B25C  33 C9                           xor ecx, ecx
0037B25E  41 83 F9 40                     cmp r9d, 0x40
0037B262  48 0F 45 CA                     cmovne rcx, rdx
0037B266  4C 23 C7                        and r8, rdi
0037B269  49 8B D0                        mov rdx, r8
0037B26C  48 33 D7                        xor rdx, rdi
0037B26F  49 0B D2                        or rdx, r10
0037B272  4D 3B D0                        cmp r10, r8
0037B275  73 03                           jae 0x14037b27a
0037B277  48 03 D1                        add rdx, rcx
0037B27A  F0 48 0F B1 95 C8 00 00 00      lock cmpxchg qword ptr [rbp + 0xc8], rdx
0037B283  E9 54 FD FF FF                  jmp 0x14037afdc
0037B288  41 8B C9                        mov ecx, r9d
0037B28B  BA 01 00 00 00                  mov edx, 1
0037B290  48 D3 E2                        shl rdx, cl
0037B293  48 FF CA                        dec rdx
0037B296  EB 9E                           jmp 0x14037b236
0037B298  41 8B C9                        mov ecx, r9d
0037B29B  41 B8 01 00 00 00               mov r8d, 1
0037B2A1  49 D3 E0                        shl r8, cl
0037B2A4  49 FF C8                        dec r8
0037B2A7  EB A8                           jmp 0x14037b251
0037B2A9  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0037B2B2  80 B8 8D 00 00 00 02            cmp byte ptr [rax + 0x8d], 2
0037B2B9  75 0A                           jne 0x14037b2c5
0037B2BB  0F AE E8                        lfence
0037B2BE  0F 31                           rdtsc
0037B2C0  E9 D5 FC FF FF                  jmp 0x14037af9a
0037B2C5  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
0037B2CE  80 B8 8D 00 00 00 01            cmp byte ptr [rax + 0x8d], 1
0037B2D5  75 E7                           jne 0x14037b2be
0037B2D7  0F AE F0                        mfence
0037B2DA  EB E2                           jmp 0x14037b2be
0037B2DC  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0037B2E1  B9 04 00 09 00                  mov ecx, 0x90004
0037B2E6  E8 65 DD FF FF                  call 0x140379050
0037B2EB  E9 E0 FC FF FF                  jmp 0x14037afd0
0037B2F0  B9 20 00 00 40                  mov ecx, 0x40000020
0037B2F5  0F 32                           rdmsr
0037B2F7  48 C1 E2 20                     shl rdx, 0x20
0037B2FB  48 0B D0                        or rdx, rax
0037B2FE  E9 D2 FC FF FF                  jmp 0x14037afd5
0037B303  48 8B C2                        mov rax, rdx
0037B306  E8 C5 F7 33 00                  call 0x1406baad0
0037B30B  E9 D5 FE FF FF                  jmp 0x14037b1e5
0037B310  33 C9                           xor ecx, ecx
0037B312  E8 B9 F7 33 00                  call 0x1406baad0
0037B317  48 8B D0                        mov rdx, rax
0037B31A  E9 B6 FC FF FF                  jmp 0x14037afd5
0037B31F  E8 AC F7 33 00                  call 0x1406baad0
0037B324  48 8B D0                        mov rdx, rax
0037B327  41 B9 80 96 98 00               mov r9d, 0x989680
0037B32D  E9 EA F9 FF FF                  jmp 0x14037ad1c
0037B332  48 8B C2                        mov rax, rdx
0037B335  E8 96 F7 33 00                  call 0x1406baad0
0037B33A  E9 28 FD FF FF                  jmp 0x14037b067
0037B33F  33 C9                           xor ecx, ecx
0037B341  E8 8A F7 33 00                  call 0x1406baad0
0037B346  48 8B D0                        mov rdx, rax
0037B349  E9 B3 FB FF FF                  jmp 0x14037af01
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0037AE18(void)
{
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB8;
}
```

## 5. (Beta) C Style

```c
void sub_0037AE18(void)
{
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0037AE18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
