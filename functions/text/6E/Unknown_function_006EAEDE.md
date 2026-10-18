# sub_006EAEDE

- RVA: `0x006EAEDE`–`0x006EB35E` (길이 `1,152` bytes)
- VA: `0x00000001406EAEDE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097354`
- 디코드: `347`개 명령, `1,152/1,152` bytes 표시
- 미해석 바이트: `8` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006EAF07` → [EtwpGetSignedFieldValue](../65/EtwpGetSignedFieldValue_function_006545DC.md) (function, `0x006545DC`)
- `0x006EAFD3` → [EtwpGetFieldValue](../3F/EtwpGetFieldValue_function_003F4D70.md) (function, `0x003F4D70`)
- `0x006EB1C3` → [wcsncmp](../50/wcsncmp_function_00501CA0.md) (function, `0x00501CA0`)
- `0x006EB2CD` → [strncmp](../6C/strncmp_function_006C6720.md) (function, `0x006C6720`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006EAEE7` → RVA `0x00000000` (`image boundary/outside`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **36**
  - `0x006EAEE1` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF0E` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF1F` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF3E` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF4B` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF58` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF65` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF72` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF7F` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAF95` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAFAB` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAFB3` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAFDA` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EAFE3` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB014` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB025` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB036` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB047` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB058` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB078` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB0A2` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB0BD` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB0E4` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB12B` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB13C` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB17B` → [EtwpApplyPredicate + 0x85](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB183` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB189` → [EtwpApplyPredicate + 0xB3](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB198` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB1E3` → [EtwpApplyPredicate + 0x85](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB1FF` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB238` → [EtwpApplyPredicate + 0x83](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB249` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB28F` → [EtwpApplyPredicate + 0x85](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB29E` → [EtwpApplyPredicate + 0xA5](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)
  - `0x006EB2EF` → [EtwpApplyPredicate + 0x85](../3F/EtwpApplyPredicate_function_003F4CB0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006EAEDE  83 F8 07                        cmp eax, 7
006EAEE1  0F 87 4C 9E D0 FF               ja 0x1403f4d33
006EAEE7  4C 8D 3D 12 51 91 FF            lea r15, [rip - 0x6eaeee]
006EAEEE  41 8B 84 87 F6 B2 6E 00         mov eax, dword ptr [r15 + rax*4 + 0x6eb2f6]
006EAEF6  49 03 C7                        add rax, r15
006EAEF9  FF E0                           jmp rax
006EAEFB  CC                              int3
006EAEFC  CC                              int3
006EAEFD  CC                              int3
006EAEFE  CC                              int3
006EAEFF  4C 8D 44 24 28                  lea r8, [rsp + 0x28]
006EAF04  49 8B C9                        mov rcx, r9
006EAF07  E8 D0 96 F6 FF                  call 0x1406545dc
006EAF0C  84 C0                           test al, al
006EAF0E  0F 84 1F 9E D0 FF               je 0x1403f4d33
006EAF14  4C 8B 43 08                     mov r8, qword ptr [rbx + 8]
006EAF18  48 8B 53 10                     mov rdx, qword ptr [rbx + 0x10]
006EAF1C  83 FE 08                        cmp esi, 8
006EAF1F  0F 87 0E 9E D0 FF               ja 0x1403f4d33
006EAF25  41 8B 8C B7 16 B3 6E 00         mov ecx, dword ptr [r15 + rsi*4 + 0x6eb316]
006EAF2D  49 03 CF                        add rcx, r15
006EAF30  FF E1                           jmp rcx
006EAF32  CC                              int3
006EAF33  CC                              int3
006EAF34  CC                              int3
006EAF35  CC                              int3
006EAF36  4C 39 44 24 28                  cmp qword ptr [rsp + 0x28], r8
006EAF3B  0F 94 C3                        sete bl
006EAF3E  E9 12 9E D0 FF                  jmp 0x1403f4d55
006EAF43  4C 39 44 24 28                  cmp qword ptr [rsp + 0x28], r8
006EAF48  0F 95 C3                        setne bl
006EAF4B  E9 05 9E D0 FF                  jmp 0x1403f4d55
006EAF50  4C 39 44 24 28                  cmp qword ptr [rsp + 0x28], r8
006EAF55  0F 9E C3                        setle bl
006EAF58  E9 F8 9D D0 FF                  jmp 0x1403f4d55
006EAF5D  4C 39 44 24 28                  cmp qword ptr [rsp + 0x28], r8
006EAF62  0F 9F C3                        setg bl
006EAF65  E9 EB 9D D0 FF                  jmp 0x1403f4d55
006EAF6A  4C 39 44 24 28                  cmp qword ptr [rsp + 0x28], r8
006EAF6F  0F 9C C3                        setl bl
006EAF72  E9 DE 9D D0 FF                  jmp 0x1403f4d55
006EAF77  4C 39 44 24 28                  cmp qword ptr [rsp + 0x28], r8
006EAF7C  0F 9D C3                        setge bl
006EAF7F  E9 D1 9D D0 FF                  jmp 0x1403f4d55
006EAF84  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
006EAF89  4C 3B C0                        cmp r8, rax
006EAF8C  7F 1B                           jg 0x1406eafa9
006EAF8E  48 3B C2                        cmp rax, rdx
006EAF91  7F 16                           jg 0x1406eafa9
006EAF93  B3 01                           mov bl, 1
006EAF95  E9 BB 9D D0 FF                  jmp 0x1403f4d55
006EAF9A  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
006EAF9F  49 3B C0                        cmp rax, r8
006EAFA2  7C EF                           jl 0x1406eaf93
006EAFA4  48 3B D0                        cmp rdx, rax
006EAFA7  7C EA                           jl 0x1406eaf93
006EAFA9  32 DB                           xor bl, bl
006EAFAB  E9 A5 9D D0 FF                  jmp 0x1403f4d55
006EAFB0  4D 85 C0                        test r8, r8
006EAFB3  0F 84 7A 9D D0 FF               je 0x1403f4d33
006EAFB9  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
006EAFBE  48 99                           cqo
006EAFC0  49 F7 F8                        idiv r8
006EAFC3  48 85 D2                        test rdx, rdx
006EAFC6  E9 70 FF FF FF                  jmp 0x1406eaf3b
006EAFCB  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
006EAFD0  49 8B C9                        mov rcx, r9
006EAFD3  E8 98 9D D0 FF                  call 0x1403f4d70
006EAFD8  84 C0                           test al, al
006EAFDA  0F 84 53 9D D0 FF               je 0x1403f4d33
006EAFE0  83 FE 08                        cmp esi, 8
006EAFE3  0F 87 4A 9D D0 FF               ja 0x1403f4d33
006EAFE9  41 8B 8C B7 3A B3 6E 00         mov ecx, dword ptr [r15 + rsi*4 + 0x6eb33a]
006EAFF1  49 03 CF                        add rcx, r15
006EAFF4  FF E1                           jmp rcx
006EAFF6  CC                              int3
006EAFF7  CC                              int3
006EAFF8  CC                              int3
006EAFF9  CC                              int3
006EAFFA  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
006EAFFE  48 39 44 24 30                  cmp qword ptr [rsp + 0x30], rax
006EB003  E9 33 FF FF FF                  jmp 0x1406eaf3b
006EB008  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
006EB00C  48 39 44 24 30                  cmp qword ptr [rsp + 0x30], rax
006EB011  0F 95 C3                        setne bl
006EB014  E9 3C 9D D0 FF                  jmp 0x1403f4d55
006EB019  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
006EB01D  48 39 44 24 30                  cmp qword ptr [rsp + 0x30], rax
006EB022  0F 96 C3                        setbe bl
006EB025  E9 2B 9D D0 FF                  jmp 0x1403f4d55
006EB02A  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
006EB02E  48 39 44 24 30                  cmp qword ptr [rsp + 0x30], rax
006EB033  0F 97 C3                        seta bl
006EB036  E9 1A 9D D0 FF                  jmp 0x1403f4d55
006EB03B  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
006EB03F  48 39 44 24 30                  cmp qword ptr [rsp + 0x30], rax
006EB044  0F 92 C3                        setb bl
006EB047  E9 09 9D D0 FF                  jmp 0x1403f4d55
006EB04C  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
006EB050  48 39 44 24 30                  cmp qword ptr [rsp + 0x30], rax
006EB055  0F 93 C3                        setae bl
006EB058  E9 F8 9C D0 FF                  jmp 0x1403f4d55
006EB05D  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
006EB062  48 39 43 08                     cmp qword ptr [rbx + 8], rax
006EB066  0F 87 3D FF FF FF               ja 0x1406eafa9
006EB06C  48 3B 43 10                     cmp rax, qword ptr [rbx + 0x10]
006EB070  0F 87 33 FF FF FF               ja 0x1406eafa9
006EB076  B3 01                           mov bl, 1
006EB078  E9 D8 9C D0 FF                  jmp 0x1403f4d55
006EB07D  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
006EB082  48 3B 43 08                     cmp rax, qword ptr [rbx + 8]
006EB086  0F 82 07 FF FF FF               jb 0x1406eaf93
006EB08C  48 39 43 10                     cmp qword ptr [rbx + 0x10], rax
006EB090  0F 82 FD FE FF FF               jb 0x1406eaf93
006EB096  E9 0E FF FF FF                  jmp 0x1406eafa9
006EB09B  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
006EB09F  48 85 C9                        test rcx, rcx
006EB0A2  0F 84 8B 9C D0 FF               je 0x1403f4d33
006EB0A8  33 D2                           xor edx, edx
006EB0AA  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
006EB0AF  48 F7 F1                        div rcx
006EB0B2  48 85 D2                        test rdx, rdx
006EB0B5  E9 81 FE FF FF                  jmp 0x1406eaf3b
006EB0BA  F6 C2 01                        test dl, 1
006EB0BD  0F 85 70 9C D0 FF               jne 0x1403f4d33
006EB0C3  D1 EA                           shr edx, 1
006EB0C5  41 0F B7 48 2C                  movzx ecx, word ptr [r8 + 0x2c]
006EB0CA  49 03 C8                        add rcx, r8
006EB0CD  41 0F B7 40 2E                  movzx eax, word ptr [r8 + 0x2e]
006EB0D2  48 D1 E8                        shr rax, 1
006EB0D5  4C 8D 04 41                     lea r8, [rcx + rax*2]
006EB0D9  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
006EB0DD  4C 8D 24 41                     lea r12, [rcx + rax*2]
006EB0E1  4D 3B E0                        cmp r12, r8
006EB0E4  0F 83 49 9C D0 FF               jae 0x1403f4d33
006EB0EA  4D 8B FC                        mov r15, r12
006EB0ED  45 0F B7 2C 24                  movzx r13d, word ptr [r12]
006EB0F2  66 45 85 ED                     test r13w, r13w
006EB0F6  74 10                           je 0x1406eb108
006EB0F8  4D 3B F8                        cmp r15, r8
006EB0FB  73 0B                           jae 0x1406eb108
006EB0FD  49 83 C7 02                     add r15, 2
006EB101  66 41 83 3F 00                  cmp word ptr [r15], 0
006EB106  75 F0                           jne 0x1406eb0f8
006EB108  4D 2B FC                        sub r15, r12
006EB10B  49 D1 FF                        sar r15, 1
006EB10E  45 85 FF                        test r15d, r15d
006EB111  0F 84 92 FE FF FF               je 0x1406eafa9
006EB117  8B CE                           mov ecx, esi
006EB119  83 E9 14                        sub ecx, 0x14
006EB11C  74 73                           je 0x1406eb191
006EB11E  83 E9 01                        sub ecx, 1
006EB121  74 6B                           je 0x1406eb18e
006EB123  83 E9 09                        sub ecx, 9
006EB126  74 0D                           je 0x1406eb135
006EB128  83 F9 01                        cmp ecx, 1
006EB12B  0F 85 02 9C D0 FF               jne 0x1403f4d33
006EB131  44 0F B6 F1                     movzx r14d, cl
006EB135  41 0F B6 DE                     movzx ebx, r14b
006EB139  44 3B FA                        cmp r15d, edx
006EB13C  0F 85 13 9C D0 FF               jne 0x1403f4d55
006EB142  B3 01                           mov bl, 1
006EB144  45 85 FF                        test r15d, r15d
006EB147  74 2E                           je 0x1406eb177
006EB149  0F B7 07                        movzx eax, word ptr [rdi]
006EB14C  66 41 39 04 24                  cmp word ptr [r12], ax
006EB151  74 08                           je 0x1406eb15b
006EB153  32 DB                           xor bl, bl
006EB155  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
006EB159  EB 1C                           jmp 0x1406eb177
006EB15B  48 83 C7 02                     add rdi, 2
006EB15F  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
006EB164  49 83 C4 02                     add r12, 2
006EB168  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
006EB16D  41 FF CF                        dec r15d
006EB170  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
006EB175  EB CD                           jmp 0x1406eb144
006EB177  EB 07                           jmp 0x1406eb180
006EB179  32 C0                           xor al, al
006EB17B  E9 B5 9B D0 FF                  jmp 0x1403f4d35
006EB180  45 84 F6                        test r14b, r14b
006EB183  0F 84 CC 9B D0 FF               je 0x1403f4d55
006EB189  E9 D5 9B D0 FF                  jmp 0x1403f4d63
006EB18E  41 B6 01                        mov r14b, 1
006EB191  41 0F B6 DE                     movzx ebx, r14b
006EB195  44 3B FA                        cmp r15d, edx
006EB198  0F 87 B7 9B D0 FF               ja 0x1403f4d55
006EB19E  41 8B C7                        mov eax, r15d
006EB1A1  8B F2                           mov esi, edx
006EB1A3  48 2B F0                        sub rsi, rax
006EB1A6  48 FF C6                        inc rsi
006EB1A9  49 8D 34 71                     lea rsi, [r9 + rsi*2]
006EB1AD  32 DB                           xor bl, bl
006EB1AF  48 3B FE                        cmp rdi, rsi
006EB1B2  73 2B                           jae 0x1406eb1df
006EB1B4  66 44 39 2F                     cmp word ptr [rdi], r13w
006EB1B8  75 1A                           jne 0x1406eb1d4
006EB1BA  45 8B C7                        mov r8d, r15d
006EB1BD  49 8B D4                        mov rdx, r12
006EB1C0  48 8B CF                        mov rcx, rdi
006EB1C3  E8 D8 6A E1 FF                  call 0x140501ca0
006EB1C8  85 C0                           test eax, eax
006EB1CA  75 08                           jne 0x1406eb1d4
006EB1CC  B3 01                           mov bl, 1
006EB1CE  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
006EB1D2  EB 0B                           jmp 0x1406eb1df
006EB1D4  48 83 C7 02                     add rdi, 2
006EB1D8  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
006EB1DD  EB D0                           jmp 0x1406eb1af
006EB1DF  EB 9F                           jmp 0x1406eb180
006EB1E1  32 C0                           xor al, al
006EB1E3  E9 4D 9B D0 FF                  jmp 0x1403f4d35
006EB1E8  45 0F B7 60 30                  movzx r12d, word ptr [r8 + 0x30]
006EB1ED  4D 03 E0                        add r12, r8
006EB1F0  41 0F B7 40 32                  movzx eax, word ptr [r8 + 0x32]
006EB1F5  49 03 C4                        add rax, r12
006EB1F8  4C 03 63 08                     add r12, qword ptr [rbx + 8]
006EB1FC  4C 3B E0                        cmp r12, rax
006EB1FF  0F 83 2E 9B D0 FF               jae 0x1403f4d33
006EB205  4D 8B FC                        mov r15, r12
006EB208  41 38 0C 24                     cmp byte ptr [r12], cl
006EB20C  74 0D                           je 0x1406eb21b
006EB20E  4C 3B F8                        cmp r15, rax
006EB211  73 08                           jae 0x1406eb21b
006EB213  49 FF C7                        inc r15
006EB216  41 38 0F                        cmp byte ptr [r15], cl
006EB219  75 F3                           jne 0x1406eb20e
006EB21B  45 2B FC                        sub r15d, r12d
006EB21E  0F 84 85 FD FF FF               je 0x1406eafa9
006EB224  8B CE                           mov ecx, esi
006EB226  83 E9 14                        sub ecx, 0x14
006EB229  74 6C                           je 0x1406eb297
006EB22B  83 E9 01                        sub ecx, 1
006EB22E  74 64                           je 0x1406eb294
006EB230  83 E9 09                        sub ecx, 9
006EB233  74 0D                           je 0x1406eb242
006EB235  83 F9 01                        cmp ecx, 1
006EB238  0F 85 F5 9A D0 FF               jne 0x1403f4d33
006EB23E  44 0F B6 F1                     movzx r14d, cl
006EB242  41 0F B6 DE                     movzx ebx, r14b
006EB246  44 3B FA                        cmp r15d, edx
006EB249  0F 85 06 9B D0 FF               jne 0x1403f4d55
006EB24F  B3 01                           mov bl, 1
006EB251  49 8B CC                        mov rcx, r12
006EB254  45 85 FF                        test r15d, r15d
006EB257  74 2F                           je 0x1406eb288
006EB259  41 0F B6 04 24                  movzx eax, byte ptr [r12]
006EB25E  38 07                           cmp byte ptr [rdi], al
006EB260  74 08                           je 0x1406eb26a
006EB262  32 DB                           xor bl, bl
006EB264  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
006EB268  EB 1E                           jmp 0x1406eb288
006EB26A  48 FF C7                        inc rdi
006EB26D  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
006EB272  4C 8D 61 01                     lea r12, [rcx + 1]
006EB276  49 8B CC                        mov rcx, r12
006EB279  4C 89 64 24 30                  mov qword ptr [rsp + 0x30], r12
006EB27E  41 FF CF                        dec r15d
006EB281  44 89 7C 24 24                  mov dword ptr [rsp + 0x24], r15d
006EB286  EB CC                           jmp 0x1406eb254
006EB288  E9 F3 FE FF FF                  jmp 0x1406eb180
006EB28D  32 C0                           xor al, al
006EB28F  E9 A1 9A D0 FF                  jmp 0x1403f4d35
006EB294  41 B6 01                        mov r14b, 1
006EB297  41 0F B6 DE                     movzx ebx, r14b
006EB29B  44 3B FA                        cmp r15d, edx
006EB29E  0F 87 B1 9A D0 FF               ja 0x1403f4d55
006EB2A4  41 0F B6 34 24                  movzx esi, byte ptr [r12]
006EB2A9  41 8B C7                        mov eax, r15d
006EB2AC  4C 8B EA                        mov r13, rdx
006EB2AF  4C 2B E8                        sub r13, rax
006EB2B2  49 FF C5                        inc r13
006EB2B5  4D 03 E9                        add r13, r9
006EB2B8  32 DB                           xor bl, bl
006EB2BA  49 3B FD                        cmp rdi, r13
006EB2BD  73 29                           jae 0x1406eb2e8
006EB2BF  40 38 37                        cmp byte ptr [rdi], sil
006EB2C2  75 1A                           jne 0x1406eb2de
006EB2C4  45 8B C7                        mov r8d, r15d
006EB2C7  49 8B D4                        mov rdx, r12
006EB2CA  48 8B CF                        mov rcx, rdi
006EB2CD  E8 4E B4 FD FF                  call 0x1406c6720
006EB2D2  85 C0                           test eax, eax
006EB2D4  75 08                           jne 0x1406eb2de
006EB2D6  B3 01                           mov bl, 1
006EB2D8  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
006EB2DC  EB 0A                           jmp 0x1406eb2e8
006EB2DE  48 FF C7                        inc rdi
006EB2E1  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
006EB2E6  EB D2                           jmp 0x1406eb2ba
006EB2E8  E9 93 FE FF FF                  jmp 0x1406eb180
006EB2ED  32 C0                           xor al, al
006EB2EF  E9 41 9A D0 FF                  jmp 0x1403f4d35
006EB2F4  66 90                           nop
006EB2F6  33 4D 3F                        xor ecx, dword ptr [rbp + 0x3f]
006EB2F9  00 FF                           add bh, bh
006EB2FB  AE                              scasb al, byte ptr [rdi]
006EB2FC  6E                              outsb dx, byte ptr [rsi]
006EB2FD  00 CB                           add bl, cl
006EB2FF  AF                              scasd eax, dword ptr [rdi]
006EB300  6E                              outsb dx, byte ptr [rsi]
006EB301  00 E8                           add al, ch
006EB303  B1 6E                           mov cl, 0x6e
006EB305  00 BA B0 6E 00 33               add byte ptr [rdx + 0x33006eb0], bh
006EB30B  4D                              .byte 0x4d
006EB30C  3F                              .byte 0x3f
006EB30D  00 33                           add byte ptr [rbx], dh
006EB30F  4D                              .byte 0x4d
006EB310  3F                              .byte 0x3f
006EB311  00 33                           add byte ptr [rbx], dh
006EB313  4D                              .byte 0x4d
006EB314  3F                              .byte 0x3f
006EB315  00 36                           add byte ptr [rsi], dh
006EB317  AF                              scasd eax, dword ptr [rdi]
006EB318  6E                              outsb dx, byte ptr [rsi]
006EB319  00 43 AF                        add byte ptr [rbx - 0x51], al
006EB31C  6E                              outsb dx, byte ptr [rsi]
006EB31D  00 50 AF                        add byte ptr [rax - 0x51], dl
006EB320  6E                              outsb dx, byte ptr [rsi]
006EB321  00 5D AF                        add byte ptr [rbp - 0x51], bl
006EB324  6E                              outsb dx, byte ptr [rsi]
006EB325  00 6A AF                        add byte ptr [rdx - 0x51], ch
006EB328  6E                              outsb dx, byte ptr [rsi]
006EB329  00 77 AF                        add byte ptr [rdi - 0x51], dh
006EB32C  6E                              outsb dx, byte ptr [rsi]
006EB32D  00 84 AF 6E 00 9A AF            add byte ptr [rdi + rbp*4 - 0x5065ff92], al
006EB334  6E                              outsb dx, byte ptr [rsi]
006EB335  00 B0 AF 6E 00 FA               add byte ptr [rax - 0x5ff9151], dh
006EB33B  AF                              scasd eax, dword ptr [rdi]
006EB33C  6E                              outsb dx, byte ptr [rsi]
006EB33D  00 08                           add byte ptr [rax], cl
006EB33F  B0 6E                           mov al, 0x6e
006EB341  00 19                           add byte ptr [rcx], bl
006EB343  B0 6E                           mov al, 0x6e
006EB345  00 2A                           add byte ptr [rdx], ch
006EB347  B0 6E                           mov al, 0x6e
006EB349  00 3B                           add byte ptr [rbx], bh
006EB34B  B0 6E                           mov al, 0x6e
006EB34D  00 4C B0 6E                     add byte ptr [rax + rsi*4 + 0x6e], cl
006EB351  00 5D B0                        add byte ptr [rbp - 0x50], bl
006EB354  6E                              outsb dx, byte ptr [rsi]
006EB355  00 7D B0                        add byte ptr [rbp - 0x50], bh
006EB358  6E                              outsb dx, byte ptr [rsi]
006EB359  00                              .byte 0x00
006EB35A  9B                              wait
006EB35B  B0 6E                           mov al, 0x6e
006EB35D  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006EAEDE(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    unsigned __int8 v_stack_p20;
    unsigned int v_stack_p24;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;

    result = ((unsigned int)(*(unsigned int *)(v_rip - 7253742 + result * 4 + 7254774))) + (v_rip - 7253742);
}
```

## 5. (Beta) C Style

```c
int64_t sub_006EAEDE(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    uint8_t v_stack_p20;
    uint32_t v_stack_p24;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;

    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x6EAEEE + result * 4 + 0x6EB2F6))) + (v_rip - 7253742);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006EAEDE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
