# sub_00BE7AF8

- RVA: `0x00BE7AF8`–`0x00BE837B` (길이 `2,179` bytes)
- VA: `0x0000000140BE7AF8`
- 실행 섹션: `INITKDBG`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2BC0`
- 디코드: `625`개 명령, `2,179/2,179` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BE7C0B` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE7C37` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE7C4E` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE7C83` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE7F53` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE811E` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE8148` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE8172` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE819F` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)
- `0x00BE8359` → [KeGuardDispatchICall](KeGuardDispatchICall_function_00BEAA60.md) (function, `0x00BEAA60`)

### Direct callers
- [sub_0050C0E0](../../text/50/Unknown_function_0050C0E0.md) at `0x00511786`
- [sub_0050C0E0](../../text/50/Unknown_function_0050C0E0.md) at `0x00511CB7`
- [sub_0050C0E0](../../text/50/Unknown_function_0050C0E0.md) at `0x005128E6`
- [FsRtlMdlReadCompleteDevEx](../BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BD1FBB`
- [FsRtlMdlReadCompleteDevEx](../BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BD224E`
- [FsRtlMdlReadCompleteDevEx](../BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BD77E3`
- [FsRtlMdlReadCompleteDevEx](../BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BD7D33`
- [FsRtlMdlReadCompleteDevEx](../BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BD8943`
- [FsRtlMdlReadCompleteDevEx](../BD/FsRtlMdlReadCompleteDevEx_function_00BD1010.md) at `0x00BE19B5`
- [sub_00BE3A04](Unknown_function_00BE3A04.md) at `0x00BE42BC`
- [sub_00BE3A04](Unknown_function_00BE3A04.md) at `0x00BE4765`
- [sub_00BE3A04](Unknown_function_00BE3A04.md) at `0x00BE53BD`
- [sub_00BE60B0](Unknown_function_00BE60B0.md) at `0x00BE6172`
- [sub_00BEFF8C](../../init/BE/Unknown_function_00BEFF8C.md) at `0x00BF0130`
- [sub_00BEFF8C](../../init/BE/Unknown_function_00BEFF8C.md) at `0x00BF0ED5`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF843B`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF856B`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF8996`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BF9AF2`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BFA0E0`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BFB5E7`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BFD285`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BFD810`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00BFEB23`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C008BF`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C00E0F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C01F04`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0342F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C03768`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C03B7A`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C03E3F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0411E`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C042B6`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C04446`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C045F6`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C04882`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C04B4F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C04E95`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C05211`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C054E4`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C057AE`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C05A5F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C065BD`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C069F5`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C06E1E`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0786A`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C07C1C`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C07DCC`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C07FA2`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C08436`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C086DF`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C08A83`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C08D30`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C090C1`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0953B`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C09AD3`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C09E3F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0A507`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0ABF1`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0B380`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0BC17`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0C43F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0CCFF`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0D1C4`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0D82C`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0DB51`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0DEEF`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0E07C`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0E21E`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0E3FD`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0E5A1`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0E77A`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0E9A3`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0EBBF`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0EE77`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0F20A`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0F447`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0F5FA`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0F80F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0FACD`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0FD01`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C0FFF7`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C10304`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C1078F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C1153D`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C11A9F`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C128AD`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C138CA`
- [sub_00BF16D0](../../init/BF/Unknown_function_00BF16D0.md) at `0x00C1485A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BE7AF8  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00BE7AFD  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00BE7B01  55                              push rbp
00BE7B02  53                              push rbx
00BE7B03  56                              push rsi
00BE7B04  57                              push rdi
00BE7B05  41 54                           push r12
00BE7B07  41 55                           push r13
00BE7B09  41 57                           push r15
00BE7B0B  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00BE7B10  48 81 EC D0 00 00 00            sub rsp, 0xd0
00BE7B17  44 8B E2                        mov r12d, edx
00BE7B1A  48 8B F9                        mov rdi, rcx
00BE7B1D  41 83 F8 03                     cmp r8d, 3
00BE7B21  0F 84 1A 03 00 00               je 0x140be7e41
00BE7B27  44 8B 99 D8 09 00 00            mov r11d, dword ptr [rcx + 0x9d8]
00BE7B2E  33 DB                           xor ebx, ebx
00BE7B30  44 8B D3                        mov r10d, ebx
00BE7B33  41 81 E3 00 00 00 08            and r11d, 0x8000000
00BE7B3A  75 07                           jne 0x140be7b43
00BE7B3C  44 8B 91 44 09 00 00            mov r10d, dword ptr [rcx + 0x944]
00BE7B43  8B 81 30 08 00 00               mov eax, dword ptr [rcx + 0x830]
00BE7B49  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
00BE7B4C  0F 31                           rdtsc
00BE7B4E  48 C1 E2 20                     shl rdx, 0x20
00BE7B52  49 BD 01 20 00 04 80 00 10 70   movabs r13, 0x7010008004002001
00BE7B5C  48 0B C2                        or rax, rdx
00BE7B5F  48 8B C8                        mov rcx, rax
00BE7B62  48 8B D0                        mov rdx, rax
00BE7B65  48 C1 C9 03                     ror rcx, 3
00BE7B69  49 8B C5                        mov rax, r13
00BE7B6C  48 33 D1                        xor rdx, rcx
00BE7B6F  48 F7 E2                        mul rdx
00BE7B72  4C 8B F8                        mov r15, rax
00BE7B75  48 89 55 A7                     mov qword ptr [rbp - 0x59], rdx
00BE7B79  44 33 FA                        xor r15d, edx
00BE7B7C  41 81 E7 FF 07 00 00            and r15d, 0x7ff
00BE7B83  0F 31                           rdtsc
00BE7B85  48 C1 E2 20                     shl rdx, 0x20
00BE7B89  45 8D 47 01                     lea r8d, [r15 + 1]
00BE7B8D  48 0B C2                        or rax, rdx
00BE7B90  BE 01 00 00 00                  mov esi, 1
00BE7B95  48 8B C8                        mov rcx, rax
00BE7B98  48 8B D0                        mov rdx, rax
00BE7B9B  48 C1 C9 03                     ror rcx, 3
00BE7B9F  49 8B C5                        mov rax, r13
00BE7BA2  48 33 D1                        xor rdx, rcx
00BE7BA5  48 F7 E2                        mul rdx
00BE7BA8  48 33 C2                        xor rax, rdx
00BE7BAB  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
00BE7BAF  33 D2                           xor edx, edx
00BE7BB1  49 F7 F0                        div r8
00BE7BB4  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
00BE7BB8  45 85 D2                        test r10d, r10d
00BE7BBB  0F 84 A2 00 00 00               je 0x140be7c63
00BE7BC1  0F 31                           rdtsc
00BE7BC3  48 C1 E2 20                     shl rdx, 0x20
00BE7BC7  48 0B C2                        or rax, rdx
00BE7BCA  48 8B C8                        mov rcx, rax
00BE7BCD  48 8B D0                        mov rdx, rax
00BE7BD0  48 C1 C9 03                     ror rcx, 3
00BE7BD4  49 8B C5                        mov rax, r13
00BE7BD7  48 33 D1                        xor rdx, rcx
00BE7BDA  48 F7 E2                        mul rdx
00BE7BDD  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
00BE7BE1  33 D0                           xor edx, eax
00BE7BE3  23 D6                           and edx, esi
00BE7BE5  C1 E2 0C                        shl edx, 0xc
00BE7BE8  81 C2 00 10 00 00               add edx, 0x1000
00BE7BEE  44 03 FA                        add r15d, edx
00BE7BF1  83 CA FF                        or edx, 0xffffffff
00BE7BF4  43 8D 04 27                     lea eax, [r15 + r12]
00BE7BF8  48 8D 48 08                     lea rcx, [rax + 8]
00BE7BFC  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
00BE7C00  48 8B 87 30 02 00 00            mov rax, qword ptr [rdi + 0x230]
00BE7C07  48 89 4D 9F                     mov qword ptr [rbp - 0x61], rcx
00BE7C0B  E8 50 2E 00 00                  call 0x140beaa60
00BE7C10  4C 8B E0                        mov r12, rax
00BE7C13  48 85 C0                        test rax, rax
00BE7C16  74 78                           je 0x140be7c90
00BE7C18  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00BE7C1C  44 8D 46 3F                     lea r8d, [rsi + 0x3f]
00BE7C20  48 8B 87 40 02 00 00            mov rax, qword ptr [rdi + 0x240]
00BE7C27  48 81 C2 FF 0F 00 00            add rdx, 0xfff
00BE7C2E  81 E2 00 F0 FF FF               and edx, 0xfffff000
00BE7C34  49 8B CC                        mov rcx, r12
00BE7C37  E8 24 2E 00 00                  call 0x140beaa60
00BE7C3C  84 C0                           test al, al
00BE7C3E  75 15                           jne 0x140be7c55
00BE7C40  48 8B 87 38 02 00 00            mov rax, qword ptr [rdi + 0x238]
00BE7C47  49 8B CC                        mov rcx, r12
00BE7C4A  48 8B 55 7F                     mov rdx, qword ptr [rbp + 0x7f]
00BE7C4E  E8 0D 2E 00 00                  call 0x140beaa60
00BE7C53  EB 3B                           jmp 0x140be7c90
00BE7C55  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00BE7C59  49 89 04 24                     mov qword ptr [r12], rax
00BE7C5D  49 83 C4 08                     add r12, 8
00BE7C61  EB 28                           jmp 0x140be7c8b
00BE7C63  48 8B 87 00 01 00 00            mov rax, qword ptr [rdi + 0x100]
00BE7C6A  43 8D 14 27                     lea edx, [r15 + r12]
00BE7C6E  44 8B 45 7F                     mov r8d, dword ptr [rbp + 0x7f]
00BE7C72  41 F7 DB                        neg r11d
00BE7C75  48 1B C9                        sbb rcx, rcx
00BE7C78  48 83 E1 C0                     and rcx, 0xffffffffffffffc0
00BE7C7C  48 81 C1 82 00 00 00            add rcx, 0x82
00BE7C83  E8 D8 2D 00 00                  call 0x140beaa60
00BE7C88  4C 8B E0                        mov r12, rax
00BE7C8B  4D 85 E4                        test r12, r12
00BE7C8E  75 0B                           jne 0x140be7c9b
00BE7C90  01 B7 60 0A 00 00               add dword ptr [rdi + 0xa60], esi
00BE7C96  E9 9E 01 00 00                  jmp 0x140be7e39
00BE7C9B  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
00BE7C9F  4D 8B C4                        mov r8, r12
00BE7CA2  44 8B D8                        mov r11d, eax
00BE7CA5  41 BA F8 FF FF FF               mov r10d, 0xfffffff8
00BE7CAB  83 F8 08                        cmp eax, 8
00BE7CAE  72 39                           jb 0x140be7ce9
00BE7CB0  44 8B C8                        mov r9d, eax
00BE7CB3  49 C1 E9 03                     shr r9, 3
00BE7CB7  0F 31                           rdtsc
00BE7CB9  48 C1 E2 20                     shl rdx, 0x20
00BE7CBD  45 03 DA                        add r11d, r10d
00BE7CC0  48 0B C2                        or rax, rdx
00BE7CC3  48 8B C8                        mov rcx, rax
00BE7CC6  48 8B D0                        mov rdx, rax
00BE7CC9  48 C1 C9 03                     ror rcx, 3
00BE7CCD  49 8B C5                        mov rax, r13
00BE7CD0  48 33 D1                        xor rdx, rcx
00BE7CD3  48 F7 E2                        mul rdx
00BE7CD6  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
00BE7CDA  48 33 D0                        xor rdx, rax
00BE7CDD  49 89 10                        mov qword ptr [r8], rdx
00BE7CE0  49 83 C0 08                     add r8, 8
00BE7CE4  4C 2B CE                        sub r9, rsi
00BE7CE7  75 CE                           jne 0x140be7cb7
00BE7CE9  45 85 DB                        test r11d, r11d
00BE7CEC  74 38                           je 0x140be7d26
00BE7CEE  0F 31                           rdtsc
00BE7CF0  48 C1 E2 20                     shl rdx, 0x20
00BE7CF4  48 0B C2                        or rax, rdx
00BE7CF7  48 8B C8                        mov rcx, rax
00BE7CFA  48 8B D0                        mov rdx, rax
00BE7CFD  48 C1 C9 03                     ror rcx, 3
00BE7D01  49 8B C5                        mov rax, r13
00BE7D04  48 33 D1                        xor rdx, rcx
00BE7D07  48 F7 E2                        mul rdx
00BE7D0A  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
00BE7D0E  48 33 D0                        xor rdx, rax
00BE7D11  41 83 C9 FF                     or r9d, 0xffffffff
00BE7D15  41 88 10                        mov byte ptr [r8], dl
00BE7D18  4C 03 C6                        add r8, rsi
00BE7D1B  48 C1 EA 08                     shr rdx, 8
00BE7D1F  45 03 D9                        add r11d, r9d
00BE7D22  75 F1                           jne 0x140be7d15
00BE7D24  EB 04                           jmp 0x140be7d2a
00BE7D26  41 83 C9 FF                     or r9d, 0xffffffff
00BE7D2A  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
00BE7D2E  44 8B 5D 6F                     mov r11d, dword ptr [rbp + 0x6f]
00BE7D32  44 2B FA                        sub r15d, edx
00BE7D35  8B C2                           mov eax, edx
00BE7D37  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00BE7D3B  4F 8D 04 1C                     lea r8, [r12 + r11]
00BE7D3F  4C 03 C0                        add r8, rax
00BE7D42  41 83 FF 08                     cmp r15d, 8
00BE7D46  72 3D                           jb 0x140be7d85
00BE7D48  45 8B DF                        mov r11d, r15d
00BE7D4B  49 C1 EB 03                     shr r11, 3
00BE7D4F  0F 31                           rdtsc
00BE7D51  48 C1 E2 20                     shl rdx, 0x20
00BE7D55  45 03 FA                        add r15d, r10d
00BE7D58  48 0B C2                        or rax, rdx
00BE7D5B  48 8B C8                        mov rcx, rax
00BE7D5E  48 8B D0                        mov rdx, rax
00BE7D61  48 C1 C9 03                     ror rcx, 3
00BE7D65  49 8B C5                        mov rax, r13
00BE7D68  48 33 D1                        xor rdx, rcx
00BE7D6B  48 F7 E2                        mul rdx
00BE7D6E  48 89 55 97                     mov qword ptr [rbp - 0x69], rdx
00BE7D72  48 33 D0                        xor rdx, rax
00BE7D75  49 89 10                        mov qword ptr [r8], rdx
00BE7D78  49 83 C0 08                     add r8, 8
00BE7D7C  4C 2B DE                        sub r11, rsi
00BE7D7F  75 CE                           jne 0x140be7d4f
00BE7D81  44 8B 5D 6F                     mov r11d, dword ptr [rbp + 0x6f]
00BE7D85  45 85 FF                        test r15d, r15d
00BE7D88  74 32                           je 0x140be7dbc
00BE7D8A  0F 31                           rdtsc
00BE7D8C  48 C1 E2 20                     shl rdx, 0x20
00BE7D90  48 0B C2                        or rax, rdx
00BE7D93  48 8B C8                        mov rcx, rax
00BE7D96  48 8B D0                        mov rdx, rax
00BE7D99  48 C1 C9 03                     ror rcx, 3
00BE7D9D  49 8B C5                        mov rax, r13
00BE7DA0  48 33 D1                        xor rdx, rcx
00BE7DA3  48 F7 E2                        mul rdx
00BE7DA6  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
00BE7DAA  48 33 D0                        xor rdx, rax
00BE7DAD  41 88 10                        mov byte ptr [r8], dl
00BE7DB0  4C 03 C6                        add r8, rsi
00BE7DB3  48 C1 EA 08                     shr rdx, 8
00BE7DB7  45 03 F9                        add r15d, r9d
00BE7DBA  75 F1                           jne 0x140be7dad
00BE7DBC  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00BE7DC0  49 03 CC                        add rcx, r12
00BE7DC3  74 74                           je 0x140be7e39
00BE7DC5  8B 97 04 08 00 00               mov edx, dword ptr [rdi + 0x804]
00BE7DCB  4C 8B C1                        mov r8, rcx
00BE7DCE  83 FA 08                        cmp edx, 8
00BE7DD1  72 21                           jb 0x140be7df4
00BE7DD3  44 8B DA                        mov r11d, edx
00BE7DD6  49 C1 EB 03                     shr r11, 3
00BE7DDA  48 8B 07                        mov rax, qword ptr [rdi]
00BE7DDD  41 03 D2                        add edx, r10d
00BE7DE0  49 89 00                        mov qword ptr [r8], rax
00BE7DE3  48 83 C7 08                     add rdi, 8
00BE7DE7  49 83 C0 08                     add r8, 8
00BE7DEB  4C 2B DE                        sub r11, rsi
00BE7DEE  75 EA                           jne 0x140be7dda
00BE7DF0  44 8B 5D 6F                     mov r11d, dword ptr [rbp + 0x6f]
00BE7DF4  85 D2                           test edx, edx
00BE7DF6  74 11                           je 0x140be7e09
00BE7DF8  4C 2B C7                        sub r8, rdi
00BE7DFB  8A 07                           mov al, byte ptr [rdi]
00BE7DFD  42 88 04 07                     mov byte ptr [rdi + r8], al
00BE7E01  48 03 FE                        add rdi, rsi
00BE7E04  41 03 D1                        add edx, r9d
00BE7E07  75 F2                           jne 0x140be7dfb
00BE7E09  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00BE7E0C  89 81 44 09 00 00               mov dword ptr [rcx + 0x944], eax
00BE7E12  8B 81 D8 09 00 00               mov eax, dword ptr [rcx + 0x9d8]
00BE7E18  44 89 99 04 08 00 00            mov dword ptr [rcx + 0x804], r11d
00BE7E1F  4C 89 A1 E8 07 00 00            mov qword ptr [rcx + 0x7e8], r12
00BE7E26  0F BA E0 1B                     bt eax, 0x1b
00BE7E2A  72 0A                           jb 0x140be7e36
00BE7E2C  0F BA E8 1C                     bts eax, 0x1c
00BE7E30  89 81 D8 09 00 00               mov dword ptr [rcx + 0x9d8], eax
00BE7E36  48 8B D9                        mov rbx, rcx
00BE7E39  48 8B C3                        mov rax, rbx
00BE7E3C  E9 27 05 00 00                  jmp 0x140be8368
00BE7E41  0F 31                           rdtsc
00BE7E43  48 C1 E2 20                     shl rdx, 0x20
00BE7E47  49 BD 01 20 00 04 80 00 10 70   movabs r13, 0x7010008004002001
00BE7E51  48 0B C2                        or rax, rdx
00BE7E54  48 8B C8                        mov rcx, rax
00BE7E57  48 8B D0                        mov rdx, rax
00BE7E5A  48 C1 C9 03                     ror rcx, 3
00BE7E5E  49 8B C5                        mov rax, r13
00BE7E61  48 33 D1                        xor rdx, rcx
00BE7E64  48 F7 E2                        mul rdx
00BE7E67  4C 8B CA                        mov r9, rdx
00BE7E6A  48 89 55 D7                     mov qword ptr [rbp - 0x29], rdx
00BE7E6E  44 33 C8                        xor r9d, eax
00BE7E71  41 81 E1 FF 07 00 00            and r9d, 0x7ff
00BE7E78  0F 31                           rdtsc
00BE7E7A  48 C1 E2 20                     shl rdx, 0x20
00BE7E7E  48 0B C2                        or rax, rdx
00BE7E81  48 8B C8                        mov rcx, rax
00BE7E84  4C 8B C0                        mov r8, rax
00BE7E87  48 C1 C9 03                     ror rcx, 3
00BE7E8B  49 8B C5                        mov rax, r13
00BE7E8E  4C 33 C1                        xor r8, rcx
00BE7E91  41 8D 49 01                     lea ecx, [r9 + 1]
00BE7E95  49 F7 E0                        mul r8
00BE7E98  48 89 55 CF                     mov qword ptr [rbp - 0x31], rdx
00BE7E9C  48 33 C2                        xor rax, rdx
00BE7E9F  33 D2                           xor edx, edx
00BE7EA1  48 F7 F1                        div rcx
00BE7EA4  48 89 55 A7                     mov qword ptr [rbp - 0x59], rdx
00BE7EA8  0F 31                           rdtsc
00BE7EAA  48 C1 E2 20                     shl rdx, 0x20
00BE7EAE  BE 01 00 00 00                  mov esi, 1
00BE7EB3  48 0B C2                        or rax, rdx
00BE7EB6  48 8B C8                        mov rcx, rax
00BE7EB9  4C 8B C0                        mov r8, rax
00BE7EBC  48 C1 C9 03                     ror rcx, 3
00BE7EC0  49 8B C5                        mov rax, r13
00BE7EC3  4C 33 C1                        xor r8, rcx
00BE7EC6  49 F7 E0                        mul r8
00BE7EC9  33 C2                           xor eax, edx
00BE7ECB  48 89 55 C7                     mov qword ptr [rbp - 0x39], rdx
00BE7ECF  23 C6                           and eax, esi
00BE7ED1  C1 E0 0C                        shl eax, 0xc
00BE7ED4  05 00 10 00 00                  add eax, 0x1000
00BE7ED9  41 03 C1                        add eax, r9d
00BE7EDC  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
00BE7EDF  0F 31                           rdtsc
00BE7EE1  48 C1 E2 20                     shl rdx, 0x20
00BE7EE5  48 0B C2                        or rax, rdx
00BE7EE8  48 8B C8                        mov rcx, rax
00BE7EEB  48 8B D0                        mov rdx, rax
00BE7EEE  48 C1 C9 03                     ror rcx, 3
00BE7EF2  49 8B C5                        mov rax, r13
00BE7EF5  48 33 D1                        xor rdx, rcx
00BE7EF8  48 F7 E2                        mul rdx
00BE7EFB  4C 8B E2                        mov r12, rdx
00BE7EFE  48 89 55 BF                     mov qword ptr [rbp - 0x41], rdx
00BE7F02  44 33 E0                        xor r12d, eax
00BE7F05  41 81 E4 FF 07 00 00            and r12d, 0x7ff
00BE7F0C  0F 31                           rdtsc
00BE7F0E  48 C1 E2 20                     shl rdx, 0x20
00BE7F12  48 0B C2                        or rax, rdx
00BE7F15  48 8B C8                        mov rcx, rax
00BE7F18  4C 8B C0                        mov r8, rax
00BE7F1B  48 C1 C9 03                     ror rcx, 3
00BE7F1F  49 8B C5                        mov rax, r13
00BE7F22  4C 33 C1                        xor r8, rcx
00BE7F25  41 8D 4C 24 01                  lea ecx, [r12 + 1]
00BE7F2A  49 F7 E0                        mul r8
00BE7F2D  44 8B 87 30 08 00 00            mov r8d, dword ptr [rdi + 0x830]
00BE7F34  48 33 C2                        xor rax, rdx
00BE7F37  48 89 55 B7                     mov qword ptr [rbp - 0x49], rdx
00BE7F3B  33 D2                           xor edx, edx
00BE7F3D  48 F7 F1                        div rcx
00BE7F40  48 8B 87 00 01 00 00            mov rax, qword ptr [rdi + 0x100]
00BE7F47  8D 4E 41                        lea ecx, [rsi + 0x41]
00BE7F4A  48 89 55 9F                     mov qword ptr [rbp - 0x61], rdx
00BE7F4E  41 8D 54 24 20                  lea edx, [r12 + 0x20]
00BE7F53  E8 08 2B 00 00                  call 0x140beaa60
00BE7F58  33 DB                           xor ebx, ebx
00BE7F5A  48 89 45 97                     mov qword ptr [rbp - 0x69], rax
00BE7F5E  48 85 C0                        test rax, rax
00BE7F61  75 10                           jne 0x140be7f73
00BE7F63  4C 8D A7 60 0A 00 00            lea r12, [rdi + 0xa60]
00BE7F6A  41 01 34 24                     add dword ptr [r12], esi
00BE7F6E  E9 EB 03 00 00                  jmp 0x140be835e
00BE7F73  4C 8B 5D 9F                     mov r11, qword ptr [rbp - 0x61]
00BE7F77  4C 8B C0                        mov r8, rax
00BE7F7A  45 8B D3                        mov r10d, r11d
00BE7F7D  41 B9 F8 FF FF FF               mov r9d, 0xfffffff8
00BE7F83  41 83 FB 08                     cmp r11d, 8
00BE7F87  72 39                           jb 0x140be7fc2
00BE7F89  45 8B FB                        mov r15d, r11d
00BE7F8C  49 C1 EF 03                     shr r15, 3
00BE7F90  0F 31                           rdtsc
00BE7F92  48 C1 E2 20                     shl rdx, 0x20
00BE7F96  45 03 D1                        add r10d, r9d
00BE7F99  48 0B C2                        or rax, rdx
00BE7F9C  48 8B C8                        mov rcx, rax
00BE7F9F  48 8B D0                        mov rdx, rax
00BE7FA2  48 C1 C9 03                     ror rcx, 3
00BE7FA6  49 8B C5                        mov rax, r13
00BE7FA9  48 33 D1                        xor rdx, rcx
00BE7FAC  48 F7 E2                        mul rdx
00BE7FAF  48 89 55 DF                     mov qword ptr [rbp - 0x21], rdx
00BE7FB3  48 33 D0                        xor rdx, rax
00BE7FB6  49 89 10                        mov qword ptr [r8], rdx
00BE7FB9  49 83 C0 08                     add r8, 8
00BE7FBD  4C 2B FE                        sub r15, rsi
00BE7FC0  75 CE                           jne 0x140be7f90
00BE7FC2  41 83 CF FF                     or r15d, 0xffffffff
00BE7FC6  45 85 D2                        test r10d, r10d
00BE7FC9  74 32                           je 0x140be7ffd
00BE7FCB  0F 31                           rdtsc
00BE7FCD  48 C1 E2 20                     shl rdx, 0x20
00BE7FD1  48 0B C2                        or rax, rdx
00BE7FD4  48 8B C8                        mov rcx, rax
00BE7FD7  48 8B D0                        mov rdx, rax
00BE7FDA  48 C1 C9 03                     ror rcx, 3
00BE7FDE  49 8B C5                        mov rax, r13
00BE7FE1  48 33 D1                        xor rdx, rcx
00BE7FE4  48 F7 E2                        mul rdx
00BE7FE7  48 89 55 E7                     mov qword ptr [rbp - 0x19], rdx
00BE7FEB  48 33 D0                        xor rdx, rax
00BE7FEE  41 88 10                        mov byte ptr [r8], dl
00BE7FF1  4C 03 C6                        add r8, rsi
00BE7FF4  48 C1 EA 08                     shr rdx, 8
00BE7FF8  45 03 D7                        add r10d, r15d
00BE7FFB  75 F1                           jne 0x140be7fee
00BE7FFD  45 2B E3                        sub r12d, r11d
00BE8000  45 8B C3                        mov r8d, r11d
00BE8003  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
00BE8007  4D 03 C3                        add r8, r11
00BE800A  4D 8D 50 20                     lea r10, [r8 + 0x20]
00BE800E  41 83 FC 08                     cmp r12d, 8
00BE8012  72 3D                           jb 0x140be8051
00BE8014  45 8B DC                        mov r11d, r12d
00BE8017  49 C1 EB 03                     shr r11, 3
00BE801B  0F 31                           rdtsc
00BE801D  48 C1 E2 20                     shl rdx, 0x20
00BE8021  45 03 E1                        add r12d, r9d
00BE8024  48 0B C2                        or rax, rdx
00BE8027  48 8B C8                        mov rcx, rax
00BE802A  48 8B D0                        mov rdx, rax
00BE802D  48 C1 C9 03                     ror rcx, 3
00BE8031  49 8B C5                        mov rax, r13
00BE8034  48 33 D1                        xor rdx, rcx
00BE8037  48 F7 E2                        mul rdx
00BE803A  48 89 55 EF                     mov qword ptr [rbp - 0x11], rdx
00BE803E  48 33 D0                        xor rdx, rax
00BE8041  49 89 12                        mov qword ptr [r10], rdx
00BE8044  49 83 C2 08                     add r10, 8
00BE8048  4C 2B DE                        sub r11, rsi
00BE804B  75 CE                           jne 0x140be801b
00BE804D  4C 8B 5D 97                     mov r11, qword ptr [rbp - 0x69]
00BE8051  45 85 E4                        test r12d, r12d
00BE8054  74 32                           je 0x140be8088
00BE8056  0F 31                           rdtsc
00BE8058  48 C1 E2 20                     shl rdx, 0x20
00BE805C  48 0B C2                        or rax, rdx
00BE805F  48 8B C8                        mov rcx, rax
00BE8062  48 8B D0                        mov rdx, rax
00BE8065  48 C1 C9 03                     ror rcx, 3
00BE8069  49 8B C5                        mov rax, r13
00BE806C  48 33 D1                        xor rdx, rcx
00BE806F  48 F7 E2                        mul rdx
00BE8072  48 89 55 F7                     mov qword ptr [rbp - 9], rdx
00BE8076  48 33 D0                        xor rdx, rax
00BE8079  41 88 12                        mov byte ptr [r10], dl
00BE807C  4C 03 D6                        add r10, rsi
00BE807F  48 C1 EA 08                     shr rdx, 8
00BE8083  45 03 E7                        add r12d, r15d
00BE8086  75 F1                           jne 0x140be8079
00BE8088  4C 8D A7 60 0A 00 00            lea r12, [rdi + 0xa60]
00BE808F  4D 85 C0                        test r8, r8
00BE8092  0F 84 C6 02 00 00               je 0x140be835e
00BE8098  B8 20 00 00 00                  mov eax, 0x20
00BE809D  49 8B C8                        mov rcx, r8
00BE80A0  48 89 4D 97                     mov qword ptr [rbp - 0x69], rcx
00BE80A4  8D 50 E4                        lea edx, [rax - 0x1c]
00BE80A7  49 89 18                        mov qword ptr [r8], rbx
00BE80AA  41 03 C1                        add eax, r9d
00BE80AD  49 83 C0 08                     add r8, 8
00BE80B1  48 2B D6                        sub rdx, rsi
00BE80B4  75 F1                           jne 0x140be80a7
00BE80B6  85 C0                           test eax, eax
00BE80B8  74 0B                           je 0x140be80c5
00BE80BA  41 88 18                        mov byte ptr [r8], bl
00BE80BD  4C 03 C6                        add r8, rsi
00BE80C0  41 03 C7                        add eax, r15d
00BE80C3  75 F5                           jne 0x140be80ba
00BE80C5  8B 87 30 08 00 00               mov eax, dword ptr [rdi + 0x830]
00BE80CB  BA 05 00 00 00                  mov edx, 5
00BE80D0  89 41 10                        mov dword ptr [rcx + 0x10], eax
00BE80D3  4C 89 59 18                     mov qword ptr [rcx + 0x18], r11
00BE80D7  B9 00 00 80 00                  mov ecx, 0x800000
00BE80DC  89 45 77                        mov dword ptr [rbp + 0x77], eax
00BE80DF  8B 87 D8 09 00 00               mov eax, dword ptr [rdi + 0x9d8]
00BE80E5  85 C1                           test ecx, eax
00BE80E7  74 07                           je 0x140be80f0
00BE80E9  BA 15 00 00 00                  mov edx, 0x15
00BE80EE  EB 08                           jmp 0x140be80f8
00BE80F0  0B C1                           or eax, ecx
00BE80F2  89 87 D8 09 00 00               mov dword ptr [rdi + 0x9d8], eax
00BE80F8  8B 4D 6F                        mov ecx, dword ptr [rbp + 0x6f]
00BE80FB  4C 8B C3                        mov r8, rbx
00BE80FE  03 4D 7F                        add ecx, dword ptr [rbp + 0x7f]
00BE8101  48 8B 87 48 03 00 00            mov rax, qword ptr [rdi + 0x348]
00BE8108  44 8B C9                        mov r9d, ecx
00BE810B  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
00BE810F  48 83 CA FF                     or rdx, 0xffffffffffffffff
00BE8113  48 89 4D AF                     mov qword ptr [rbp - 0x51], rcx
00BE8117  48 8B CB                        mov rcx, rbx
00BE811A  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00BE811E  E8 3D 29 00 00                  call 0x140beaa60
00BE8123  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00BE8127  48 8B C8                        mov rcx, rax
00BE812A  48 85 C0                        test rax, rax
00BE812D  0F 84 1B 02 00 00               je 0x140be834e
00BE8133  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
00BE8137  8B 55 77                        mov edx, dword ptr [rbp + 0x77]
00BE813A  48 89 08                        mov qword ptr [rax], rcx
00BE813D  48 8B 87 50 03 00 00            mov rax, qword ptr [rdi + 0x350]
00BE8144  48 8B 4D AF                     mov rcx, qword ptr [rbp - 0x51]
00BE8148  E8 13 29 00 00                  call 0x140beaa60
00BE814D  48 8B C8                        mov rcx, rax
00BE8150  48 85 C0                        test rax, rax
00BE8153  0F 84 F5 01 00 00               je 0x140be834e
00BE8159  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
00BE815D  44 8B CE                        mov r9d, esi
00BE8160  4C 8B 45 9F                     mov r8, qword ptr [rbp - 0x61]
00BE8164  8B 55 77                        mov edx, dword ptr [rbp + 0x77]
00BE8167  48 89 48 08                     mov qword ptr [rax + 8], rcx
00BE816B  48 8B 87 58 03 00 00            mov rax, qword ptr [rdi + 0x358]
00BE8172  E8 E9 28 00 00                  call 0x140beaa60
00BE8177  48 8B 55 AF                     mov rdx, qword ptr [rbp - 0x51]
00BE817B  4C 8B C8                        mov r9, rax
00BE817E  48 81 C2 FF 0F 00 00            add rdx, 0xfff
00BE8185  48 89 45 9F                     mov qword ptr [rbp - 0x61], rax
00BE8189  48 8B 87 40 02 00 00            mov rax, qword ptr [rdi + 0x240]
00BE8190  81 E2 00 F0 FF FF               and edx, 0xfffff000
00BE8196  41 B8 40 00 00 00               mov r8d, 0x40
00BE819C  49 8B C9                        mov rcx, r9
00BE819F  E8 BC 28 00 00                  call 0x140beaa60
00BE81A4  84 C0                           test al, al
00BE81A6  0F 84 A2 01 00 00               je 0x140be834e
00BE81AC  4C 8B 5D A7                     mov r11, qword ptr [rbp - 0x59]
00BE81B0  41 BA F8 FF FF FF               mov r10d, 0xfffffff8
00BE81B6  4C 8B 65 9F                     mov r12, qword ptr [rbp - 0x61]
00BE81BA  45 8B CB                        mov r9d, r11d
00BE81BD  4D 8B C4                        mov r8, r12
00BE81C0  41 83 FB 08                     cmp r11d, 8
00BE81C4  72 3D                           jb 0x140be8203
00BE81C6  45 8B DB                        mov r11d, r11d
00BE81C9  49 C1 EB 03                     shr r11, 3
00BE81CD  0F 31                           rdtsc
00BE81CF  48 C1 E2 20                     shl rdx, 0x20
00BE81D3  45 03 CA                        add r9d, r10d
00BE81D6  48 0B C2                        or rax, rdx
00BE81D9  48 8B C8                        mov rcx, rax
00BE81DC  48 8B D0                        mov rdx, rax
00BE81DF  48 C1 C9 03                     ror rcx, 3
00BE81E3  49 8B C5                        mov rax, r13
00BE81E6  48 33 D1                        xor rdx, rcx
00BE81E9  48 F7 E2                        mul rdx
00BE81EC  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
00BE81F0  48 33 D0                        xor rdx, rax
00BE81F3  49 89 10                        mov qword ptr [r8], rdx
00BE81F6  49 83 C0 08                     add r8, 8
00BE81FA  4C 2B DE                        sub r11, rsi
00BE81FD  75 CE                           jne 0x140be81cd
00BE81FF  4C 8B 5D A7                     mov r11, qword ptr [rbp - 0x59]
00BE8203  45 85 C9                        test r9d, r9d
00BE8206  74 32                           je 0x140be823a
00BE8208  0F 31                           rdtsc
00BE820A  48 C1 E2 20                     shl rdx, 0x20
00BE820E  48 0B C2                        or rax, rdx
00BE8211  48 8B C8                        mov rcx, rax
00BE8214  48 8B D0                        mov rdx, rax
00BE8217  48 C1 C9 03                     ror rcx, 3
00BE821B  49 8B C5                        mov rax, r13
00BE821E  48 33 D1                        xor rdx, rcx
00BE8221  48 F7 E2                        mul rdx
00BE8224  48 89 55 07                     mov qword ptr [rbp + 7], rdx
00BE8228  48 33 D0                        xor rdx, rax
00BE822B  41 88 10                        mov byte ptr [r8], dl
00BE822E  4C 03 C6                        add r8, rsi
00BE8231  48 C1 EA 08                     shr rdx, 8
00BE8235  45 03 CF                        add r9d, r15d
00BE8238  75 F1                           jne 0x140be822b
00BE823A  44 8B 4D 7F                     mov r9d, dword ptr [rbp + 0x7f]
00BE823E  41 8B C3                        mov eax, r11d
00BE8241  45 2B CB                        sub r9d, r11d
00BE8244  44 8B 5D 6F                     mov r11d, dword ptr [rbp + 0x6f]
00BE8248  48 89 45 7F                     mov qword ptr [rbp + 0x7f], rax
00BE824C  4E 8D 04 18                     lea r8, [rax + r11]
00BE8250  4D 03 C4                        add r8, r12
00BE8253  41 83 F9 08                     cmp r9d, 8
00BE8257  72 3D                           jb 0x140be8296
00BE8259  45 8B E1                        mov r12d, r9d
00BE825C  49 C1 EC 03                     shr r12, 3
00BE8260  0F 31                           rdtsc
00BE8262  48 C1 E2 20                     shl rdx, 0x20
00BE8266  45 03 CA                        add r9d, r10d
00BE8269  48 0B C2                        or rax, rdx
00BE826C  48 8B C8                        mov rcx, rax
00BE826F  48 8B D0                        mov rdx, rax
00BE8272  48 C1 C9 03                     ror rcx, 3
00BE8276  49 8B C5                        mov rax, r13
00BE8279  48 33 D1                        xor rdx, rcx
00BE827C  48 F7 E2                        mul rdx
00BE827F  48 89 55 0F                     mov qword ptr [rbp + 0xf], rdx
00BE8283  48 33 D0                        xor rdx, rax
00BE8286  49 89 10                        mov qword ptr [r8], rdx
00BE8289  49 83 C0 08                     add r8, 8
00BE828D  4C 2B E6                        sub r12, rsi
00BE8290  75 CE                           jne 0x140be8260
00BE8292  4C 8B 65 9F                     mov r12, qword ptr [rbp - 0x61]
00BE8296  45 85 C9                        test r9d, r9d
00BE8299  74 32                           je 0x140be82cd
00BE829B  0F 31                           rdtsc
00BE829D  48 C1 E2 20                     shl rdx, 0x20
00BE82A1  48 0B C2                        or rax, rdx
00BE82A4  48 8B C8                        mov rcx, rax
00BE82A7  48 8B D0                        mov rdx, rax
00BE82AA  48 C1 C9 03                     ror rcx, 3
00BE82AE  49 8B C5                        mov rax, r13
00BE82B1  48 33 D1                        xor rdx, rcx
00BE82B4  48 F7 E2                        mul rdx
00BE82B7  48 89 55 17                     mov qword ptr [rbp + 0x17], rdx
00BE82BB  48 33 D0                        xor rdx, rax
00BE82BE  41 88 10                        mov byte ptr [r8], dl
00BE82C1  4C 03 C6                        add r8, rsi
00BE82C4  48 C1 EA 08                     shr rdx, 8
00BE82C8  45 03 CF                        add r9d, r15d
00BE82CB  75 F1                           jne 0x140be82be
00BE82CD  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
00BE82D1  49 03 CC                        add rcx, r12
00BE82D4  0F 84 88 00 00 00               je 0x140be8362
00BE82DA  8B 97 04 08 00 00               mov edx, dword ptr [rdi + 0x804]
00BE82E0  4C 8B C1                        mov r8, rcx
00BE82E3  83 FA 08                        cmp edx, 8
00BE82E6  72 1D                           jb 0x140be8305
00BE82E8  44 8B CA                        mov r9d, edx
00BE82EB  49 C1 E9 03                     shr r9, 3
00BE82EF  48 8B 07                        mov rax, qword ptr [rdi]
00BE82F2  41 03 D2                        add edx, r10d
00BE82F5  49 89 00                        mov qword ptr [r8], rax
00BE82F8  48 83 C7 08                     add rdi, 8
00BE82FC  49 83 C0 08                     add r8, 8
00BE8300  4C 2B CE                        sub r9, rsi
00BE8303  75 EA                           jne 0x140be82ef
00BE8305  85 D2                           test edx, edx
00BE8307  74 11                           je 0x140be831a
00BE8309  4C 2B C7                        sub r8, rdi
00BE830C  8A 07                           mov al, byte ptr [rdi]
00BE830E  41 88 04 38                     mov byte ptr [r8 + rdi], al
00BE8312  48 03 FE                        add rdi, rsi
00BE8315  41 03 D7                        add edx, r15d
00BE8318  75 F2                           jne 0x140be830c
00BE831A  48 8B 45 97                     mov rax, qword ptr [rbp - 0x69]
00BE831E  48 89 81 E8 07 00 00            mov qword ptr [rcx + 0x7e8], rax
00BE8325  8B 81 D8 09 00 00               mov eax, dword ptr [rcx + 0x9d8]
00BE832B  44 89 99 04 08 00 00            mov dword ptr [rcx + 0x804], r11d
00BE8332  C7 81 44 09 00 00 03 00 00 00   mov dword ptr [rcx + 0x944], 3
00BE833C  0F BA E0 1B                     bt eax, 0x1b
00BE8340  72 23                           jb 0x140be8365
00BE8342  0F BA E8 1C                     bts eax, 0x1c
00BE8346  89 81 D8 09 00 00               mov dword ptr [rcx + 0x9d8], eax
00BE834C  EB 17                           jmp 0x140be8365
00BE834E  48 8B 87 68 03 00 00            mov rax, qword ptr [rdi + 0x368]
00BE8355  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00BE8359  E8 02 27 00 00                  call 0x140beaa60
00BE835E  41 01 34 24                     add dword ptr [r12], esi
00BE8362  48 8B CB                        mov rcx, rbx
00BE8365  48 8B C1                        mov rax, rcx
00BE8368  48 81 C4 D0 00 00 00            add rsp, 0xd0
00BE836F  41 5F                           pop r15
00BE8371  41 5D                           pop r13
00BE8373  41 5C                           pop r12
00BE8375  5F                              pop rdi
00BE8376  5E                              pop rsi
00BE8377  5B                              pop rbx
00BE8378  5D                              pop rbp
00BE8379  C3                              ret
00BE837A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00BE7AF8(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;

    v_stack_p18 = a3;
    v_stack_p10 = (unsigned int)(a2);
    v_rsp = (v_rsp) - (208);
    if (a3 == 3) goto loc_00BE7E41;
    v_rbx = 0;
    v_r11 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2520))) & (0x8000000ULL));
    v_r10 = 0;
    if (!(condition_is_not_equal)) {
        v_r10 = *(unsigned int *)(a1 + 2372);
    }
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2096)));
    a2 = (a2) << (32);
    result = ((unsigned int)(*(unsigned int *)(a1 + 2096))) | (a2);
    a2 = (result) ^ (result);
    v_stack_mB8 = a2;
    v_r15 = (unsigned int)((v_r13) ^ ((unsigned int)(a2)));
    v_r15 = (unsigned int)((v_r15) & (0x7FFULL));
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a2 = (result) ^ (result);
    result = (v_r13) ^ (a2);
    v_stack_mA8 = a2;
    a2 = 0;
    v_stack_mC8 = 0;
    if ((unsigned int)(v_r10) == 0) goto loc_00BE7C63;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_mA0 = a2;
    a2 = (unsigned int)((a2) ^ ((unsigned int)(v_r13)));
    a2 = (unsigned int)((a2) & (1));
    a2 = (unsigned int)((a2) << (12));
    a2 = (unsigned int)((a2) + (0x1000ULL));
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(a2)));
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_stack_p20 = v_r15 + (unsigned int)((unsigned int)(a2)) * 1;
    v_stack_mC0 = v_r15 + (unsigned int)((unsigned int)(a2)) * 1 + 8;
    result = KeGuardDispatchICall(v_r15 + (unsigned int)((unsigned int)(a2)) * 1 + 8, a2, v_r15 + 1, a4);
    if (result == 0) goto loc_00BE7C90;
    a2 = (v_stack_p20) + (0xFFFULL);
    a2 = (unsigned int)((a2) & (0xFFFFF000ULL));
    result = KeGuardDispatchICall(result, a2, 1 + 63, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00BE7C55;
    result = KeGuardDispatchICall(result, v_stack_p20, 1 + 63, a4);
    goto loc_00BE7C90;
loc_00BE7C55:
    *(unsigned __int64 *)(result) = v_stack_mC0;
    v_r12 = (result) + (8);
    goto loc_00BE7C8B;
loc_00BE7C63:
    v_r11 = (unsigned int)(-(v_r11));
    a1 = (result) & (-64);
    a1 = (a1) + (130);
    result = KeGuardDispatchICall(a1, v_r15 + v_r12 * 1, (unsigned int)(v_stack_p20), a4);
loc_00BE7C8B:
    if (result != 0) goto loc_00BE7C9B;
loc_00BE7C90:
    goto loc_00BE7E39;
loc_00BE7C9B:
    if (((unsigned int)(v_stack_mC8)) < 8) goto loc_00BE7CE9;
    a4 = ((unsigned int)((unsigned int)(v_stack_mC8))) >> (3);
loc_00BE7CB7:
    a2 = (v_r15 + v_r12 * 1) << (32);
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mC8))) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (v_stack_mC8) | (a2);
    a2 = (result) ^ (result);
    v_stack_m98 = a2;
    a2 = (a2) ^ (v_r13);
    *(unsigned __int64 *)(result) = a2;
    a3 = (result) + (8);
    a4 = (a4) - (1);
    if (condition_is_not_equal) goto loc_00BE7CB7;
loc_00BE7CE9:
    if ((unsigned int)(v_r11) == 0) goto loc_00BE7D26;
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a2 = (result) ^ (result);
    v_stack_m90 = a2;
    a2 = (a2) ^ (v_r13);
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
loc_00BE7D15:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a2);
    a3 = (a3) + (1);
    a2 = (a2) >> (8);
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_00BE7D15;
    goto loc_00BE7D2A;
loc_00BE7D26:
    a4 = (unsigned int)((a4) | (0xFFFFFFFFULL));
loc_00BE7D2A:
    v_r15 = (unsigned int)((v_r15) - ((unsigned int)(v_stack_mC8)));
    v_stack_mC0 = (unsigned int)((unsigned int)(v_stack_mC8));
    a3 = (result + (unsigned int)(v_stack_p10) * 1) + ((unsigned int)((unsigned int)(v_stack_mC8)));
    if (((unsigned int)(v_r15)) < 8) goto loc_00BE7D85;
    v_r11 = ((unsigned int)((unsigned int)(v_r15))) >> (3);
loc_00BE7D4F:
    a2 = (v_stack_mC8) << (32);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = ((unsigned int)((unsigned int)(v_stack_mC8))) | (a2);
    a2 = (result) ^ (result);
    v_stack_mC8 = a2;
    a2 = (a2) ^ (v_r13);
    *(unsigned __int64 *)(a3) = a2;
    a3 = (a3) + (8);
    v_r11 = (v_r11) - (1);
    if (condition_is_not_equal) goto loc_00BE7D4F;
loc_00BE7D85:
    if ((unsigned int)(v_r15) == 0) goto loc_00BE7DBC;
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a2 = (result) ^ (result);
    v_stack_m88 = a2;
    a2 = (a2) ^ (v_r13);
loc_00BE7DAD:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a2);
    a3 = (a3) + (1);
    a2 = (a2) >> (8);
    v_r15 = (unsigned int)((v_r15) + ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_00BE7DAD;
loc_00BE7DBC:
    a1 = (v_stack_mC0) + (result);
    if (condition_is_equal) goto loc_00BE7E39;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2052)))) < 8) goto loc_00BE7DF4;
    v_r11 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2052))))) >> (3);
loc_00BE7DDA:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 2052))) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a1);
    v_rdi = (a1) + (8);
    a3 = (a1) + (8);
    v_r11 = (v_r11) - (1);
    if (condition_is_not_equal) goto loc_00BE7DDA;
loc_00BE7DF4:
    if ((unsigned int)(a2) == 0) goto loc_00BE7E09;
    a3 = (a3) - (v_rdi);
loc_00BE7DFB:
    *(unsigned __int8 *)(v_rdi + a3 * 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi));
    v_rdi = (v_rdi) + (1);
    a2 = (unsigned int)((a2) + ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_00BE7DFB;
loc_00BE7E09:
    *(unsigned int *)(a1 + 2372) = (unsigned int)((unsigned int)(v_stack_p18));
    *(unsigned int *)(a1 + 2052) = (unsigned int)((unsigned int)(v_stack_p10));
    *(unsigned __int64 *)(a1 + 2024) = result;
    if (!(condition_is_below)) {
        *(unsigned int *)(a1 + 2520) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2520)));
    }
loc_00BE7E39:
    goto loc_00BE8368;
loc_00BE7E41:
    a2 = (a2) << (32);
    result = (a1) | (a2);
    a2 = (result) ^ (result);
    v_stack_m88 = a2;
    a4 = (unsigned int)((a2) ^ ((unsigned int)(v_r13)));
    a4 = (unsigned int)((a4) & (0x7FFULL));
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a3 = (result) ^ (result);
    v_stack_m90 = a2;
    result = (v_r13) ^ (a2);
    a2 = 0;
    v_stack_mB8 = 0;
    a2 = (a2) << (32);
    result = (result) | (a2);
    a3 = (result) ^ (result);
    result = (unsigned int)((v_r13) ^ ((unsigned int)(a2)));
    v_stack_m98 = a2;
    result = (unsigned int)((result) & (1));
    result = (unsigned int)((result) << (12));
    result = (unsigned int)((result) + (0x1000ULL));
    result = (unsigned int)((result) + ((unsigned int)(a4)));
    v_stack_p20 = (unsigned int)(result);
    a2 = (a2) << (32);
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_mA0 = a2;
    v_r12 = (unsigned int)((a2) ^ ((unsigned int)(v_r13)));
    v_r12 = (unsigned int)((v_r12) & (0x7FFULL));
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a3 = (result) ^ (result);
    result = (v_r13) ^ (a2);
    v_stack_mA8 = a2;
    a2 = 0;
    v_stack_mC0 = 0;
    result = KeGuardDispatchICall(1 + 65, v_r12 + 32, (unsigned int)(*(unsigned int *)(v_rdi + 2096)), a4);
    v_rbx = 0;
    v_stack_mC8 = result;
    if (result != 0) goto loc_00BE7F73;
    goto loc_00BE835E;
loc_00BE7F73:
    if (((unsigned int)(v_stack_mC0)) < 8) goto loc_00BE7FC2;
    v_r15 = ((unsigned int)((unsigned int)(v_stack_mC0))) >> (3);
loc_00BE7F90:
    a2 = (v_r12 + 32) << (32);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mC0))) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m80 = a2;
    a2 = (a2) ^ (v_r13);
    *(unsigned __int64 *)(result) = a2;
    a3 = (result) + (8);
    v_r15 = (v_r15) - (1);
    if (condition_is_not_equal) goto loc_00BE7F90;
loc_00BE7FC2:
    v_r15 = (unsigned int)((v_r15) | (0xFFFFFFFFULL));
    if ((unsigned int)(v_r10) == 0) goto loc_00BE7FFD;
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a2 = (result) ^ (result);
    v_stack_m78 = a2;
    a2 = (a2) ^ (v_r13);
loc_00BE7FEE:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a2);
    a3 = (a3) + (1);
    a2 = (a2) >> (8);
    v_r10 = (unsigned int)((v_r10) + ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_00BE7FEE;
loc_00BE7FFD:
    v_r12 = (unsigned int)((v_rdi + 2656) - ((unsigned int)(v_stack_mC0)));
    a3 = ((unsigned int)((unsigned int)(v_stack_mC0))) + (v_stack_mC8);
    if (((unsigned int)(v_r12)) < 8) goto loc_00BE8051;
    v_r11 = ((unsigned int)((unsigned int)(v_r12))) >> (3);
loc_00BE801B:
    a2 = (a2) << (32);
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (v_r13) | (a2);
    a2 = (result) ^ (result);
    v_stack_m70 = a2;
    a2 = (a2) ^ (v_r13);
    *(unsigned __int64 *)(a3 + 32) = a2;
    v_r10 = (a3 + 32) + (8);
    v_r11 = (v_r11) - (1);
    if (condition_is_not_equal) goto loc_00BE801B;
loc_00BE8051:
    if ((unsigned int)(v_r12) == 0) goto loc_00BE8088;
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a2 = (result) ^ (result);
    v_stack_m68 = a2;
    a2 = (a2) ^ (v_r13);
loc_00BE8079:
    *(unsigned __int8 *)(v_r10) = (unsigned __int8)(a2);
    v_r10 = (v_r10) + (1);
    a2 = (a2) >> (8);
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_00BE8079;
loc_00BE8088:
    if (a3 == 0) goto loc_00BE835E;
    v_stack_mC8 = a3;
loc_00BE80A7:
    *(unsigned __int64 *)(a3) = 0;
    result = (unsigned int)((32) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    a3 = (a3) + (8);
    a2 = (32 - 28) - (1);
    if (condition_is_not_equal) goto loc_00BE80A7;
    if ((unsigned int)(result) == 0) goto loc_00BE80C5;
loc_00BE80BA:
    *(unsigned __int8 *)(a3) = 0;
    a3 = (a3) + (1);
    result = (unsigned int)((result) + ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_00BE80BA;
loc_00BE80C5:
    *(unsigned int *)(a3 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 2096)));
    *(unsigned __int64 *)(a3 + 24) = v_stack_mC8;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 2096)));
    if ((((unsigned int)((unsigned int)(0x800000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 2520))))) == 0) goto loc_00BE80F0;
    goto loc_00BE80F8;
loc_00BE80F0:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 2520))) | ((unsigned int)((unsigned int)(0x800000ULL))));
    *(unsigned int *)(v_rdi + 2520) = (unsigned int)(result);
loc_00BE80F8:
    a1 = (unsigned int)(((unsigned int)(v_stack_p10)) + (v_stack_p20));
    v_stack_mE0 = 21;
    a2 = (21) | (-1);
    v_stack_mB0 = a1;
    v_stack_mE8 = 1;
    result = KeGuardDispatchICall(0, a2, 0, (unsigned int)((unsigned int)(a1)));
    v_stack_mC0 = result;
    if (result == 0) goto loc_00BE834E;
    *(unsigned __int64 *)(v_stack_mC8) = result;
    result = KeGuardDispatchICall(v_stack_mB0, (unsigned int)(v_stack_p18), 0, (unsigned int)((unsigned int)(a1)));
    if (result == 0) goto loc_00BE834E;
    *(unsigned __int64 *)(v_stack_mC8 + 8) = result;
    result = KeGuardDispatchICall(result, (unsigned int)(v_stack_p18), v_stack_mC0, 1);
    a2 = (v_stack_mB0) + (0xFFFULL);
    v_stack_mC0 = result;
    a2 = (unsigned int)((a2) & (0xFFFFF000ULL));
    result = KeGuardDispatchICall(result, a2, 64, result);
    if ((unsigned __int8)(result) == 0) goto loc_00BE834E;
    if (((unsigned int)(v_stack_mB8)) < 8) goto loc_00BE8203;
    v_r11 = ((unsigned int)((unsigned int)(v_stack_mB8))) >> (3);
loc_00BE81CD:
    a2 = (a2) << (32);
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_mB8))) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = (result) | (a2);
    a2 = (result) ^ (result);
    v_stack_m60 = a2;
    a2 = (a2) ^ (v_r13);
    *(unsigned __int64 *)(v_stack_mC0) = a2;
    a3 = (v_stack_mC0) + (8);
    v_r11 = (v_r11) - (1);
    if (condition_is_not_equal) goto loc_00BE81CD;
loc_00BE8203:
    if ((unsigned int)(a4) == 0) goto loc_00BE823A;
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a2 = (result) ^ (result);
    v_stack_m58 = a2;
    a2 = (a2) ^ (v_r13);
loc_00BE822B:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a2);
    a3 = (a3) + (1);
    a2 = (a2) >> (8);
    a4 = (unsigned int)((a4) + ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_00BE822B;
loc_00BE823A:
    a4 = (unsigned int)(((unsigned int)(v_stack_p20)) - ((unsigned int)(v_stack_mB8)));
    v_stack_p20 = (unsigned int)((unsigned int)(v_stack_mB8));
    a3 = ((unsigned int)((unsigned int)(v_stack_mB8)) + (unsigned int)(v_stack_p10) * 1) + (v_stack_mC0);
    if (((unsigned int)(a4)) < 8) goto loc_00BE8296;
    v_r12 = ((unsigned int)((unsigned int)(a4))) >> (3);
loc_00BE8260:
    a2 = (a2) << (32);
    a4 = (unsigned int)((a4) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    result = ((unsigned int)((unsigned int)(v_stack_mB8))) | (a2);
    a2 = (result) ^ (result);
    v_stack_m50 = a2;
    a2 = (a2) ^ (v_r13);
    *(unsigned __int64 *)(a3) = a2;
    a3 = (a3) + (8);
    v_r12 = (v_r12) - (1);
    if (condition_is_not_equal) goto loc_00BE8260;
loc_00BE8296:
    if ((unsigned int)(a4) == 0) goto loc_00BE82CD;
    a2 = (a2) << (32);
    result = (v_r13) | (a2);
    a2 = (result) ^ (result);
    v_stack_m48 = a2;
    a2 = (a2) ^ (v_r13);
loc_00BE82BE:
    *(unsigned __int8 *)(a3) = (unsigned __int8)(a2);
    a3 = (a3) + (1);
    a2 = (a2) >> (8);
    a4 = (unsigned int)((a4) + ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_00BE82BE;
loc_00BE82CD:
    a1 = (v_stack_p20) + (v_stack_mC0);
    if (condition_is_equal) goto loc_00BE8362;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 2052)))) < 8) goto loc_00BE8305;
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 2052))))) >> (3);
loc_00BE82EF:
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 2052))) + ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(v_rdi);
    v_rdi = (v_rdi) + (8);
    a3 = (a1) + (8);
    a4 = (a4) - (1);
    if (condition_is_not_equal) goto loc_00BE82EF;
loc_00BE8305:
    if ((unsigned int)(a2) == 0) goto loc_00BE831A;
    a3 = (a3) - (v_rdi);
loc_00BE830C:
    *(unsigned __int8 *)(a3 + v_rdi * 1) = (unsigned __int8)(*(unsigned __int8 *)(v_rdi));
    v_rdi = (v_rdi) + (1);
    a2 = (unsigned int)((a2) + ((unsigned int)(v_r15)));
    if (condition_is_not_equal) goto loc_00BE830C;
loc_00BE831A:
    *(unsigned __int64 *)(a1 + 2024) = v_stack_mC8;
    *(unsigned int *)(a1 + 2052) = (unsigned int)((unsigned int)(v_stack_p10));
    *(unsigned int *)(a1 + 2372) = 3;
    if (condition_is_below) goto loc_00BE8365;
    *(unsigned int *)(a1 + 2520) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 2520)));
    goto loc_00BE8365;
loc_00BE834E:
    result = KeGuardDispatchICall(v_stack_mC8, a2, a3, a4);
loc_00BE835E:
loc_00BE8362:
loc_00BE8365:
loc_00BE8368:
    v_rsp = (v_rsp) + (208);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00BE7AF8(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;

    v_stack_p18 = Arg3;
    v_stack_p10 = (uint32_t)(Arg2);
    local_rsp = (local_rsp) - (208);
    if (Arg3 == 3) goto loc_00BE7E41;
    local_rbx = 0;
    local_r11 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x9D8))) & (0x8000000ULL));
    local_r10 = 0;
    if (!(condition_is_not_equal)) {
        local_r10 = *(uint32_t *)(arg1 + 0x944);
    }
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x830)));
    Arg2 = (Arg2) << (32);
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x830))) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_mB8 = Arg2;
    local_r15 = (uint32_t)((local_r13) ^ ((uint32_t)(Arg2)));
    local_r15 = (uint32_t)((local_r15) & (0x7FFULL));
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg2 = (result) ^ (result);
    result = (local_r13) ^ (Arg2);
    v_stack_mA8 = Arg2;
    Arg2 = 0;
    v_stack_mC8 = 0;
    if ((uint32_t)(local_r10) == 0) goto loc_00BE7C63;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_mA0 = Arg2;
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)(local_r13)));
    Arg2 = (uint32_t)((Arg2) & (1));
    Arg2 = (uint32_t)((Arg2) << (12));
    Arg2 = (uint32_t)((Arg2) + (0x1000ULL));
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(Arg2)));
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    v_stack_p20 = local_r15 + (uint32_t)((uint32_t)(Arg2)) * 1;
    v_stack_mC0 = local_r15 + (uint32_t)((uint32_t)(Arg2)) * 1 + 8;
    result = KeGuardDispatchICall(local_r15 + (uint32_t)((uint32_t)(Arg2)) * 1 + 8, Arg2, local_r15 + 1, a4);
    if (result == 0) goto loc_00BE7C90;
    Arg2 = (v_stack_p20) + (0xFFFULL);
    Arg2 = (uint32_t)((Arg2) & (0xFFFFF000ULL));
    result = KeGuardDispatchICall(result, Arg2, 1 + 63, a4);
    if ((uint8_t)(result) != 0) goto loc_00BE7C55;
    result = KeGuardDispatchICall(result, v_stack_p20, 1 + 63, a4);
    goto loc_00BE7C90;
loc_00BE7C55:
    *(uint64_t *)(result) = v_stack_mC0;
    local_r12 = (result) + (8);
    goto loc_00BE7C8B;
loc_00BE7C63:
    local_r11 = (uint32_t)(-(local_r11));
    Arg1 = (result) & (-64);
    Arg1 = (Arg1) + (130);
    result = KeGuardDispatchICall(Arg1, local_r15 + local_r12 * 1, (uint32_t)(v_stack_p20), a4);
loc_00BE7C8B:
    if (result != 0) goto loc_00BE7C9B;
loc_00BE7C90:
    goto loc_00BE7E39;
loc_00BE7C9B:
    if (((uint32_t)(v_stack_mC8)) < 8) goto loc_00BE7CE9;
    a4 = ((uint32_t)((uint32_t)(v_stack_mC8))) >> (3);
loc_00BE7CB7:
    Arg2 = (local_r15 + local_r12 * 1) << (32);
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mC8))) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (v_stack_mC8) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m98 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
    *(uint64_t *)(result) = Arg2;
    Arg3 = (result) + (8);
    a4 = (a4) - (1);
    if (condition_is_not_equal) goto loc_00BE7CB7;
loc_00BE7CE9:
    if ((uint32_t)(local_r11) == 0) goto loc_00BE7D26;
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m90 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
    a4 = (uint32_t)((a4) | (0xFFFFFFFFULL));
loc_00BE7D15:
    *(uint8_t *)(Arg3) = (uint8_t)(Arg2);
    Arg3 = (Arg3) + (1);
    Arg2 = (Arg2) >> (8);
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)(a4)));
    if (condition_is_not_equal) goto loc_00BE7D15;
    goto loc_00BE7D2A;
loc_00BE7D26:
    a4 = (uint32_t)((a4) | (0xFFFFFFFFULL));
loc_00BE7D2A:
    local_r15 = (uint32_t)((local_r15) - ((uint32_t)(v_stack_mC8)));
    v_stack_mC0 = (uint32_t)((uint32_t)(v_stack_mC8));
    Arg3 = (result + (uint32_t)(v_stack_p10) * 1) + ((uint32_t)((uint32_t)(v_stack_mC8)));
    if (((uint32_t)(local_r15)) < 8) goto loc_00BE7D85;
    local_r11 = ((uint32_t)((uint32_t)(local_r15))) >> (3);
loc_00BE7D4F:
    Arg2 = (v_stack_mC8) << (32);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = ((uint32_t)((uint32_t)(v_stack_mC8))) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_mC8 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
    *(uint64_t *)(Arg3) = Arg2;
    Arg3 = (Arg3) + (8);
    local_r11 = (local_r11) - (1);
    if (condition_is_not_equal) goto loc_00BE7D4F;
loc_00BE7D85:
    if ((uint32_t)(local_r15) == 0) goto loc_00BE7DBC;
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m88 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
loc_00BE7DAD:
    *(uint8_t *)(Arg3) = (uint8_t)(Arg2);
    Arg3 = (Arg3) + (1);
    Arg2 = (Arg2) >> (8);
    local_r15 = (uint32_t)((local_r15) + ((uint32_t)(a4)));
    if (condition_is_not_equal) goto loc_00BE7DAD;
loc_00BE7DBC:
    Arg1 = (v_stack_mC0) + (result);
    if (condition_is_equal) goto loc_00BE7E39;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804)))) < 8) goto loc_00BE7DF4;
    local_r11 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x804))))) >> (3);
loc_00BE7DDA:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x804))) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    *(uint64_t *)(arg1) = *(uint64_t *)(arg1);
    local_rdi = (Arg1) + (8);
    Arg3 = (Arg1) + (8);
    local_r11 = (local_r11) - (1);
    if (condition_is_not_equal) goto loc_00BE7DDA;
loc_00BE7DF4:
    if ((uint32_t)(Arg2) == 0) goto loc_00BE7E09;
    Arg3 = (Arg3) - (local_rdi);
loc_00BE7DFB:
    *(uint8_t *)(local_rdi + Arg3 * 1) = (uint8_t)(*(uint8_t *)(local_rdi));
    local_rdi = (local_rdi) + (1);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(a4)));
    if (condition_is_not_equal) goto loc_00BE7DFB;
loc_00BE7E09:
    *(uint32_t *)(arg1 + 0x944) = (uint32_t)((uint32_t)(v_stack_p18));
    *(uint32_t *)(arg1 + 0x804) = (uint32_t)((uint32_t)(v_stack_p10));
    *(uint64_t *)(arg1 + 0x7E8) = result;
    if (!(condition_is_below)) {
        *(uint32_t *)(arg1 + 0x9D8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8)));
    }
loc_00BE7E39:
    goto loc_00BE8368;
loc_00BE7E41:
    Arg2 = (Arg2) << (32);
    result = (Arg1) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m88 = Arg2;
    a4 = (uint32_t)((Arg2) ^ ((uint32_t)(local_r13)));
    a4 = (uint32_t)((a4) & (0x7FFULL));
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg3 = (result) ^ (result);
    v_stack_m90 = Arg2;
    result = (local_r13) ^ (Arg2);
    Arg2 = 0;
    v_stack_mB8 = 0;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg3 = (result) ^ (result);
    result = (uint32_t)((local_r13) ^ ((uint32_t)(Arg2)));
    v_stack_m98 = Arg2;
    result = (uint32_t)((result) & (1));
    result = (uint32_t)((result) << (12));
    result = (uint32_t)((result) + (0x1000ULL));
    result = (uint32_t)((result) + ((uint32_t)(a4)));
    v_stack_p20 = (uint32_t)(result);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_mA0 = Arg2;
    local_r12 = (uint32_t)((Arg2) ^ ((uint32_t)(local_r13)));
    local_r12 = (uint32_t)((local_r12) & (0x7FFULL));
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg3 = (result) ^ (result);
    result = (local_r13) ^ (Arg2);
    v_stack_mA8 = Arg2;
    Arg2 = 0;
    v_stack_mC0 = 0;
    result = KeGuardDispatchICall(1 + 65, local_r12 + 32, (uint32_t)(*(uint32_t *)(local_rdi + 0x830)), a4);
    local_rbx = 0;
    v_stack_mC8 = result;
    if (result != 0) goto loc_00BE7F73;
    goto loc_00BE835E;
loc_00BE7F73:
    if (((uint32_t)(v_stack_mC0)) < 8) goto loc_00BE7FC2;
    local_r15 = ((uint32_t)((uint32_t)(v_stack_mC0))) >> (3);
loc_00BE7F90:
    Arg2 = (local_r12 + 32) << (32);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mC0))) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m80 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
    *(uint64_t *)(result) = Arg2;
    Arg3 = (result) + (8);
    local_r15 = (local_r15) - (1);
    if (condition_is_not_equal) goto loc_00BE7F90;
loc_00BE7FC2:
    local_r15 = (uint32_t)((local_r15) | (0xFFFFFFFFULL));
    if ((uint32_t)(local_r10) == 0) goto loc_00BE7FFD;
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m78 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
loc_00BE7FEE:
    *(uint8_t *)(Arg3) = (uint8_t)(Arg2);
    Arg3 = (Arg3) + (1);
    Arg2 = (Arg2) >> (8);
    local_r10 = (uint32_t)((local_r10) + ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_00BE7FEE;
loc_00BE7FFD:
    local_r12 = (uint32_t)((local_rdi + 2656) - ((uint32_t)(v_stack_mC0)));
    Arg3 = ((uint32_t)((uint32_t)(v_stack_mC0))) + (v_stack_mC8);
    if (((uint32_t)(local_r12)) < 8) goto loc_00BE8051;
    local_r11 = ((uint32_t)((uint32_t)(local_r12))) >> (3);
loc_00BE801B:
    Arg2 = (Arg2) << (32);
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (local_r13) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m70 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
    *(uint64_t *)(Arg3 + 0x20) = Arg2;
    local_r10 = (Arg3 + 32) + (8);
    local_r11 = (local_r11) - (1);
    if (condition_is_not_equal) goto loc_00BE801B;
loc_00BE8051:
    if ((uint32_t)(local_r12) == 0) goto loc_00BE8088;
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m68 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
loc_00BE8079:
    *(uint8_t *)(local_r10) = (uint8_t)(Arg2);
    local_r10 = (local_r10) + (1);
    Arg2 = (Arg2) >> (8);
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_00BE8079;
loc_00BE8088:
    if (Arg3 == 0) goto loc_00BE835E;
    v_stack_mC8 = Arg3;
loc_00BE80A7:
    *(uint64_t *)(Arg3) = 0;
    result = (uint32_t)((32) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    Arg3 = (Arg3) + (8);
    Arg2 = (32 - 28) - (1);
    if (condition_is_not_equal) goto loc_00BE80A7;
    if ((uint32_t)(result) == 0) goto loc_00BE80C5;
loc_00BE80BA:
    *(uint8_t *)(Arg3) = 0;
    Arg3 = (Arg3) + (1);
    result = (uint32_t)((result) + ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_00BE80BA;
loc_00BE80C5:
    *(uint32_t *)(Arg3 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x830)));
    *(uint64_t *)(Arg3 + 0x18) = v_stack_mC8;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x830)));
    if ((((uint32_t)((uint32_t)(0x800000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x9D8))))) == 0) goto loc_00BE80F0;
    goto loc_00BE80F8;
loc_00BE80F0:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x9D8))) | ((uint32_t)((uint32_t)(0x800000ULL))));
    *(uint32_t *)(local_rdi + 0x9D8) = (uint32_t)(result);
loc_00BE80F8:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_p10)) + (v_stack_p20));
    v_stack_mE0 = 21;
    Arg2 = (21) | (-1);
    v_stack_mB0 = Arg1;
    v_stack_mE8 = 1;
    result = KeGuardDispatchICall(0, Arg2, 0, (uint32_t)((uint32_t)(Arg1)));
    v_stack_mC0 = result;
    if (result == 0) goto loc_00BE834E;
    *(uint64_t *)(v_stack_mC8) = result;
    result = KeGuardDispatchICall(v_stack_mB0, (uint32_t)(v_stack_p18), 0, (uint32_t)((uint32_t)(Arg1)));
    if (result == 0) goto loc_00BE834E;
    *(uint64_t *)(v_stack_mC8 + 0x8) = result;
    result = KeGuardDispatchICall(result, (uint32_t)(v_stack_p18), v_stack_mC0, 1);
    Arg2 = (v_stack_mB0) + (0xFFFULL);
    v_stack_mC0 = result;
    Arg2 = (uint32_t)((Arg2) & (0xFFFFF000ULL));
    result = KeGuardDispatchICall(result, Arg2, 64, result);
    if ((uint8_t)(result) == 0) goto loc_00BE834E;
    if (((uint32_t)(v_stack_mB8)) < 8) goto loc_00BE8203;
    local_r11 = ((uint32_t)((uint32_t)(v_stack_mB8))) >> (3);
loc_00BE81CD:
    Arg2 = (Arg2) << (32);
    a4 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_mB8))) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = (result) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m60 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
    *(uint64_t *)(v_stack_mC0) = Arg2;
    Arg3 = (v_stack_mC0) + (8);
    local_r11 = (local_r11) - (1);
    if (condition_is_not_equal) goto loc_00BE81CD;
loc_00BE8203:
    if ((uint32_t)(a4) == 0) goto loc_00BE823A;
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m58 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
loc_00BE822B:
    *(uint8_t *)(Arg3) = (uint8_t)(Arg2);
    Arg3 = (Arg3) + (1);
    Arg2 = (Arg2) >> (8);
    a4 = (uint32_t)((a4) + ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_00BE822B;
loc_00BE823A:
    a4 = (uint32_t)(((uint32_t)(v_stack_p20)) - ((uint32_t)(v_stack_mB8)));
    v_stack_p20 = (uint32_t)((uint32_t)(v_stack_mB8));
    Arg3 = ((uint32_t)((uint32_t)(v_stack_mB8)) + (uint32_t)(v_stack_p10) * 1) + (v_stack_mC0);
    if (((uint32_t)(a4)) < 8) goto loc_00BE8296;
    local_r12 = ((uint32_t)((uint32_t)(a4))) >> (3);
loc_00BE8260:
    Arg2 = (Arg2) << (32);
    a4 = (uint32_t)((a4) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    result = ((uint32_t)((uint32_t)(v_stack_mB8))) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m50 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
    *(uint64_t *)(Arg3) = Arg2;
    Arg3 = (Arg3) + (8);
    local_r12 = (local_r12) - (1);
    if (condition_is_not_equal) goto loc_00BE8260;
loc_00BE8296:
    if ((uint32_t)(a4) == 0) goto loc_00BE82CD;
    Arg2 = (Arg2) << (32);
    result = (local_r13) | (Arg2);
    Arg2 = (result) ^ (result);
    v_stack_m48 = Arg2;
    Arg2 = (Arg2) ^ (local_r13);
loc_00BE82BE:
    *(uint8_t *)(Arg3) = (uint8_t)(Arg2);
    Arg3 = (Arg3) + (1);
    Arg2 = (Arg2) >> (8);
    a4 = (uint32_t)((a4) + ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_00BE82BE;
loc_00BE82CD:
    Arg1 = (v_stack_p20) + (v_stack_mC0);
    if (condition_is_equal) goto loc_00BE8362;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x804)))) < 8) goto loc_00BE8305;
    a4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x804))))) >> (3);
loc_00BE82EF:
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x804))) + ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    *(uint64_t *)(arg1) = *(uint64_t *)(local_rdi);
    local_rdi = (local_rdi) + (8);
    Arg3 = (Arg1) + (8);
    a4 = (a4) - (1);
    if (condition_is_not_equal) goto loc_00BE82EF;
loc_00BE8305:
    if ((uint32_t)(Arg2) == 0) goto loc_00BE831A;
    Arg3 = (Arg3) - (local_rdi);
loc_00BE830C:
    *(uint8_t *)(Arg3 + local_rdi * 1) = (uint8_t)(*(uint8_t *)(local_rdi));
    local_rdi = (local_rdi) + (1);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(local_r15)));
    if (condition_is_not_equal) goto loc_00BE830C;
loc_00BE831A:
    *(uint64_t *)(arg1 + 0x7E8) = v_stack_mC8;
    *(uint32_t *)(arg1 + 0x804) = (uint32_t)((uint32_t)(v_stack_p10));
    *(uint32_t *)(arg1 + 0x944) = 3;
    if (condition_is_below) goto loc_00BE8365;
    *(uint32_t *)(arg1 + 0x9D8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9D8)));
    goto loc_00BE8365;
loc_00BE834E:
    result = KeGuardDispatchICall(v_stack_mC8, Arg2, Arg3, a4);
loc_00BE835E:
loc_00BE8362:
loc_00BE8365:
loc_00BE8368:
    local_rsp = (local_rsp) + (208);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0 + r8*1` | `8` | `W` |
| `Arg1` | `+ 0x100` | `64` | `R` |
| `Arg1` | `+ 0x230` | `64` | `R` |
| `Arg1` | `+ 0x238` | `64` | `R` |
| `Arg1` | `+ 0x240` | `64` | `R` |
| `Arg1` | `+ 0x348` | `64` | `R` |
| `Arg1` | `+ 0x350` | `64` | `R` |
| `Arg1` | `+ 0x358` | `64` | `R` |
| `Arg1` | `+ 0x368` | `64` | `R` |
| `Arg1` | `+ 0x804` | `32` | `R` |
| `Arg1` | `+ 0x830` | `32` | `R` |
| `Arg1` | `+ 0x944` | `32` | `R` |
| `Arg1` | `+ 0x9D8` | `32` | `R` |
| `Arg1` | `+ 0x9D8` | `32` | `W` |
| `Arg1` | `+ 0xA60` | `32` | `R/W` |
| `Arg1` | `+ 0xA60` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=initkdbg&rva=0x00BE7AF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
