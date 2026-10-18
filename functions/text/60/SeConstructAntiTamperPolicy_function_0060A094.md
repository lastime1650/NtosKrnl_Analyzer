# SeConstructAntiTamperPolicy

- RVA: `0x0060A094`–`0x0060A77F` (길이 `1,771` bytes)
- VA: `0x000000014060A094`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CA900`
- 디코드: `539`개 명령, `1,771/1,771` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **35**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0060A0DB` → [SepConstructAntiTamperBaselinePolicy](SepConstructAntiTamperBaselinePolicy_function_0060A83C.md) (function, `0x0060A83C`)
- `0x0060A0FD` → [SepConstructAntiTamperBaselinePolicy](SepConstructAntiTamperBaselinePolicy_function_0060A83C.md) (function, `0x0060A83C`)
- `0x0060A12D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0060A19A` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A1B9` → [SepFoldAntiTamperRelaxationIfeo](SepFoldAntiTamperRelaxationIfeo_function_0060AEA4.md) (function, `0x0060AEA4`)
- `0x0060A1DF` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A1F2` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A265` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A284` → [SepFoldAntiTamperRelaxationIfeo](SepFoldAntiTamperRelaxationIfeo_function_0060AEA4.md) (function, `0x0060AEA4`)
- `0x0060A2A9` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A2BC` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A30A` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A32A` → [SepFoldAntiTamperRelaxationIfeo](SepFoldAntiTamperRelaxationIfeo_function_0060AEA4.md) (function, `0x0060AEA4`)
- `0x0060A350` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A363` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A3AC` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A3CC` → [SepFoldAntiTamperRelaxationIfeo](SepFoldAntiTamperRelaxationIfeo_function_0060AEA4.md) (function, `0x0060AEA4`)
- `0x0060A3F2` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A405` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A44C` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A46C` → [SepFoldAntiTamperRelaxationIfeo](SepFoldAntiTamperRelaxationIfeo_function_0060AEA4.md) (function, `0x0060AEA4`)
- `0x0060A492` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A4A5` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A516` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A536` → [SepFoldAntiTamperRelaxationIfeo](SepFoldAntiTamperRelaxationIfeo_function_0060AEA4.md) (function, `0x0060AEA4`)
- `0x0060A55B` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A56E` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A5B6` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A5D6` → [SepFoldAntiTamperRelaxationIfeo](SepFoldAntiTamperRelaxationIfeo_function_0060AEA4.md) (function, `0x0060AEA4`)
- `0x0060A5FC` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A60F` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A654` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A667` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A6AD` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)
- `0x0060A6C0` → [SepFoldAntiTamperRelaxation](SepFoldAntiTamperRelaxation_function_0060AE88.md) (function, `0x0060AE88`)

### Direct callers
- [PspAllocateProcess](../../page/A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A16191`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0060A12D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0060A094  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0060A099  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0060A09E  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0060A0A3  55                              push rbp
0060A0A4  41 54                           push r12
0060A0A6  41 55                           push r13
0060A0A8  41 56                           push r14
0060A0AA  41 57                           push r15
0060A0AC  48 8B EC                        mov rbp, rsp
0060A0AF  48 83 EC 40                     sub rsp, 0x40
0060A0B3  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0060A0B7  49 8B D8                        mov rbx, r8
0060A0BA  48 8B F2                        mov rsi, rdx
0060A0BD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0060A0C1  48 83 20 00                     and qword ptr [rax], 0
0060A0C5  48 85 D2                        test rdx, rdx
0060A0C8  75 1B                           jne 0x14060a0e5
0060A0CA  48 85 DB                        test rbx, rbx
0060A0CD  75 19                           jne 0x14060a0e8
0060A0CF  48 85 C9                        test rcx, rcx
0060A0D2  0F 84 86 06 00 00               je 0x14060a75e
0060A0D8  48 8B D0                        mov rdx, rax
0060A0DB  E8 5C 07 00 00                  call 0x14060a83c
0060A0E0  E9 7B 06 00 00                  jmp 0x14060a760
0060A0E5  48 85 DB                        test rbx, rbx
0060A0E8  41 0F 95 C5                     setne r13b
0060A0EC  48 83 65 E8 00                  and qword ptr [rbp - 0x18], 0
0060A0F1  45 32 F6                        xor r14b, r14b
0060A0F4  48 85 C9                        test rcx, rcx
0060A0F7  74 24                           je 0x14060a11d
0060A0F9  48 8D 55 E8                     lea rdx, [rbp - 0x18]
0060A0FD  E8 3A 07 00 00                  call 0x14060a83c
0060A102  45 33 D2                        xor r10d, r10d
0060A105  85 C0                           test eax, eax
0060A107  0F 88 53 06 00 00               js 0x14060a760
0060A10D  4C 8B 5D E8                     mov r11, qword ptr [rbp - 0x18]
0060A111  4D 85 DB                        test r11, r11
0060A114  41 0F 95 C6                     setne r14b
0060A118  4D 85 DB                        test r11, r11
0060A11B  75 2A                           jne 0x14060a147
0060A11D  BA 40 00 00 00                  mov edx, 0x40
0060A122  B9 00 01 00 00                  mov ecx, 0x100
0060A127  41 B8 53 65 41 50               mov r8d, 0x50416553
0060A12D  E8 BE 7F 57 00                  call 0x140b820f0
0060A132  45 33 D2                        xor r10d, r10d
0060A135  4C 8B D8                        mov r11, rax
0060A138  48 85 C0                        test rax, rax
0060A13B  75 0A                           jne 0x14060a147
0060A13D  B8 9A 00 00 C0                  mov eax, 0xc000009a
0060A142  E9 19 06 00 00                  jmp 0x14060a760
0060A147  40 B7 03                        mov dil, 3
0060A14A  41 BF 01 00 00 00               mov r15d, 1
0060A150  48 85 F6                        test rsi, rsi
0060A153  74 0E                           je 0x14060a163
0060A155  48 8B 06                        mov rax, qword ptr [rsi]
0060A158  40 22 C7                        and al, dil
0060A15B  41 3A C7                        cmp al, r15b
0060A15E  75 03                           jne 0x14060a163
0060A160  45 09 3B                        or dword ptr [r11], r15d
0060A163  48 85 DB                        test rbx, rbx
0060A166  74 0B                           je 0x14060a173
0060A168  8B 43 04                        mov eax, dword ptr [rbx + 4]
0060A16B  41 84 C7                        test r15b, al
0060A16E  74 03                           je 0x14060a173
0060A170  45 09 3B                        or dword ptr [r11], r15d
0060A173  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A177  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A17B  45 84 F6                        test r14b, r14b
0060A17E  74 0C                           je 0x14060a18c
0060A180  41 8B 43 08                     mov eax, dword ptr [r11 + 8]
0060A184  45 8A CF                        mov r9b, r15b
0060A187  41 84 C7                        test r15b, al
0060A18A  75 03                           jne 0x14060a18f
0060A18C  45 8A CA                        mov r9b, r10b
0060A18F  45 8A C6                        mov r8b, r14b
0060A192  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A196  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A19A  E8 E9 0C 00 00                  call 0x14060ae88
0060A19F  48 85 F6                        test rsi, rsi
0060A1A2  74 1D                           je 0x14060a1c1
0060A1A4  4C 8B 06                        mov r8, qword ptr [rsi]
0060A1A7  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A1AB  41 C0 E8 02                     shr r8b, 2
0060A1AF  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A1B3  44 22 C7                        and r8b, dil
0060A1B6  45 8A CF                        mov r9b, r15b
0060A1B9  E8 E6 0C 00 00                  call 0x14060aea4
0060A1BE  45 33 D2                        xor r10d, r10d
0060A1C1  48 85 DB                        test rbx, rbx
0060A1C4  74 0B                           je 0x14060a1d1
0060A1C6  8B 43 08                        mov eax, dword ptr [rbx + 8]
0060A1C9  45 8A CF                        mov r9b, r15b
0060A1CC  41 84 C7                        test r15b, al
0060A1CF  75 03                           jne 0x14060a1d4
0060A1D1  45 8A CA                        mov r9b, r10b
0060A1D4  45 8A C5                        mov r8b, r13b
0060A1D7  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A1DB  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A1DF  E8 A4 0C 00 00                  call 0x14060ae88
0060A1E4  45 33 C9                        xor r9d, r9d
0060A1E7  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A1EB  45 33 C0                        xor r8d, r8d
0060A1EE  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A1F2  E8 91 0C 00 00                  call 0x14060ae88
0060A1F7  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A1FB  74 09                           je 0x14060a206
0060A1FD  41 8B CF                        mov ecx, r15d
0060A200  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A204  74 03                           je 0x14060a209
0060A206  41 8B CA                        mov ecx, r10d
0060A209  41 8B 43 08                     mov eax, dword ptr [r11 + 8]
0060A20D  83 E0 FE                        and eax, 0xfffffffe
0060A210  0B C1                           or eax, ecx
0060A212  41 89 43 08                     mov dword ptr [r11 + 8], eax
0060A216  48 85 F6                        test rsi, rsi
0060A219  74 13                           je 0x14060a22e
0060A21B  48 8B 06                        mov rax, qword ptr [rsi]
0060A21E  48 C1 E8 0E                     shr rax, 0xe
0060A222  40 22 C7                        and al, dil
0060A225  41 3A C7                        cmp al, r15b
0060A228  75 04                           jne 0x14060a22e
0060A22A  45 09 7B 20                     or dword ptr [r11 + 0x20], r15d
0060A22E  48 85 DB                        test rbx, rbx
0060A231  74 0C                           je 0x14060a23f
0060A233  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0060A236  41 84 C7                        test r15b, al
0060A239  74 04                           je 0x14060a23f
0060A23B  45 09 7B 20                     or dword ptr [r11 + 0x20], r15d
0060A23F  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A243  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A247  45 84 F6                        test r14b, r14b
0060A24A  74 0B                           je 0x14060a257
0060A24C  41 8B 43 20                     mov eax, dword ptr [r11 + 0x20]
0060A250  45 8A CF                        mov r9b, r15b
0060A253  A8 02                           test al, 2
0060A255  75 03                           jne 0x14060a25a
0060A257  45 8A CA                        mov r9b, r10b
0060A25A  45 8A C6                        mov r8b, r14b
0060A25D  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A261  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A265  E8 1E 0C 00 00                  call 0x14060ae88
0060A26A  48 85 F6                        test rsi, rsi
0060A26D  74 1D                           je 0x14060a28c
0060A26F  4C 8B 06                        mov r8, qword ptr [rsi]
0060A272  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A276  49 C1 E8 10                     shr r8, 0x10
0060A27A  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A27E  44 22 C7                        and r8b, dil
0060A281  45 8A CF                        mov r9b, r15b
0060A284  E8 1B 0C 00 00                  call 0x14060aea4
0060A289  45 33 D2                        xor r10d, r10d
0060A28C  48 85 DB                        test rbx, rbx
0060A28F  74 0A                           je 0x14060a29b
0060A291  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0060A294  45 8A CF                        mov r9b, r15b
0060A297  A8 02                           test al, 2
0060A299  75 03                           jne 0x14060a29e
0060A29B  45 8A CA                        mov r9b, r10b
0060A29E  45 8A C5                        mov r8b, r13b
0060A2A1  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A2A5  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A2A9  E8 DA 0B 00 00                  call 0x14060ae88
0060A2AE  45 33 C9                        xor r9d, r9d
0060A2B1  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A2B5  45 33 C0                        xor r8d, r8d
0060A2B8  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A2BC  E8 C7 0B 00 00                  call 0x14060ae88
0060A2C1  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A2C5  74 0A                           je 0x14060a2d1
0060A2C7  41 8D 41 02                     lea eax, [r9 + 2]
0060A2CB  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A2CF  74 03                           je 0x14060a2d4
0060A2D1  41 8B C2                        mov eax, r10d
0060A2D4  41 8B 7B 20                     mov edi, dword ptr [r11 + 0x20]
0060A2D8  41 BC 04 00 00 00               mov r12d, 4
0060A2DE  83 E7 FD                        and edi, 0xfffffffd
0060A2E1  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A2E5  0B F8                           or edi, eax
0060A2E7  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A2EB  41 89 7B 20                     mov dword ptr [r11 + 0x20], edi
0060A2EF  45 84 F6                        test r14b, r14b
0060A2F2  74 08                           je 0x14060a2fc
0060A2F4  45 8A CF                        mov r9b, r15b
0060A2F7  41 84 FC                        test r12b, dil
0060A2FA  75 03                           jne 0x14060a2ff
0060A2FC  45 8A CA                        mov r9b, r10b
0060A2FF  45 8A C6                        mov r8b, r14b
0060A302  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A306  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A30A  E8 79 0B 00 00                  call 0x14060ae88
0060A30F  48 85 F6                        test rsi, rsi
0060A312  74 1E                           je 0x14060a332
0060A314  4C 8B 06                        mov r8, qword ptr [rsi]
0060A317  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A31B  49 C1 E8 12                     shr r8, 0x12
0060A31F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A323  41 80 E0 03                     and r8b, 3
0060A327  45 8A CF                        mov r9b, r15b
0060A32A  E8 75 0B 00 00                  call 0x14060aea4
0060A32F  45 33 D2                        xor r10d, r10d
0060A332  48 85 DB                        test rbx, rbx
0060A335  74 0B                           je 0x14060a342
0060A337  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0060A33A  45 8A CF                        mov r9b, r15b
0060A33D  41 84 C4                        test r12b, al
0060A340  75 03                           jne 0x14060a345
0060A342  45 8A CA                        mov r9b, r10b
0060A345  45 8A C5                        mov r8b, r13b
0060A348  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A34C  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A350  E8 33 0B 00 00                  call 0x14060ae88
0060A355  45 33 C9                        xor r9d, r9d
0060A358  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A35C  45 33 C0                        xor r8d, r8d
0060A35F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A363  E8 20 0B 00 00                  call 0x14060ae88
0060A368  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A36C  74 09                           je 0x14060a377
0060A36E  41 8B C4                        mov eax, r12d
0060A371  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A375  74 03                           je 0x14060a37a
0060A377  41 8B C2                        mov eax, r10d
0060A37A  83 E7 FB                        and edi, 0xfffffffb
0060A37D  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A381  0B F8                           or edi, eax
0060A383  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A387  41 89 7B 20                     mov dword ptr [r11 + 0x20], edi
0060A38B  41 BF 08 00 00 00               mov r15d, 8
0060A391  45 84 F6                        test r14b, r14b
0060A394  74 08                           je 0x14060a39e
0060A396  41 B1 01                        mov r9b, 1
0060A399  41 84 FF                        test r15b, dil
0060A39C  75 03                           jne 0x14060a3a1
0060A39E  45 8A CA                        mov r9b, r10b
0060A3A1  45 8A C6                        mov r8b, r14b
0060A3A4  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A3A8  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A3AC  E8 D7 0A 00 00                  call 0x14060ae88
0060A3B1  48 85 F6                        test rsi, rsi
0060A3B4  74 1E                           je 0x14060a3d4
0060A3B6  4C 8B 06                        mov r8, qword ptr [rsi]
0060A3B9  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A3BD  49 C1 E8 14                     shr r8, 0x14
0060A3C1  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A3C5  41 80 E0 03                     and r8b, 3
0060A3C9  41 B1 01                        mov r9b, 1
0060A3CC  E8 D3 0A 00 00                  call 0x14060aea4
0060A3D1  45 33 D2                        xor r10d, r10d
0060A3D4  48 85 DB                        test rbx, rbx
0060A3D7  74 0B                           je 0x14060a3e4
0060A3D9  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0060A3DC  41 B1 01                        mov r9b, 1
0060A3DF  41 84 C7                        test r15b, al
0060A3E2  75 03                           jne 0x14060a3e7
0060A3E4  45 8A CA                        mov r9b, r10b
0060A3E7  45 8A C5                        mov r8b, r13b
0060A3EA  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A3EE  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A3F2  E8 91 0A 00 00                  call 0x14060ae88
0060A3F7  45 33 C9                        xor r9d, r9d
0060A3FA  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A3FE  45 33 C0                        xor r8d, r8d
0060A401  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A405  E8 7E 0A 00 00                  call 0x14060ae88
0060A40A  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A40E  74 06                           je 0x14060a416
0060A410  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A414  74 03                           je 0x14060a419
0060A416  45 8B FA                        mov r15d, r10d
0060A419  83 E7 F7                        and edi, 0xfffffff7
0060A41C  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A420  41 0B FF                        or edi, r15d
0060A423  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A427  41 89 7B 20                     mov dword ptr [r11 + 0x20], edi
0060A42B  41 BF 10 00 00 00               mov r15d, 0x10
0060A431  45 84 F6                        test r14b, r14b
0060A434  74 08                           je 0x14060a43e
0060A436  41 B1 01                        mov r9b, 1
0060A439  41 84 FF                        test r15b, dil
0060A43C  75 03                           jne 0x14060a441
0060A43E  45 8A CA                        mov r9b, r10b
0060A441  45 8A C6                        mov r8b, r14b
0060A444  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A448  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A44C  E8 37 0A 00 00                  call 0x14060ae88
0060A451  48 85 F6                        test rsi, rsi
0060A454  74 1E                           je 0x14060a474
0060A456  4C 8B 06                        mov r8, qword ptr [rsi]
0060A459  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A45D  49 C1 E8 16                     shr r8, 0x16
0060A461  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A465  41 80 E0 03                     and r8b, 3
0060A469  41 B1 01                        mov r9b, 1
0060A46C  E8 33 0A 00 00                  call 0x14060aea4
0060A471  45 33 D2                        xor r10d, r10d
0060A474  48 85 DB                        test rbx, rbx
0060A477  74 0B                           je 0x14060a484
0060A479  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
0060A47C  41 B1 01                        mov r9b, 1
0060A47F  41 84 C7                        test r15b, al
0060A482  75 03                           jne 0x14060a487
0060A484  45 8A CA                        mov r9b, r10b
0060A487  45 8A C5                        mov r8b, r13b
0060A48A  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A48E  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A492  E8 F1 09 00 00                  call 0x14060ae88
0060A497  45 33 C9                        xor r9d, r9d
0060A49A  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A49E  45 33 C0                        xor r8d, r8d
0060A4A1  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A4A5  E8 DE 09 00 00                  call 0x14060ae88
0060A4AA  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A4AE  74 06                           je 0x14060a4b6
0060A4B0  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A4B4  74 03                           je 0x14060a4b9
0060A4B6  45 8B FA                        mov r15d, r10d
0060A4B9  83 E7 EF                        and edi, 0xffffffef
0060A4BC  41 0B FF                        or edi, r15d
0060A4BF  41 BF 01 00 00 00               mov r15d, 1
0060A4C5  41 89 7B 20                     mov dword ptr [r11 + 0x20], edi
0060A4C9  48 85 F6                        test rsi, rsi
0060A4CC  74 11                           je 0x14060a4df
0060A4CE  48 8B 06                        mov rax, qword ptr [rsi]
0060A4D1  C0 E8 04                        shr al, 4
0060A4D4  24 03                           and al, 3
0060A4D6  41 3A C7                        cmp al, r15b
0060A4D9  75 04                           jne 0x14060a4df
0060A4DB  45 09 7B 24                     or dword ptr [r11 + 0x24], r15d
0060A4DF  48 85 DB                        test rbx, rbx
0060A4E2  74 0C                           je 0x14060a4f0
0060A4E4  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0060A4E7  41 84 C7                        test r15b, al
0060A4EA  74 04                           je 0x14060a4f0
0060A4EC  45 09 7B 24                     or dword ptr [r11 + 0x24], r15d
0060A4F0  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A4F4  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A4F8  45 84 F6                        test r14b, r14b
0060A4FB  74 0B                           je 0x14060a508
0060A4FD  41 8B 43 24                     mov eax, dword ptr [r11 + 0x24]
0060A501  45 8A CF                        mov r9b, r15b
0060A504  A8 02                           test al, 2
0060A506  75 03                           jne 0x14060a50b
0060A508  45 8A CA                        mov r9b, r10b
0060A50B  45 8A C6                        mov r8b, r14b
0060A50E  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A512  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A516  E8 6D 09 00 00                  call 0x14060ae88
0060A51B  48 85 F6                        test rsi, rsi
0060A51E  74 1E                           je 0x14060a53e
0060A520  4C 8B 06                        mov r8, qword ptr [rsi]
0060A523  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A527  41 C0 E8 06                     shr r8b, 6
0060A52B  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A52F  41 80 E0 03                     and r8b, 3
0060A533  45 33 C9                        xor r9d, r9d
0060A536  E8 69 09 00 00                  call 0x14060aea4
0060A53B  45 33 D2                        xor r10d, r10d
0060A53E  48 85 DB                        test rbx, rbx
0060A541  74 0A                           je 0x14060a54d
0060A543  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0060A546  45 8A CF                        mov r9b, r15b
0060A549  A8 02                           test al, 2
0060A54B  75 03                           jne 0x14060a550
0060A54D  45 8A CA                        mov r9b, r10b
0060A550  45 8A C5                        mov r8b, r13b
0060A553  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A557  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A55B  E8 28 09 00 00                  call 0x14060ae88
0060A560  45 33 C9                        xor r9d, r9d
0060A563  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A567  45 33 C0                        xor r8d, r8d
0060A56A  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A56E  E8 15 09 00 00                  call 0x14060ae88
0060A573  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A577  74 0A                           je 0x14060a583
0060A579  41 8D 41 02                     lea eax, [r9 + 2]
0060A57D  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A581  74 03                           je 0x14060a586
0060A583  41 8B C2                        mov eax, r10d
0060A586  41 8B 7B 24                     mov edi, dword ptr [r11 + 0x24]
0060A58A  83 E7 FD                        and edi, 0xfffffffd
0060A58D  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A591  0B F8                           or edi, eax
0060A593  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A597  41 89 7B 24                     mov dword ptr [r11 + 0x24], edi
0060A59B  45 84 F6                        test r14b, r14b
0060A59E  74 08                           je 0x14060a5a8
0060A5A0  45 8A CF                        mov r9b, r15b
0060A5A3  41 84 FC                        test r12b, dil
0060A5A6  75 03                           jne 0x14060a5ab
0060A5A8  45 8A CA                        mov r9b, r10b
0060A5AB  45 8A C6                        mov r8b, r14b
0060A5AE  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A5B2  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A5B6  E8 CD 08 00 00                  call 0x14060ae88
0060A5BB  48 85 F6                        test rsi, rsi
0060A5BE  74 1E                           je 0x14060a5de
0060A5C0  4C 8B 06                        mov r8, qword ptr [rsi]
0060A5C3  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A5C7  49 C1 E8 08                     shr r8, 8
0060A5CB  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A5CF  41 80 E0 03                     and r8b, 3
0060A5D3  45 33 C9                        xor r9d, r9d
0060A5D6  E8 C9 08 00 00                  call 0x14060aea4
0060A5DB  45 33 D2                        xor r10d, r10d
0060A5DE  48 85 DB                        test rbx, rbx
0060A5E1  74 0B                           je 0x14060a5ee
0060A5E3  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0060A5E6  45 8A CF                        mov r9b, r15b
0060A5E9  41 84 C4                        test r12b, al
0060A5EC  75 03                           jne 0x14060a5f1
0060A5EE  45 8A CA                        mov r9b, r10b
0060A5F1  45 8A C5                        mov r8b, r13b
0060A5F4  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A5F8  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A5FC  E8 87 08 00 00                  call 0x14060ae88
0060A601  45 33 C9                        xor r9d, r9d
0060A604  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A608  45 33 C0                        xor r8d, r8d
0060A60B  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A60F  E8 74 08 00 00                  call 0x14060ae88
0060A614  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A618  74 06                           je 0x14060a620
0060A61A  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A61E  74 03                           je 0x14060a623
0060A620  45 8B E2                        mov r12d, r10d
0060A623  83 E7 FB                        and edi, 0xfffffffb
0060A626  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A62A  41 0B FC                        or edi, r12d
0060A62D  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A631  41 89 7B 24                     mov dword ptr [r11 + 0x24], edi
0060A635  45 84 F6                        test r14b, r14b
0060A638  74 0C                           je 0x14060a646
0060A63A  41 8B 43 28                     mov eax, dword ptr [r11 + 0x28]
0060A63E  45 8A CF                        mov r9b, r15b
0060A641  41 84 C7                        test r15b, al
0060A644  75 03                           jne 0x14060a649
0060A646  45 8A CA                        mov r9b, r10b
0060A649  45 8A C6                        mov r8b, r14b
0060A64C  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A650  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A654  E8 2F 08 00 00                  call 0x14060ae88
0060A659  45 33 C9                        xor r9d, r9d
0060A65C  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A660  45 33 C0                        xor r8d, r8d
0060A663  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A667  E8 1C 08 00 00                  call 0x14060ae88
0060A66C  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A670  74 09                           je 0x14060a67b
0060A672  41 8B CF                        mov ecx, r15d
0060A675  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A679  74 03                           je 0x14060a67e
0060A67B  41 8B CA                        mov ecx, r10d
0060A67E  41 8B 43 28                     mov eax, dword ptr [r11 + 0x28]
0060A682  83 E0 FE                        and eax, 0xfffffffe
0060A685  44 88 55 E0                     mov byte ptr [rbp - 0x20], r10b
0060A689  0B C1                           or eax, ecx
0060A68B  44 88 55 E1                     mov byte ptr [rbp - 0x1f], r10b
0060A68F  41 89 43 28                     mov dword ptr [r11 + 0x28], eax
0060A693  45 84 F6                        test r14b, r14b
0060A696  74 07                           je 0x14060a69f
0060A698  45 8A CF                        mov r9b, r15b
0060A69B  A8 02                           test al, 2
0060A69D  75 03                           jne 0x14060a6a2
0060A69F  45 8A CA                        mov r9b, r10b
0060A6A2  45 8A C6                        mov r8b, r14b
0060A6A5  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A6A9  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A6AD  E8 D6 07 00 00                  call 0x14060ae88
0060A6B2  45 33 C9                        xor r9d, r9d
0060A6B5  48 8D 55 E1                     lea rdx, [rbp - 0x1f]
0060A6B9  45 33 C0                        xor r8d, r8d
0060A6BC  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0060A6C0  E8 C3 07 00 00                  call 0x14060ae88
0060A6C5  44 38 55 E0                     cmp byte ptr [rbp - 0x20], r10b
0060A6C9  74 0A                           je 0x14060a6d5
0060A6CB  41 8D 49 02                     lea ecx, [r9 + 2]
0060A6CF  44 38 55 E1                     cmp byte ptr [rbp - 0x1f], r10b
0060A6D3  74 03                           je 0x14060a6d8
0060A6D5  41 8B CA                        mov ecx, r10d
0060A6D8  83 E0 FD                        and eax, 0xfffffffd
0060A6DB  0B C1                           or eax, ecx
0060A6DD  41 89 43 28                     mov dword ptr [r11 + 0x28], eax
0060A6E1  48 85 F6                        test rsi, rsi
0060A6E4  74 12                           je 0x14060a6f8
0060A6E6  48 8B 06                        mov rax, qword ptr [rsi]
0060A6E9  48 C1 E8 0A                     shr rax, 0xa
0060A6ED  24 03                           and al, 3
0060A6EF  41 3A C7                        cmp al, r15b
0060A6F2  75 04                           jne 0x14060a6f8
0060A6F4  45 09 7B 34                     or dword ptr [r11 + 0x34], r15d
0060A6F8  48 85 DB                        test rbx, rbx
0060A6FB  74 0C                           je 0x14060a709
0060A6FD  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
0060A700  41 84 C7                        test r15b, al
0060A703  74 04                           je 0x14060a709
0060A705  45 09 7B 34                     or dword ptr [r11 + 0x34], r15d
0060A709  48 85 F6                        test rsi, rsi
0060A70C  74 13                           je 0x14060a721
0060A70E  48 8B 06                        mov rax, qword ptr [rsi]
0060A711  48 C1 E8 0C                     shr rax, 0xc
0060A715  24 03                           and al, 3
0060A717  41 3A C7                        cmp al, r15b
0060A71A  75 05                           jne 0x14060a721
0060A71C  41 83 4B 34 02                  or dword ptr [r11 + 0x34], 2
0060A721  48 85 DB                        test rbx, rbx
0060A724  74 0C                           je 0x14060a732
0060A726  8B 43 14                        mov eax, dword ptr [rbx + 0x14]
0060A729  A8 02                           test al, 2
0060A72B  74 05                           je 0x14060a732
0060A72D  41 83 4B 34 02                  or dword ptr [r11 + 0x34], 2
0060A732  45 84 F6                        test r14b, r14b
0060A735  74 06                           je 0x14060a73d
0060A737  41 8A 53 38                     mov dl, byte ptr [r11 + 0x38]
0060A73B  EB 03                           jmp 0x14060a740
0060A73D  41 8A D2                        mov dl, r10b
0060A740  48 85 DB                        test rbx, rbx
0060A743  74 0E                           je 0x14060a753
0060A745  0F B6 4B 18                     movzx ecx, byte ptr [rbx + 0x18]
0060A749  3A CA                           cmp cl, dl
0060A74B  0F B6 C2                        movzx eax, dl
0060A74E  0F 47 C1                        cmova eax, ecx
0060A751  8A D0                           mov dl, al
0060A753  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0060A757  41 88 53 38                     mov byte ptr [r11 + 0x38], dl
0060A75B  4C 89 18                        mov qword ptr [rax], r11
0060A75E  33 C0                           xor eax, eax
0060A760  4C 8D 5C 24 40                  lea r11, [rsp + 0x40]
0060A765  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0060A769  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0060A76D  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0060A771  49 8B E3                        mov rsp, r11
0060A774  41 5F                           pop r15
0060A776  41 5E                           pop r14
0060A778  41 5D                           pop r13
0060A77A  41 5C                           pop r12
0060A77C  5D                              pop rbp
0060A77D  C3                              ret
0060A77E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeConstructAntiTamperPolicy(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int8 v_stack_m47;
    unsigned __int8 v_stack_m48;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    v_rsp = (v_rsp) - (64);
    v_stack_m38 = a5;
    if (a2 != 0) goto loc_0060A0E5;
    if (a3 != 0) goto loc_0060A0E8;
    if (a1 == 0) goto loc_0060A75E;
    result = SepConstructAntiTamperBaselinePolicy(a1, a5, a3, a4);
    goto loc_0060A760;
loc_0060A0E5:
loc_0060A0E8:
    v_r13 = (a3 != 0) ? 1 : 0;
    v_r14 = 0;
    if (a1 == 0) goto loc_0060A11D;
    result = SepConstructAntiTamperBaselinePolicy(a1, v_stack_m40, a3, a4);
    v_r10 = 0;
    if (sign_flag) goto loc_0060A760;
    v_r14 = (v_stack_m40 != 0) ? 1 : 0;
    if (v_stack_m40 != 0) goto loc_0060A147;
loc_0060A11D:
    result = ExAllocatePool2(256, 64, (unsigned int)(0x50416553ULL), a4);
    v_r10 = 0;
    if (result != 0) goto loc_0060A147;
    goto loc_0060A760;
loc_0060A147:
    if (a2 == 0) goto loc_0060A163;
    result = (unsigned __int8)((*(unsigned __int64 *)(a2)) & (3));
    if (((unsigned __int8)(result)) == 1) {
    }
    if (a3 == 0) goto loc_0060A173;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 4))))) != 0) {
    }
    v_stack_m48 = 0;
    v_stack_m47 = 0;
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A18C;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 8))))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(a2);
        a2 = v_stack_m47;
        a3 = (unsigned __int8)((a3) >> (2));
        a1 = v_stack_m48;
        a3 = (unsigned __int8)((a3) & (3));
        a4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(a1, a2, a3, a4);
        v_r10 = 0;
    }
    if (a3 == 0) goto loc_0060A1D1;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 8))))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r13), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A206;
    if (v_stack_m47 != 0) {
        a1 = 0;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 8))) & (0xFFFFFFFEULL));
    result = (unsigned int)((result) | ((unsigned int)(a1)));
    *(unsigned int *)(result + 8) = (unsigned int)(result);
    if (a2 == 0) goto loc_0060A22E;
    result = (*(unsigned __int64 *)(a2)) >> (14);
    result = (unsigned __int8)((result) & (3));
    if (((unsigned __int8)(result)) == 1) {
    }
    if (0 == 0) goto loc_0060A23F;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12))))) != 0) {
    }
    v_stack_m48 = 0;
    v_stack_m47 = 0;
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A257;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 32)))) & (2)) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(a2);
        a2 = v_stack_m47;
        a3 = (a3) >> (16);
        a1 = v_stack_m48;
        a3 = (unsigned __int8)((a3) & (3));
        a4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(a1, a2, a3, a4);
        v_r10 = 0;
    }
    if (a3 == 0) goto loc_0060A29B;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12)))) & (2)) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r13), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A2D1;
    result = a4 + 2;
    if (v_stack_m47 != 0) {
        result = 0;
    }
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 32))) & (0xFFFFFFFDULL));
    v_stack_m48 = 0;
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    v_stack_m47 = 0;
    *(unsigned int *)(result + 32) = (unsigned int)(v_rdi);
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A2FC;
    if (((4) & ((unsigned __int8)(v_rdi))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(a2);
        a2 = v_stack_m47;
        a3 = (a3) >> (18);
        a1 = v_stack_m48;
        a3 = (unsigned __int8)((a3) & (3));
        a4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(a1, a2, a3, a4);
        v_r10 = 0;
    }
    if (a3 == 0) goto loc_0060A342;
    if (((4) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12))))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r13), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A377;
    result = 4;
    if (v_stack_m47 != 0) {
        result = 0;
    }
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFBULL));
    v_stack_m48 = 0;
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    v_stack_m47 = 0;
    *(unsigned int *)(result + 32) = (unsigned int)(v_rdi);
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A39E;
    if (((8) & ((unsigned __int8)(v_rdi))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(a2);
        a2 = v_stack_m47;
        a3 = (a3) >> (20);
        a1 = v_stack_m48;
        a3 = (unsigned __int8)((a3) & (3));
        a4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(a1, a2, a3, a4);
        v_r10 = 0;
    }
    if (a3 == 0) goto loc_0060A3E4;
    if (((8) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12))))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r13), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A416;
    v_r15 = 8;
    if (v_stack_m47 != 0) {
        v_r15 = 0;
    }
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFF7ULL));
    v_stack_m48 = 0;
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_r15)));
    v_stack_m47 = 0;
    *(unsigned int *)(result + 32) = (unsigned int)(v_rdi);
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A43E;
    if (((16) & ((unsigned __int8)(v_rdi))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(a2);
        a2 = v_stack_m47;
        a3 = (a3) >> (22);
        a1 = v_stack_m48;
        a3 = (unsigned __int8)((a3) & (3));
        a4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(a1, a2, a3, a4);
        v_r10 = 0;
    }
    if (a3 == 0) goto loc_0060A484;
    if (((16) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12))))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r13), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A4B6;
    v_r15 = 16;
    if (v_stack_m47 != 0) {
        v_r15 = 0;
    }
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFEFULL));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_r15)));
    *(unsigned int *)(result + 32) = (unsigned int)(v_rdi);
    if (a2 == 0) goto loc_0060A4DF;
    result = (unsigned __int8)((*(unsigned __int64 *)(a2)) >> (4));
    result = (unsigned __int8)((result) & (3));
    if (((unsigned __int8)(result)) == 1) {
    }
    if (0 == 0) goto loc_0060A4F0;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 16))))) != 0) {
    }
    v_stack_m48 = 0;
    v_stack_m47 = 0;
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A508;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 36)))) & (2)) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(a2);
        a2 = v_stack_m47;
        a3 = (unsigned __int8)((a3) >> (6));
        a1 = v_stack_m48;
        a3 = (unsigned __int8)((a3) & (3));
        a4 = 0;
        result = SepFoldAntiTamperRelaxationIfeo(a1, a2, a3, a4);
        v_r10 = 0;
    }
    if (a3 == 0) goto loc_0060A54D;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 16)))) & (2)) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r13), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A583;
    result = a4 + 2;
    if (v_stack_m47 != 0) {
        result = 0;
    }
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 36))) & (0xFFFFFFFDULL));
    v_stack_m48 = 0;
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    v_stack_m47 = 0;
    *(unsigned int *)(result + 36) = (unsigned int)(v_rdi);
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A5A8;
    if (((4) & ((unsigned __int8)(v_rdi))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    if (a2 != 0) {
        a3 = *(unsigned __int64 *)(a2);
        a2 = v_stack_m47;
        a3 = (a3) >> (8);
        a1 = v_stack_m48;
        a3 = (unsigned __int8)((a3) & (3));
        a4 = 0;
        result = SepFoldAntiTamperRelaxationIfeo(a1, a2, a3, a4);
        v_r10 = 0;
    }
    if (a3 == 0) goto loc_0060A5EE;
    if (((4) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 16))))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r13), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A620;
    v_r12 = 4;
    if (v_stack_m47 != 0) {
        v_r12 = 0;
    }
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFBULL));
    v_stack_m48 = 0;
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_r12)));
    v_stack_m47 = 0;
    *(unsigned int *)(result + 36) = (unsigned int)(v_rdi);
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A646;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 40))))) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A67B;
    if (v_stack_m47 != 0) {
        a1 = 0;
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 40))) & (0xFFFFFFFEULL));
    v_stack_m48 = 0;
    result = (unsigned int)((result) | ((unsigned int)(a1)));
    v_stack_m47 = 0;
    *(unsigned int *)(result + 40) = (unsigned int)(result);
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A69F;
    if ((((unsigned __int8)(result)) & (2)) == 0) {
        a4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (unsigned __int8)(v_r14), a4);
    a4 = 0;
    a3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, a3, a4);
    if (v_stack_m48 == 0) goto loc_0060A6D5;
    if (v_stack_m47 != 0) {
        a1 = 0;
    }
    result = (unsigned int)((result) & (0xFFFFFFFDULL));
    result = (unsigned int)((result) | ((unsigned int)(a1)));
    *(unsigned int *)(result + 40) = (unsigned int)(result);
    if (a2 == 0) goto loc_0060A6F8;
    result = (*(unsigned __int64 *)(a2)) >> (10);
    result = (unsigned __int8)((result) & (3));
    if (((unsigned __int8)(result)) == 1) {
    }
    if (0 == 0) goto loc_0060A709;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 20))))) != 0) {
    }
    if (a2 == 0) goto loc_0060A721;
    result = (*(unsigned __int64 *)(a2)) >> (12);
    result = (unsigned __int8)((result) & (3));
    if (((unsigned __int8)(result)) == 1) {
    }
    if (0 == 0) goto loc_0060A732;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 20)))) & (2)) != 0) {
    }
    if ((unsigned __int8)(v_r14) == 0) goto loc_0060A73D;
    goto loc_0060A740;
loc_0060A73D:
loc_0060A740:
    result = (unsigned int)(*(unsigned int *)(a3 + 20));
    if (0 != 0) {
        a1 = *(unsigned __int8 *)(a3 + 24);
        result = 0;
        if (((unsigned __int8)(a1)) > 0) { result = (unsigned int)(a1); }
        a2 = (unsigned __int8)(result);
    }
    *(unsigned __int8 *)(result + 56) = (unsigned __int8)(a2);
    *(unsigned __int64 *)(v_stack_m38) = result;
loc_0060A75E:
    result = 0;
loc_0060A760:
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeConstructAntiTamperPolicy(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint8_t v_stack_m47;
    uint8_t v_stack_m48;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    local_rsp = (local_rsp) - (64);
    v_stack_m38 = Arg5;
    if (Arg2 != 0) goto loc_0060A0E5;
    if (Arg3 != 0) goto loc_0060A0E8;
    if (Arg1 == 0) goto loc_0060A75E;
    result = SepConstructAntiTamperBaselinePolicy(Arg1, Arg5, Arg3, Arg4);
    goto loc_0060A760;
loc_0060A0E5:
loc_0060A0E8:
    local_r13 = (Arg3 != 0) ? 1 : 0;
    local_r14 = 0;
    if (Arg1 == 0) goto loc_0060A11D;
    result = SepConstructAntiTamperBaselinePolicy(Arg1, v_stack_m40, Arg3, Arg4);
    local_r10 = 0;
    if (sign_flag) goto loc_0060A760;
    local_r14 = (v_stack_m40 != 0) ? 1 : 0;
    if (v_stack_m40 != 0) goto loc_0060A147;
loc_0060A11D:
    result = ExAllocatePool2(256, 64, (uint32_t)(0x50416553ULL), Arg4);
    local_r10 = 0;
    if (result != 0) goto loc_0060A147;
    goto loc_0060A760;
loc_0060A147:
    if (Arg2 == 0) goto loc_0060A163;
    result = (uint8_t)((*(uint64_t *)(Arg2)) & (3));
    if (((uint8_t)(result)) == 1) {
    }
    if (Arg3 == 0) goto loc_0060A173;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4))))) != 0) {
    }
    v_stack_m48 = 0;
    v_stack_m47 = 0;
    if ((uint8_t)(local_r14) == 0) goto loc_0060A18C;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x8))))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(Arg2);
        Arg2 = v_stack_m47;
        Arg3 = (uint8_t)((Arg3) >> (2));
        Arg1 = v_stack_m48;
        Arg3 = (uint8_t)((Arg3) & (3));
        Arg4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    if (Arg3 == 0) goto loc_0060A1D1;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x8))))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r13), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A206;
    if (v_stack_m47 != 0) {
        Arg1 = 0;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x8))) & (0xFFFFFFFEULL));
    result = (uint32_t)((result) | ((uint32_t)(Arg1)));
    *(uint32_t *)(result + 0x8) = (uint32_t)(result);
    if (Arg2 == 0) goto loc_0060A22E;
    result = (*(uint64_t *)(Arg2)) >> (14);
    result = (uint8_t)((result) & (3));
    if (((uint8_t)(result)) == 1) {
    }
    if (0 == 0) goto loc_0060A23F;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))))) != 0) {
    }
    v_stack_m48 = 0;
    v_stack_m47 = 0;
    if ((uint8_t)(local_r14) == 0) goto loc_0060A257;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x20)))) & (2)) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(Arg2);
        Arg2 = v_stack_m47;
        Arg3 = (Arg3) >> (16);
        Arg1 = v_stack_m48;
        Arg3 = (uint8_t)((Arg3) & (3));
        Arg4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    if (Arg3 == 0) goto loc_0060A29B;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC)))) & (2)) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r13), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A2D1;
    result = Arg4 + 2;
    if (v_stack_m47 != 0) {
        result = 0;
    }
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x20))) & (0xFFFFFFFDULL));
    v_stack_m48 = 0;
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    v_stack_m47 = 0;
    *(uint32_t *)(result + 0x20) = (uint32_t)(local_rdi);
    if ((uint8_t)(local_r14) == 0) goto loc_0060A2FC;
    if (((4) & ((uint8_t)(local_rdi))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(Arg2);
        Arg2 = v_stack_m47;
        Arg3 = (Arg3) >> (18);
        Arg1 = v_stack_m48;
        Arg3 = (uint8_t)((Arg3) & (3));
        Arg4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    if (Arg3 == 0) goto loc_0060A342;
    if (((4) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r13), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A377;
    result = 4;
    if (v_stack_m47 != 0) {
        result = 0;
    }
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFBULL));
    v_stack_m48 = 0;
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    v_stack_m47 = 0;
    *(uint32_t *)(result + 0x20) = (uint32_t)(local_rdi);
    if ((uint8_t)(local_r14) == 0) goto loc_0060A39E;
    if (((8) & ((uint8_t)(local_rdi))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(Arg2);
        Arg2 = v_stack_m47;
        Arg3 = (Arg3) >> (20);
        Arg1 = v_stack_m48;
        Arg3 = (uint8_t)((Arg3) & (3));
        Arg4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    if (Arg3 == 0) goto loc_0060A3E4;
    if (((8) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r13), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A416;
    local_r15 = 8;
    if (v_stack_m47 != 0) {
        local_r15 = 0;
    }
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFF7ULL));
    v_stack_m48 = 0;
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(local_r15)));
    v_stack_m47 = 0;
    *(uint32_t *)(result + 0x20) = (uint32_t)(local_rdi);
    if ((uint8_t)(local_r14) == 0) goto loc_0060A43E;
    if (((16) & ((uint8_t)(local_rdi))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(Arg2);
        Arg2 = v_stack_m47;
        Arg3 = (Arg3) >> (22);
        Arg1 = v_stack_m48;
        Arg3 = (uint8_t)((Arg3) & (3));
        Arg4 = 1;
        result = SepFoldAntiTamperRelaxationIfeo(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    if (Arg3 == 0) goto loc_0060A484;
    if (((16) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r13), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A4B6;
    local_r15 = 16;
    if (v_stack_m47 != 0) {
        local_r15 = 0;
    }
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFEFULL));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(local_r15)));
    *(uint32_t *)(result + 0x20) = (uint32_t)(local_rdi);
    if (Arg2 == 0) goto loc_0060A4DF;
    result = (uint8_t)((*(uint64_t *)(Arg2)) >> (4));
    result = (uint8_t)((result) & (3));
    if (((uint8_t)(result)) == 1) {
    }
    if (0 == 0) goto loc_0060A4F0;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10))))) != 0) {
    }
    v_stack_m48 = 0;
    v_stack_m47 = 0;
    if ((uint8_t)(local_r14) == 0) goto loc_0060A508;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x24)))) & (2)) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(Arg2);
        Arg2 = v_stack_m47;
        Arg3 = (uint8_t)((Arg3) >> (6));
        Arg1 = v_stack_m48;
        Arg3 = (uint8_t)((Arg3) & (3));
        Arg4 = 0;
        result = SepFoldAntiTamperRelaxationIfeo(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    if (Arg3 == 0) goto loc_0060A54D;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10)))) & (2)) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r13), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A583;
    result = Arg4 + 2;
    if (v_stack_m47 != 0) {
        result = 0;
    }
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x24))) & (0xFFFFFFFDULL));
    v_stack_m48 = 0;
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    v_stack_m47 = 0;
    *(uint32_t *)(result + 0x24) = (uint32_t)(local_rdi);
    if ((uint8_t)(local_r14) == 0) goto loc_0060A5A8;
    if (((4) & ((uint8_t)(local_rdi))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    if (Arg2 != 0) {
        Arg3 = *(uint64_t *)(Arg2);
        Arg2 = v_stack_m47;
        Arg3 = (Arg3) >> (8);
        Arg1 = v_stack_m48;
        Arg3 = (uint8_t)((Arg3) & (3));
        Arg4 = 0;
        result = SepFoldAntiTamperRelaxationIfeo(Arg1, Arg2, Arg3, Arg4);
        local_r10 = 0;
    }
    if (Arg3 == 0) goto loc_0060A5EE;
    if (((4) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x10))))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r13), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A620;
    local_r12 = 4;
    if (v_stack_m47 != 0) {
        local_r12 = 0;
    }
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFBULL));
    v_stack_m48 = 0;
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(local_r12)));
    v_stack_m47 = 0;
    *(uint32_t *)(result + 0x24) = (uint32_t)(local_rdi);
    if ((uint8_t)(local_r14) == 0) goto loc_0060A646;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x28))))) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A67B;
    if (v_stack_m47 != 0) {
        Arg1 = 0;
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x28))) & (0xFFFFFFFEULL));
    v_stack_m48 = 0;
    result = (uint32_t)((result) | ((uint32_t)(Arg1)));
    v_stack_m47 = 0;
    *(uint32_t *)(result + 0x28) = (uint32_t)(result);
    if ((uint8_t)(local_r14) == 0) goto loc_0060A69F;
    if ((((uint8_t)(result)) & (2)) == 0) {
        Arg4 = 0;
    }
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, (uint8_t)(local_r14), Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = SepFoldAntiTamperRelaxation(v_stack_m48, v_stack_m47, Arg3, Arg4);
    if (v_stack_m48 == 0) goto loc_0060A6D5;
    if (v_stack_m47 != 0) {
        Arg1 = 0;
    }
    result = (uint32_t)((result) & (0xFFFFFFFDULL));
    result = (uint32_t)((result) | ((uint32_t)(Arg1)));
    *(uint32_t *)(result + 0x28) = (uint32_t)(result);
    if (Arg2 == 0) goto loc_0060A6F8;
    result = (*(uint64_t *)(Arg2)) >> (10);
    result = (uint8_t)((result) & (3));
    if (((uint8_t)(result)) == 1) {
    }
    if (0 == 0) goto loc_0060A709;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x14))))) != 0) {
    }
    if (Arg2 == 0) goto loc_0060A721;
    result = (*(uint64_t *)(Arg2)) >> (12);
    result = (uint8_t)((result) & (3));
    if (((uint8_t)(result)) == 1) {
    }
    if (0 == 0) goto loc_0060A732;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x14)))) & (2)) != 0) {
    }
    if ((uint8_t)(local_r14) == 0) goto loc_0060A73D;
    goto loc_0060A740;
loc_0060A73D:
loc_0060A740:
    result = (uint32_t)(*(uint32_t *)(Arg3 + 0x14));
    if (0 != 0) {
        Arg1 = *(uint8_t *)(Arg3 + 0x18);
        result = 0;
        if (((uint8_t)(Arg1)) > 0) { result = (uint32_t)(Arg1); }
        Arg2 = (uint8_t)(result);
    }
    *(uint8_t *)(result + 0x38) = (uint8_t)(Arg2);
    *(uint64_t *)(v_stack_m38) = result;
loc_0060A75E:
    result = 0;
loc_0060A760:
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0060A094&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
