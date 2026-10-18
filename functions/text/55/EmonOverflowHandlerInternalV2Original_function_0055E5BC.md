# EmonOverflowHandlerInternalV2Original

- RVA: `0x0055E5BC`–`0x0055EA4B` (길이 `1,167` bytes)
- VA: `0x000000014055E5BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C4948`
- 디코드: `317`개 명령, `1,167/1,167` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **10**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x0055E607` → [EmonPebsOverflowHandler](EmonPebsOverflowHandler_function_0055ED7C.md) (function, `0x0055ED7C`)
- `0x0055E653` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0055E7B5` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0055E7BE` → [KeProfileInterruptWithSource](../4A/KeProfileInterruptWithSource_function_004A34D0.md) (function, `0x004A34D0`)
- `0x0055E824` → [PoGetProcessorIdleAccounting](../4F/PoGetProcessorIdleAccounting_function_004FBEA0.md) (function, `0x004FBEA0`)
- `0x0055E834` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0055E8B6` → [PoGetProcessorIdleAccounting](../4F/PoGetProcessorIdleAccounting_function_004FBEA0.md) (function, `0x004FBEA0`)
- `0x0055E8D9` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x0055E94A` → [KeProfileInterruptWithSource](../4A/KeProfileInterruptWithSource_function_004A34D0.md) (function, `0x004A34D0`)
- `0x0055E9A3` → [EmonIsModifiedByBadActorInternalOriginal](../49/EmonIsModifiedByBadActorInternalOriginal_function_004928FC.md) (function, `0x004928FC`)

### Direct callers
- [EmonOverflowHandlerOriginal](EmonOverflowHandlerOriginal_function_0055EA60.md) at `0x0055EA8B`

### Static image references
- `0x0055E5F2` → RVA `0x00F8FE28` (`.data`; read)
- `0x0055E619` → RVA `0x00F8FE00` (`.data`; read)
- `0x0055E670` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x0055E7A1` → RVA `0x00E10360` (`.data`; read)
- `0x0055E7CB` → RVA `0x00FC21E8` (`.data`; read)
- `0x0055E86E` → RVA `0x00F8FE14` (`.data`; read)
- `0x0055E9F5` → RVA `0x00F8FE10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0055E5BC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0055E5C1  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0055E5C6  55                              push rbp
0055E5C7  56                              push rsi
0055E5C8  57                              push rdi
0055E5C9  41 54                           push r12
0055E5CB  41 55                           push r13
0055E5CD  41 56                           push r14
0055E5CF  41 57                           push r15
0055E5D1  48 8B EC                        mov rbp, rsp
0055E5D4  48 83 EC 60                     sub rsp, 0x60
0055E5D8  83 65 50 00                     and dword ptr [rbp + 0x50], 0
0055E5DC  4C 8B E1                        mov r12, rcx
0055E5DF  B9 8E 03 00 00                  mov ecx, 0x38e
0055E5E4  8B FA                           mov edi, edx
0055E5E6  0F 32                           rdmsr
0055E5E8  48 C1 E2 20                     shl rdx, 0x20
0055E5EC  48 0B C2                        or rax, rdx
0055E5EF  48 8B D8                        mov rbx, rax
0055E5F2  48 23 1D 2F 18 A3 00            and rbx, qword ptr [rip + 0xa3182f]
0055E5F9  48 0F BA E3 3E                  bt rbx, 0x3e
0055E5FE  48 89 5D F8                     mov qword ptr [rbp - 8], rbx
0055E602  4C 8B F3                        mov r14, rbx
0055E605  73 12                           jae 0x14055e619
0055E607  E8 70 07 00 00                  call 0x14055ed7c
0055E60C  48 B8 FF FF FF FF FF FF FF BF   movabs rax, 0xbfffffffffffffff
0055E616  4C 23 F0                        and r14, rax
0055E619  48 8B 1D E0 17 A3 00            mov rbx, qword ptr [rip + 0xa317e0]
0055E620  4C 8D 2D D9 17 A3 00            lea r13, [rip + 0xa317d9]
0055E627  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
0055E62B  4C 8B FF                        mov r15, rdi
0055E62E  49 3B DD                        cmp rbx, r13
0055E631  74 33                           je 0x14055e666
0055E633  48 8D 34 BF                     lea rsi, [rdi + rdi*4]
0055E637  48 03 F6                        add rsi, rsi
0055E63A  48 8B 7C F3 20                  mov rdi, qword ptr [rbx + rsi*8 + 0x20]
0055E63F  49 23 FE                        and rdi, r14
0055E642  74 14                           je 0x14055e658
0055E644  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0055E648  48 85 C0                        test rax, rax
0055E64B  74 0B                           je 0x14055e658
0055E64D  48 8B D3                        mov rdx, rbx
0055E650  48 8B CF                        mov rcx, rdi
0055E653  E8 78 C4 15 00                  call 0x1406baad0
0055E658  48 8B 1B                        mov rbx, qword ptr [rbx]
0055E65B  48 F7 D7                        not rdi
0055E65E  4C 23 F7                        and r14, rdi
0055E661  49 3B DD                        cmp rbx, r13
0055E664  75 D4                           jne 0x14055e63a
0055E666  49 0F BC F6                     bsf rsi, r14
0055E66A  0F 84 5A 03 00 00               je 0x14055e9ca
0055E670  48 8D 15 C9 A5 A6 00            lea rdx, [rip + 0xa6a5c9]
0055E677  45 33 DB                        xor r11d, r11d
0055E67A  8B C6                           mov eax, esi
0055E67C  41 8B CB                        mov ecx, r11d
0055E67F  49 0F B3 C6                     btr r14, rax
0055E683  83 FE 20                        cmp esi, 0x20
0055E686  72 08                           jb 0x14055e690
0055E688  83 C6 E0                        add esi, -0x20
0055E68B  B9 01 00 00 00                  mov ecx, 1
0055E690  4A 8B 04 FA                     mov rax, qword ptr [rdx + r15*8]
0055E694  4C 8B 78 58                     mov r15, qword ptr [rax + 0x58]
0055E698  85 C9                           test ecx, ecx
0055E69A  74 24                           je 0x14055e6c0
0055E69C  83 E9 01                        sub ecx, 1
0055E69F  74 1B                           je 0x14055e6bc
0055E6A1  83 E9 63                        sub ecx, 0x63
0055E6A4  74 10                           je 0x14055e6b6
0055E6A6  83 F9 01                        cmp ecx, 1
0055E6A9  74 05                           je 0x14055e6b0
0055E6AB  4D 8B FB                        mov r15, r11
0055E6AE  EB 10                           jmp 0x14055e6c0
0055E6B0  49 83 C7 48                     add r15, 0x48
0055E6B4  EB 0A                           jmp 0x14055e6c0
0055E6B6  49 83 C7 30                     add r15, 0x30
0055E6BA  EB 04                           jmp 0x14055e6c0
0055E6BC  49 83 C7 18                     add r15, 0x18
0055E6C0  4C 8D 04 76                     lea r8, [rsi + rsi*2]
0055E6C4  49 C1 E0 04                     shl r8, 4
0055E6C8  4D 03 47 10                     add r8, qword ptr [r15 + 0x10]
0055E6CC  45 39 58 18                     cmp dword ptr [r8 + 0x18], r11d
0055E6D0  0F 85 E6 02 00 00               jne 0x14055e9bc
0055E6D6  41 8B 17                        mov edx, dword ptr [r15]
0055E6D9  49 8B DB                        mov rbx, r11
0055E6DC  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
0055E6E0  45 8B EB                        mov r13d, r11d
0055E6E3  4C 89 5D D0                     mov qword ptr [rbp - 0x30], r11
0055E6E7  44 88 5D 50                     mov byte ptr [rbp + 0x50], r11b
0055E6EB  4C 89 5D E8                     mov qword ptr [rbp - 0x18], r11
0055E6EF  83 FA 01                        cmp edx, 1
0055E6F2  74 39                           je 0x14055e72d
0055E6F4  89 75 58                        mov dword ptr [rbp + 0x58], esi
0055E6F7  44 8B D6                        mov r10d, esi
0055E6FA  85 D2                           test edx, edx
0055E6FC  74 0A                           je 0x14055e708
0055E6FE  83 FA 01                        cmp edx, 1
0055E701  74 32                           je 0x14055e735
0055E703  E9 8B 00 00 00                  jmp 0x14055e793
0055E708  8D 8E 86 01 00 00               lea ecx, [rsi + 0x186]
0055E70E  0F 32                           rdmsr
0055E710  48 C1 E2 20                     shl rdx, 0x20
0055E714  48 0B C2                        or rax, rdx
0055E717  89 75 58                        mov dword ptr [rbp + 0x58], esi
0055E71A  48 8B D0                        mov rdx, rax
0055E71D  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0055E721  48 81 E2 FF FF AF FF            and rdx, 0xffffffffffafffff
0055E728  48 8B C2                        mov rax, rdx
0055E72B  EB 59                           jmp 0x14055e786
0055E72D  44 8D 56 20                     lea r10d, [rsi + 0x20]
0055E731  44 89 55 58                     mov dword ptr [rbp + 0x58], r10d
0055E735  B9 8D 03 00 00                  mov ecx, 0x38d
0055E73A  0F 32                           rdmsr
0055E73C  48 C1 E2 20                     shl rdx, 0x20
0055E740  8D 0C B5 00 00 00 00            lea ecx, [rsi*4]
0055E747  48 0B C2                        or rax, rdx
0055E74A  4C 8B C8                        mov r9, rax
0055E74D  B8 0F 00 00 00                  mov eax, 0xf
0055E752  48 D3 E0                        shl rax, cl
0055E755  B9 8F 03 00 00                  mov ecx, 0x38f
0055E75A  48 F7 D0                        not rax
0055E75D  4C 23 C8                        and r9, rax
0055E760  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
0055E764  0F 32                           rdmsr
0055E766  48 C1 E2 20                     shl rdx, 0x20
0055E76A  48 0B C2                        or rax, rdx
0055E76D  41 8B CA                        mov ecx, r10d
0055E770  4C 8B C8                        mov r9, rax
0055E773  49 0F B3 C9                     btr r9, rcx
0055E777  B9 8F 03 00 00                  mov ecx, 0x38f
0055E77C  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
0055E780  49 8B D1                        mov rdx, r9
0055E783  49 8B C1                        mov rax, r9
0055E786  48 C1 EA 20                     shr rdx, 0x20
0055E78A  49 8B D8                        mov rbx, r8
0055E78D  0F 30                           wrmsr
0055E78F  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
0055E793  8B 53 24                        mov edx, dword ptr [rbx + 0x24]
0055E796  49 8B CC                        mov rcx, r12
0055E799  85 D2                           test edx, edx
0055E79B  0F 85 A9 01 00 00               jne 0x14055e94a
0055E7A1  48 8B 05 B8 1B 8B 00            mov rax, qword ptr [rip + 0x8b1bb8]
0055E7A8  4C 89 5D D8                     mov qword ptr [rbp - 0x28], r11
0055E7AC  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
0055E7B0  48 85 C0                        test rax, rax
0055E7B3  74 07                           je 0x14055e7bc
0055E7B5  E8 16 C3 15 00                  call 0x1406baad0
0055E7BA  EB 07                           jmp 0x14055e7c3
0055E7BC  33 D2                           xor edx, edx
0055E7BE  E8 0D 4D F4 FF                  call 0x1404a34d0
0055E7C3  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0055E7CB  48 8B 3D 16 3A A6 00            mov rdi, qword ptr [rip + 0xa63a16]
0055E7D2  8B C8                           mov ecx, eax
0055E7D4  48 69 D9 28 01 00 00            imul rbx, rcx, 0x128
0055E7DB  8B 4C 3B 18                     mov ecx, dword ptr [rbx + rdi + 0x18]
0055E7DF  85 C9                           test ecx, ecx
0055E7E1  74 73                           je 0x14055e856
0055E7E3  8B 44 3B 20                     mov eax, dword ptr [rbx + rdi + 0x20]
0055E7E7  44 8B 6C 3B 10                  mov r13d, dword ptr [rbx + rdi + 0x10]
0055E7EC  44 8B E0                        mov r12d, eax
0055E7EF  49 C1 E4 04                     shl r12, 4
0055E7F3  4C 03 E3                        add r12, rbx
0055E7F6  FF C0                           inc eax
0055E7F8  83 E0 0F                        and eax, 0xf
0055E7FB  89 44 3B 20                     mov dword ptr [rbx + rdi + 0x20], eax
0055E7FF  8B 44 3B 14                     mov eax, dword ptr [rbx + rdi + 0x14]
0055E803  85 C0                           test eax, eax
0055E805  75 7F                           jne 0x14055e886
0055E807  33 D2                           xor edx, edx
0055E809  B8 10 27 00 00                  mov eax, 0x2710
0055E80E  F7 F1                           div ecx
0055E810  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0055E814  85 C0                           test eax, eax
0055E816  75 08                           jne 0x14055e820
0055E818  C7 44 3B 14 01 00 00 00         mov dword ptr [rbx + rdi + 0x14], 1
0055E820  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0055E824  E8 77 D6 F9 FF                  call 0x1404fbea0
0055E829  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0055E82D  33 C9                           xor ecx, ecx
0055E82F  48 89 44 3B 08                  mov qword ptr [rbx + rdi + 8], rax
0055E834  E8 A7 FF E1 FF                  call 0x14037e7e0
0055E839  48 8B 0D A8 39 A6 00            mov rcx, qword ptr [rip + 0xa639a8]
0055E840  48 89 04 0B                     mov qword ptr [rbx + rcx], rax
0055E844  45 89 6C 3C 28                  mov dword ptr [r12 + rdi + 0x28], r13d
0055E849  48 8B 04 0B                     mov rax, qword ptr [rbx + rcx]
0055E84D  49 89 44 3C 30                  mov qword ptr [r12 + rdi + 0x30], rax
0055E852  4C 8B 65 40                     mov r12, qword ptr [rbp + 0x40]
0055E856  48 8B 5D C8                     mov rbx, qword ptr [rbp - 0x38]
0055E85A  41 8B 0F                        mov ecx, dword ptr [r15]
0055E85D  85 C9                           test ecx, ecx
0055E85F  0F 84 90 01 00 00               je 0x14055e9f5
0055E865  83 F9 01                        cmp ecx, 1
0055E868  0F 85 28 01 00 00               jne 0x14055e996
0055E86E  8B 0D A0 15 A3 00               mov ecx, dword ptr [rip + 0xa315a0]
0055E874  83 F9 40                        cmp ecx, 0x40
0055E877  0F 82 DA 00 00 00               jb 0x14055e957
0055E87D  48 83 C8 FF                     or rax, 0xffffffffffffffff
0055E881  E9 DC 00 00 00                  jmp 0x14055e962
0055E886  83 E8 01                        sub eax, 1
0055E889  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0055E88D  75 C3                           jne 0x14055e852
0055E88F  33 D2                           xor edx, edx
0055E891  B8 10 27 00 00                  mov eax, 0x2710
0055E896  F7 F1                           div ecx
0055E898  89 45 C0                        mov dword ptr [rbp - 0x40], eax
0055E89B  89 44 3B 14                     mov dword ptr [rbx + rdi + 0x14], eax
0055E89F  85 C0                           test eax, eax
0055E8A1  75 0F                           jne 0x14055e8b2
0055E8A3  C7 44 3B 14 01 00 00 00         mov dword ptr [rbx + rdi + 0x14], 1
0055E8AB  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
0055E8B2  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0055E8B6  E8 E5 D5 F9 FF                  call 0x1404fbea0
0055E8BB  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0055E8BF  48 3B 44 3B 08                  cmp rax, qword ptr [rbx + rdi + 8]
0055E8C4  0F 85 63 FF FF FF               jne 0x14055e82d
0055E8CA  41 8B C5                        mov eax, r13d
0055E8CD  48 8D 4D E0                     lea rcx, [rbp - 0x20]
0055E8D1  0F AF 45 C0                     imul eax, dword ptr [rbp - 0x40]
0055E8D5  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0055E8D9  E8 02 FF E1 FF                  call 0x14037e7e0
0055E8DE  4C 8B 05 03 39 A6 00            mov r8, qword ptr [rip + 0xa63903]
0055E8E5  48 8B C8                        mov rcx, rax
0055E8E8  4C 8B C8                        mov r9, rax
0055E8EB  4A 2B 0C 03                     sub rcx, qword ptr [rbx + r8]
0055E8EF  75 0F                           jne 0x14055e900
0055E8F1  45 89 6C 3C 28                  mov dword ptr [r12 + rdi + 0x28], r13d
0055E8F6  4D 89 4C 3C 30                  mov qword ptr [r12 + rdi + 0x30], r9
0055E8FB  E9 52 FF FF FF                  jmp 0x14055e852
0055E900  42 8B 44 03 18                  mov eax, dword ptr [rbx + r8 + 0x18]
0055E905  33 D2                           xor edx, edx
0055E907  48 0F AF 45 D8                  imul rax, qword ptr [rbp - 0x28]
0055E90C  48 F7 F1                        div rcx
0055E90F  48 8B C8                        mov rcx, rax
0055E912  48 B8 BD 42 7A E5 D5 94 BF D6   movabs rax, 0xd6bf94d5e57a42bd
0055E91C  48 0F AF 4D E0                  imul rcx, qword ptr [rbp - 0x20]
0055E921  48 F7 E1                        mul rcx
0055E924  4C 8B EA                        mov r13, rdx
0055E927  49 C1 ED 17                     shr r13, 0x17
0055E92B  49 8D 85 00 F0 FF FF            lea rax, [r13 - 0x1000]
0055E932  48 3D FF EF FF 7F               cmp rax, 0x7fffefff
0055E938  76 05                           jbe 0x14055e93f
0055E93A  46 8B 6C 03 1C                  mov r13d, dword ptr [rbx + r8 + 0x1c]
0055E93F  46 89 6C 03 10                  mov dword ptr [rbx + r8 + 0x10], r13d
0055E944  4E 89 0C 03                     mov qword ptr [rbx + r8], r9
0055E948  EB A7                           jmp 0x14055e8f1
0055E94A  E8 81 4B F4 FF                  call 0x1404a34d0
0055E94F  44 8B 2B                        mov r13d, dword ptr [rbx]
0055E952  E9 03 FF FF FF                  jmp 0x14055e85a
0055E957  B8 01 00 00 00                  mov eax, 1
0055E95C  48 D3 E0                        shl rax, cl
0055E95F  48 FF C8                        dec rax
0055E962  41 8B D5                        mov edx, r13d
0055E965  8D 8E 09 03 00 00               lea ecx, [rsi + 0x309]
0055E96B  48 F7 DA                        neg rdx
0055E96E  48 23 D0                        and rdx, rax
0055E971  48 8B C2                        mov rax, rdx
0055E974  48 C1 EA 20                     shr rdx, 0x20
0055E978  0F 30                           wrmsr
0055E97A  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0055E97D  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0055E981  48 0F AB C1                     bts rcx, rax
0055E985  48 8B D1                        mov rdx, rcx
0055E988  48 8B C1                        mov rax, rcx
0055E98B  48 C1 EA 20                     shr rdx, 0x20
0055E98F  B9 8F 03 00 00                  mov ecx, 0x38f
0055E994  0F 30                           wrmsr
0055E996  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
0055E99A  4C 8D 4D 50                     lea r9, [rbp + 0x50]
0055E99E  49 8B D7                        mov rdx, r15
0055E9A1  8B CE                           mov ecx, esi
0055E9A3  E8 54 3F F3 FF                  call 0x1404928fc
0055E9A8  45 33 DB                        xor r11d, r11d
0055E9AB  48 8D 15 8E A2 A6 00            lea rdx, [rip + 0xa6a28e]
0055E9B2  44 38 5D 50                     cmp byte ptr [rbp + 0x50], r11b
0055E9B6  74 04                           je 0x14055e9bc
0055E9B8  C6 43 28 01                     mov byte ptr [rbx + 0x28], 1
0055E9BC  49 0F BC F6                     bsf rsi, r14
0055E9C0  4C 8B 7D F0                     mov r15, qword ptr [rbp - 0x10]
0055E9C4  0F 85 B0 FC FF FF               jne 0x14055e67a
0055E9CA  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
0055E9CE  B9 90 03 00 00                  mov ecx, 0x390
0055E9D3  48 8B C2                        mov rax, rdx
0055E9D6  48 C1 EA 20                     shr rdx, 0x20
0055E9DA  0F 30                           wrmsr
0055E9DC  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
0055E9E4  48 83 C4 60                     add rsp, 0x60
0055E9E8  41 5F                           pop r15
0055E9EA  41 5E                           pop r14
0055E9EC  41 5D                           pop r13
0055E9EE  41 5C                           pop r12
0055E9F0  5F                              pop rdi
0055E9F1  5E                              pop rsi
0055E9F2  5D                              pop rbp
0055E9F3  C3                              ret
0055E9F4  CC                              int3
0055E9F5  8B 0D 15 14 A3 00               mov ecx, dword ptr [rip + 0xa31415]
0055E9FB  83 F9 40                        cmp ecx, 0x40
0055E9FE  72 06                           jb 0x14055ea06
0055EA00  48 83 C8 FF                     or rax, 0xffffffffffffffff
0055EA04  EB 0B                           jmp 0x14055ea11
0055EA06  B8 01 00 00 00                  mov eax, 1
0055EA0B  48 D3 E0                        shl rax, cl
0055EA0E  48 FF C8                        dec rax
0055EA11  41 8B D5                        mov edx, r13d
0055EA14  8D 8E C1 00 00 00               lea ecx, [rsi + 0xc1]
0055EA1A  48 F7 DA                        neg rdx
0055EA1D  48 23 D0                        and rdx, rax
0055EA20  48 8B C2                        mov rax, rdx
0055EA23  48 C1 EA 20                     shr rdx, 0x20
0055EA27  0F 30                           wrmsr
0055EA29  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
0055EA2D  8D 8E 86 01 00 00               lea ecx, [rsi + 0x186]
0055EA33  49 8B D0                        mov rdx, r8
0055EA36  48 81 CA 00 00 50 00            or rdx, 0x500000
0055EA3D  48 8B C2                        mov rax, rdx
0055EA40  48 C1 EA 20                     shr rdx, 0x20
0055EA44  0F 30                           wrmsr
0055EA46  E9 4F FF FF FF                  jmp 0x14055e99a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EmonOverflowHandlerInternalV2Original(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (96);
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_rbx = (result) & (*(unsigned __int64 *)(v_rip + 10688559));
    v_stack_m40 = v_rbx;
    v_r14 = v_rbx;
    if (!(condition_is_above_or_equal)) {
        result = EmonPebsOverflowHandler(910, a2, a3, a4);
        v_r14 = (v_rbx) & (result);
    }
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    if ((*(unsigned __int64 *)(v_rip + 10688480)) == (v_rip + 10688473)) goto loc_0055E666;
    v_rsi = ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4) + ((unsigned int)((unsigned int)(a2)) + (unsigned int)((unsigned int)(a2)) * 4);
loc_0055E63A:
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10688480) + v_rsi * 8 + 32)) & (v_r14);
    if (condition_is_equal) goto loc_0055E658;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10688480) + 16);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10688480) + 16) != 0) {
        a2 = *(unsigned __int64 *)(v_rip + 10688480);
        a1 = v_rdi;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rdi = ~(v_rdi);
    v_r14 = (v_r14) & (v_rdi);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10688480))) != (v_rip + 10688473)) goto loc_0055E63A;
loc_0055E666:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10688480))) == (v_rip + 10688473)) goto loc_0055E9CA;
    v_r11 = 0;
loc_0055E67A:
    if (((unsigned int)(v_rsi)) >= 32) {
        v_rsi = (unsigned int)((v_rsi) + (-32));
        a1 = 1;
    }
    if ((unsigned int)(a1) == 0) goto loc_0055E6C0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0055E6BC;
    a1 = (unsigned int)((a1) - (99));
    if (condition_is_equal) goto loc_0055E6B6;
    if (((unsigned int)(a1)) == 1) goto loc_0055E6B0;
    goto loc_0055E6C0;
loc_0055E6B0:
    v_r15 = (0) + (72);
    goto loc_0055E6C0;
loc_0055E6B6:
    v_r15 = (v_r15) + (48);
    goto loc_0055E6C0;
loc_0055E6BC:
    v_r15 = (v_r15) + (24);
loc_0055E6C0:
    a3 = (v_rsi + v_rsi * 2) << (4);
    a3 = (a3) + (*(unsigned __int64 *)(v_r15 + 16));
    if ((*(unsigned int *)(a3 + 24)) != 0) goto loc_0055E9BC;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_p18 = 0;
    v_stack_m50 = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))) == 1) goto loc_0055E72D;
    v_stack_p20 = (unsigned int)(v_rsi);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15))) == 0) goto loc_0055E708;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))) == 1) goto loc_0055E735;
    goto loc_0055E793;
loc_0055E708:
    a2 = ((unsigned int)(*(unsigned int *)(v_r15))) << (32);
    result = (*(unsigned __int64 *)(v_rip + 10921417 + (unsigned int)((unsigned int)(a2)) * 8)) | (a2);
    v_stack_p20 = (unsigned int)(v_rsi);
    v_stack_m68 = result;
    a2 = (result) & (0xFFFFFFFFFFAFFFFFULL);
    goto loc_0055E786;
loc_0055E72D:
    v_stack_p20 = (unsigned int)(v_rsi + 32);
loc_0055E735:
    a2 = (a2) << (32);
    result = (a2) | (a2);
    result = (15) << ((unsigned __int8)(v_rsi * 4));
    result = ~(result);
    a4 = (result) & (result);
    v_stack_m68 = a4;
    a2 = (a2) << (32);
    result = (result) | (a2);
    v_stack_m50 = result;
loc_0055E786:
    a2 = (result) >> (32);
    v_stack_m70 = a3;
loc_0055E793:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 36))) != 0) goto loc_0055E94A;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    if (*(unsigned __int64 *)(v_rip + 9116600) == 0) goto loc_0055E7BC;
    result = guard_dispatch_icall(a1, (unsigned int)(*(unsigned int *)(a3 + 36)), a3, result);
    goto loc_0055E7C3;
loc_0055E7BC:
    a2 = 0;
    result = KeProfileInterruptWithSource(a1, a2, a3, result);
loc_0055E7C3:
    v_rbx = (a3) * ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 24))) == 0) goto loc_0055E856;
    v_r12 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 32))))) << (4);
    v_r12 = (v_r12) + (v_rbx);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 32))) + 1);
    result = (unsigned int)((result) & (15));
    *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 32) = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 20))) != 0) goto loc_0055E886;
    a2 = 0;
    *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 20) = (unsigned int)((unsigned int)(0x2710ULL));
    if ((unsigned int)((unsigned int)(0x2710ULL)) == 0) {
        *(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 20) = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m60, a2, a3, result);
loc_0055E82D:
    a1 = 0;
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 8) = v_stack_m60;
    result = KeQueryPerformanceCounter(a1, a2, a3, result);
    *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893736) * 1) = result;
    *(unsigned int *)(v_r12 + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 16)));
    *(unsigned __int64 *)(v_r12 + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 48) = *(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893736) * 1);
loc_0055E852:
loc_0055E856:
loc_0055E85A:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15))) == 0) goto loc_0055E9F5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_r15)))) != 1) goto loc_0055E996;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10687904)))) < 64) goto loc_0055E957;
    result = (*(unsigned __int64 *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893736) * 1)) | (-1);
    goto loc_0055E962;
loc_0055E886:
    result = (unsigned int)((result) - (1));
    *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 20) = (unsigned int)(result);
    if (condition_is_not_equal) goto loc_0055E852;
    a2 = 0;
    v_stack_m78 = (unsigned int)((unsigned int)(0x2710ULL));
    *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 20) = (unsigned int)((unsigned int)(0x2710ULL));
    if ((unsigned int)((unsigned int)(0x2710ULL)) == 0) {
        *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 20) = 1;
        v_stack_m78 = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m60, a2, a3, result);
    if (v_stack_m60 != (*(unsigned __int64 *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 8))) goto loc_0055E82D;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 16))))) * (v_stack_m78));
    v_stack_m60 = result;
    result = KeQueryPerformanceCounter(v_stack_m58, a2, a3, result);
    a1 = (result) - (*(unsigned __int64 *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893571) * 1));
    if (condition_is_not_equal) goto loc_0055E900;
loc_0055E8F1:
    *(unsigned int *)(v_stack_p8 + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 40) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 16)));
    *(unsigned __int64 *)(v_stack_p8 + *(unsigned __int64 *)(v_rip + 10893846) * 1 + 48) = result;
    goto loc_0055E852;
loc_0055E900:
    a2 = 0;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893571) * 1 + 24))) * (v_stack_m60);
    a1 = (result) * (v_stack_m58);
    v_r13 = (0) >> (23);
    if ((v_r13 - 4096) >= = 0x7FFFEFFFULL) {
        v_r13 = *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893571) * 1 + 28);
    }
    *(unsigned int *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893571) * 1 + 16) = (unsigned int)(v_r13);
    *(unsigned __int64 *)(v_stack_m70 + *(unsigned __int64 *)(v_rip + 10893571) * 1) = result;
    goto loc_0055E8F1;
loc_0055E94A:
    result = KeProfileInterruptWithSource(a1, a2, *(unsigned __int64 *)(v_rip + 10893571), result);
    goto loc_0055E85A;
loc_0055E957:
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - 1;
loc_0055E962:
    a2 = -((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70)))));
    a2 = (a2) & (result);
    a2 = (a2) >> (32);
    a2 = (v_stack_m50) >> (32);
loc_0055E996:
loc_0055E99A:
    result = EmonIsModifiedByBadActorInternalOriginal((unsigned int)((unsigned int)(v_rsi)), v_r15, v_stack_m68, v_stack_p18);
    v_r11 = 0;
    if (v_stack_p18 != 0) {
        *(unsigned __int8 *)(v_stack_m70 + 40) = 1;
    }
    if (v_stack_p18 != 0) goto loc_0055E67A;
loc_0055E9CA:
    a2 = (v_stack_m40) >> (32);
    v_rsp = (v_rsp) + (96);
    return v_stack_m40;
loc_0055E9F5:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10687509)))) < 64) goto loc_0055EA06;
    result = (v_stack_m40) | (-1);
    goto loc_0055EA11;
loc_0055EA06:
    result = (1) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10687509))));
    result = (result) - 1;
loc_0055EA11:
    a2 = -((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m70)))));
    a2 = (a2) & (result);
    a2 = (a2) >> (32);
    a2 = (v_stack_m68) | (0x500000ULL);
    a2 = (a2) >> (32);
    goto loc_0055E99A;
}
```

## 5. (Beta) C Style

```c
int64_t EmonOverflowHandlerInternalV2Original(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (96);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    local_rbx = (result) & (*(uint64_t *)(v_rip + 0xA3182F));
    v_stack_m40 = local_rbx;
    local_r14 = local_rbx;
    if (!(condition_is_above_or_equal)) {
        result = EmonPebsOverflowHandler(910, Arg2, a3, a4);
        local_r14 = (local_rbx) & (result);
    }
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    if ((*(uint64_t *)(v_rip + 0xA317E0)) == (v_rip + 10688473)) goto loc_0055E666;
    local_rsi = ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4) + ((uint32_t)((uint32_t)(Arg2)) + (uint32_t)((uint32_t)(Arg2)) * 4);
loc_0055E63A:
    local_rdi = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA317E0) + local_rsi * 8 + 0x20)) & (local_r14);
    if (condition_is_equal) goto loc_0055E658;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0xA317E0) + 0x10);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0xA317E0) + 0x10) != 0) {
        Arg2 = *(uint64_t *)(v_rip + 0xA317E0);
        Arg1 = local_rdi;
        result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    }
    local_rdi = ~(local_rdi);
    local_r14 = (local_r14) & (local_rdi);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA317E0))) != (v_rip + 10688473)) goto loc_0055E63A;
loc_0055E666:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xA317E0))) == (v_rip + 10688473)) goto loc_0055E9CA;
    local_r11 = 0;
loc_0055E67A:
    if (((uint32_t)(local_rsi)) >= 32) {
        local_rsi = (uint32_t)((local_rsi) + (-32));
        Arg1 = 1;
    }
    if ((uint32_t)(Arg1) == 0) goto loc_0055E6C0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0055E6BC;
    Arg1 = (uint32_t)((Arg1) - (99));
    if (condition_is_equal) goto loc_0055E6B6;
    if (((uint32_t)(Arg1)) == 1) goto loc_0055E6B0;
    goto loc_0055E6C0;
loc_0055E6B0:
    local_r15 = (0) + (72);
    goto loc_0055E6C0;
loc_0055E6B6:
    local_r15 = (local_r15) + (48);
    goto loc_0055E6C0;
loc_0055E6BC:
    local_r15 = (local_r15) + (24);
loc_0055E6C0:
    a3 = (local_rsi + local_rsi * 2) << (4);
    a3 = (a3) + (*(uint64_t *)(local_r15 + 0x10));
    if ((*(uint32_t *)(a3 + 0x18)) != 0) goto loc_0055E9BC;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_p18 = 0;
    v_stack_m50 = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))) == 1) goto loc_0055E72D;
    v_stack_p20 = (uint32_t)(local_rsi);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15))) == 0) goto loc_0055E708;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))) == 1) goto loc_0055E735;
    goto loc_0055E793;
loc_0055E708:
    Arg2 = ((uint32_t)(*(uint32_t *)(local_r15))) << (32);
    result = (*(uint64_t *)(v_rip + 0xA6A5C9 + (uint32_t)((uint32_t)(arg2)) * 8)) | (Arg2);
    v_stack_p20 = (uint32_t)(local_rsi);
    v_stack_m68 = result;
    Arg2 = (result) & (0xFFFFFFFFFFAFFFFFULL);
    goto loc_0055E786;
loc_0055E72D:
    v_stack_p20 = (uint32_t)(local_rsi + 32);
loc_0055E735:
    Arg2 = (Arg2) << (32);
    result = (Arg2) | (Arg2);
    result = (15) << ((uint8_t)(local_rsi * 4));
    result = ~(result);
    a4 = (result) & (result);
    v_stack_m68 = a4;
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    v_stack_m50 = result;
loc_0055E786:
    Arg2 = (result) >> (32);
    v_stack_m70 = a3;
loc_0055E793:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(a3 + 0x24))) != 0) goto loc_0055E94A;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    if (*(uint64_t *)(v_rip + 0x8B1BB8) == 0) goto loc_0055E7BC;
    result = guard_dispatch_icall(Arg1, (uint32_t)(*(uint32_t *)(a3 + 0x24)), a3, result);
    goto loc_0055E7C3;
loc_0055E7BC:
    Arg2 = 0;
    result = KeProfileInterruptWithSource(Arg1, Arg2, a3, result);
loc_0055E7C3:
    local_rbx = (a3) * ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x18))) == 0) goto loc_0055E856;
    local_r12 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x20))))) << (4);
    local_r12 = (local_r12) + (local_rbx);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x20))) + 1);
    result = (uint32_t)((result) & (15));
    *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x20) = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x14))) != 0) goto loc_0055E886;
    Arg2 = 0;
    *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x14) = (uint32_t)((uint32_t)(0x2710ULL));
    if ((uint32_t)((uint32_t)(0x2710ULL)) == 0) {
        *(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x14) = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m60, Arg2, a3, result);
loc_0055E82D:
    Arg1 = 0;
    *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x8) = v_stack_m60;
    result = KeQueryPerformanceCounter(Arg1, Arg2, a3, result);
    *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA639A8) * 1) = result;
    *(uint32_t *)(local_r12 + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x10)));
    *(uint64_t *)(local_r12 + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x30) = *(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA639A8) * 1);
loc_0055E852:
loc_0055E856:
loc_0055E85A:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15))) == 0) goto loc_0055E9F5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_r15)))) != 1) goto loc_0055E996;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA315A0)))) < 64) goto loc_0055E957;
    result = (*(uint64_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA639A8) * 1)) | (-1);
    goto loc_0055E962;
loc_0055E886:
    result = (uint32_t)((result) - (1));
    *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x14) = (uint32_t)(result);
    if (condition_is_not_equal) goto loc_0055E852;
    Arg2 = 0;
    v_stack_m78 = (uint32_t)((uint32_t)(0x2710ULL));
    *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x14) = (uint32_t)((uint32_t)(0x2710ULL));
    if ((uint32_t)((uint32_t)(0x2710ULL)) == 0) {
        *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x14) = 1;
        v_stack_m78 = 1;
    }
    result = PoGetProcessorIdleAccounting(v_stack_m60, Arg2, a3, result);
    if (v_stack_m60 != (*(uint64_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x8))) goto loc_0055E82D;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x10))))) * (v_stack_m78));
    v_stack_m60 = result;
    result = KeQueryPerformanceCounter(v_stack_m58, Arg2, a3, result);
    Arg1 = (result) - (*(uint64_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63903) * 1));
    if (condition_is_not_equal) goto loc_0055E900;
loc_0055E8F1:
    *(uint32_t *)(v_stack_p8 + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x28) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x10)));
    *(uint64_t *)(v_stack_p8 + *(uint64_t *)(v_rip + 0xA63A16) * 1 + 0x30) = result;
    goto loc_0055E852;
loc_0055E900:
    Arg2 = 0;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63903) * 1 + 0x18))) * (v_stack_m60);
    Arg1 = (result) * (v_stack_m58);
    local_r13 = (0) >> (23);
    if ((local_r13 - 4096) >= = 0x7FFFEFFFULL) {
        local_r13 = *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63903) * 1 + 0x1C);
    }
    *(uint32_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63903) * 1 + 0x10) = (uint32_t)(local_r13);
    *(uint64_t *)(v_stack_m70 + *(uint64_t *)(v_rip + 0xA63903) * 1) = result;
    goto loc_0055E8F1;
loc_0055E94A:
    result = KeProfileInterruptWithSource(Arg1, Arg2, *(uint64_t *)(v_rip + 0xA63903), result);
    goto loc_0055E85A;
loc_0055E957:
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - 1;
loc_0055E962:
    Arg2 = -((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70)))));
    Arg2 = (Arg2) & (result);
    Arg2 = (Arg2) >> (32);
    Arg2 = (v_stack_m50) >> (32);
loc_0055E996:
loc_0055E99A:
    result = EmonIsModifiedByBadActorInternalOriginal((uint32_t)((uint32_t)(local_rsi)), local_r15, v_stack_m68, v_stack_p18);
    local_r11 = 0;
    if (v_stack_p18 != 0) {
        *(uint8_t *)(v_stack_m70 + 0x28) = 1;
    }
    if (v_stack_p18 != 0) goto loc_0055E67A;
loc_0055E9CA:
    Arg2 = (v_stack_m40) >> (32);
    local_rsp = (local_rsp) + (96);
    return v_stack_m40;
loc_0055E9F5:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA31415)))) < 64) goto loc_0055EA06;
    result = (v_stack_m40) | (-1);
    goto loc_0055EA11;
loc_0055EA06:
    result = (1) << ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA31415))));
    result = (result) - 1;
loc_0055EA11:
    Arg2 = -((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m70)))));
    Arg2 = (Arg2) & (result);
    Arg2 = (Arg2) >> (32);
    Arg2 = (v_stack_m68) | (0x500000ULL);
    Arg2 = (Arg2) >> (32);
    goto loc_0055E99A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0 + rdi*4` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0055E5BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
