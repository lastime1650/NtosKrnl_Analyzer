# KasanDriverLoadImageInternal

- RVA: `0x004C2840`–`0x004C2DB3` (길이 `1,395` bytes)
- VA: `0x00000001404C2840`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCB10`
- 디코드: `353`개 명령, `1,395/1,395` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x004C2909` → [strncmp](../6C/strncmp_function_006C6720.md) (function, `0x006C6720`)
- `0x004C2A11` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x004C2A62` → [KasanTrackAddress](../46/KasanTrackAddress_function_00462520.md) (function, `0x00462520`)
- `0x004C2B05` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C2B33` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C2B83` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C2B9F` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C2BBB` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C2BD6` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C2C48` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004C2C7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004C2C9B` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C2CB7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C2CD0` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x004C2CDD` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004C2D1E` → [KasanUnloadInfoCompare](../5A/KasanUnloadInfoCompare_function_005AADC0.md) (function, `0x005AADC0`)
- `0x004C2D6D` → [RtlRbInsertNodeEx](../2E/RtlRbInsertNodeEx_function_002E4570.md) (function, `0x002E4570`)
- `0x004C2D83` → [KasaniSendTelemetryDriver](../5A/KasaniSendTelemetryDriver_function_005ABD40.md) (function, `0x005ABD40`)
- `0x004C2D93` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)

### Direct callers
- [KasanDriverLoadImage](KasanDriverLoadImage_function_004C2820.md) at `0x004C2826`
- [KasanInitializeLoadedModules](../../init/C3/KasanInitializeLoadedModules_function_00C36D20.md) at `0x00C36D3F`
- [MiInitializeLoadedModuleList](../../init/C6/MiInitializeLoadedModuleList_function_00C6BCDC.md) at `0x00C6BEEB`

### Static image references
- `0x004C28FF` → RVA `0x006CB490` (` ?? ::FNODOBFM::`string'`; read)
- `0x004C2934` → RVA `0x00FCEC68` (`ALMOSTRO`; read)
- `0x004C2962` → RVA `0x00FC52D8` (`ALMOSTRO`; read)
- `0x004C2ADC` → RVA `0x00FC6ED8` (`ALMOSTRO`; read)
- `0x004C2CD6` → RVA `0x00F65500` (`.data`; read)
- `0x004C2CE2` → RVA `0x00E663E0` (`.data`; read)
- `0x004C2CE9` → RVA `0x00E663D8` (`.data`; read)
- `0x004C2D72` → RVA `0x00FCEC6B` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x004C2A11` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x004C2C7C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C2840  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
004C2844  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
004C2849  53                              push rbx
004C284A  55                              push rbp
004C284B  56                              push rsi
004C284C  57                              push rdi
004C284D  41 54                           push r12
004C284F  41 55                           push r13
004C2851  41 56                           push r14
004C2853  41 57                           push r15
004C2855  48 83 EC 48                     sub rsp, 0x48
004C2859  48 8B 69 30                     mov rbp, qword ptr [rcx + 0x30]
004C285D  4C 8B E1                        mov r12, rcx
004C2860  44 8B B9 98 00 00 00            mov r15d, dword ptr [rcx + 0x98]
004C2867  4C 03 FD                        add r15, rbp
004C286A  48 8D 45 FF                     lea rax, [rbp - 1]
004C286E  48 83 F8 FD                     cmp rax, -3
004C2872  0F 87 20 05 00 00               ja 0x1404c2d98
004C2878  B8 4D 5A 00 00                  mov eax, 0x5a4d
004C287D  66 39 45 00                     cmp word ptr [rbp], ax
004C2881  0F 85 11 05 00 00               jne 0x1404c2d98
004C2887  8B 55 3C                        mov edx, dword ptr [rbp + 0x3c]
004C288A  48 03 D5                        add rdx, rbp
004C288D  48 3B D5                        cmp rdx, rbp
004C2890  0F 82 02 05 00 00               jb 0x1404c2d98
004C2896  48 B9 FF FF FE FF FF 7F 00 00   movabs rcx, 0x7ffffffeffff
004C28A0  48 3B E9                        cmp rbp, rcx
004C28A3  77 19                           ja 0x1404c28be
004C28A5  48 8D 82 07 01 00 00            lea rax, [rdx + 0x107]
004C28AC  48 3B C2                        cmp rax, rdx
004C28AF  0F 82 E3 04 00 00               jb 0x1404c2d98
004C28B5  48 3B C1                        cmp rax, rcx
004C28B8  0F 87 DA 04 00 00               ja 0x1404c2d98
004C28BE  81 3A 50 45 00 00               cmp dword ptr [rdx], 0x4550
004C28C4  0F 85 CE 04 00 00               jne 0x1404c2d98
004C28CA  48 85 D2                        test rdx, rdx
004C28CD  0F 84 C5 04 00 00               je 0x1404c2d98
004C28D3  0F B7 7A 14                     movzx edi, word ptr [rdx + 0x14]
004C28D7  0F B7 72 06                     movzx esi, word ptr [rdx + 6]
004C28DB  48 83 C7 18                     add rdi, 0x18
004C28DF  48 03 FA                        add rdi, rdx
004C28E2  45 33 ED                        xor r13d, r13d
004C28E5  41 0F B7 DD                     movzx ebx, r13w
004C28E9  0F 1F 80 00 00 00 00            nop dword ptr [rax]
004C28F0  66 3B DE                        cmp bx, si
004C28F3  0F 83 9F 04 00 00               jae 0x1404c2d98
004C28F9  41 B8 08 00 00 00               mov r8d, 8
004C28FF  48 8D 15 8A 8B 20 00            lea rdx, [rip + 0x208b8a]
004C2906  48 8B CF                        mov rcx, rdi
004C2909  E8 12 3E 20 00                  call 0x1406c6720
004C290E  85 C0                           test eax, eax
004C2910  74 09                           je 0x1404c291b
004C2912  48 83 C7 28                     add rdi, 0x28
004C2916  66 FF C3                        inc bx
004C2919  EB D5                           jmp 0x1404c28f0
004C291B  48 85 FF                        test rdi, rdi
004C291E  0F 84 74 04 00 00               je 0x1404c2d98
004C2924  8B 5F 0C                        mov ebx, dword ptr [rdi + 0xc]
004C2927  44 8B 77 08                     mov r14d, dword ptr [rdi + 8]
004C292B  48 03 DD                        add rbx, rbp
004C292E  0F 84 64 04 00 00               je 0x1404c2d98
004C2934  44 38 2D 2D C3 B0 00            cmp byte ptr [rip + 0xb0c32d], r13b
004C293B  0F 84 6B 04 00 00               je 0x1404c2dac
004C2941  49 83 FE 40                     cmp r14, 0x40
004C2945  0F 82 61 04 00 00               jb 0x1404c2dac
004C294B  41 F6 C6 3F                     test r14b, 0x3f
004C294F  0F 85 57 04 00 00               jne 0x1404c2dac
004C2955  83 3B 02                        cmp dword ptr [rbx], 2
004C2958  0F 85 4E 04 00 00               jne 0x1404c2dac
004C295E  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
004C2962  48 8B 05 6F 29 B0 00            mov rax, qword ptr [rip + 0xb0296f]
004C2969  48 89 01                        mov qword ptr [rcx], rax
004C296C  44 39 AC 24 98 00 00 00         cmp dword ptr [rsp + 0x98], r13d
004C2974  0F 85 1E 04 00 00               jne 0x1404c2d98
004C297A  48 8D 43 40                     lea rax, [rbx + 0x40]
004C297E  49 83 C6 C0                     add r14, -0x40
004C2982  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004C2987  4D 8B C5                        mov r8, r13
004C298A  48 8D 43 48                     lea rax, [rbx + 0x48]
004C298E  49 C1 EE 06                     shr r14, 6
004C2992  4D 3B C6                        cmp r8, r14
004C2995  73 51                           jae 0x1404c29e8
004C2997  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
004C299B  48 85 D2                        test rdx, rdx
004C299E  0F 84 08 04 00 00               je 0x1404c2dac
004C29A4  48 39 10                        cmp qword ptr [rax], rdx
004C29A7  0F 87 FF 03 00 00               ja 0x1404c2dac
004C29AD  48 8B 48 F8                     mov rcx, qword ptr [rax - 8]
004C29B1  48 3B CD                        cmp rcx, rbp
004C29B4  0F 82 F2 03 00 00               jb 0x1404c2dac
004C29BA  49 3B CF                        cmp rcx, r15
004C29BD  0F 83 E9 03 00 00               jae 0x1404c2dac
004C29C3  4C 8D 0C 11                     lea r9, [rcx + rdx]
004C29C7  4C 3B C9                        cmp r9, rcx
004C29CA  72 12                           jb 0x1404c29de
004C29CC  4D 3B CF                        cmp r9, r15
004C29CF  0F 87 D7 03 00 00               ja 0x1404c2dac
004C29D5  49 FF C0                        inc r8
004C29D8  48 83 C0 40                     add rax, 0x40
004C29DC  EB B4                           jmp 0x1404c2992
004C29DE  B8 95 00 00 C0                  mov eax, 0xc0000095
004C29E3  E9 B2 03 00 00                  jmp 0x1404c2d9a
004C29E8  B8 10 00 00 00                  mov eax, 0x10
004C29ED  4C 89 AC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r13
004C29F5  49 F7 E6                        mul r14
004C29F8  48 85 D2                        test rdx, rdx
004C29FB  75 E1                           jne 0x1404c29de
004C29FD  48 8D 50 28                     lea rdx, [rax + 0x28]
004C2A01  48 3B D0                        cmp rdx, rax
004C2A04  72 D8                           jb 0x1404c29de
004C2A06  B9 40 00 00 00                  mov ecx, 0x40
004C2A0B  41 B8 4B 61 55 6E               mov r8d, 0x6e55614b
004C2A11  E8 DA F6 6B 00                  call 0x140b820f0
004C2A16  4C 8B E8                        mov r13, rax
004C2A19  48 85 C0                        test rax, rax
004C2A1C  75 0A                           jne 0x1404c2a28
004C2A1E  B8 9A 00 00 C0                  mov eax, 0xc000009a
004C2A23  E9 72 03 00 00                  jmp 0x1404c2d9a
004C2A28  33 F6                           xor esi, esi
004C2A2A  4C 89 60 18                     mov qword ptr [rax + 0x18], r12
004C2A2E  4C 89 70 20                     mov qword ptr [rax + 0x20], r14
004C2A32  44 8B E6                        mov r12d, esi
004C2A35  48 83 C0 30                     add rax, 0x30
004C2A39  48 BE 00 00 00 00 00 80 FF FF   movabs rsi, 0xffff800000000000
004C2A43  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
004C2A4B  48 83 C3 50                     add rbx, 0x50
004C2A4F  4D 3B E6                        cmp r12, r14
004C2A52  0F 83 7E 02 00 00               jae 0x1404c2cd6
004C2A58  48 8B 13                        mov rdx, qword ptr [rbx]
004C2A5B  45 33 C0                        xor r8d, r8d
004C2A5E  48 8B 4B F0                     mov rcx, qword ptr [rbx - 0x10]
004C2A62  E8 B9 FA F9 FF                  call 0x140462520
004C2A67  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
004C2A6E  8B F8                           mov edi, eax
004C2A70  85 C0                           test eax, eax
004C2A72  0F 88 64 01 00 00               js 0x1404c2bdc
004C2A78  80 3D E9 C1 B0 00 00            cmp byte ptr [rip + 0xb0c1e9], 0
004C2A7F  48 8B 0B                        mov rcx, qword ptr [rbx]
004C2A82  48 8B 7B F8                     mov rdi, qword ptr [rbx - 8]
004C2A86  4C 8B 4B F0                     mov r9, qword ptr [rbx - 0x10]
004C2A8A  0F 84 B2 00 00 00               je 0x1404c2b42
004C2A90  4C 3B CE                        cmp r9, rsi
004C2A93  0F 82 28 01 00 00               jb 0x1404c2bc1
004C2A99  41 F6 C1 07                     test r9b, 7
004C2A9D  0F 85 02 01 00 00               jne 0x1404c2ba5
004C2AA3  48 3B F9                        cmp rdi, rcx
004C2AA6  0F 87 DD 00 00 00               ja 0x1404c2b89
004C2AAC  49 8D 04 09                     lea rax, [r9 + rcx]
004C2AB0  49 3B C1                        cmp rax, r9
004C2AB3  0F 82 B7 00 00 00               jb 0x1404c2b70
004C2AB9  48 8D 41 FF                     lea rax, [rcx - 1]
004C2ABD  48 BE 00 00 00 00 00 80 00 00   movabs rsi, 0x800000000000
004C2AC7  83 E0 07                        and eax, 7
004C2ACA  4C 8D 7F FF                     lea r15, [rdi - 1]
004C2ACE  41 83 E7 07                     and r15d, 7
004C2AD2  49 03 F1                        add rsi, r9
004C2AD5  4C 2B F8                        sub r15, rax
004C2AD8  48 C1 EE 03                     shr rsi, 3
004C2ADC  48 03 35 F5 43 B0 00            add rsi, qword ptr [rip + 0xb043f5]
004C2AE3  4C 2B FF                        sub r15, rdi
004C2AE6  48 8B C7                        mov rax, rdi
004C2AE9  4C 03 F9                        add r15, rcx
004C2AEC  48 C1 E8 03                     shr rax, 3
004C2AF0  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
004C2AF8  48 85 C0                        test rax, rax
004C2AFB  74 15                           je 0x1404c2b12
004C2AFD  4C 8B C0                        mov r8, rax
004C2B00  33 D2                           xor edx, edx
004C2B02  48 8B CE                        mov rcx, rsi
004C2B05  E8 36 41 20 00                  call 0x1406c6c40
004C2B0A  48 03 B4 24 A0 00 00 00         add rsi, qword ptr [rsp + 0xa0]
004C2B12  40 F6 C7 07                     test dil, 7
004C2B16  74 0A                           je 0x1404c2b22
004C2B18  40 80 E7 07                     and dil, 7
004C2B1C  40 88 3E                        mov byte ptr [rsi], dil
004C2B1F  48 FF C6                        inc rsi
004C2B22  49 C1 EF 03                     shr r15, 3
004C2B26  4D 85 FF                        test r15, r15
004C2B29  74 0D                           je 0x1404c2b38
004C2B2B  4D 8B C7                        mov r8, r15
004C2B2E  B2 84                           mov dl, 0x84
004C2B30  48 8B CE                        mov rcx, rsi
004C2B33  E8 08 41 20 00                  call 0x1406c6c40
004C2B38  48 BE 00 00 00 00 00 80 FF FF   movabs rsi, 0xffff800000000000
004C2B42  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
004C2B4A  49 FF C4                        inc r12
004C2B4D  48 8B 43 F0                     mov rax, qword ptr [rbx - 0x10]
004C2B51  48 89 41 F8                     mov qword ptr [rcx - 8], rax
004C2B55  48 8B 03                        mov rax, qword ptr [rbx]
004C2B58  48 89 01                        mov qword ptr [rcx], rax
004C2B5B  48 83 C1 10                     add rcx, 0x10
004C2B5F  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
004C2B67  48 83 C3 40                     add rbx, 0x40
004C2B6B  E9 DF FE FF FF                  jmp 0x1404c2a4f
004C2B70  BA 02 00 00 00                  mov edx, 2
004C2B75  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
004C2B7A  B9 F1 01 00 00                  mov ecx, 0x1f1
004C2B7F  44 8D 42 01                     lea r8d, [rdx + 1]
004C2B83  E8 D8 AA 03 00                  call 0x1404fd660
004C2B88  CC                              int3
004C2B89  BA 02 00 00 00                  mov edx, 2
004C2B8E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
004C2B93  4C 8B CF                        mov r9, rdi
004C2B96  B9 F1 01 00 00                  mov ecx, 0x1f1
004C2B9B  44 8D 42 01                     lea r8d, [rdx + 1]
004C2B9F  E8 BC AA 03 00                  call 0x1404fd660
004C2BA4  CC                              int3
004C2BA5  BA 02 00 00 00                  mov edx, 2
004C2BAA  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
004C2BB3  44 8B C2                        mov r8d, edx
004C2BB6  B9 F1 01 00 00                  mov ecx, 0x1f1
004C2BBB  E8 A0 AA 03 00                  call 0x1404fd660
004C2BC0  CC                              int3
004C2BC1  45 33 F6                        xor r14d, r14d
004C2BC4  B9 F1 01 00 00                  mov ecx, 0x1f1
004C2BC9  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
004C2BCE  41 8D 56 02                     lea edx, [r14 + 2]
004C2BD2  45 8D 46 01                     lea r8d, [r14 + 1]
004C2BD6  E8 85 AA 03 00                  call 0x1404fd660
004C2BDB  CC                              int3
004C2BDC  45 33 F6                        xor r14d, r14d
004C2BDF  41 8B EE                        mov ebp, r14d
004C2BE2  4D 85 E4                        test r12, r12
004C2BE5  0F 84 8C 00 00 00               je 0x1404c2c77
004C2BEB  4C 8B 7C 24 30                  mov r15, qword ptr [rsp + 0x30]
004C2BF0  44 38 35 71 C0 B0 00            cmp byte ptr [rip + 0xb0c071], r14b
004C2BF7  49 8B 5F 10                     mov rbx, qword ptr [r15 + 0x10]
004C2BFB  4D 8B 0F                        mov r9, qword ptr [r15]
004C2BFE  74 64                           je 0x1404c2c64
004C2C00  4C 3B CE                        cmp r9, rsi
004C2C03  0F 82 B4 00 00 00               jb 0x1404c2cbd
004C2C09  41 F6 C1 07                     test r9b, 7
004C2C0D  0F 85 8E 00 00 00               jne 0x1404c2ca1
004C2C13  49 8D 04 19                     lea rax, [r9 + rbx]
004C2C17  49 3B C1                        cmp rax, r9
004C2C1A  72 6C                           jb 0x1404c2c88
004C2C1C  48 BF 00 00 00 00 00 80 00 00   movabs rdi, 0x800000000000
004C2C26  48 8B F3                        mov rsi, rbx
004C2C29  49 03 F9                        add rdi, r9
004C2C2C  48 C1 EE 03                     shr rsi, 3
004C2C30  48 C1 EF 03                     shr rdi, 3
004C2C34  48 03 3D 9D 42 B0 00            add rdi, qword ptr [rip + 0xb0429d]
004C2C3B  48 85 F6                        test rsi, rsi
004C2C3E  74 10                           je 0x1404c2c50
004C2C40  4C 8B C6                        mov r8, rsi
004C2C43  33 D2                           xor edx, edx
004C2C45  48 8B CF                        mov rcx, rdi
004C2C48  E8 F3 3F 20 00                  call 0x1406c6c40
004C2C4D  48 03 FE                        add rdi, rsi
004C2C50  48 BE 00 00 00 00 00 80 FF FF   movabs rsi, 0xffff800000000000
004C2C5A  F6 C3 07                        test bl, 7
004C2C5D  74 05                           je 0x1404c2c64
004C2C5F  80 E3 07                        and bl, 7
004C2C62  88 1F                           mov byte ptr [rdi], bl
004C2C64  48 FF C5                        inc rbp
004C2C67  49 83 C7 40                     add r15, 0x40
004C2C6B  49 3B EC                        cmp rbp, r12
004C2C6E  72 80                           jb 0x1404c2bf0
004C2C70  8B BC 24 A0 00 00 00            mov edi, dword ptr [rsp + 0xa0]
004C2C77  33 D2                           xor edx, edx
004C2C79  49 8B CD                        mov rcx, r13
004C2C7C  E8 EF FB 6B 00                  call 0x140b82870
004C2C81  8B C7                           mov eax, edi
004C2C83  E9 12 01 00 00                  jmp 0x1404c2d9a
004C2C88  BA 02 00 00 00                  mov edx, 2
004C2C8D  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
004C2C92  B9 F1 01 00 00                  mov ecx, 0x1f1
004C2C97  44 8D 42 01                     lea r8d, [rdx + 1]
004C2C9B  E8 C0 A9 03 00                  call 0x1404fd660
004C2CA0  CC                              int3
004C2CA1  BA 02 00 00 00                  mov edx, 2
004C2CA6  48 C7 44 24 20 08 00 00 00      mov qword ptr [rsp + 0x20], 8
004C2CAF  44 8B C2                        mov r8d, edx
004C2CB2  B9 F1 01 00 00                  mov ecx, 0x1f1
004C2CB7  E8 A4 A9 03 00                  call 0x1404fd660
004C2CBC  CC                              int3
004C2CBD  BA 02 00 00 00                  mov edx, 2
004C2CC2  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
004C2CC7  B9 F1 01 00 00                  mov ecx, 0x1f1
004C2CCC  44 8D 42 FF                     lea r8d, [rdx - 1]
004C2CD0  E8 8B A9 03 00                  call 0x1404fd660
004C2CD5  CC                              int3
004C2CD6  48 8D 0D 23 28 AA 00            lea rcx, [rip + 0xaa2823]
004C2CDD  E8 8E 57 D4 FF                  call 0x140208470
004C2CE2  48 8B 15 F7 36 9A 00            mov rdx, qword ptr [rip + 0x9a36f7]
004C2CE9  4C 8D 35 E8 36 9A 00            lea r14, [rip + 0x9a36e8]
004C2CF0  48 8B 0D E1 36 9A 00            mov rcx, qword ptr [rip + 0x9a36e1]
004C2CF7  0F B6 F8                        movzx edi, al
004C2CFA  F6 C2 01                        test dl, 1
004C2CFD  74 08                           je 0x1404c2d07
004C2CFF  48 85 C9                        test rcx, rcx
004C2D02  74 3D                           je 0x1404c2d41
004C2D04  49 33 CE                        xor rcx, r14
004C2D07  0F B6 DA                        movzx ebx, dl
004C2D0A  45 32 C0                        xor r8b, r8b
004C2D0D  83 E3 01                        and ebx, 1
004C2D10  48 8B F1                        mov rsi, rcx
004C2D13  48 85 C9                        test rcx, rcx
004C2D16  74 4C                           je 0x1404c2d64
004C2D18  48 8B D6                        mov rdx, rsi
004C2D1B  48 8B CD                        mov rcx, rbp
004C2D1E  E8 9D 80 0E 00                  call 0x1405aadc0
004C2D23  85 C0                           test eax, eax
004C2D25  78 21                           js 0x1404c2d48
004C2D27  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
004C2D2B  85 DB                           test ebx, ebx
004C2D2D  74 08                           je 0x1404c2d37
004C2D2F  48 85 C0                        test rax, rax
004C2D32  74 08                           je 0x1404c2d3c
004C2D34  48 33 C6                        xor rax, rsi
004C2D37  48 85 C0                        test rax, rax
004C2D3A  75 20                           jne 0x1404c2d5c
004C2D3C  41 B0 01                        mov r8b, 1
004C2D3F  EB 23                           jmp 0x1404c2d64
004C2D41  45 32 C0                        xor r8b, r8b
004C2D44  33 F6                           xor esi, esi
004C2D46  EB 1C                           jmp 0x1404c2d64
004C2D48  48 8B 06                        mov rax, qword ptr [rsi]
004C2D4B  85 DB                           test ebx, ebx
004C2D4D  74 08                           je 0x1404c2d57
004C2D4F  48 85 C0                        test rax, rax
004C2D52  74 0D                           je 0x1404c2d61
004C2D54  48 33 C6                        xor rax, rsi
004C2D57  48 85 C0                        test rax, rax
004C2D5A  74 05                           je 0x1404c2d61
004C2D5C  48 8B F0                        mov rsi, rax
004C2D5F  EB B7                           jmp 0x1404c2d18
004C2D61  45 32 C0                        xor r8b, r8b
004C2D64  4D 8B CD                        mov r9, r13
004C2D67  48 8B D6                        mov rdx, rsi
004C2D6A  49 8B CE                        mov rcx, r14
004C2D6D  E8 FE 17 E2 FF                  call 0x1402e4570
004C2D72  80 3D F2 BE B0 00 00            cmp byte ptr [rip + 0xb0bef2], 0
004C2D79  74 0D                           je 0x1404c2d88
004C2D7B  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
004C2D83  E8 B8 8F 0E 00                  call 0x1405abd40
004C2D88  40 0F B6 D7                     movzx edx, dil
004C2D8C  48 8D 0D 6D 27 AA 00            lea rcx, [rip + 0xaa276d]
004C2D93  E8 08 FE EC FF                  call 0x140392ba0
004C2D98  33 C0                           xor eax, eax
004C2D9A  48 83 C4 48                     add rsp, 0x48
004C2D9E  41 5F                           pop r15
004C2DA0  41 5E                           pop r14
004C2DA2  41 5D                           pop r13
004C2DA4  41 5C                           pop r12
004C2DA6  5F                              pop rdi
004C2DA7  5E                              pop rsi
004C2DA8  5D                              pop rbp
004C2DA9  5B                              pop rbx
004C2DAA  C3                              ret
004C2DAB  CC                              int3
004C2DAC  B8 01 00 00 C0                  mov eax, 0xc0000001
004C2DB1  EB E7                           jmp 0x1404c2d9a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KasanDriverLoadImageInternal(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (72);
    v_r15 = ((unsigned int)(*(unsigned int *)(a1 + 152))) + (*(unsigned __int64 *)(a1 + 48));
    if ((*(unsigned __int64 *)(a1 + 48) - 1) > -3) goto loc_004C2D98;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 48))) != ((unsigned __int16)((unsigned int)(0x5A4DULL)))) goto loc_004C2D98;
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 60))) + (*(unsigned __int64 *)(a1 + 48));
    if (a2 < (*(unsigned __int64 *)(a1 + 48))) goto loc_004C2D98;
    if ((*(unsigned __int64 *)(a1 + 48)) > a1) goto loc_004C28BE;
    if ((a2 + 263) < a2) goto loc_004C2D98;
    if ((a2 + 263) > a1) goto loc_004C2D98;
loc_004C28BE:
    if ((*(unsigned int *)(a2)) != 0x4550ULL) goto loc_004C2D98;
    if (a2 == 0) goto loc_004C2D98;
    v_rdi = (*(unsigned __int16 *)(a2 + 20)) + (24);
    v_rdi = (v_rdi) + (a2);
    v_r13 = 0;
loc_004C28F0:
    if (0 >= ((unsigned __int16)(*(unsigned __int16 *)(a2 + 6)))) goto loc_004C2D98;
    result = strncmp(v_rdi, v_rip + 2132874, 8, a4);
    if ((unsigned int)(result) == 0) goto loc_004C291B;
    v_rdi = (v_rdi) + (40);
    v_rbx = (unsigned __int16)((0) + 1);
    goto loc_004C28F0;
loc_004C291B:
    if (v_rdi == 0) goto loc_004C2D98;
    v_rbx = ((unsigned int)(*(unsigned int *)(v_rdi + 12))) + (*(unsigned __int64 *)(a1 + 48));
    if (condition_is_equal) goto loc_004C2D98;
    if ((*(unsigned __int8 *)(v_rip + 11584301)) == 0) goto loc_004C2DAC;
    if (((unsigned int)(*(unsigned int *)(v_rdi + 8))) < 64) goto loc_004C2DAC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) & (63)) != 0) goto loc_004C2DAC;
    if ((*(unsigned int *)(v_rbx)) != 2) goto loc_004C2DAC;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8)) = *(unsigned __int64 *)(v_rip + 11544943);
    if (v_stack_p10 != 0) goto loc_004C2D98;
    v_r14 = ((unsigned int)(*(unsigned int *)(v_rdi + 8))) + (-64);
    v_stack_m58 = v_rbx + 64;
    v_r14 = (v_r14) >> (6);
loc_004C2992:
    if (0 >= v_r14) goto loc_004C29E8;
    if (*(unsigned __int64 *)(v_rbx + 72 + 8) == 0) goto loc_004C2DAC;
    if ((*(unsigned __int64 *)(v_rbx + 72)) > (*(unsigned __int64 *)(v_rbx + 72 + 8))) goto loc_004C2DAC;
    if ((*(unsigned __int64 *)(v_rbx + 72 - 8)) < (*(unsigned __int64 *)(a1 + 48))) goto loc_004C2DAC;
    if ((*(unsigned __int64 *)(v_rbx + 72 - 8)) >= v_r15) goto loc_004C2DAC;
    if ((*(unsigned __int64 *)(v_rbx + 72 - 8) + *(unsigned __int64 *)(v_rbx + 72 + 8) * 1) < (*(unsigned __int64 *)(v_rbx + 72 - 8))) goto loc_004C29DE;
    if ((*(unsigned __int64 *)(v_rbx + 72 - 8) + *(unsigned __int64 *)(v_rbx + 72 + 8) * 1) > v_r15) goto loc_004C2DAC;
    a3 = (0) + 1;
    result = (v_rbx + 72) + (64);
    goto loc_004C2992;
loc_004C29DE:
    goto loc_004C2D9A;
loc_004C29E8:
    v_stack_p18 = 0;
    if (*(unsigned __int64 *)(v_rbx + 72 + 8) != 0) goto loc_004C29DE;
    if ((16 + 40) < 16) goto loc_004C29DE;
    result = ExAllocatePool2(64, 16 + 40, (unsigned int)(0x6E55614BULL), *(unsigned __int64 *)(v_rbx + 72 - 8) + *(unsigned __int64 *)(v_rbx + 72 + 8) * 1);
    if (result != 0) goto loc_004C2A28;
    goto loc_004C2D9A;
loc_004C2A28:
    v_rsi = 0;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 24) = a1;
    *(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 32) = v_r14;
    result = ((unsigned int)(0xC000009AULL)) + (48);
    v_stack_p20 = result;
    v_rbx = (v_rbx) + (80);
loc_004C2A4F:
    if (0 >= v_r14) goto loc_004C2CD6;
    a3 = 0;
    result = KasanTrackAddress(*(unsigned __int64 *)(v_rbx - 16), *(unsigned __int64 *)(v_rbx), a3, *(unsigned __int64 *)(v_rbx + 72 - 8) + *(unsigned __int64 *)(v_rbx + 72 + 8) * 1);
    v_stack_p18 = (unsigned int)(result);
    if (sign_flag) goto loc_004C2BDC;
    if ((*(unsigned __int8 *)(v_rip + 11583977)) == 0) goto loc_004C2B42;
    if ((*(unsigned __int64 *)(v_rbx - 16)) < 0) goto loc_004C2BC1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx - 16))) & (7)) != 0) goto loc_004C2BA5;
    if ((*(unsigned __int64 *)(v_rbx - 8)) > (*(unsigned __int64 *)(v_rbx))) goto loc_004C2B89;
    if ((*(unsigned __int64 *)(v_rbx - 16) + *(unsigned __int64 *)(v_rbx) * 1) < (*(unsigned __int64 *)(v_rbx - 16))) goto loc_004C2B70;
    result = (unsigned int)((*(unsigned __int64 *)(v_rbx) - 1) & (7));
    v_r15 = (unsigned int)((*(unsigned __int64 *)(v_rbx - 8) - 1) & (7));
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rbx - 16));
    v_r15 = (v_r15) - (result);
    v_rsi = (v_rsi) >> (3);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_rip + 11551733));
    v_r15 = (v_r15) - (*(unsigned __int64 *)(v_rbx - 8));
    v_r15 = (v_r15) + (*(unsigned __int64 *)(v_rbx));
    result = (*(unsigned __int64 *)(v_rbx - 8)) >> (3);
    v_stack_p18 = result;
    if (result != 0) {
        a3 = result;
        a2 = 0;
        a1 = v_rsi;
        result = memset(a1, a2, a3, *(unsigned __int64 *)(v_rbx - 16));
        v_rsi = (v_rsi) + (v_stack_p18);
    }
    v_rdi = *(unsigned __int64 *)(v_rbx - 8);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx - 8))) & (7)) != 0) {
        v_rdi = (unsigned __int8)((*(unsigned __int64 *)(v_rbx - 8)) & (7));
        *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(v_rdi);
        v_rsi = (v_rsi) + 1;
    }
    v_r15 = (v_r15) >> (3);
    if (v_r15 != 0) {
        a3 = v_r15;
        a2 = 132;
        a1 = v_rsi;
        result = memset(a1, a2, a3, *(unsigned __int64 *)(v_rbx - 16));
    }
loc_004C2B42:
    v_r12 = (0) + 1;
    *(unsigned __int64 *)(v_stack_p20 - 8) = *(unsigned __int64 *)(v_rbx - 16);
    *(unsigned __int64 *)(v_stack_p20) = *(unsigned __int64 *)(v_rbx);
    a1 = (v_stack_p20) + (16);
    v_stack_p20 = a1;
    v_rbx = (v_rbx) + (64);
    goto loc_004C2A4F;
loc_004C2B70:
    v_stack_m68 = a1;
    result = KeBugCheckEx(497, 2, 2 + 1, *(unsigned __int64 *)(v_rbx - 16));
loc_004C2B89:
    v_stack_m68 = 497;
    result = KeBugCheckEx(497, 2, 2 + 1, v_rdi);
loc_004C2BA5:
    v_stack_m68 = 8;
    result = KeBugCheckEx(497, 2, 2, v_rdi);
loc_004C2BC1:
    v_r14 = 0;
    v_stack_m68 = 0;
    result = KeBugCheckEx(497, v_r14 + 2, v_r14 + 1, v_rdi);
loc_004C2BDC:
    v_r14 = 0;
    if (v_r12 == 0) goto loc_004C2C77;
loc_004C2BF0:
    if ((*(unsigned __int8 *)(v_rip + 11583601)) == 0) goto loc_004C2C64;
    if ((*(unsigned __int64 *)(v_stack_m58)) < v_rsi) goto loc_004C2CBD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m58))) & (7)) != 0) goto loc_004C2CA1;
    if ((*(unsigned __int64 *)(v_stack_m58) + *(unsigned __int64 *)(v_stack_m58 + 16) * 1) < (*(unsigned __int64 *)(v_stack_m58))) goto loc_004C2C88;
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_stack_m58));
    v_rsi = (*(unsigned __int64 *)(v_stack_m58 + 16)) >> (3);
    v_rdi = (v_rdi) >> (3);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_rip + 11551389));
    result = *(unsigned __int64 *)(v_stack_m58) + *(unsigned __int64 *)(v_stack_m58 + 16) * 1;
    if (v_rsi != 0) {
        a3 = v_rsi;
        a2 = 0;
        a1 = v_rdi;
        result = memset(a1, a2, a3, *(unsigned __int64 *)(v_stack_m58));
        v_rdi = (v_rdi) + (v_rsi);
    }
    v_rbx = *(unsigned __int64 *)(v_stack_m58 + 16);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m58 + 16))) & (7)) != 0) {
        v_rbx = (unsigned __int8)((*(unsigned __int64 *)(v_stack_m58 + 16)) & (7));
        *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(v_rbx);
    }
    v_rbp = (0) + 1;
    v_r15 = (v_stack_m58) + (64);
    if (v_rbp < v_r12) goto loc_004C2BF0;
loc_004C2C77:
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, a3, *(unsigned __int64 *)(v_stack_m58));
    goto loc_004C2D9A;
loc_004C2C88:
    v_stack_m68 = v_rbx;
    result = KeBugCheckEx(497, 2, 2 + 1, *(unsigned __int64 *)(v_stack_m58));
loc_004C2CA1:
    v_stack_m68 = 8;
    result = KeBugCheckEx(497, 2, 2, *(unsigned __int64 *)(v_stack_m58));
loc_004C2CBD:
    v_stack_m68 = 0;
    result = KeBugCheckEx(497, 2, 2 - 1, *(unsigned __int64 *)(v_stack_m58));
loc_004C2CD6:
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11151395, 2, 2 - 1, *(unsigned __int64 *)(v_stack_m58));
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10106615))) & (1)) == 0) goto loc_004C2D07;
    if (*(unsigned __int64 *)(v_rip + 10106593) == 0) goto loc_004C2D41;
    a1 = (*(unsigned __int64 *)(v_rip + 10106593)) ^ (v_rip + 10106600);
loc_004C2D07:
    a3 = 0;
    v_rbx = (unsigned int)(((unsigned __int8)(*(unsigned __int64 *)(v_rip + 10106615))) & (1));
    if (a1 == 0) goto loc_004C2D64;
loc_004C2D18:
    result = KasanUnloadInfoCompare(v_rbp, a1, a3, *(unsigned __int64 *)(v_stack_m58));
    if (sign_flag) goto loc_004C2D48;
    if ((unsigned int)(v_rbx) == 0) goto loc_004C2D37;
    if (*(unsigned __int64 *)(a1 + 8) == 0) goto loc_004C2D3C;
    result = (*(unsigned __int64 *)(a1 + 8)) ^ (a1);
loc_004C2D37:
    if (result != 0) goto loc_004C2D5C;
loc_004C2D3C:
    goto loc_004C2D64;
loc_004C2D41:
    a3 = 0;
    v_rsi = 0;
    goto loc_004C2D64;
loc_004C2D48:
    if ((unsigned int)(v_rbx) == 0) goto loc_004C2D57;
    if (*(unsigned __int64 *)(v_rsi) == 0) goto loc_004C2D61;
    result = (*(unsigned __int64 *)(v_rsi)) ^ (0);
loc_004C2D57:
    if (result == 0) goto loc_004C2D61;
loc_004C2D5C:
    goto loc_004C2D18;
loc_004C2D61:
    a3 = 0;
loc_004C2D64:
    result = RtlRbInsertNodeEx(v_rip + 10106600, result, a3, result);
    if ((*(unsigned __int8 *)(v_rip + 11583218)) != 0) {
        a1 = v_stack_p8;
        result = KasaniSendTelemetryDriver(a1, result, a3, result);
    }
    result = KeReleaseSpinLock(v_rip + 11151213, (unsigned __int8)((unsigned __int8)(result)), a3, result);
loc_004C2D98:
    result = 0;
loc_004C2D9A:
    v_rsp = (v_rsp) + (72);
    return result;
loc_004C2DAC:
    goto loc_004C2D9A;
}
```

## 5. (Beta) C Style

```c
int64_t KasanDriverLoadImageInternal(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (72);
    local_r15 = ((uint32_t)(*(uint32_t *)(arg1 + 0x98))) + (*(uint64_t *)(arg1 + 0x30));
    if ((*(uint64_t *)(arg1 + 0x30) - 1) > -3) goto loc_004C2D98;
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x30))) != ((uint16_t)((uint32_t)(0x5A4DULL)))) goto loc_004C2D98;
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0x3C))) + (*(uint64_t *)(arg1 + 0x30));
    if (Arg2 < (*(uint64_t *)(arg1 + 0x30))) goto loc_004C2D98;
    if ((*(uint64_t *)(arg1 + 0x30)) > Arg1) goto loc_004C28BE;
    if ((Arg2 + 263) < Arg2) goto loc_004C2D98;
    if ((Arg2 + 263) > Arg1) goto loc_004C2D98;
loc_004C28BE:
    if ((*(uint32_t *)(Arg2)) != 0x4550ULL) goto loc_004C2D98;
    if (Arg2 == 0) goto loc_004C2D98;
    local_rdi = (*(uint16_t *)(Arg2 + 0x14)) + (24);
    local_rdi = (local_rdi) + (Arg2);
    local_r13 = 0;
loc_004C28F0:
    if (0 >= ((uint16_t)(*(uint16_t *)(Arg2 + 0x6)))) goto loc_004C2D98;
    result = strncmp(local_rdi, v_rip + 2132874, 8, a4);
    if ((uint32_t)(result) == 0) goto loc_004C291B;
    local_rdi = (local_rdi) + (40);
    local_rbx = (uint16_t)((0) + 1);
    goto loc_004C28F0;
loc_004C291B:
    if (local_rdi == 0) goto loc_004C2D98;
    local_rbx = ((uint32_t)(*(uint32_t *)(local_rdi + 0xC))) + (*(uint64_t *)(arg1 + 0x30));
    if (condition_is_equal) goto loc_004C2D98;
    if ((*(uint8_t *)(v_rip + 0xB0C32D)) == 0) goto loc_004C2DAC;
    if (((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) < 64) goto loc_004C2DAC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) & (63)) != 0) goto loc_004C2DAC;
    if ((*(uint32_t *)(local_rbx)) != 2) goto loc_004C2DAC;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8)) = *(uint64_t *)(v_rip + 0xB0296F);
    if (v_stack_p10 != 0) goto loc_004C2D98;
    local_r14 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) + (-64);
    v_stack_m58 = local_rbx + 64;
    local_r14 = (local_r14) >> (6);
loc_004C2992:
    if (0 >= local_r14) goto loc_004C29E8;
    if (*(uint64_t *)(local_rbx + 0x48 + 0x8) == 0) goto loc_004C2DAC;
    if ((*(uint64_t *)(local_rbx + 0x48)) > (*(uint64_t *)(local_rbx + 0x48 + 0x8))) goto loc_004C2DAC;
    if ((*(uint64_t *)(local_rbx + 0x48 - 0x8)) < (*(uint64_t *)(arg1 + 0x30))) goto loc_004C2DAC;
    if ((*(uint64_t *)(local_rbx + 0x48 - 0x8)) >= local_r15) goto loc_004C2DAC;
    if ((*(uint64_t *)(local_rbx + 0x48 - 0x8) + *(uint64_t *)(local_rbx + 0x48 + 0x8) * 1) < (*(uint64_t *)(local_rbx + 0x48 - 0x8))) goto loc_004C29DE;
    if ((*(uint64_t *)(local_rbx + 0x48 - 0x8) + *(uint64_t *)(local_rbx + 0x48 + 0x8) * 1) > local_r15) goto loc_004C2DAC;
    a3 = (0) + 1;
    result = (local_rbx + 72) + (64);
    goto loc_004C2992;
loc_004C29DE:
    goto loc_004C2D9A;
loc_004C29E8:
    v_stack_p18 = 0;
    if (*(uint64_t *)(local_rbx + 0x48 + 0x8) != 0) goto loc_004C29DE;
    if ((16 + 40) < 16) goto loc_004C29DE;
    result = ExAllocatePool2(64, 16 + 40, (uint32_t)(0x6E55614BULL), *(uint64_t *)(local_rbx + 0x48 - 0x8) + *(uint64_t *)(local_rbx + 0x48 + 0x8) * 1);
    if (result != 0) goto loc_004C2A28;
    goto loc_004C2D9A;
loc_004C2A28:
    local_rsi = 0;
    *(void **)((uint32_t)(0xC000009AULL) + 0x18) = Arg1;
    *(uint64_t *)((uint32_t)(0xC000009AULL) + 0x20) = local_r14;
    result = ((uint32_t)(0xC000009AULL)) + (48);
    v_stack_p20 = result;
    local_rbx = (local_rbx) + (80);
loc_004C2A4F:
    if (0 >= local_r14) goto loc_004C2CD6;
    a3 = 0;
    result = KasanTrackAddress(*(uint64_t *)(local_rbx - 0x10), *(uint64_t *)(local_rbx), a3, *(uint64_t *)(local_rbx + 0x48 - 0x8) + *(uint64_t *)(local_rbx + 0x48 + 0x8) * 1);
    v_stack_p18 = (uint32_t)(result);
    if (sign_flag) goto loc_004C2BDC;
    if ((*(uint8_t *)(v_rip + 0xB0C1E9)) == 0) goto loc_004C2B42;
    if ((*(uint64_t *)(local_rbx - 0x10)) < 0) goto loc_004C2BC1;
    if ((((uint8_t)(*(uint64_t *)(local_rbx - 0x10))) & (7)) != 0) goto loc_004C2BA5;
    if ((*(uint64_t *)(local_rbx - 0x8)) > (*(uint64_t *)(local_rbx))) goto loc_004C2B89;
    if ((*(uint64_t *)(local_rbx - 0x10) + *(uint64_t *)(local_rbx) * 1) < (*(uint64_t *)(local_rbx - 0x10))) goto loc_004C2B70;
    result = (uint32_t)((*(uint64_t *)(local_rbx) - 1) & (7));
    local_r15 = (uint32_t)((*(uint64_t *)(local_rbx - 0x8) - 1) & (7));
    local_rsi = (local_rsi) + (*(uint64_t *)(local_rbx - 0x10));
    local_r15 = (local_r15) - (result);
    local_rsi = (local_rsi) >> (3);
    local_rsi = (local_rsi) + (*(uint64_t *)(v_rip + 0xB043F5));
    local_r15 = (local_r15) - (*(uint64_t *)(local_rbx - 0x8));
    local_r15 = (local_r15) + (*(uint64_t *)(local_rbx));
    result = (*(uint64_t *)(local_rbx - 0x8)) >> (3);
    v_stack_p18 = result;
    if (result != 0) {
        a3 = result;
        Arg2 = 0;
        Arg1 = local_rsi;
        result = memset(Arg1, Arg2, a3, *(uint64_t *)(local_rbx - 0x10));
        local_rsi = (local_rsi) + (v_stack_p18);
    }
    local_rdi = *(uint64_t *)(local_rbx - 0x8);
    if ((((uint8_t)(*(uint64_t *)(local_rbx - 0x8))) & (7)) != 0) {
        local_rdi = (uint8_t)((*(uint64_t *)(local_rbx - 0x8)) & (7));
        *(uint8_t *)(local_rsi) = (uint8_t)(local_rdi);
        local_rsi = (local_rsi) + 1;
    }
    local_r15 = (local_r15) >> (3);
    if (local_r15 != 0) {
        a3 = local_r15;
        Arg2 = 132;
        Arg1 = local_rsi;
        result = memset(Arg1, Arg2, a3, *(uint64_t *)(local_rbx - 0x10));
    }
loc_004C2B42:
    local_r12 = (0) + 1;
    *(uint64_t *)(v_stack_p20 - 0x8) = *(uint64_t *)(local_rbx - 0x10);
    *(uint64_t *)(v_stack_p20) = *(uint64_t *)(local_rbx);
    Arg1 = (v_stack_p20) + (16);
    v_stack_p20 = Arg1;
    local_rbx = (local_rbx) + (64);
    goto loc_004C2A4F;
loc_004C2B70:
    v_stack_m68 = Arg1;
    result = KeBugCheckEx(497, 2, 2 + 1, *(uint64_t *)(local_rbx - 0x10));
loc_004C2B89:
    v_stack_m68 = 497;
    result = KeBugCheckEx(497, 2, 2 + 1, local_rdi);
loc_004C2BA5:
    v_stack_m68 = 8;
    result = KeBugCheckEx(497, 2, 2, local_rdi);
loc_004C2BC1:
    local_r14 = 0;
    v_stack_m68 = 0;
    result = KeBugCheckEx(497, local_r14 + 2, local_r14 + 1, local_rdi);
loc_004C2BDC:
    local_r14 = 0;
    if (local_r12 == 0) goto loc_004C2C77;
loc_004C2BF0:
    if ((*(uint8_t *)(v_rip + 0xB0C071)) == 0) goto loc_004C2C64;
    if ((*(uint64_t *)(v_stack_m58)) < local_rsi) goto loc_004C2CBD;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m58))) & (7)) != 0) goto loc_004C2CA1;
    if ((*(uint64_t *)(v_stack_m58) + *(uint64_t *)(v_stack_m58 + 0x10) * 1) < (*(uint64_t *)(v_stack_m58))) goto loc_004C2C88;
    local_rdi = (local_rdi) + (*(uint64_t *)(v_stack_m58));
    local_rsi = (*(uint64_t *)(v_stack_m58 + 0x10)) >> (3);
    local_rdi = (local_rdi) >> (3);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_rip + 0xB0429D));
    result = *(uint64_t *)(v_stack_m58) + *(uint64_t *)(v_stack_m58 + 0x10) * 1;
    if (local_rsi != 0) {
        a3 = local_rsi;
        Arg2 = 0;
        Arg1 = local_rdi;
        result = memset(Arg1, Arg2, a3, *(uint64_t *)(v_stack_m58));
        local_rdi = (local_rdi) + (local_rsi);
    }
    local_rbx = *(uint64_t *)(v_stack_m58 + 0x10);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m58 + 0x10))) & (7)) != 0) {
        local_rbx = (uint8_t)((*(uint64_t *)(v_stack_m58 + 0x10)) & (7));
        *(uint8_t *)(local_rdi) = (uint8_t)(local_rbx);
    }
    local_rbp = (0) + 1;
    local_r15 = (v_stack_m58) + (64);
    if (local_rbp < local_r12) goto loc_004C2BF0;
loc_004C2C77:
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, a3, *(uint64_t *)(v_stack_m58));
    goto loc_004C2D9A;
loc_004C2C88:
    v_stack_m68 = local_rbx;
    result = KeBugCheckEx(497, 2, 2 + 1, *(uint64_t *)(v_stack_m58));
loc_004C2CA1:
    v_stack_m68 = 8;
    result = KeBugCheckEx(497, 2, 2, *(uint64_t *)(v_stack_m58));
loc_004C2CBD:
    v_stack_m68 = 0;
    result = KeBugCheckEx(497, 2, 2 - 1, *(uint64_t *)(v_stack_m58));
loc_004C2CD6:
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11151395, 2, 2 - 1, *(uint64_t *)(v_stack_m58));
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x9A36F7))) & (1)) == 0) goto loc_004C2D07;
    if (*(uint64_t *)(v_rip + 0x9A36E1) == 0) goto loc_004C2D41;
    Arg1 = (*(uint64_t *)(v_rip + 0x9A36E1)) ^ (v_rip + 10106600);
loc_004C2D07:
    a3 = 0;
    local_rbx = (uint32_t)(((uint8_t)(*(uint64_t *)(v_rip + 0x9A36F7))) & (1));
    if (Arg1 == NULL) goto loc_004C2D64;
loc_004C2D18:
    result = KasanUnloadInfoCompare(local_rbp, Arg1, a3, *(uint64_t *)(v_stack_m58));
    if (sign_flag) goto loc_004C2D48;
    if ((uint32_t)(local_rbx) == 0) goto loc_004C2D37;
    if (*(uint64_t *)(arg1 + 0x8) == 0) goto loc_004C2D3C;
    result = (*(uint64_t *)(arg1 + 0x8)) ^ (Arg1);
loc_004C2D37:
    if (result != 0) goto loc_004C2D5C;
loc_004C2D3C:
    goto loc_004C2D64;
loc_004C2D41:
    a3 = 0;
    local_rsi = 0;
    goto loc_004C2D64;
loc_004C2D48:
    if ((uint32_t)(local_rbx) == 0) goto loc_004C2D57;
    if (*(uint64_t *)(local_rsi) == 0) goto loc_004C2D61;
    result = (*(uint64_t *)(local_rsi)) ^ (0);
loc_004C2D57:
    if (result == 0) goto loc_004C2D61;
loc_004C2D5C:
    goto loc_004C2D18;
loc_004C2D61:
    a3 = 0;
loc_004C2D64:
    result = RtlRbInsertNodeEx(v_rip + 10106600, result, a3, result);
    if ((*(uint8_t *)(v_rip + 0xB0BEF2)) != 0) {
        Arg1 = v_stack_p8;
        result = KasaniSendTelemetryDriver(Arg1, result, a3, result);
    }
    result = KeReleaseSpinLock(v_rip + 11151213, (uint8_t)((uint8_t)(result)), a3, result);
loc_004C2D98:
    result = 0;
loc_004C2D9A:
    local_rsp = (local_rsp) + (72);
    return result;
loc_004C2DAC:
    goto loc_004C2D9A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x98` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C2840&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
