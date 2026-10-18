# FsepPropagateGovernedFeatureEffectiveState

- RVA: `0x0083A89C`–`0x0083ACAF` (길이 `1,043` bytes)
- VA: `0x000000014083A89C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D7770`
- 디코드: `296`개 명령, `1,043/1,043` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0083A8E2` → [AllocateZeroMemory](../../text/4F/AllocateZeroMemory_function_004FC53C.md) (function, `0x004FC53C`)
- `0x0083AC8B` → [SafeFree](../../text/4F/SafeFree_function_004FCD88.md) (function, `0x004FCD88`)

### Direct callers
- [FseInitializeGovernedFeaturesEffectiveStates](../AC/FseInitializeGovernedFeaturesEffectiveStates_function_00AC0DAC.md) at `0x00AC0E1D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0083A8E2` → [AllocateZeroMemory](../../text/4F/AllocateZeroMemory_function_004FC53C.md) (`PAGE` → `.text`)
  - `0x0083AC8B` → [SafeFree](../../text/4F/SafeFree_function_004FCD88.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0083A89C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0083A8A1  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0083A8A6  55                              push rbp
0083A8A7  56                              push rsi
0083A8A8  57                              push rdi
0083A8A9  41 54                           push r12
0083A8AB  41 55                           push r13
0083A8AD  41 56                           push r14
0083A8AF  41 57                           push r15
0083A8B1  48 8B EC                        mov rbp, rsp
0083A8B4  48 81 EC 80 00 00 00            sub rsp, 0x80
0083A8BB  45 8B 01                        mov r8d, dword ptr [r9]
0083A8BE  8B F2                           mov esi, edx
0083A8C0  83 65 BC 00                     and dword ptr [rbp - 0x44], 0
0083A8C4  48 8B F9                        mov rdi, rcx
0083A8C7  48 83 65 C0 00                  and qword ptr [rbp - 0x40], 0
0083A8CC  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0083A8D0  41 0F B7 D0                     movzx edx, r8w
0083A8D4  49 8B D9                        mov rbx, r9
0083A8D7  41 0F B7 C0                     movzx eax, r8w
0083A8DB  48 C1 E2 03                     shl rdx, 3
0083A8DF  89 45 B8                        mov dword ptr [rbp - 0x48], eax
0083A8E2  E8 55 1C CC FF                  call 0x1404fc53c
0083A8E7  44 8B F0                        mov r14d, eax
0083A8EA  85 C0                           test eax, eax
0083A8EC  0F 88 95 03 00 00               js 0x14083ac87
0083A8F2  44 8B 5B 04                     mov r11d, dword ptr [rbx + 4]
0083A8F6  44 8B 45 BC                     mov r8d, dword ptr [rbp - 0x44]
0083A8FA  4C 8B 53 08                     mov r10, qword ptr [rbx + 8]
0083A8FE  4C 8B 6B 10                     mov r13, qword ptr [rbx + 0x10]
0083A902  4C 03 D3                        add r10, rbx
0083A905  4C 8B 65 C0                     mov r12, qword ptr [rbp - 0x40]
0083A909  4C 03 EB                        add r13, rbx
0083A90C  41 0F B7 C3                     movzx eax, r11w
0083A910  89 45 A4                        mov dword ptr [rbp - 0x5c], eax
0083A913  89 45 CC                        mov dword ptr [rbp - 0x34], eax
0083A916  0F B7 CE                        movzx ecx, si
0083A919  89 4D A0                        mov dword ptr [rbp - 0x60], ecx
0083A91C  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0083A920  4B 89 04 C4                     mov qword ptr [r12 + r8*8], rax
0083A924  B8 01 00 00 00                  mov eax, 1
0083A929  44 03 C0                        add r8d, eax
0083A92C  4C 89 55 A8                     mov qword ptr [rbp - 0x58], r10
0083A930  44 89 45 BC                     mov dword ptr [rbp - 0x44], r8d
0083A934  4C 89 6D B0                     mov qword ptr [rbp - 0x50], r13
0083A938  44 89 5D 50                     mov dword ptr [rbp + 0x50], r11d
0083A93C  89 45 C8                        mov dword ptr [rbp - 0x38], eax
0083A93F  C7 45 58 02 00 00 00            mov dword ptr [rbp + 0x58], 2
0083A946  EB 1B                           jmp 0x14083a963
0083A948  BE 01 00 00 00                  mov esi, 1
0083A94D  EB 02                           jmp 0x14083a951
0083A94F  8B F0                           mov esi, eax
0083A951  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
0083A955  44 8B 5D 50                     mov r11d, dword ptr [rbp + 0x50]
0083A959  EB 0A                           jmp 0x14083a965
0083A95B  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
0083A95F  44 8B 5D 50                     mov r11d, dword ptr [rbp + 0x50]
0083A963  8B F0                           mov esi, eax
0083A965  45 85 C0                        test r8d, r8d
0083A968  0F 84 19 03 00 00               je 0x14083ac87
0083A96E  41 FF C8                        dec r8d
0083A971  44 89 45 BC                     mov dword ptr [rbp - 0x44], r8d
0083A975  4F 8B 0C C4                     mov r9, qword ptr [r12 + r8*8]
0083A979  41 0F B7 D9                     movzx ebx, r9w
0083A97D  8B C3                           mov eax, ebx
0083A97F  4C 89 4D A0                     mov qword ptr [rbp - 0x60], r9
0083A983  48 03 C0                        add rax, rax
0083A986  8D 4B 01                        lea ecx, [rbx + 1]
0083A989  48 03 C9                        add rcx, rcx
0083A98C  41 0F 10 04 C2                  movups xmm0, xmmword ptr [r10 + rax*8]
0083A991  F3 0F 7F 45 D8                  movdqu xmmword ptr [rbp - 0x28], xmm0
0083A996  41 0F 10 04 CA                  movups xmm0, xmmword ptr [r10 + rcx*8]
0083A99B  41 8B C9                        mov ecx, r9d
0083A99E  C1 F9 10                        sar ecx, 0x10
0083A9A1  F3 0F 7F 45 E8                  movdqu xmmword ptr [rbp - 0x18], xmm0
0083A9A6  85 C9                           test ecx, ecx
0083A9A8  0F 84 A7 02 00 00               je 0x14083ac55
0083A9AE  83 F9 01                        cmp ecx, 1
0083A9B1  0F 85 CA 02 00 00               jne 0x14083ac81
0083A9B7  49 C1 E9 20                     shr r9, 0x20
0083A9BB  41 0F B7 C1                     movzx eax, r9w
0083A9BF  41 3B C3                        cmp eax, r11d
0083A9C2  75 13                           jne 0x14083a9d7
0083A9C4  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0083A9C8  48 C1 E8 20                     shr rax, 0x20
0083A9CC  41 33 C1                        xor eax, r9d
0083A9CF  0F B7 D0                        movzx edx, ax
0083A9D2  41 33 D1                        xor edx, r9d
0083A9D5  EB 11                           jmp 0x14083a9e8
0083A9D7  8B 4D A4                        mov ecx, dword ptr [rbp - 0x5c]
0083A9DA  8D 41 01                        lea eax, [rcx + 1]
0083A9DD  81 E1 00 00 FF FF               and ecx, 0xffff0000
0083A9E3  0F B7 D0                        movzx edx, ax
0083A9E6  0B D1                           or edx, ecx
0083A9E8  44 0F B7 4D EC                  movzx r9d, word ptr [rbp - 0x14]
0083A9ED  0F B7 C2                        movzx eax, dx
0083A9F0  89 55 A4                        mov dword ptr [rbp - 0x5c], edx
0083A9F3  41 3B C1                        cmp eax, r9d
0083A9F6  0F 83 69 FF FF FF               jae 0x14083a965
0083A9FC  0F B7 CA                        movzx ecx, dx
0083A9FF  41 0F B7 44 8D 02               movzx eax, word ptr [r13 + rcx*4 + 2]
0083AA05  66 2B C6                        sub ax, si
0083AA08  66 3B C6                        cmp ax, si
0083AA0B  76 0C                           jbe 0x14083aa19
0083AA0D  8D 42 01                        lea eax, [rdx + 1]
0083AA10  33 C2                           xor eax, edx
0083AA12  0F B7 C0                        movzx eax, ax
0083AA15  33 D0                           xor edx, eax
0083AA17  EB D4                           jmp 0x14083a9ed
0083AA19  0F B7 C2                        movzx eax, dx
0083AA1C  41 3B C1                        cmp eax, r9d
0083AA1F  0F 83 40 FF FF FF               jae 0x14083a965
0083AA25  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0083AA29  44 8B 7D E4                     mov r15d, dword ptr [rbp - 0x1c]
0083AA2D  4C 8B 5D A8                     mov r11, qword ptr [rbp - 0x58]
0083AA31  4B 89 04 C4                     mov qword ptr [r12 + r8*8], rax
0083AA35  44 03 C6                        add r8d, esi
0083AA38  0F B7 CA                        movzx ecx, dx
0083AA3B  41 8B F7                        mov esi, r15d
0083AA3E  D1 EE                           shr esi, 1
0083AA40  44 8B CE                        mov r9d, esi
0083AA43  44 89 45 BC                     mov dword ptr [rbp - 0x44], r8d
0083AA47  41 83 E1 03                     and r9d, 3
0083AA4B  41 8B 44 8D 00                  mov eax, dword ptr [r13 + rcx*4]
0083AA50  45 0F B7 54 8D 02               movzx r10d, word ptr [r13 + rcx*4 + 2]
0083AA56  B9 01 00 00 00                  mov ecx, 1
0083AA5B  0F B7 C0                        movzx eax, ax
0083AA5E  44 8B E8                        mov r13d, eax
0083AA61  8B D0                           mov edx, eax
0083AA63  4D 03 ED                        add r13, r13
0083AA66  47 8B 5C EB 0C                  mov r11d, dword ptr [r11 + r13*8 + 0xc]
0083AA6B  44 84 D9                        test cl, r11b
0083AA6E  75 07                           jne 0x14083aa77
0083AA70  8B 04 87                        mov eax, dword ptr [rdi + rax*4]
0083AA73  84 C1                           test cl, al
0083AA75  75 15                           jne 0x14083aa8c
0083AA77  41 8B CB                        mov ecx, r11d
0083AA7A  41 8B C3                        mov eax, r11d
0083AA7D  C1 E8 03                        shr eax, 3
0083AA80  D1 E9                           shr ecx, 1
0083AA82  83 E0 0F                        and eax, 0xf
0083AA85  C1 E1 04                        shl ecx, 4
0083AA88  0B C1                           or eax, ecx
0083AA8A  03 C0                           add eax, eax
0083AA8C  45 8B DF                        mov r11d, r15d
0083AA8F  8B C8                           mov ecx, eax
0083AA91  41 C1 EB 03                     shr r11d, 3
0083AA95  83 E1 60                        and ecx, 0x60
0083AA98  41 83 E3 0F                     and r11d, 0xf
0083AA9C  41 83 F9 02                     cmp r9d, 2
0083AAA0  75 0B                           jne 0x14083aaad
0083AAA2  41 83 FB 0F                     cmp r11d, 0xf
0083AAA6  75 0E                           jne 0x14083aab6
0083AAA8  45 33 DB                        xor r11d, r11d
0083AAAB  EB 09                           jmp 0x14083aab6
0083AAAD  45 85 C9                        test r9d, r9d
0083AAB0  0F 84 BC 00 00 00               je 0x14083ab72
0083AAB6  D1 E8                           shr eax, 1
0083AAB8  83 E0 0F                        and eax, 0xf
0083AABB  44 3B D8                        cmp r11d, eax
0083AABE  76 42                           jbe 0x14083ab02
0083AAC0  B8 02 00 00 00                  mov eax, 2
0083AAC5  66 44 3B D0                     cmp r10w, ax
0083AAC9  B8 01 00 00 00                  mov eax, 1
0083AACE  75 05                           jne 0x14083aad5
0083AAD0  44 3B C8                        cmp r9d, eax
0083AAD3  74 0A                           je 0x14083aadf
0083AAD5  66 44 3B D0                     cmp r10w, ax
0083AAD9  0F 85 93 00 00 00               jne 0x14083ab72
0083AADF  8A C8                           mov cl, al
0083AAE1  66 44 3B 55 58                  cmp r10w, word ptr [rbp + 0x58]
0083AAE6  75 0E                           jne 0x14083aaf6
0083AAE8  44 3B C8                        cmp r9d, eax
0083AAEB  0F 85 E7 00 00 00               jne 0x14083abd8
0083AAF1  E9 DD 00 00 00                  jmp 0x14083abd3
0083AAF6  66 44 3B D0                     cmp r10w, ax
0083AAFA  0F 85 D8 00 00 00               jne 0x14083abd8
0083AB00  EB 5D                           jmp 0x14083ab5f
0083AB02  0F 85 A3 00 00 00               jne 0x14083abab
0083AB08  66 44 3B 55 C8                  cmp r10w, word ptr [rbp - 0x38]
0083AB0D  75 79                           jne 0x14083ab88
0083AB0F  41 BA 02 00 00 00               mov r10d, 2
0083AB15  45 3B CA                        cmp r9d, r10d
0083AB18  75 0E                           jne 0x14083ab28
0083AB1A  83 F9 20                        cmp ecx, 0x20
0083AB1D  75 1F                           jne 0x14083ab3e
0083AB1F  85 C0                           test eax, eax
0083AB21  75 1B                           jne 0x14083ab3e
0083AB23  8D 48 01                        lea ecx, [rax + 1]
0083AB26  EB 41                           jmp 0x14083ab69
0083AB28  B8 01 00 00 00                  mov eax, 1
0083AB2D  44 3B C8                        cmp r9d, eax
0083AB30  75 0C                           jne 0x14083ab3e
0083AB32  83 F9 20                        cmp ecx, 0x20
0083AB35  74 07                           je 0x14083ab3e
0083AB37  8A C8                           mov cl, al
0083AB39  E9 9A 00 00 00                  jmp 0x14083abd8
0083AB3E  8B 04 97                        mov eax, dword ptr [rdi + rdx*4]
0083AB41  41 BA 01 00 00 00               mov r10d, 1
0083AB47  A8 60                           test al, 0x60
0083AB49  0F 95 C1                        setne cl
0083AB4C  41 84 C2                        test r10b, al
0083AB4F  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0083AB53  0F 95 C0                        setne al
0083AB56  84 C8                           test al, cl
0083AB58  75 1C                           jne 0x14083ab76
0083AB5A  B9 01 00 00 00                  mov ecx, 1
0083AB5F  B8 02 00 00 00                  mov eax, 2
0083AB64  44 3B C8                        cmp r9d, eax
0083AB67  75 6F                           jne 0x14083abd8
0083AB69  F7 04 97 00 01 00 00            test dword ptr [rdi + rdx*4], 0x100
0083AB70  74 66                           je 0x14083abd8
0083AB72  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0083AB76  44 8B 5D 50                     mov r11d, dword ptr [rbp + 0x50]
0083AB7A  BE 01 00 00 00                  mov esi, 1
0083AB7F  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
0083AB83  E9 DD FD FF FF                  jmp 0x14083a965
0083AB88  B8 02 00 00 00                  mov eax, 2
0083AB8D  66 44 3B D0                     cmp r10w, ax
0083AB91  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0083AB95  0F 85 AD FD FF FF               jne 0x14083a948
0083AB9B  B8 01 00 00 00                  mov eax, 1
0083ABA0  44 3B C8                        cmp r9d, eax
0083ABA3  0F 85 B2 FD FF FF               jne 0x14083a95b
0083ABA9  EB 26                           jmp 0x14083abd1
0083ABAB  B8 02 00 00 00                  mov eax, 2
0083ABB0  66 44 3B D0                     cmp r10w, ax
0083ABB4  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0083ABB8  75 BC                           jne 0x14083ab76
0083ABBA  B8 01 00 00 00                  mov eax, 1
0083ABBF  44 3B C8                        cmp r9d, eax
0083ABC2  0F 85 87 FD FF FF               jne 0x14083a94f
0083ABC8  83 F9 20                        cmp ecx, 0x20
0083ABCB  0F 84 8A FD FF FF               je 0x14083a95b
0083ABD1  8A C8                           mov cl, al
0083ABD3  0F BA 2C 97 08                  bts dword ptr [rdi + rdx*4], 8
0083ABD8  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0083ABDC  83 E6 03                        and esi, 3
0083ABDF  0F B6 C9                        movzx ecx, cl
0083ABE2  03 F6                           add esi, esi
0083ABE4  83 E1 01                        and ecx, 1
0083ABE7  C1 E3 07                        shl ebx, 7
0083ABEA  41 81 E7 00 00 80 FF            and r15d, 0xff800000
0083ABF1  0F BA EA 10                     bts edx, 0x10
0083ABF5  43 8B 44 EA 0C                  mov eax, dword ptr [r10 + r13*8 + 0xc]
0083ABFA  83 E0 FE                        and eax, 0xfffffffe
0083ABFD  89 55 D0                        mov dword ptr [rbp - 0x30], edx
0083AC00  33 C8                           xor ecx, eax
0083AC02  42 8D 04 DD 00 00 00 00         lea eax, [r11*8]
0083AC0A  44 8B 5D 50                     mov r11d, dword ptr [rbp + 0x50]
0083AC0E  83 E1 87                        and ecx, 0xffffff87
0083AC11  0B C8                           or ecx, eax
0083AC13  8B 45 CC                        mov eax, dword ptr [rbp - 0x34]
0083AC16  83 E1 F9                        and ecx, 0xfffffff9
0083AC19  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
0083AC1C  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
0083AC20  33 F1                           xor esi, ecx
0083AC22  81 E6 7F 00 80 FF               and esi, 0xff80007f
0083AC28  0B F3                           or esi, ebx
0083AC2A  44 33 FE                        xor r15d, esi
0083AC2D  41 81 E7 00 00 80 00            and r15d, 0x800000
0083AC34  44 33 FE                        xor r15d, esi
0083AC37  BE 01 00 00 00                  mov esi, 1
0083AC3C  47 89 7C EA 0C                  mov dword ptr [r10 + r13*8 + 0xc], r15d
0083AC41  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
0083AC45  4B 89 04 C4                     mov qword ptr [r12 + r8*8], rax
0083AC49  44 03 C6                        add r8d, esi
0083AC4C  44 89 45 BC                     mov dword ptr [rbp - 0x44], r8d
0083AC50  E9 10 FD FF FF                  jmp 0x14083a965
0083AC55  8B 45 EC                        mov eax, dword ptr [rbp - 0x14]
0083AC58  33 45 DC                        xor eax, dword ptr [rbp - 0x24]
0083AC5B  0F B7 C0                        movzx eax, ax
0083AC5E  85 C0                           test eax, eax
0083AC60  0F 84 FF FC FF FF               je 0x14083a965
0083AC66  0F BA EB 10                     bts ebx, 0x10
0083AC6A  89 5D A0                        mov dword ptr [rbp - 0x60], ebx
0083AC6D  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0083AC71  4B 89 04 C4                     mov qword ptr [r12 + r8*8], rax
0083AC75  41 FF C0                        inc r8d
0083AC78  44 89 45 BC                     mov dword ptr [rbp - 0x44], r8d
0083AC7C  E9 E4 FC FF FF                  jmp 0x14083a965
0083AC81  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
0083AC87  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0083AC8B  E8 F8 20 CC FF                  call 0x1404fcd88
0083AC90  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
0083AC98  41 8B C6                        mov eax, r14d
0083AC9B  48 81 C4 80 00 00 00            add rsp, 0x80
0083ACA2  41 5F                           pop r15
0083ACA4  41 5E                           pop r14
0083ACA6  41 5D                           pop r13
0083ACA8  41 5C                           pop r12
0083ACAA  5F                              pop rdi
0083ACAB  5E                              pop rsi
0083ACAC  5D                              pop rbp
0083ACAD  C3                              ret
0083ACAE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsepPropagateGovernedFeatureEffectiveState(__int64 a1, int a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int16 v_stack_m4C;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (128);
    a2 = ((unsigned __int16)((unsigned int)(*(unsigned int *)(a4)))) << (3);
    v_stack_m80 = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(a4))));
    result = AllocateZeroMemory(v_stack_m78, a2, (unsigned int)(*(unsigned int *)(a4)), a4);
    if (sign_flag) goto loc_0083AC87;
    v_r10 = (*(unsigned __int64 *)(a4 + 8)) + (a4);
    v_r13 = (*(unsigned __int64 *)(a4 + 16)) + (a4);
    v_stack_m94 = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(a4 + 4))));
    v_stack_m6C = (unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(a4 + 4))));
    v_stack_m98 = (unsigned int)((unsigned __int16)((unsigned int)(a2)));
    *(unsigned __int64 *)(v_stack_m78 + (unsigned int)(v_stack_m7C) * 8) = v_stack_m98;
    a3 = (unsigned int)(((unsigned int)(v_stack_m7C)) + (1));
    v_stack_m90 = v_r10;
    v_stack_m7C = a3;
    v_stack_m88 = v_r13;
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 4)));
    v_stack_m70 = 1;
    v_stack_p20 = 2;
    goto loc_0083A963;
loc_0083A948:
    goto loc_0083A951;
loc_0083A94F:
loc_0083A951:
    goto loc_0083A965;
loc_0083A95B:
loc_0083A963:
loc_0083A965:
    if (a3 == 0) goto loc_0083AC87;
    a3 = (unsigned int)((a3) - 1);
    v_stack_m7C = a3;
    v_stack_m98 = *(unsigned __int64 *)(v_stack_m78 + a3 * 8);
    result = ((unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(v_stack_m78 + a3 * 8))))) + ((unsigned int)((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(v_stack_m78 + a3 * 8)))));
    a1 = ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m78 + a3 * 8)) + 1) + ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m78 + a3 * 8)) + 1);
    v_stack_m60 = v_xmm0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m78 + a3 * 8)))) >> (16));
    v_stack_m50 = v_xmm0;
    if ((unsigned int)(a1) == 0) goto loc_0083AC55;
    if (((unsigned int)(a1)) != 1) goto loc_0083AC81;
    a4 = (*(unsigned __int64 *)(v_stack_m78 + a3 * 8)) >> (32);
    if (((unsigned int)((unsigned __int16)(a4))) != ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_0083A9D7;
    result = (v_stack_m60) >> (32);
    result = (unsigned int)((result) ^ ((unsigned int)(a4)));
    a2 = (unsigned int)(((unsigned __int16)(result)) ^ ((unsigned int)(a4)));
    goto loc_0083A9E8;
loc_0083A9D7:
    a1 = (unsigned int)(((unsigned int)(v_stack_m94)) & (0xFFFF0000ULL));
    a2 = (unsigned int)(((unsigned __int16)((unsigned int)(v_stack_m94) + 1)) | ((unsigned int)(a1)));
loc_0083A9E8:
loc_0083A9ED:
    v_stack_m94 = a2;
    if (((unsigned int)((unsigned __int16)(a2))) >= ((unsigned int)(v_stack_m4C))) goto loc_0083A965;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_m88 + (unsigned __int16)(a2) * 4 + 2)) - (1));
    if (((unsigned __int16)(result)) <= 1) goto loc_0083AA19;
    result = (unsigned int)((a2 + 1) ^ (a2));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned __int16)(result))));
    goto loc_0083A9ED;
loc_0083AA19:
    if (((unsigned int)((unsigned __int16)(a2))) >= ((unsigned int)(v_stack_m4C))) goto loc_0083A965;
    *(unsigned __int64 *)(v_stack_m78 + a3 * 8) = v_stack_m98;
    a3 = (unsigned int)((a3) + (1));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m54)))) >> (1));
    v_stack_m7C = a3;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) & (3));
    v_r13 = ((unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4)))))) + ((unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4))))));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m90 + v_r13 * 8 + 12))))) != 0) goto loc_0083AA77;
    result = (unsigned int)(*(unsigned int *)(a1 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4))) * 4));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + (unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4))) * 4))))) == 0) {
        a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + v_r13 * 8 + 12)));
        result = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + v_r13 * 8 + 12)));
        result = (unsigned int)((result) >> (3));
        a1 = (unsigned int)((a1) >> (1));
        result = (unsigned int)((result) & (15));
        a1 = (unsigned int)((a1) << (4));
        result = (unsigned int)((result) | ((unsigned int)(a1)));
        result = (unsigned int)((result) + ((unsigned int)(result)));
    }
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m54)))) >> (3));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (96));
    v_r11 = (unsigned int)((v_r11) & (15));
    if (((unsigned int)(a4)) != 2) goto loc_0083AAAD;
    if (((unsigned int)(v_r11)) != 15) goto loc_0083AAB6;
    v_r11 = 0;
    goto loc_0083AAB6;
loc_0083AAAD:
    if ((unsigned int)(a4) == 0) goto loc_0083AB72;
loc_0083AAB6:
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) & (15));
    if (0 <= ((unsigned int)(result))) goto loc_0083AB02;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88 + (unsigned __int16)(a2) * 4 + 2))) != 2) goto loc_0083AAD5;
    if (((unsigned int)(a4)) == 1) goto loc_0083AADF;
loc_0083AAD5:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88 + (unsigned __int16)(a2) * 4 + 2))) != 1) goto loc_0083AB72;
loc_0083AADF:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88 + (unsigned __int16)(a2) * 4 + 2))) != v_stack_p20) goto loc_0083AAF6;
    if (((unsigned int)(a4)) != 1) goto loc_0083ABD8;
    goto loc_0083ABD3;
loc_0083AAF6:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88 + (unsigned __int16)(a2) * 4 + 2))) != 1) goto loc_0083ABD8;
    goto loc_0083AB5F;
loc_0083AB02:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88 + (unsigned __int16)(a2) * 4 + 2))) != 1) goto loc_0083ABAB;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m88 + (unsigned __int16)(a2) * 4 + 2))) != v_stack_m70) goto loc_0083AB88;
    if (((unsigned int)(a4)) != 2) goto loc_0083AB28;
    if (1 != 32) goto loc_0083AB3E;
    if (1 != 0) goto loc_0083AB3E;
    goto loc_0083AB69;
loc_0083AB28:
    if (((unsigned int)(a4)) != 1) goto loc_0083AB3E;
    if (((unsigned int)(1 + 1)) == 32) goto loc_0083AB3E;
    goto loc_0083ABD8;
loc_0083AB3E:
    a1 = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4))))) * 4)))) & (96)) != 0) ? 1 : 0;
    result = (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4))))) * 4))))) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_0083AB76;
loc_0083AB5F:
    if (((unsigned int)(a4)) != 2) goto loc_0083ABD8;
loc_0083AB69:
    if (((*(unsigned int *)(a1 + (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4))))) * 4)) & (256)) == 0) goto loc_0083ABD8;
loc_0083AB72:
loc_0083AB76:
    goto loc_0083A965;
loc_0083AB88:
    if (((unsigned __int16)(v_stack_m90)) != 2) goto loc_0083A948;
    if (((unsigned int)(a4)) != 1) goto loc_0083A95B;
    goto loc_0083ABD1;
loc_0083ABAB:
    if (((unsigned __int16)(v_stack_m90)) != 2) goto loc_0083AB76;
    if (((unsigned int)(a4)) != 1) goto loc_0083A94F;
    if (1 == 32) goto loc_0083A95B;
loc_0083ABD1:
loc_0083ABD3:
loc_0083ABD8:
    v_rsi = (unsigned int)((1) & (3));
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(v_rsi)));
    a1 = (unsigned int)((1) & (1));
    v_rbx = (unsigned int)(((unsigned __int16)(*(unsigned __int64 *)(v_stack_m78 + a3 * 8))) << (7));
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m54)) & (0xFF800000ULL));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m90 + v_stack_m88 * 8 + 12))) & (0xFFFFFFFEULL));
    v_stack_m68 = (unsigned int)((unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4))))));
    a1 = (unsigned int)((a1) ^ ((unsigned int)(result)));
    a1 = (unsigned int)((a1) & (0xFFFFFF87ULL));
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned int)(v_stack_p18) * 8)));
    a1 = (unsigned int)((a1) & (0xFFFFFFF9ULL));
    v_stack_m64 = (unsigned int)((unsigned int)(v_stack_m6C));
    v_rsi = (unsigned int)((v_rsi) ^ ((unsigned int)(a1)));
    v_rsi = (unsigned int)((v_rsi) & (0xFF80007FULL));
    v_rsi = (unsigned int)((v_rsi) | ((unsigned int)(v_rbx)));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(v_rsi)));
    v_r15 = (unsigned int)((v_r15) & (0x800000ULL));
    v_r15 = (unsigned int)((v_r15) ^ ((unsigned int)(v_rsi)));
    *(unsigned int *)(v_stack_m90 + v_stack_m88 * 8 + 12) = (unsigned int)(v_r15);
    *(unsigned __int64 *)(v_stack_m78 + a3 * 8) = v_stack_m68;
    a3 = (unsigned int)((a3) + (1));
    v_stack_m7C = a3;
    goto loc_0083A965;
loc_0083AC55:
    result = (unsigned int)(((unsigned int)(v_stack_m4C)) ^ (v_stack_m5C));
    if ((unsigned int)((unsigned __int16)(result)) == 0) goto loc_0083A965;
    v_stack_m98 = (unsigned int)(v_rbx);
    *(unsigned __int64 *)(v_stack_m78 + a3 * 8) = v_stack_m98;
    a3 = (unsigned int)((a3) + 1);
    v_stack_m7C = a3;
    goto loc_0083A965;
loc_0083AC81:
loc_0083AC87:
    result = SafeFree(v_stack_m78, (unsigned int)((unsigned int)((unsigned __int16)((unsigned int)(*(unsigned int *)(v_stack_m88 + (unsigned __int16)(a2) * 4))))), a3, a4);
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)(0xC000000DULL)));
}
```

## 5. (Beta) C Style

```c
int64_t FsepPropagateGovernedFeatureEffectiveState(void *Arg1, int32_t Arg2, int32_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint16_t v_stack_m4C;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (128);
    Arg2 = ((uint16_t)((uint32_t)(*(uint32_t *)(arg4)))) << (3);
    v_stack_m80 = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(arg4))));
    result = AllocateZeroMemory(v_stack_m78, Arg2, (uint32_t)(*(uint32_t *)(arg4)), Arg4);
    if (sign_flag) goto loc_0083AC87;
    local_r10 = (*(uint64_t *)(arg4 + 0x8)) + (Arg4);
    local_r13 = (*(uint64_t *)(arg4 + 0x10)) + (Arg4);
    v_stack_m94 = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))));
    v_stack_m6C = (uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4))));
    v_stack_m98 = (uint32_t)((uint16_t)((uint32_t)(Arg2)));
    *(uint64_t *)(v_stack_m78 + (uint32_t)(v_stack_m7C) * 8) = v_stack_m98;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m7C)) + (1));
    v_stack_m90 = local_r10;
    v_stack_m7C = Arg3;
    v_stack_m88 = local_r13;
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x4)));
    v_stack_m70 = 1;
    v_stack_p20 = 2;
    goto loc_0083A963;
loc_0083A948:
    goto loc_0083A951;
loc_0083A94F:
loc_0083A951:
    goto loc_0083A965;
loc_0083A95B:
loc_0083A963:
loc_0083A965:
    if (Arg3 == 0) goto loc_0083AC87;
    Arg3 = (uint32_t)((Arg3) - 1);
    v_stack_m7C = Arg3;
    v_stack_m98 = *(uint64_t *)(v_stack_m78 + Arg3 * 8);
    result = ((uint32_t)((uint32_t)((uint16_t)(*(uint64_t *)(v_stack_m78 + Arg3 * 8))))) + ((uint32_t)((uint32_t)((uint16_t)(*(uint64_t *)(v_stack_m78 + Arg3 * 8)))));
    Arg1 = ((uint16_t)(*(uint64_t *)(v_stack_m78 + Arg3 * 8)) + 1) + ((uint16_t)(*(uint64_t *)(v_stack_m78 + Arg3 * 8)) + 1);
    v_stack_m60 = v_xmm0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m78 + Arg3 * 8)))) >> (16));
    v_stack_m50 = v_xmm0;
    if ((uint32_t)(Arg1) == 0) goto loc_0083AC55;
    if (((uint32_t)(Arg1)) != 1) goto loc_0083AC81;
    Arg4 = (*(uint64_t *)(v_stack_m78 + Arg3 * 8)) >> (32);
    if (((uint32_t)((uint16_t)(Arg4))) != ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_0083A9D7;
    result = (v_stack_m60) >> (32);
    result = (uint32_t)((result) ^ ((uint32_t)(Arg4)));
    Arg2 = (uint32_t)(((uint16_t)(result)) ^ ((uint32_t)(Arg4)));
    goto loc_0083A9E8;
loc_0083A9D7:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m94)) & (0xFFFF0000ULL));
    Arg2 = (uint32_t)(((uint16_t)((uint32_t)(v_stack_m94) + 1)) | ((uint32_t)(Arg1)));
loc_0083A9E8:
loc_0083A9ED:
    v_stack_m94 = Arg2;
    if (((uint32_t)((uint16_t)(Arg2))) >= ((uint32_t)(v_stack_m4C))) goto loc_0083A965;
    result = (uint16_t)((*(uint16_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4 + 0x2)) - (1));
    if (((uint16_t)(result)) <= 1) goto loc_0083AA19;
    result = (uint32_t)((Arg2 + 1) ^ (Arg2));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint16_t)(result))));
    goto loc_0083A9ED;
loc_0083AA19:
    if (((uint32_t)((uint16_t)(Arg2))) >= ((uint32_t)(v_stack_m4C))) goto loc_0083A965;
    *(uint64_t *)(v_stack_m78 + Arg3 * 8) = v_stack_m98;
    Arg3 = (uint32_t)((Arg3) + (1));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m54)))) >> (1));
    v_stack_m7C = Arg3;
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) & (3));
    local_r13 = ((uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4)))))) + ((uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4))))));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + local_r13 * 8 + 0xC))))) != 0) goto loc_0083AA77;
    result = (uint32_t)(*(uint32_t *)(arg1 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4))) * 4));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + (uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4))) * 4))))) == 0) {
        Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + local_r13 * 8 + 0xC)));
        result = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + local_r13 * 8 + 0xC)));
        result = (uint32_t)((result) >> (3));
        Arg1 = (uint32_t)((Arg1) >> (1));
        result = (uint32_t)((result) & (15));
        Arg1 = (uint32_t)((Arg1) << (4));
        result = (uint32_t)((result) | ((uint32_t)(Arg1)));
        result = (uint32_t)((result) + ((uint32_t)(result)));
    }
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m54)))) >> (3));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (96));
    local_r11 = (uint32_t)((local_r11) & (15));
    if (((uint32_t)(Arg4)) != 2) goto loc_0083AAAD;
    if (((uint32_t)(local_r11)) != 15) goto loc_0083AAB6;
    local_r11 = 0;
    goto loc_0083AAB6;
loc_0083AAAD:
    if ((uint32_t)(Arg4) == 0) goto loc_0083AB72;
loc_0083AAB6:
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) & (15));
    if (0 <= ((uint32_t)(result))) goto loc_0083AB02;
    if (((uint16_t)(*(uint16_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4 + 0x2))) != 2) goto loc_0083AAD5;
    if (((uint32_t)(Arg4)) == 1) goto loc_0083AADF;
loc_0083AAD5:
    if (((uint16_t)(*(uint16_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4 + 0x2))) != 1) goto loc_0083AB72;
loc_0083AADF:
    if (((uint16_t)(*(uint16_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4 + 0x2))) != v_stack_p20) goto loc_0083AAF6;
    if (((uint32_t)(Arg4)) != 1) goto loc_0083ABD8;
    goto loc_0083ABD3;
loc_0083AAF6:
    if (((uint16_t)(*(uint16_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4 + 0x2))) != 1) goto loc_0083ABD8;
    goto loc_0083AB5F;
loc_0083AB02:
    if (((uint16_t)(*(uint16_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4 + 0x2))) != 1) goto loc_0083ABAB;
    if (((uint16_t)(*(uint16_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4 + 0x2))) != v_stack_m70) goto loc_0083AB88;
    if (((uint32_t)(Arg4)) != 2) goto loc_0083AB28;
    if (1 != 32) goto loc_0083AB3E;
    if (1 != 0) goto loc_0083AB3E;
    goto loc_0083AB69;
loc_0083AB28:
    if (((uint32_t)(Arg4)) != 1) goto loc_0083AB3E;
    if (((uint32_t)(1 + 1)) == 32) goto loc_0083AB3E;
    goto loc_0083ABD8;
loc_0083AB3E:
    Arg1 = ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4))))) * 4)))) & (96)) != 0) ? 1 : 0;
    result = (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4))))) * 4))))) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_0083AB76;
loc_0083AB5F:
    if (((uint32_t)(Arg4)) != 2) goto loc_0083ABD8;
loc_0083AB69:
    if (((*(uint32_t *)(arg1 + (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4))))) * 4)) & (256)) == 0) goto loc_0083ABD8;
loc_0083AB72:
loc_0083AB76:
    goto loc_0083A965;
loc_0083AB88:
    if (((uint16_t)(v_stack_m90)) != 2) goto loc_0083A948;
    if (((uint32_t)(Arg4)) != 1) goto loc_0083A95B;
    goto loc_0083ABD1;
loc_0083ABAB:
    if (((uint16_t)(v_stack_m90)) != 2) goto loc_0083AB76;
    if (((uint32_t)(Arg4)) != 1) goto loc_0083A94F;
    if (1 == 32) goto loc_0083A95B;
loc_0083ABD1:
loc_0083ABD3:
loc_0083ABD8:
    local_rsi = (uint32_t)((1) & (3));
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(local_rsi)));
    Arg1 = (uint32_t)((1) & (1));
    local_rbx = (uint32_t)(((uint16_t)(*(uint64_t *)(v_stack_m78 + Arg3 * 8))) << (7));
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m54)) & (0xFF800000ULL));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m90 + v_stack_m88 * 8 + 0xC))) & (0xFFFFFFFEULL));
    v_stack_m68 = (uint32_t)((uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4))))));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)(result)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFF87ULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint32_t)(v_stack_p18) * 8)));
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFF9ULL));
    v_stack_m64 = (uint32_t)((uint32_t)(v_stack_m6C));
    local_rsi = (uint32_t)((local_rsi) ^ ((uint32_t)(Arg1)));
    local_rsi = (uint32_t)((local_rsi) & (0xFF80007FULL));
    local_rsi = (uint32_t)((local_rsi) | ((uint32_t)(local_rbx)));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(local_rsi)));
    local_r15 = (uint32_t)((local_r15) & (0x800000ULL));
    local_r15 = (uint32_t)((local_r15) ^ ((uint32_t)(local_rsi)));
    *(uint32_t *)(v_stack_m90 + v_stack_m88 * 8 + 0xC) = (uint32_t)(local_r15);
    *(uint64_t *)(v_stack_m78 + Arg3 * 8) = v_stack_m68;
    Arg3 = (uint32_t)((Arg3) + (1));
    v_stack_m7C = Arg3;
    goto loc_0083A965;
loc_0083AC55:
    result = (uint32_t)(((uint32_t)(v_stack_m4C)) ^ (v_stack_m5C));
    if ((uint32_t)((uint16_t)(result)) == 0) goto loc_0083A965;
    v_stack_m98 = (uint32_t)(local_rbx);
    *(uint64_t *)(v_stack_m78 + Arg3 * 8) = v_stack_m98;
    Arg3 = (uint32_t)((Arg3) + 1);
    v_stack_m7C = Arg3;
    goto loc_0083A965;
loc_0083AC81:
loc_0083AC87:
    result = SafeFree(v_stack_m78, (uint32_t)((uint32_t)((uint16_t)((uint32_t)(*(uint32_t *)(v_stack_m88 + (uint16_t)(Arg2) * 4))))), Arg3, Arg4);
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)(0xC000000DULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rax*4` | `32` | `R` |
| `Arg1` | `+ 0x0 + rdx*4` | `32` | `R` |
| `Arg1` | `+ 0x0 + rdx*4` | `32` | `R/W` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x4` | `32` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0083A89C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
