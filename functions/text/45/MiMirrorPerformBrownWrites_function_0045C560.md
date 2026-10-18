# MiMirrorPerformBrownWrites

- RVA: `0x0045C560`–`0x0045CEAB` (길이 `2,379` bytes)
- VA: `0x000000014045C560`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9550`
- 디코드: `611`개 명령, `2,379/2,379` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **19**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x0045C7AE` → [PopMirrorPhysicalMemory](../../pagelk/B7/PopMirrorPhysicalMemory_function_00B77D10.md) (function, `0x00B77D10`)
- `0x0045C961` → [MiUnlinkPageFromListEx](../28/MiUnlinkPageFromListEx_function_00287590.md) (function, `0x00287590`)
- `0x0045C973` → [MiDiscardTransitionPteEx](../37/MiDiscardTransitionPteEx_function_00375954.md) (function, `0x00375954`)
- `0x0045C9A6` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0045CA66` → [MiRemoveLockedPageChargeAndDecRef](../24/MiRemoveLockedPageChargeAndDecRef_function_002459D0.md) (function, `0x002459D0`)
- `0x0045CA9C` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0045CAE0` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0045CBC0` → [KiLowerIrqlProcessIrqlFlags](../4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x0045CC8F` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0045CC9C` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0045CCA9` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0045CCE8` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x0045CD40` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0045CD52` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0045CD6D` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x0045CD7F` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x0045CDA2` → [MiAddLockedPageCharge](../28/MiAddLockedPageCharge_function_0028B550.md) (function, `0x0028B550`)
- `0x0045CDB8` → [MiPfnReferenceCountIsZero](../2B/MiPfnReferenceCountIsZero_function_002B9E40.md) (function, `0x002B9E40`)
- `0x0045CEA1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [MiMirrorBrownPhase](../../pagelk/B7/MiMirrorBrownPhase_function_00B7C6B4.md) at `0x00B7C793`

### Static image references
- `0x0045C5A6` → RVA `0x00E30190` (`.data`; read)
- `0x0045C5AD` → RVA `0x00E30198` (`.data`; read)
- `0x0045C784` → RVA `0x00B77D10` (`PopMirrorPhysicalMemory`; read)
- `0x0045C850` → RVA `0x00E301A8` (`.data`; read)
- `0x0045C8F9` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0045C93D` → RVA `0x00E30088` (`.data`; read)
- `0x0045C9E3` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0045CD32` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0045C7AE` → [PopMirrorPhysicalMemory](../../pagelk/B7/PopMirrorPhysicalMemory_function_00B77D10.md) (`.text` → `PAGELK`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0045C560  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0045C565  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0045C569  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0045C56E  53                              push rbx
0045C56F  55                              push rbp
0045C570  56                              push rsi
0045C571  57                              push rdi
0045C572  41 54                           push r12
0045C574  41 55                           push r13
0045C576  41 56                           push r14
0045C578  41 57                           push r15
0045C57A  48 83 EC 68                     sub rsp, 0x68
0045C57E  45 33 DB                        xor r11d, r11d
0045C581  44 8B EA                        mov r13d, edx
0045C584  41 8B EB                        mov ebp, r11d
0045C587  44 89 9C 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r11d
0045C58F  41 8B F3                        mov esi, r11d
0045C592  44 89 5C 24 28                  mov dword ptr [rsp + 0x28], r11d
0045C597  45 8B FB                        mov r15d, r11d
0045C59A  4C 89 5C 24 40                  mov qword ptr [rsp + 0x40], r11
0045C59F  45 8B F3                        mov r14d, r11d
0045C5A2  49 83 CC FF                     or r12, 0xffffffffffffffff
0045C5A6  4C 8B 15 E3 3B 9D 00            mov r10, qword ptr [rip + 0x9d3be3]
0045C5AD  48 8B 3D E4 3B 9D 00            mov rdi, qword ptr [rip + 0x9d3be4]
0045C5B4  49 3B F2                        cmp rsi, r10
0045C5B7  4D 1B C9                        sbb r9, r9
0045C5BA  4C 23 CE                        and r9, rsi
0045C5BD  4D 8D 42 FF                     lea r8, [r10 - 1]
0045C5C1  49 8B C0                        mov rax, r8
0045C5C4  44 89 5C 24 48                  mov dword ptr [rsp + 0x48], r11d
0045C5C9  49 2B C1                        sub rax, r9
0045C5CC  48 FF C0                        inc rax
0045C5CF  48 83 F8 01                     cmp rax, 1
0045C5D3  0F 82 B6 08 00 00               jb 0x14045ce8f
0045C5D9  49 8B C0                        mov rax, r8
0045C5DC  41 8A C9                        mov cl, r9b
0045C5DF  48 C1 E8 06                     shr rax, 6
0045C5E3  80 E1 3F                        and cl, 0x3f
0045C5E6  BA 01 00 00 00                  mov edx, 1
0045C5EB  48 D3 E2                        shl rdx, cl
0045C5EE  48 FF CA                        dec rdx
0045C5F1  4C 8D 1C C7                     lea r11, [rdi + rax*8]
0045C5F5  49 8B C1                        mov rax, r9
0045C5F8  48 C1 E8 06                     shr rax, 6
0045C5FC  48 8D 1C C7                     lea rbx, [rdi + rax*8]
0045C600  48 8B 03                        mov rax, qword ptr [rbx]
0045C603  48 F7 D0                        not rax
0045C606  48 0B D0                        or rdx, rax
0045C609  49 3B D4                        cmp rdx, r12
0045C60C  75 2B                           jne 0x14045c639
0045C60E  48 83 C3 08                     add rbx, 8
0045C612  49 3B DB                        cmp rbx, r11
0045C615  0F 86 06 02 00 00               jbe 0x14045c821
0045C61B  49 8B DC                        mov rbx, r12
0045C61E  45 33 DB                        xor r11d, r11d
0045C621  4D 85 C9                        test r9, r9
0045C624  74 39                           je 0x14045c65f
0045C626  4C 8D 46 01                     lea r8, [rsi + 1]
0045C62A  4D 8B CB                        mov r9, r11
0045C62D  4D 3B C2                        cmp r8, r10
0045C630  4D 0F 47 C2                     cmova r8, r10
0045C634  49 FF C8                        dec r8
0045C637  EB 88                           jmp 0x14045c5c1
0045C639  48 2B DF                        sub rbx, rdi
0045C63C  48 F7 D2                        not rdx
0045C63F  48 0F BC C2                     bsf rax, rdx
0045C643  48 C1 FB 03                     sar rbx, 3
0045C647  48 C1 E3 06                     shl rbx, 6
0045C64B  48 03 D8                        add rbx, rax
0045C64E  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0045C652  49 3B D8                        cmp rbx, r8
0045C655  77 C4                           ja 0x14045c61b
0045C657  49 3B DC                        cmp rbx, r12
0045C65A  74 C2                           je 0x14045c61e
0045C65C  45 33 DB                        xor r11d, r11d
0045C65F  48 3B DE                        cmp rbx, rsi
0045C662  0F 82 95 01 00 00               jb 0x14045c7fd
0045C668  49 3B DC                        cmp rbx, r12
0045C66B  0F 84 8C 01 00 00               je 0x14045c7fd
0045C671  48 8B 05 18 3B 9D 00            mov rax, qword ptr [rip + 0x9d3b18]
0045C678  4D 8B E3                        mov r12, r11
0045C67B  44 89 5C 24 2C                  mov dword ptr [rsp + 0x2c], r11d
0045C680  4C 89 5C 24 20                  mov qword ptr [rsp + 0x20], r11
0045C685  48 3B C3                        cmp rax, rbx
0045C688  0F 86 4B 03 00 00               jbe 0x14045c9d9
0045C68E  4C 8B 15 03 3B 9D 00            mov r10, qword ptr [rip + 0x9d3b03]
0045C695  48 FF C8                        dec rax
0045C698  48 C1 E8 06                     shr rax, 6
0045C69C  BE 01 00 00 00                  mov esi, 1
0045C6A1  8A CB                           mov cl, bl
0045C6A3  80 E1 3F                        and cl, 0x3f
0045C6A6  4D 8D 0C C2                     lea r9, [r10 + rax*8]
0045C6AA  48 8B C3                        mov rax, rbx
0045C6AD  48 C1 E8 06                     shr rax, 6
0045C6B1  49 8D 14 C2                     lea rdx, [r10 + rax*8]
0045C6B5  8B C6                           mov eax, esi
0045C6B7  4C 8B 02                        mov r8, qword ptr [rdx]
0045C6BA  48 D3 E0                        shl rax, cl
0045C6BD  48 2B C6                        sub rax, rsi
0045C6C0  4C 0B C0                        or r8, rax
0045C6C3  48 8D 42 08                     lea rax, [rdx + 8]
0045C6C7  49 F7 D0                        not r8
0045C6CA  4D 85 C0                        test r8, r8
0045C6CD  0F 84 59 01 00 00               je 0x14045c82c
0045C6D3  49 0F BC C8                     bsf rcx, r8
0045C6D7  48 8B FA                        mov rdi, rdx
0045C6DA  49 2B FA                        sub rdi, r10
0045C6DD  8B C1                           mov eax, ecx
0045C6DF  48 C1 FF 03                     sar rdi, 3
0045C6E3  48 C1 E7 06                     shl rdi, 6
0045C6E7  48 03 F8                        add rdi, rax
0045C6EA  89 4C 24 2C                     mov dword ptr [rsp + 0x2c], ecx
0045C6EE  48 8B 05 9B 3A 9D 00            mov rax, qword ptr [rip + 0x9d3a9b]
0045C6F5  48 3B F8                        cmp rdi, rax
0045C6F8  0F 87 A7 01 00 00               ja 0x14045c8a5
0045C6FE  48 8B C6                        mov rax, rsi
0045C701  48 D3 E0                        shl rax, cl
0045C704  48 2B C6                        sub rax, rsi
0045C707  49 0B C0                        or rax, r8
0045C70A  48 F7 D0                        not rax
0045C70D  48 85 C0                        test rax, rax
0045C710  75 15                           jne 0x14045c727
0045C712  48 8D 42 08                     lea rax, [rdx + 8]
0045C716  49 3B C1                        cmp rax, r9
0045C719  0F 87 22 01 00 00               ja 0x14045c841
0045C71F  48 8B D0                        mov rdx, rax
0045C722  48 8B 00                        mov rax, qword ptr [rax]
0045C725  EB E6                           jmp 0x14045c70d
0045C727  48 0F BC C0                     bsf rax, rax
0045C72B  4C 8B E2                        mov r12, rdx
0045C72E  89 44 24 2C                     mov dword ptr [rsp + 0x2c], eax
0045C732  4D 2B E2                        sub r12, r10
0045C735  49 C1 FC 03                     sar r12, 3
0045C739  49 C1 E4 06                     shl r12, 6
0045C73D  4C 03 E0                        add r12, rax
0045C740  48 8B 05 49 3A 9D 00            mov rax, qword ptr [rip + 0x9d3a49]
0045C747  4C 3B E0                        cmp r12, rax
0045C74A  4C 0F 47 E0                     cmova r12, rax
0045C74E  4C 2B E7                        sub r12, rdi
0045C751  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0045C756  4D 85 E4                        test r12, r12
0045C759  0F 84 7A 02 00 00               je 0x14045c9d9
0045C75F  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0045C764  48 2B FB                        sub rdi, rbx
0045C767  41 8B F5                        mov esi, r13d
0045C76A  83 E6 08                        and esi, 8
0045C76D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0045C772  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
0045C776  0F 85 CF 00 00 00               jne 0x14045c84b
0045C77C  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
0045C784  4C 8D 05 85 B5 71 00            lea r8, [rip + 0x71b585]
0045C78B  4C 03 F7                        add r14, rdi
0045C78E  48 8B D7                        mov rdx, rdi
0045C791  48 8B CB                        mov rcx, rbx
0045C794  48 C1 E2 0C                     shl rdx, 0xc
0045C798  48 C1 E1 0C                     shl rcx, 0xc
0045C79C  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0045C7A0  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
0045C7A5  49 3B C0                        cmp rax, r8
0045C7A8  0F 85 F3 06 00 00               jne 0x14045cea1
0045C7AE  E8 5D B5 71 00                  call 0x140b77d10
0045C7B3  45 33 DB                        xor r11d, r11d
0045C7B6  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
0045C7BD  85 F6                           test esi, esi
0045C7BF  0F 85 3A 02 00 00               jne 0x14045c9ff
0045C7C5  8B AC 24 C8 00 00 00            mov ebp, dword ptr [rsp + 0xc8]
0045C7CC  85 ED                           test ebp, ebp
0045C7CE  78 2D                           js 0x14045c7fd
0045C7D0  44 8B 7C 24 28                  mov r15d, dword ptr [rsp + 0x28]
0045C7D5  44 8B AC 24 B8 00 00 00         mov r13d, dword ptr [rsp + 0xb8]
0045C7DD  49 8D 34 1C                     lea rsi, [r12 + rbx]
0045C7E1  48 03 F7                        add rsi, rdi
0045C7E4  48 3B 35 A5 39 9D 00            cmp rsi, qword ptr [rip + 0x9d39a5]
0045C7EB  49 C7 C4 FF FF FF FF            mov r12, 0xffffffffffffffff
0045C7F2  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
0045C7F7  0F 82 A9 FD FF FF               jb 0x14045c5a6
0045C7FD  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0045C802  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
0045C80A  48 89 01                        mov qword ptr [rcx], rax
0045C80D  8B C5                           mov eax, ebp
0045C80F  48 83 C4 68                     add rsp, 0x68
0045C813  41 5F                           pop r15
0045C815  41 5E                           pop r14
0045C817  41 5D                           pop r13
0045C819  41 5C                           pop r12
0045C81B  5F                              pop rdi
0045C81C  5E                              pop rsi
0045C81D  5D                              pop rbp
0045C81E  5B                              pop rbx
0045C81F  C3                              ret
0045C820  CC                              int3
0045C821  48 8B 13                        mov rdx, qword ptr [rbx]
0045C824  48 F7 D2                        not rdx
0045C827  E9 DD FD FF FF                  jmp 0x14045c609
0045C82C  49 3B C1                        cmp rax, r9
0045C82F  77 6D                           ja 0x14045c89e
0045C831  48 83 C2 08                     add rdx, 8
0045C835  48 83 C0 08                     add rax, 8
0045C839  4C 8B 02                        mov r8, qword ptr [rdx]
0045C83C  E9 86 FE FF FF                  jmp 0x14045c6c7
0045C841  B8 40 00 00 00                  mov eax, 0x40
0045C846  E9 E0 FE FF FF                  jmp 0x14045c72b
0045C84B  45 85 FF                        test r15d, r15d
0045C84E  74 5D                           je 0x14045c8ad
0045C850  48 8B 05 51 39 9D 00            mov rax, qword ptr [rip + 0x9d3951]
0045C857  4C 8B CB                        mov r9, rbx
0045C85A  41 83 E1 1F                     and r9d, 0x1f
0045C85E  48 8B CB                        mov rcx, rbx
0045C861  48 C1 E9 05                     shr rcx, 5
0045C865  48 8B D7                        mov rdx, rdi
0045C868  4C 8D 04 88                     lea r8, [rax + rcx*4]
0045C86C  49 8D 04 39                     lea rax, [r9 + rdi]
0045C870  48 83 F8 20                     cmp rax, 0x20
0045C874  0F 87 AA 03 00 00               ja 0x14045cc24
0045C87A  48 83 FF 20                     cmp rdi, 0x20
0045C87E  0F 84 A2 04 00 00               je 0x14045cd26
0045C884  48 8B CF                        mov rcx, rdi
0045C887  B8 01 00 00 00                  mov eax, 1
0045C88C  D3 E0                           shl eax, cl
0045C88E  41 8B C9                        mov ecx, r9d
0045C891  FF C8                           dec eax
0045C893  D3 E0                           shl eax, cl
0045C895  F0 41 09 00                     lock or dword ptr [r8], eax
0045C899  E9 3F FF FF FF                  jmp 0x14045c7dd
0045C89E  48 8B 05 EB 38 9D 00            mov rax, qword ptr [rip + 0x9d38eb]
0045C8A5  48 8B F8                        mov rdi, rax
0045C8A8  E9 A9 FE FF FF                  jmp 0x14045c756
0045C8AD  B8 00 01 00 00                  mov eax, 0x100
0045C8B2  4C 8D 34 5B                     lea r14, [rbx + rbx*2]
0045C8B6  48 3B F8                        cmp rdi, rax
0045C8B9  48 8B F3                        mov rsi, rbx
0045C8BC  48 0F 47 F8                     cmova rdi, rax
0045C8C0  49 83 CF FF                     or r15, 0xffffffffffffffff
0045C8C4  49 C1 E6 04                     shl r14, 4
0045C8C8  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0045C8D2  48 8B C0                        mov rax, rax
0045C8D5  4C 03 F0                        add r14, rax
0045C8D8  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
0045C8DD  48 8D 04 7F                     lea rax, [rdi + rdi*2]
0045C8E1  48 C1 E0 04                     shl rax, 4
0045C8E5  49 03 C6                        add rax, r14
0045C8E8  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0045C8ED  45 0F 20 C5                     mov r13, cr8
0045C8F1  41 8D 57 03                     lea edx, [r15 + 3]
0045C8F5  44 0F 22 C2                     mov cr8, rdx
0045C8F9  44 39 1D 20 A4 B6 00            cmp dword ptr [rip + 0xb6a420], r11d
0045C900  0F 85 86 03 00 00               jne 0x14045cc8c
0045C906  49 8D 5E 18                     lea rbx, [r14 + 0x18]
0045C90A  41 8B EB                        mov ebp, r11d
0045C90D  F0 48 0F BA 2B 3F               lock bts qword ptr [rbx], 0x3f
0045C913  0F 82 C8 00 00 00               jb 0x14045c9e1
0045C919  8B 43 08                        mov eax, dword ptr [rbx + 8]
0045C91C  66 85 C0                        test ax, ax
0045C91F  0F 85 72 05 00 00               jne 0x14045ce97
0045C925  8A 43 0A                        mov al, byte ptr [rbx + 0xa]
0045C928  BA 02 00 00 00                  mov edx, 2
0045C92D  24 07                           and al, 7
0045C92F  2A C2                           sub al, dl
0045C931  3A C2                           cmp al, dl
0045C933  0F 87 5E 05 00 00               ja 0x14045ce97
0045C939  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0045C93D  48 8B 0D 44 37 9D 00            mov rcx, qword ptr [rip + 0x9d3744]
0045C944  48 C1 E8 2B                     shr rax, 0x2b
0045C948  25 FF 03 00 00                  and eax, 0x3ff
0045C94D  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
0045C951  8B 40 04                        mov eax, dword ptr [rax + 4]
0045C954  84 C0                           test al, al
0045C956  0F 88 99 01 00 00               js 0x14045caf5
0045C95C  33 D2                           xor edx, edx
0045C95E  49 8B CE                        mov rcx, r14
0045C961  E8 2A AC E2 FF                  call 0x140287590
0045C966  33 D2                           xor edx, edx
0045C968  A8 03                           test al, 3
0045C96A  0F 84 1C 04 00 00               je 0x14045cd8c
0045C970  49 8B CE                        mov rcx, r14
0045C973  E8 DC 8F F1 FF                  call 0x140375954
0045C978  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0045C982  F0 48 21 03                     lock and qword ptr [rbx], rax
0045C986  45 33 DB                        xor r11d, r11d
0045C989  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0045C98E  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
0045C996  44 39 1D 83 A3 B6 00            cmp dword ptr [rip + 0xb6a383], r11d
0045C99D  74 0F                           je 0x14045c9ae
0045C99F  44 0F 20 C1                     mov rcx, cr8
0045C9A3  41 8A D5                        mov dl, r13b
0045C9A6  E8 ED 8C 09 00                  call 0x1404f5698
0045C9AB  45 33 DB                        xor r11d, r11d
0045C9AE  41 0F B6 C5                     movzx eax, r13b
0045C9B2  44 0F 22 C0                     mov cr8, rax
0045C9B6  49 83 FF FF                     cmp r15, -1
0045C9BA  0F 85 48 02 00 00               jne 0x14045cc08
0045C9C0  8B AC 24 C8 00 00 00            mov ebp, dword ptr [rsp + 0xc8]
0045C9C7  44 8B 7C 24 28                  mov r15d, dword ptr [rsp + 0x28]
0045C9CC  44 8B AC 24 B8 00 00 00         mov r13d, dword ptr [rsp + 0xb8]
0045C9D4  E9 0B FE FF FF                  jmp 0x14045c7e4
0045C9D9  48 8B F8                        mov rdi, rax
0045C9DC  E9 83 FD FF FF                  jmp 0x14045c764
0045C9E1  FF C5                           inc ebp
0045C9E3  85 2D C3 88 B6 00               test dword ptr [rip + 0xb688c3], ebp
0045C9E9  0F 84 43 03 00 00               je 0x14045cd32
0045C9EF  F3 90                           pause
0045C9F1  48 8B 03                        mov rax, qword ptr [rbx]
0045C9F4  48 85 C0                        test rax, rax
0045C9F7  0F 89 10 FF FF FF               jns 0x14045c90d
0045C9FD  EB E2                           jmp 0x14045c9e1
0045C9FF  48 8D 34 5B                     lea rsi, [rbx + rbx*2]
0045CA03  4C 89 5C 24 38                  mov qword ptr [rsp + 0x38], r11
0045CA08  48 C1 E6 04                     shl rsi, 4
0045CA0C  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0045CA16  48 8B C0                        mov rax, rax
0045CA19  4C 8D 2C 7F                     lea r13, [rdi + rdi*2]
0045CA1D  48 03 F0                        add rsi, rax
0045CA20  49 C1 E5 04                     shl r13, 4
0045CA24  4C 03 EE                        add r13, rsi
0045CA27  45 0F 20 C7                     mov r15, cr8
0045CA2B  B8 02 00 00 00                  mov eax, 2
0045CA30  44 0F 22 C0                     mov cr8, rax
0045CA34  44 39 1D E5 A2 B6 00            cmp dword ptr [rip + 0xb6a2e5], r11d
0045CA3B  0F 85 A2 02 00 00               jne 0x14045cce3
0045CA41  4C 8D 76 18                     lea r14, [rsi + 0x18]
0045CA45  BF 02 00 00 00                  mov edi, 2
0045CA4A  49 BC FF FF FF FF FF FF FF 7F   movabs r12, 0x7fffffffffffffff
0045CA54  41 8B EB                        mov ebp, r11d
0045CA57  F0 49 0F BA 2E 3F               lock bts qword ptr [r14], 0x3f
0045CA5D  0F 82 EA 01 00 00               jb 0x14045cc4d
0045CA63  48 8B CE                        mov rcx, rsi
0045CA66  E8 65 8F DE FF                  call 0x1402459d0
0045CA6B  F0 4D 21 26                     lock and qword ptr [r14], r12
0045CA6F  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0045CA74  48 83 C6 30                     add rsi, 0x30
0045CA78  48 FF C1                        inc rcx
0045CA7B  49 83 C6 30                     add r14, 0x30
0045CA7F  45 33 DB                        xor r11d, r11d
0045CA82  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0045CA87  F6 C1 3F                        test cl, 0x3f
0045CA8A  75 35                           jne 0x14045cac1
0045CA8C  44 39 1D 8D A2 B6 00            cmp dword ptr [rip + 0xb6a28d], r11d
0045CA93  74 0F                           je 0x14045caa4
0045CA95  44 0F 20 C1                     mov rcx, cr8
0045CA99  41 8A D7                        mov dl, r15b
0045CA9C  E8 F7 8B 09 00                  call 0x1404f5698
0045CAA1  45 33 DB                        xor r11d, r11d
0045CAA4  41 0F B6 C7                     movzx eax, r15b
0045CAA8  44 0F 22 C0                     mov cr8, rax
0045CAAC  44 0F 20 C1                     mov rcx, cr8
0045CAB0  44 0F 22 C7                     mov cr8, rdi
0045CAB4  44 39 1D 65 A2 B6 00            cmp dword ptr [rip + 0xb6a265], r11d
0045CABB  0F 85 E5 01 00 00               jne 0x14045cca6
0045CAC1  49 3B F5                        cmp rsi, r13
0045CAC4  72 8E                           jb 0x14045ca54
0045CAC6  44 39 1D 53 A2 B6 00            cmp dword ptr [rip + 0xb6a253], r11d
0045CACD  48 8B 7C 24 30                  mov rdi, qword ptr [rsp + 0x30]
0045CAD2  4C 8B 64 24 20                  mov r12, qword ptr [rsp + 0x20]
0045CAD7  74 0F                           je 0x14045cae8
0045CAD9  44 0F 20 C1                     mov rcx, cr8
0045CADD  41 8A D7                        mov dl, r15b
0045CAE0  E8 B3 8B 09 00                  call 0x1404f5698
0045CAE5  45 33 DB                        xor r11d, r11d
0045CAE8  41 0F B6 C7                     movzx eax, r15b
0045CAEC  44 0F 22 C0                     mov cr8, rax
0045CAF0  E9 D0 FC FF FF                  jmp 0x14045c7c5
0045CAF5  48 8B 05 AC 36 9D 00            mov rax, qword ptr [rip + 0x9d36ac]
0045CAFC  4C 8B CE                        mov r9, rsi
0045CAFF  41 83 E1 1F                     and r9d, 0x1f
0045CB03  48 8B CE                        mov rcx, rsi
0045CB06  48 C1 E9 05                     shr rcx, 5
0045CB0A  BD 01 00 00 00                  mov ebp, 1
0045CB0F  8B D5                           mov edx, ebp
0045CB11  4C 8D 04 88                     lea r8, [rax + rcx*4]
0045CB15  49 8D 41 01                     lea rax, [r9 + 1]
0045CB19  48 83 F8 20                     cmp rax, 0x20
0045CB1D  0F 87 93 01 00 00               ja 0x14045ccb6
0045CB23  41 8B C9                        mov ecx, r9d
0045CB26  8B C5                           mov eax, ebp
0045CB28  D3 E0                           shl eax, cl
0045CB2A  F0 41 09 00                     lock or dword ptr [r8], eax
0045CB2E  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0045CB38  F0 48 21 03                     lock and qword ptr [rbx], rax
0045CB3C  49 83 FF FF                     cmp r15, -1
0045CB40  0F 85 50 FE FF FF               jne 0x14045c996
0045CB46  EB 57                           jmp 0x14045cb9f
0045CB48  48 8B 05 59 36 9D 00            mov rax, qword ptr [rip + 0x9d3659]
0045CB4F  4C 8B CE                        mov r9, rsi
0045CB52  41 83 E1 1F                     and r9d, 0x1f
0045CB56  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0045CB5B  48 8B CE                        mov rcx, rsi
0045CB5E  BD 01 00 00 00                  mov ebp, 1
0045CB63  48 C1 E9 05                     shr rcx, 5
0045CB67  8B D5                           mov edx, ebp
0045CB69  4C 8D 04 88                     lea r8, [rax + rcx*4]
0045CB6D  49 8D 41 01                     lea rax, [r9 + 1]
0045CB71  48 83 F8 20                     cmp rax, 0x20
0045CB75  0F 87 52 01 00 00               ja 0x14045cccd
0045CB7B  41 8B C9                        mov ecx, r9d
0045CB7E  8B C5                           mov eax, ebp
0045CB80  D3 E0                           shl eax, cl
0045CB82  F7 D0                           not eax
0045CB84  F0 41 21 00                     lock and dword ptr [r8], eax
0045CB88  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0045CB92  F0 48 21 03                     lock and qword ptr [rbx], rax
0045CB96  49 83 FF FF                     cmp r15, -1
0045CB9A  75 03                           jne 0x14045cb9f
0045CB9C  4C 8B FE                        mov r15, rsi
0045CB9F  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0045CBA4  48 03 C5                        add rax, rbp
0045CBA7  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0045CBAC  A8 0F                           test al, 0xf
0045CBAE  75 3A                           jne 0x14045cbea
0045CBB0  44 39 1D 69 A1 B6 00            cmp dword ptr [rip + 0xb6a169], r11d
0045CBB7  74 0F                           je 0x14045cbc8
0045CBB9  44 0F 20 C1                     mov rcx, cr8
0045CBBD  41 8A D5                        mov dl, r13b
0045CBC0  E8 D3 8A 09 00                  call 0x1404f5698
0045CBC5  45 33 DB                        xor r11d, r11d
0045CBC8  41 0F B6 C5                     movzx eax, r13b
0045CBCC  44 0F 22 C0                     mov cr8, rax
0045CBD0  44 0F 20 C1                     mov rcx, cr8
0045CBD4  BA 02 00 00 00                  mov edx, 2
0045CBD9  44 0F 22 C2                     mov cr8, rdx
0045CBDD  44 39 1D 3C A1 B6 00            cmp dword ptr [rip + 0xb6a13c], r11d
0045CBE4  0F 85 B2 00 00 00               jne 0x14045cc9c
0045CBEA  49 83 C6 30                     add r14, 0x30
0045CBEE  48 83 C3 30                     add rbx, 0x30
0045CBF2  48 03 F5                        add rsi, rbp
0045CBF5  45 33 DB                        xor r11d, r11d
0045CBF8  4C 3B 74 24 50                  cmp r14, qword ptr [rsp + 0x50]
0045CBFD  0F 82 07 FD FF FF               jb 0x14045c90a
0045CC03  E9 8E FD FF FF                  jmp 0x14045c996
0045CC08  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
0045CC0D  48 8B FE                        mov rdi, rsi
0045CC10  8B 74 24 38                     mov esi, dword ptr [rsp + 0x38]
0045CC14  49 2B FF                        sub rdi, r15
0045CC17  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
0045CC1C  49 8B DF                        mov rbx, r15
0045CC1F  E9 58 FB FF FF                  jmp 0x14045c77c
0045CC24  4D 85 C9                        test r9, r9
0045CC27  0F 85 C8 00 00 00               jne 0x14045ccf5
0045CC2D  48 83 FA 20                     cmp rdx, 0x20
0045CC31  73 38                           jae 0x14045cc6b
0045CC33  48 85 D2                        test rdx, rdx
0045CC36  0F 84 A1 FB FF FF               je 0x14045c7dd
0045CC3C  48 8B CA                        mov rcx, rdx
0045CC3F  B8 01 00 00 00                  mov eax, 1
0045CC44  D3 E0                           shl eax, cl
0045CC46  FF C8                           dec eax
0045CC48  E9 48 FC FF FF                  jmp 0x14045c895
0045CC4D  FF C5                           inc ebp
0045CC4F  85 2D 57 86 B6 00               test dword ptr [rip + 0xb68657], ebp
0045CC55  0F 84 04 01 00 00               je 0x14045cd5f
0045CC5B  F3 90                           pause
0045CC5D  49 8B 06                        mov rax, qword ptr [r14]
0045CC60  48 85 C0                        test rax, rax
0045CC63  0F 89 EE FD FF FF               jns 0x14045ca57
0045CC69  EB E2                           jmp 0x14045cc4d
0045CC6B  48 8B CA                        mov rcx, rdx
0045CC6E  48 C1 E9 05                     shr rcx, 5
0045CC72  48 6B C1 E0                     imul rax, rcx, -0x20
0045CC76  48 03 D0                        add rdx, rax
0045CC79  41 C7 00 FF FF FF FF            mov dword ptr [r8], 0xffffffff
0045CC80  49 83 C0 04                     add r8, 4
0045CC84  48 83 E9 01                     sub rcx, 1
0045CC88  74 A9                           je 0x14045cc33
0045CC8A  EB ED                           jmp 0x14045cc79
0045CC8C  41 8A CD                        mov cl, r13b
0045CC8F  E8 68 8A 09 00                  call 0x1404f56fc
0045CC94  45 33 DB                        xor r11d, r11d
0045CC97  E9 6A FC FF FF                  jmp 0x14045c906
0045CC9C  E8 5B 8A 09 00                  call 0x1404f56fc
0045CCA1  E9 44 FF FF FF                  jmp 0x14045cbea
0045CCA6  40 8A D7                        mov dl, dil
0045CCA9  E8 4E 8A 09 00                  call 0x1404f56fc
0045CCAE  45 33 DB                        xor r11d, r11d
0045CCB1  E9 0B FE FF FF                  jmp 0x14045cac1
0045CCB6  4D 85 C9                        test r9, r9
0045CCB9  0F 85 12 01 00 00               jne 0x14045cdd1
0045CCBF  48 8B CA                        mov rcx, rdx
0045CCC2  8B C5                           mov eax, ebp
0045CCC4  D3 E0                           shl eax, cl
0045CCC6  2B C5                           sub eax, ebp
0045CCC8  E9 5D FE FF FF                  jmp 0x14045cb2a
0045CCCD  4D 85 C9                        test r9, r9
0045CCD0  0F 85 56 01 00 00               jne 0x14045ce2c
0045CCD6  48 8B CA                        mov rcx, rdx
0045CCD9  83 C8 FF                        or eax, 0xffffffff
0045CCDC  D3 E0                           shl eax, cl
0045CCDE  E9 A1 FE FF FF                  jmp 0x14045cb84
0045CCE3  8A D0                           mov dl, al
0045CCE5  41 8A CF                        mov cl, r15b
0045CCE8  E8 0F 8A 09 00                  call 0x1404f56fc
0045CCED  45 33 DB                        xor r11d, r11d
0045CCF0  E9 4C FD FF FF                  jmp 0x14045ca41
0045CCF5  8B C3                           mov eax, ebx
0045CCF7  BA 20 00 00 00                  mov edx, 0x20
0045CCFC  83 E0 1F                        and eax, 0x1f
0045CCFF  2B D0                           sub edx, eax
0045CD01  B8 01 00 00 00                  mov eax, 1
0045CD06  8B CA                           mov ecx, edx
0045CD08  D3 E0                           shl eax, cl
0045CD0A  49 8B C9                        mov rcx, r9
0045CD0D  FF C8                           dec eax
0045CD0F  D3 E0                           shl eax, cl
0045CD11  F0 41 09 00                     lock or dword ptr [r8], eax
0045CD15  8B C2                           mov eax, edx
0045CD17  48 8B D7                        mov rdx, rdi
0045CD1A  48 2B D0                        sub rdx, rax
0045CD1D  49 83 C0 04                     add r8, 4
0045CD21  E9 07 FF FF FF                  jmp 0x14045cc2d
0045CD26  41 C7 00 FF FF FF FF            mov dword ptr [r8], 0xffffffff
0045CD2D  E9 AB FA FF FF                  jmp 0x14045c7dd
0045CD32  8B 05 80 9D B6 00               mov eax, dword ptr [rip + 0xb69d80]
0045CD38  A8 40                           test al, 0x40
0045CD3A  0F 84 AF FC FF FF               je 0x14045c9ef
0045CD40  E8 4B 27 EB FF                  call 0x14030f490
0045CD45  45 33 DB                        xor r11d, r11d
0045CD48  84 C0                           test al, al
0045CD4A  0F 84 9F FC FF FF               je 0x14045c9ef
0045CD50  8B CD                           mov ecx, ebp
0045CD52  E8 09 27 EB FF                  call 0x14030f460
0045CD57  45 33 DB                        xor r11d, r11d
0045CD5A  E9 92 FC FF FF                  jmp 0x14045c9f1
0045CD5F  8B 05 53 9D B6 00               mov eax, dword ptr [rip + 0xb69d53]
0045CD65  A8 40                           test al, 0x40
0045CD67  0F 84 EE FE FF FF               je 0x14045cc5b
0045CD6D  E8 1E 27 EB FF                  call 0x14030f490
0045CD72  45 33 DB                        xor r11d, r11d
0045CD75  84 C0                           test al, al
0045CD77  0F 84 DE FE FF FF               je 0x14045cc5b
0045CD7D  8B CD                           mov ecx, ebp
0045CD7F  E8 DC 26 EB FF                  call 0x14030f460
0045CD84  45 33 DB                        xor r11d, r11d
0045CD87  E9 D1 FE FF FF                  jmp 0x14045cc5d
0045CD8C  48 8B 03                        mov rax, qword ptr [rbx]
0045CD8F  48 B9 00 00 00 00 00 00 00 C0   movabs rcx, 0xc000000000000000
0045CD99  48 23 C1                        and rax, rcx
0045CD9C  49 8B CE                        mov rcx, r14
0045CD9F  48 89 03                        mov qword ptr [rbx], rax
0045CDA2  E8 A9 E7 E2 FF                  call 0x14028b550
0045CDA7  45 33 DB                        xor r11d, r11d
0045CDAA  85 C0                           test eax, eax
0045CDAC  0F 85 96 FD FF FF               jne 0x14045cb48
0045CDB2  48 8B D6                        mov rdx, rsi
0045CDB5  49 8B CE                        mov rcx, r14
0045CDB8  E8 83 D0 E5 FF                  call 0x1402b9e40
0045CDBD  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
0045CDC7  F0 49 21 46 18                  lock and qword ptr [r14 + 0x18], rax
0045CDCC  E9 B5 FB FF FF                  jmp 0x14045c986
0045CDD1  8B C6                           mov eax, esi
0045CDD3  BA 20 00 00 00                  mov edx, 0x20
0045CDD8  83 E0 1F                        and eax, 0x1f
0045CDDB  2B D0                           sub edx, eax
0045CDDD  8B C5                           mov eax, ebp
0045CDDF  8B CA                           mov ecx, edx
0045CDE1  D3 E0                           shl eax, cl
0045CDE3  49 8B C9                        mov rcx, r9
0045CDE6  2B C5                           sub eax, ebp
0045CDE8  D3 E0                           shl eax, cl
0045CDEA  F0 41 09 00                     lock or dword ptr [r8], eax
0045CDEE  8B C2                           mov eax, edx
0045CDF0  49 83 C0 04                     add r8, 4
0045CDF4  48 8B D5                        mov rdx, rbp
0045CDF7  48 2B D0                        sub rdx, rax
0045CDFA  48 83 FA 20                     cmp rdx, 0x20
0045CDFE  72 1E                           jb 0x14045ce1e
0045CE00  48 8B CA                        mov rcx, rdx
0045CE03  48 C1 E9 05                     shr rcx, 5
0045CE07  48 6B C1 E0                     imul rax, rcx, -0x20
0045CE0B  48 03 D0                        add rdx, rax
0045CE0E  41 C7 00 FF FF FF FF            mov dword ptr [r8], 0xffffffff
0045CE15  49 83 C0 04                     add r8, 4
0045CE19  48 2B CD                        sub rcx, rbp
0045CE1C  75 F0                           jne 0x14045ce0e
0045CE1E  48 85 D2                        test rdx, rdx
0045CE21  0F 84 07 FD FF FF               je 0x14045cb2e
0045CE27  E9 93 FE FF FF                  jmp 0x14045ccbf
0045CE2C  8B C6                           mov eax, esi
0045CE2E  BA 20 00 00 00                  mov edx, 0x20
0045CE33  83 E0 1F                        and eax, 0x1f
0045CE36  2B D0                           sub edx, eax
0045CE38  8B C5                           mov eax, ebp
0045CE3A  8B CA                           mov ecx, edx
0045CE3C  D3 E0                           shl eax, cl
0045CE3E  49 8B C9                        mov rcx, r9
0045CE41  2B C5                           sub eax, ebp
0045CE43  D3 E0                           shl eax, cl
0045CE45  F7 D0                           not eax
0045CE47  F0 41 21 00                     lock and dword ptr [r8], eax
0045CE4B  8B C2                           mov eax, edx
0045CE4D  49 83 C0 04                     add r8, 4
0045CE51  48 8B D5                        mov rdx, rbp
0045CE54  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0045CE59  48 2B D0                        sub rdx, rax
0045CE5C  48 83 FA 20                     cmp rdx, 0x20
0045CE60  72 1F                           jb 0x14045ce81
0045CE62  48 8B CA                        mov rcx, rdx
0045CE65  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
0045CE6A  48 C1 E9 05                     shr rcx, 5
0045CE6E  48 6B C1 E0                     imul rax, rcx, -0x20
0045CE72  48 03 D0                        add rdx, rax
0045CE75  45 89 18                        mov dword ptr [r8], r11d
0045CE78  49 83 C0 04                     add r8, 4
0045CE7C  48 2B CD                        sub rcx, rbp
0045CE7F  75 F4                           jne 0x14045ce75
0045CE81  48 85 D2                        test rdx, rdx
0045CE84  0F 84 FE FC FF FF               je 0x14045cb88
0045CE8A  E9 47 FE FF FF                  jmp 0x14045ccd6
0045CE8F  49 8B DC                        mov rbx, r12
0045CE92  E9 8A F7 FF FF                  jmp 0x14045c621
0045CE97  BD 01 00 00 00                  mov ebp, 1
0045CE9C  E9 8D FC FF FF                  jmp 0x14045cb2e
0045CEA1  E8 2A DC 25 00                  call 0x1406baad0
0045CEA6  E9 08 F9 FF FF                  jmp 0x14045c7b3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMirrorPerformBrownWrites(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;
    unsigned int v_stack_pB8;
    unsigned int v_stack_pC8;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (104);
    v_r11 = 0;
    v_stack_p20 = 0;
    v_stack_m80 = 0;
    v_stack_m68 = 0;
    v_r12 = (v_r12) | (-1);
loc_0045C5A6:
    a4 = (a4) & (0);
loc_0045C5C1:
    v_stack_m60 = 0;
    result = (*(unsigned __int64 *)(v_rip + 10304483) - 1) - (a4);
    result = (result) + 1;
    if (result < 1) goto loc_0045CE8F;
    result = (*(unsigned __int64 *)(v_rip + 10304483) - 1) >> (6);
    a1 = (unsigned __int8)(((unsigned __int8)(a4)) & (63));
    a2 = (1) << ((unsigned __int8)(a1));
    a2 = (a2) - 1;
    result = (a4) >> (6);
    result = ~(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10304484) + result * 8));
    a2 = (a2) | (result);
loc_0045C609:
    if (a2 != v_r12) goto loc_0045C639;
    v_rbx = (*(unsigned __int64 *)(v_rip + 10304484) + result * 8) + (8);
    if (v_rbx <= (*(unsigned __int64 *)(v_rip + 10304484) + result * 8)) goto loc_0045C821;
loc_0045C61B:
loc_0045C61E:
    v_r11 = 0;
loc_0045C621:
    if (a4 == 0) goto loc_0045C65F;
    a3 = 0 + 1;
    if ((0 + 1) > (*(unsigned __int64 *)(v_rip + 10304483))) { a3 = *(unsigned __int64 *)(v_rip + 10304483); }
    a3 = (a3) - 1;
    goto loc_0045C5C1;
loc_0045C639:
    v_rbx = (v_r12) - (*(unsigned __int64 *)(v_rip + 10304484));
    a2 = ~(a2);
    v_rbx = (v_rbx) >> (3);
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) + (result);
    v_stack_m60 = (unsigned int)(result);
    if (v_rbx > a3) goto loc_0045C61B;
    if (v_rbx == v_r12) goto loc_0045C61E;
    v_r11 = 0;
loc_0045C65F:
    if (v_rbx < 0) goto loc_0045C7FD;
    if (v_rbx == v_r12) goto loc_0045C7FD;
    v_stack_m7C = 0;
    v_stack_m88 = 0;
    if ((*(unsigned __int64 *)(v_rip + 10304280)) <= v_rbx) goto loc_0045C9D9;
    result = (*(unsigned __int64 *)(v_rip + 10304280)) - 1;
    result = (result) >> (6);
    a1 = (unsigned __int8)(((unsigned __int8)(v_rbx)) & (63));
    result = (v_rbx) >> (6);
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - (1);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10304259) + result * 8)) | (result);
loc_0045C6C7:
    a3 = ~(a3);
    if (a3 == 0) goto loc_0045C82C;
    v_rdi = (*(unsigned __int64 *)(v_rip + 10304259) + result * 8) - (*(unsigned __int64 *)(v_rip + 10304259));
    v_rdi = (v_rdi) >> (3);
    v_rdi = (v_rdi) << (6);
    v_rdi = (v_rdi) + ((unsigned int)((unsigned int)(a1)));
    v_stack_m7C = (unsigned int)(a1);
    if (v_rdi > (*(unsigned __int64 *)(v_rip + 10304155))) goto loc_0045C8A5;
    result = (1) << ((unsigned __int8)(a1));
    result = (result) - (1);
    result = (result) | (a3);
    result = ~(result);
loc_0045C70D:
    if (result != 0) goto loc_0045C727;
    if ((*(unsigned __int64 *)(v_rip + 10304259) + result * 8 + 8) > (*(unsigned __int64 *)(v_rip + 10304259) + result * 8)) goto loc_0045C841;
    goto loc_0045C70D;
loc_0045C727:
loc_0045C72B:
    v_stack_m7C = (unsigned int)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10304259) + result * 8 + 8));
    v_r12 = (*(unsigned __int64 *)(v_rip + 10304259) + result * 8 + 8) - (*(unsigned __int64 *)(v_rip + 10304259));
    v_r12 = (v_r12) >> (3);
    v_r12 = (v_r12) << (6);
    v_r12 = (v_r12) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 10304259) + result * 8 + 8));
    if (v_r12 > (*(unsigned __int64 *)(v_rip + 10304073))) { v_r12 = *(unsigned __int64 *)(v_rip + 10304073); }
    v_r12 = (v_r12) - (v_rdi);
    v_stack_m88 = v_r12;
loc_0045C756:
    if (v_r12 == 0) goto loc_0045C9D9;
    v_stack_m88 = v_r12;
loc_0045C764:
    v_rdi = (v_rdi) - (v_rbx);
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) & (8));
    v_stack_m78 = v_rdi;
    v_stack_m70 = (unsigned int)(v_rsi);
    if (condition_is_not_equal) goto loc_0045C84B;
loc_0045C77C:
    v_r14 = (0) + (v_rdi);
    a2 = (v_rdi) << (12);
    a1 = (v_rbx) << (12);
    v_stack_m68 = v_r14;
    if ((*(unsigned __int64 *)(v_stack_p8 + 16)) != (v_rip + 7452037)) goto loc_0045CEA1;
    result = PopMirrorPhysicalMemory(a1, a2, v_rip + 7452037, *(unsigned __int64 *)(v_rip + 10304259) + result * 8);
loc_0045C7B3:
    v_r11 = 0;
    v_stack_p20 = (unsigned int)(result);
    if ((unsigned int)(v_rsi) != 0) goto loc_0045C9FF;
loc_0045C7C5:
    if (sign_flag) goto loc_0045C7FD;
loc_0045C7DD:
    v_rsi = (v_r12 + v_rbx * 1) + (v_rdi);
loc_0045C7E4:
    if (v_rsi < (*(unsigned __int64 *)(v_rip + 10303909))) goto loc_0045C5A6;
loc_0045C7FD:
    *(unsigned __int64 *)(v_stack_p18) = v_stack_m68;
    v_rsp = (v_rsp) + (104);
    return (unsigned int)((unsigned int)((unsigned int)(v_stack_p20)));
loc_0045C821:
    a2 = ~(*(unsigned __int64 *)(v_rbx));
    goto loc_0045C609;
loc_0045C82C:
    if (((unsigned int)((unsigned int)((unsigned int)(v_stack_p20)))) > (*(unsigned __int64 *)(v_rip + 10304259) + result * 8)) goto loc_0045C89E;
    a2 = (a2) + (8);
    result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_p20)))) + (8);
    goto loc_0045C6C7;
loc_0045C841:
    goto loc_0045C72B;
loc_0045C84B:
    if ((unsigned int)((unsigned int)(v_stack_m80)) == 0) goto loc_0045C8AD;
    a4 = (unsigned int)((v_rbx) & (31));
    a1 = (v_rbx) >> (5);
    if ((a4 + v_rdi * 1) > 32) goto loc_0045CC24;
    if (v_rdi == 32) goto loc_0045CD26;
    result = (unsigned int)((1) << ((unsigned __int8)(v_rdi)));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << ((unsigned __int8)((unsigned int)((unsigned int)(a4)))));
loc_0045C895:
    goto loc_0045C7DD;
loc_0045C89E:
loc_0045C8A5:
    goto loc_0045C756;
loc_0045C8AD:
    v_rdi = *(unsigned __int64 *)(v_rip + 10303723);
    if ((*(unsigned __int64 *)(v_rip + 10303723)) > 256) { v_rdi = 256; }
    v_r15 = ((unsigned int)(v_stack_m80)) | (-1);
    v_r14 = (v_rbx + v_rbx * 2) << (4);
    v_r14 = (v_r14) + (256);
    v_stack_p30 = 0;
    result = (v_rdi + v_rdi * 2) << (4);
    result = (result) + (v_r14);
    v_stack_p50 = result;
    if ((*(unsigned int *)(v_rip + 11969568)) != 0) goto loc_0045CC8C;
loc_0045C906:
loc_0045C90A:
loc_0045C90D:
    if ((*(unsigned int *)(v_rip + 11969568)) < 0) goto loc_0045C9E1;
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)(v_r14 + 24 + 8))) != 0) goto loc_0045CE97;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r14 + 24 + 10)) & (7));
    result = (unsigned __int8)((result) - (2));
    if (((unsigned __int8)(result)) > 2) goto loc_0045CE97;
    result = (*(unsigned __int64 *)(v_r14 + 24 + 16)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0045CAF5;
    a2 = 0;
    result = MiUnlinkPageFromListEx(v_r14, a2, *(unsigned __int64 *)(v_rip + 10303825) + a1 * 4, a4);
    a2 = 0;
    if ((((unsigned __int8)(result)) & (3)) == 0) goto loc_0045CD8C;
    result = MiDiscardTransitionPteEx(v_r14, a2, *(unsigned __int64 *)(v_rip + 10303825) + a1 * 4, a4);
loc_0045C986:
    v_r11 = 0;
    v_stack_p20 = -1;
    v_stack_p28 = 1;
loc_0045C996:
    if ((*(unsigned int *)(v_rip + 11969411)) != 0) {
        a1 = v_r15 + 3;
        a2 = (unsigned __int8)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rip + 10303825) + a1 * 4, a4);
        v_r11 = 0;
    }
    if (v_r15 != -1) goto loc_0045CC08;
    goto loc_0045C7E4;
loc_0045C9D9:
    goto loc_0045C764;
loc_0045C9E1:
    v_rbp = (unsigned int)(((unsigned int)(v_stack_pC8)) + 1);
    if (((*(unsigned int *)(v_rip + 11962563)) & ((unsigned int)(v_rbp))) == 0) goto loc_0045CD32;
loc_0045C9EF:
loc_0045C9F1:
    if (!sign_flag) goto loc_0045C90D;
    goto loc_0045C9E1;
loc_0045C9FF:
    v_stack_p38 = 0;
    v_rsi = (v_r14 + 24 + v_r14 + 24 * 2) << (4);
    v_rsi = (v_rsi) + (*(unsigned __int64 *)(v_r14 + 24));
    v_r13 = ((unsigned __int8)(v_cr8) + (unsigned __int8)(v_cr8) * 2) << (4);
    v_r13 = (v_r13) + (v_rsi);
    if ((*(unsigned int *)(v_rip + 11969253)) != 0) goto loc_0045CCE3;
loc_0045CA41:
loc_0045CA54:
loc_0045CA57:
    if ((*(unsigned int *)(v_rip + 11969253)) < 0) goto loc_0045CC4D;
    result = MiRemoveLockedPageChargeAndDecRef(v_rsi, a2, *(unsigned __int64 *)(v_rip + 10303825) + a1 * 4, a4);
    v_rsi = (v_rsi) + (48);
    a1 = (v_stack_p38) + 1;
    v_r14 = (v_rsi + 24) + (48);
    v_r11 = 0;
    v_stack_p38 = a1;
    if ((((unsigned __int8)(a1)) & (63)) != 0) goto loc_0045CAC1;
    if ((*(unsigned int *)(v_rip + 11969165)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rip + 10303825) + a1 * 4, a4);
        v_r11 = 0;
    }
    if ((*(unsigned int *)(v_rip + 11969125)) != 0) goto loc_0045CCA6;
loc_0045CAC1:
    if (v_rsi < v_r13) goto loc_0045CA54;
    result = (unsigned __int8)((unsigned __int8)(v_cr8));
    if ((*(unsigned int *)(v_rip + 11969107)) != 0) {
        a1 = 2;
        a2 = (unsigned __int8)((unsigned __int8)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rip + 10303825) + a1 * 4, a4);
        v_r11 = 0;
    }
    goto loc_0045C7C5;
loc_0045CAF5:
    a4 = (unsigned int)((v_rsi) & (31));
    a1 = (v_rsi) >> (5);
    if ((a4 + 1) > 32) goto loc_0045CCB6;
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(a4)))));
loc_0045CB2A:
loc_0045CB2E:
    if (((unsigned __int8)(v_cr8)) != -1) goto loc_0045C996;
    goto loc_0045CB9F;
loc_0045CB48:
    a4 = (unsigned int)((v_rsi) & (31));
    v_stack_p20 = v_stack_p20;
    a1 = (v_rsi) >> (5);
    if ((a4 + 1) > 32) goto loc_0045CCCD;
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)((unsigned int)(a4)))));
    result = (unsigned int)(~(result));
loc_0045CB84:
loc_0045CB88:
    v_r15 = (unsigned __int8)(v_cr8);
    if (((unsigned __int8)(v_cr8)) == -1) {
        v_r15 = v_rsi;
    }
    result = (v_stack_p30) + (1);
    v_stack_p30 = result;
    if ((((unsigned __int8)(result)) & (15)) != 0) goto loc_0045CBEA;
    if ((*(unsigned int *)(v_rip + 11968873)) != 0) {
        a1 = (unsigned __int8)((unsigned __int8)(v_cr8));
        a2 = (unsigned __int8)(v_r13);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(v_rip + 10303065) + a1 * 4, a4);
        v_r11 = 0;
    }
    if ((*(unsigned int *)(v_rip + 11968828)) != 0) goto loc_0045CC9C;
loc_0045CBEA:
    v_r14 = (v_r14) + (48);
    v_rbx = (v_r14 + 24) + (48);
    v_rsi = (v_rsi) + (1);
    v_r11 = 0;
    if (v_r14 < v_stack_p50) goto loc_0045C90A;
    goto loc_0045C996;
loc_0045CC08:
    v_rdi = (v_rsi) - (v_r15);
    v_stack_p30 = v_rdi;
    goto loc_0045C77C;
loc_0045CC24:
    if (a4 != 0) goto loc_0045CCF5;
loc_0045CC2D:
    if (2 >= 32) goto loc_0045CC6B;
loc_0045CC33:
    if (2 == 0) goto loc_0045C7DD;
    result = (unsigned int)((1) << (2));
    result = (unsigned int)((result) - 1);
    goto loc_0045C895;
loc_0045CC4D:
    v_rbp = (unsigned int)((1) + 1);
    if (((*(unsigned int *)(v_rip + 11961943)) & ((unsigned int)(v_rbp))) == 0) goto loc_0045CD5F;
loc_0045CC5B:
loc_0045CC5D:
    if (!sign_flag) goto loc_0045CA57;
    goto loc_0045CC4D;
loc_0045CC6B:
    a1 = (2) >> (5);
    result = (*(unsigned __int64 *)(v_stack_p40)) * (a1);
    a2 = (2) + (result);
loc_0045CC79:
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 10303065) + a1 * 4) = 0xFFFFFFFFULL;
    a3 = (*(unsigned __int64 *)(v_rip + 10303065) + a1 * 4) + (4);
    a1 = (a1) - (1);
    if (condition_is_equal) goto loc_0045CC33;
    goto loc_0045CC79;
loc_0045CC8C:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_r13), a2, a3, a4);
    v_r11 = 0;
    goto loc_0045C906;
loc_0045CC9C:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_r13), a2, a3, a4);
    goto loc_0045CBEA;
loc_0045CCA6:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_r13), (unsigned __int8)(v_rdi), a3, a4);
    v_r11 = 0;
    goto loc_0045CAC1;
loc_0045CCB6:
    if (a4 != 0) goto loc_0045CDD1;
loc_0045CCBF:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) << ((unsigned __int8)((unsigned __int8)(v_rdi))));
    result = (unsigned int)((result) - ((unsigned int)(v_rbp)));
    goto loc_0045CB2A;
loc_0045CCCD:
    if (a4 != 0) goto loc_0045CE2C;
loc_0045CCD6:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) << ((unsigned __int8)((unsigned __int8)(v_rdi))));
    goto loc_0045CB84;
loc_0045CCE3:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_r15), (unsigned __int8)(result), a3, a4);
    v_r11 = 0;
    goto loc_0045CA41;
loc_0045CCF5:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(result)));
    result = (unsigned int)((1) << ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned int)((result) - 1);
    result = (unsigned int)((result) << ((unsigned __int8)(a4)));
    a2 = (v_rdi) - ((unsigned int)(a2));
    a3 = (a3) + (4);
    goto loc_0045CC2D;
loc_0045CD26:
    *(unsigned int *)(a3) = 0xFFFFFFFFULL;
    goto loc_0045C7DD;
loc_0045CD32:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11967872)))) & (64)) == 0) goto loc_0045C9EF;
    result = KiCheckVpBackingLongSpinWaitHypercall(a4, a2, a3, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0045C9EF;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    v_r11 = 0;
    goto loc_0045C9F1;
loc_0045CD5F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11967827)))) & (64)) == 0) goto loc_0045CC5B;
    result = KiCheckVpBackingLongSpinWaitHypercall((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    v_r11 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_0045CC5B;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_rbp)), a2, a3, a4);
    v_r11 = 0;
    goto loc_0045CC5D;
loc_0045CD8C:
    result = (*(unsigned __int64 *)(v_r15)) & ((unsigned int)((unsigned int)(v_rbp)));
    *(unsigned __int64 *)(v_r15) = result;
    result = MiAddLockedPageCharge(v_stack_p40, a2, a3, a4);
    v_r11 = 0;
    if ((unsigned int)(result) != 0) goto loc_0045CB48;
    result = MiPfnReferenceCountIsZero(v_stack_p40, (unsigned int)(v_stack_p38), a3, a4);
    goto loc_0045C986;
loc_0045CDD1:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p38)))) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) << ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned int)((result) - ((unsigned int)(v_rbp)));
    result = (unsigned int)((result) << ((unsigned __int8)(a4)));
    a3 = (a3) + (4);
    a2 = (v_rbp) - ((unsigned int)(a2));
    if (a2 < 32) goto loc_0045CE1E;
    a1 = (a2) >> (5);
    result = ((unsigned int)(a2)) * (a1);
    a2 = (a2) + (result);
loc_0045CE0E:
    *(unsigned int *)(a3) = 0xFFFFFFFFULL;
    a3 = (a3) + (4);
    a1 = (a1) - (v_rbp);
    if (condition_is_not_equal) goto loc_0045CE0E;
loc_0045CE1E:
    if (a2 == 0) goto loc_0045CB2E;
    goto loc_0045CCBF;
loc_0045CE2C:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p38)))) & (31));
    a2 = (unsigned int)((32) - ((unsigned int)(result)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbp))) << ((unsigned __int8)((unsigned int)(a2))));
    result = (unsigned int)((result) - ((unsigned int)(v_rbp)));
    result = (unsigned int)((result) << ((unsigned __int8)(a4)));
    result = (unsigned int)(~(result));
    a3 = (a3) + (4);
    v_stack_p20 = v_stack_p20;
    a2 = (v_rbp) - ((unsigned int)(a2));
    if (a2 < 32) goto loc_0045CE81;
    v_stack_p20 = v_stack_p20;
    a1 = (a2) >> (5);
    result = ((unsigned int)(a2)) * (a1);
    a2 = (a2) + (result);
loc_0045CE75:
    *(unsigned int *)(a3) = 0;
    a3 = (a3) + (4);
    a1 = (a1) - (v_rbp);
    if (condition_is_not_equal) goto loc_0045CE75;
loc_0045CE81:
    if (a2 == 0) goto loc_0045CB88;
    goto loc_0045CCD6;
loc_0045CE8F:
    goto loc_0045C621;
loc_0045CE97:
    goto loc_0045CB2E;
loc_0045CEA1:
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_0045C7B3;
}
```

## 5. (Beta) C Style

```c
int64_t MiMirrorPerformBrownWrites(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;
    uint32_t v_stack_pB8;
    uint32_t v_stack_pC8;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (104);
    local_r11 = 0;
    v_stack_p20 = 0;
    v_stack_m80 = 0;
    v_stack_m68 = 0;
    local_r12 = (local_r12) | (-1);
loc_0045C5A6:
    Arg4 = (Arg4) & (0);
loc_0045C5C1:
    v_stack_m60 = 0;
    result = (*(uint64_t *)(v_rip + 0x9D3BE3) - 1) - (Arg4);
    result = (result) + 1;
    if (result < 1) goto loc_0045CE8F;
    result = (*(uint64_t *)(v_rip + 0x9D3BE3) - 1) >> (6);
    Arg1 = (uint8_t)(((uint8_t)(Arg4)) & (63));
    Arg2 = (1) << ((uint8_t)(Arg1));
    Arg2 = (Arg2) - 1;
    result = (Arg4) >> (6);
    result = ~(*(uint64_t *)(*(uint64_t *)(v_rip + 0x9D3BE4) + result * 8));
    Arg2 = (Arg2) | (result);
loc_0045C609:
    if (Arg2 != local_r12) goto loc_0045C639;
    local_rbx = (*(uint64_t *)(v_rip + 0x9D3BE4) + result * 8) + (8);
    if (local_rbx <= (*(uint64_t *)(v_rip + 0x9D3BE4) + result * 8)) goto loc_0045C821;
loc_0045C61B:
loc_0045C61E:
    local_r11 = 0;
loc_0045C621:
    if (Arg4 == 0) goto loc_0045C65F;
    Arg3 = 0 + 1;
    if ((0 + 1) > (*(uint64_t *)(v_rip + 0x9D3BE3))) { Arg3 = *(uint64_t *)(v_rip + 0x9D3BE3); }
    Arg3 = (Arg3) - 1;
    goto loc_0045C5C1;
loc_0045C639:
    local_rbx = (local_r12) - (*(uint64_t *)(v_rip + 0x9D3BE4));
    Arg2 = ~(Arg2);
    local_rbx = (local_rbx) >> (3);
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) + (result);
    v_stack_m60 = (uint32_t)(result);
    if (local_rbx > Arg3) goto loc_0045C61B;
    if (local_rbx == local_r12) goto loc_0045C61E;
    local_r11 = 0;
loc_0045C65F:
    if (local_rbx < 0) goto loc_0045C7FD;
    if (local_rbx == local_r12) goto loc_0045C7FD;
    v_stack_m7C = 0;
    v_stack_m88 = 0;
    if ((*(uint64_t *)(v_rip + 0x9D3B18)) <= local_rbx) goto loc_0045C9D9;
    result = (*(uint64_t *)(v_rip + 0x9D3B18)) - 1;
    result = (result) >> (6);
    Arg1 = (uint8_t)(((uint8_t)(local_rbx)) & (63));
    result = (local_rbx) >> (6);
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - (1);
    Arg3 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x9D3B03) + result * 8)) | (result);
loc_0045C6C7:
    Arg3 = ~(Arg3);
    if (Arg3 == 0) goto loc_0045C82C;
    local_rdi = (*(uint64_t *)(v_rip + 0x9D3B03) + result * 8) - (*(uint64_t *)(v_rip + 0x9D3B03));
    local_rdi = (local_rdi) >> (3);
    local_rdi = (local_rdi) << (6);
    local_rdi = (local_rdi) + ((uint32_t)((uint32_t)(Arg1)));
    v_stack_m7C = (uint32_t)(Arg1);
    if (local_rdi > (*(uint64_t *)(v_rip + 0x9D3A9B))) goto loc_0045C8A5;
    result = (1) << ((uint8_t)(Arg1));
    result = (result) - (1);
    result = (result) | (Arg3);
    result = ~(result);
loc_0045C70D:
    if (result != 0) goto loc_0045C727;
    if ((*(uint64_t *)(v_rip + 0x9D3B03) + result * 8 + 8) > (*(uint64_t *)(v_rip + 0x9D3B03) + result * 8)) goto loc_0045C841;
    goto loc_0045C70D;
loc_0045C727:
loc_0045C72B:
    v_stack_m7C = (uint32_t)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x9D3B03) + result * 8 + 0x8));
    local_r12 = (*(uint64_t *)(v_rip + 0x9D3B03) + result * 8 + 8) - (*(uint64_t *)(v_rip + 0x9D3B03));
    local_r12 = (local_r12) >> (3);
    local_r12 = (local_r12) << (6);
    local_r12 = (local_r12) + (*(uint64_t *)(*(uint64_t *)(v_rip + 0x9D3B03) + result * 8 + 0x8));
    if (local_r12 > (*(uint64_t *)(v_rip + 0x9D3A49))) { local_r12 = *(uint64_t *)(v_rip + 0x9D3A49); }
    local_r12 = (local_r12) - (local_rdi);
    v_stack_m88 = local_r12;
loc_0045C756:
    if (local_r12 == 0) goto loc_0045C9D9;
    v_stack_m88 = local_r12;
loc_0045C764:
    local_rdi = (local_rdi) - (local_rbx);
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) & (8));
    v_stack_m78 = local_rdi;
    v_stack_m70 = (uint32_t)(local_rsi);
    if (condition_is_not_equal) goto loc_0045C84B;
loc_0045C77C:
    local_r14 = (0) + (local_rdi);
    Arg2 = (local_rdi) << (12);
    Arg1 = (local_rbx) << (12);
    v_stack_m68 = local_r14;
    if ((*(uint64_t *)(v_stack_p8 + 0x10)) != (v_rip + 7452037)) goto loc_0045CEA1;
    result = PopMirrorPhysicalMemory(Arg1, Arg2, v_rip + 7452037, *(uint64_t *)(v_rip + 0x9D3B03) + result * 8);
loc_0045C7B3:
    local_r11 = 0;
    v_stack_p20 = (uint32_t)(result);
    if ((uint32_t)(local_rsi) != 0) goto loc_0045C9FF;
loc_0045C7C5:
    if (sign_flag) goto loc_0045C7FD;
loc_0045C7DD:
    local_rsi = (local_r12 + local_rbx * 1) + (local_rdi);
loc_0045C7E4:
    if (local_rsi < (*(uint64_t *)(v_rip + 0x9D39A5))) goto loc_0045C5A6;
loc_0045C7FD:
    *(uint64_t *)(v_stack_p18) = v_stack_m68;
    local_rsp = (local_rsp) + (104);
    return (uint32_t)((uint32_t)((uint32_t)(v_stack_p20)));
loc_0045C821:
    Arg2 = ~(*(uint64_t *)(local_rbx));
    goto loc_0045C609;
loc_0045C82C:
    if (((uint32_t)((uint32_t)((uint32_t)(v_stack_p20)))) > (*(uint64_t *)(v_rip + 0x9D3B03) + result * 8)) goto loc_0045C89E;
    Arg2 = (Arg2) + (8);
    result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_p20)))) + (8);
    goto loc_0045C6C7;
loc_0045C841:
    goto loc_0045C72B;
loc_0045C84B:
    if ((uint32_t)((uint32_t)(v_stack_m80)) == 0) goto loc_0045C8AD;
    Arg4 = (uint32_t)((local_rbx) & (31));
    Arg1 = (local_rbx) >> (5);
    if ((Arg4 + local_rdi * 1) > 32) goto loc_0045CC24;
    if (local_rdi == 32) goto loc_0045CD26;
    result = (uint32_t)((1) << ((uint8_t)(local_rdi)));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << ((uint8_t)((uint32_t)((uint32_t)(Arg4)))));
loc_0045C895:
    goto loc_0045C7DD;
loc_0045C89E:
loc_0045C8A5:
    goto loc_0045C756;
loc_0045C8AD:
    local_rdi = *(uint64_t *)(v_rip + 0x9D38EB);
    if ((*(uint64_t *)(v_rip + 0x9D38EB)) > 256) { local_rdi = 256; }
    local_r15 = ((uint32_t)(v_stack_m80)) | (-1);
    local_r14 = (local_rbx + local_rbx * 2) << (4);
    local_r14 = (local_r14) + (256);
    v_stack_p30 = 0;
    result = (local_rdi + local_rdi * 2) << (4);
    result = (result) + (local_r14);
    v_stack_p50 = result;
    if ((*(uint32_t *)(v_rip + 0xB6A420)) != 0) goto loc_0045CC8C;
loc_0045C906:
loc_0045C90A:
loc_0045C90D:
    if ((*(uint32_t *)(v_rip + 0xB6A420)) < 0) goto loc_0045C9E1;
    if ((uint16_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x18 + 0x8))) != 0) goto loc_0045CE97;
    result = (uint8_t)((*(uint8_t *)(local_r14 + 0x18 + 0xA)) & (7));
    result = (uint8_t)((result) - (2));
    if (((uint8_t)(result)) > 2) goto loc_0045CE97;
    result = (*(uint64_t *)(local_r14 + 0x18 + 0x10)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    if (sign_flag) goto loc_0045CAF5;
    Arg2 = 0;
    result = MiUnlinkPageFromListEx(local_r14, Arg2, *(uint64_t *)(v_rip + 0x9D3951) + Arg1 * 4, Arg4);
    Arg2 = 0;
    if ((((uint8_t)(result)) & (3)) == 0) goto loc_0045CD8C;
    result = MiDiscardTransitionPteEx(local_r14, Arg2, *(uint64_t *)(v_rip + 0x9D3951) + Arg1 * 4, Arg4);
loc_0045C986:
    local_r11 = 0;
    v_stack_p20 = -1;
    v_stack_p28 = 1;
loc_0045C996:
    if ((*(uint32_t *)(v_rip + 0xB6A383)) != 0) {
        Arg1 = local_r15 + 3;
        Arg2 = (uint8_t)(v_cr8);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(v_rip + 0x9D3951) + Arg1 * 4, Arg4);
        local_r11 = 0;
    }
    if (local_r15 != -1) goto loc_0045CC08;
    goto loc_0045C7E4;
loc_0045C9D9:
    goto loc_0045C764;
loc_0045C9E1:
    local_rbp = (uint32_t)(((uint32_t)(v_stack_pC8)) + 1);
    if (((*(uint32_t *)(v_rip + 0xB688C3)) & ((uint32_t)(local_rbp))) == 0) goto loc_0045CD32;
loc_0045C9EF:
loc_0045C9F1:
    if (!sign_flag) goto loc_0045C90D;
    goto loc_0045C9E1;
loc_0045C9FF:
    v_stack_p38 = 0;
    local_rsi = (local_r14 + 24 + local_r14 + 24 * 2) << (4);
    local_rsi = (local_rsi) + (*(uint64_t *)(local_r14 + 0x18));
    local_r13 = ((uint8_t)(v_cr8) + (uint8_t)(v_cr8) * 2) << (4);
    local_r13 = (local_r13) + (local_rsi);
    if ((*(uint32_t *)(v_rip + 0xB6A2E5)) != 0) goto loc_0045CCE3;
loc_0045CA41:
loc_0045CA54:
loc_0045CA57:
    if ((*(uint32_t *)(v_rip + 0xB6A2E5)) < 0) goto loc_0045CC4D;
    result = MiRemoveLockedPageChargeAndDecRef(local_rsi, Arg2, *(uint64_t *)(v_rip + 0x9D3951) + Arg1 * 4, Arg4);
    local_rsi = (local_rsi) + (48);
    Arg1 = (v_stack_p38) + 1;
    local_r14 = (local_rsi + 24) + (48);
    local_r11 = 0;
    v_stack_p38 = Arg1;
    if ((((uint8_t)(Arg1)) & (63)) != 0) goto loc_0045CAC1;
    if ((*(uint32_t *)(v_rip + 0xB6A28D)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(v_rip + 0x9D3951) + Arg1 * 4, Arg4);
        local_r11 = 0;
    }
    if ((*(uint32_t *)(v_rip + 0xB6A265)) != 0) goto loc_0045CCA6;
loc_0045CAC1:
    if (local_rsi < local_r13) goto loc_0045CA54;
    result = (uint8_t)((uint8_t)(v_cr8));
    if ((*(uint32_t *)(v_rip + 0xB6A253)) != 0) {
        Arg1 = 2;
        Arg2 = (uint8_t)((uint8_t)(v_cr8));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(v_rip + 0x9D3951) + Arg1 * 4, Arg4);
        local_r11 = 0;
    }
    goto loc_0045C7C5;
loc_0045CAF5:
    Arg4 = (uint32_t)((local_rsi) & (31));
    Arg1 = (local_rsi) >> (5);
    if ((Arg4 + 1) > 32) goto loc_0045CCB6;
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(Arg4)))));
loc_0045CB2A:
loc_0045CB2E:
    if (((uint8_t)(v_cr8)) != -1) goto loc_0045C996;
    goto loc_0045CB9F;
loc_0045CB48:
    Arg4 = (uint32_t)((local_rsi) & (31));
    v_stack_p20 = v_stack_p20;
    Arg1 = (local_rsi) >> (5);
    if ((Arg4 + 1) > 32) goto loc_0045CCCD;
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)((uint32_t)(Arg4)))));
    result = (uint32_t)(~(result));
loc_0045CB84:
loc_0045CB88:
    local_r15 = (uint8_t)(v_cr8);
    if (((uint8_t)(v_cr8)) == -1) {
        local_r15 = local_rsi;
    }
    result = (v_stack_p30) + (1);
    v_stack_p30 = result;
    if ((((uint8_t)(result)) & (15)) != 0) goto loc_0045CBEA;
    if ((*(uint32_t *)(v_rip + 0xB6A169)) != 0) {
        Arg1 = (uint8_t)((uint8_t)(v_cr8));
        Arg2 = (uint8_t)(local_r13);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(v_rip + 0x9D3659) + Arg1 * 4, Arg4);
        local_r11 = 0;
    }
    if ((*(uint32_t *)(v_rip + 0xB6A13C)) != 0) goto loc_0045CC9C;
loc_0045CBEA:
    local_r14 = (local_r14) + (48);
    local_rbx = (local_r14 + 24) + (48);
    local_rsi = (local_rsi) + (1);
    local_r11 = 0;
    if (local_r14 < v_stack_p50) goto loc_0045C90A;
    goto loc_0045C996;
loc_0045CC08:
    local_rdi = (local_rsi) - (local_r15);
    v_stack_p30 = local_rdi;
    goto loc_0045C77C;
loc_0045CC24:
    if (Arg4 != 0) goto loc_0045CCF5;
loc_0045CC2D:
    if (2 >= 32) goto loc_0045CC6B;
loc_0045CC33:
    if (2 == 0) goto loc_0045C7DD;
    result = (uint32_t)((1) << (2));
    result = (uint32_t)((result) - 1);
    goto loc_0045C895;
loc_0045CC4D:
    local_rbp = (uint32_t)((1) + 1);
    if (((*(uint32_t *)(v_rip + 0xB68657)) & ((uint32_t)(local_rbp))) == 0) goto loc_0045CD5F;
loc_0045CC5B:
loc_0045CC5D:
    if (!sign_flag) goto loc_0045CA57;
    goto loc_0045CC4D;
loc_0045CC6B:
    Arg1 = (2) >> (5);
    result = (*(uint64_t *)(v_stack_p40)) * (Arg1);
    Arg2 = (2) + (result);
loc_0045CC79:
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x9D3659) + Arg1 * 4) = 0xFFFFFFFFULL;
    Arg3 = (*(uint64_t *)(v_rip + 0x9D3659) + Arg1 * 4) + (4);
    Arg1 = (Arg1) - (1);
    if (condition_is_equal) goto loc_0045CC33;
    goto loc_0045CC79;
loc_0045CC8C:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_r13), Arg2, Arg3, Arg4);
    local_r11 = 0;
    goto loc_0045C906;
loc_0045CC9C:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_r13), Arg2, Arg3, Arg4);
    goto loc_0045CBEA;
loc_0045CCA6:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_r13), (uint8_t)(local_rdi), Arg3, Arg4);
    local_r11 = 0;
    goto loc_0045CAC1;
loc_0045CCB6:
    if (Arg4 != 0) goto loc_0045CDD1;
loc_0045CCBF:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) << ((uint8_t)((uint8_t)(local_rdi))));
    result = (uint32_t)((result) - ((uint32_t)(local_rbp)));
    goto loc_0045CB2A;
loc_0045CCCD:
    if (Arg4 != 0) goto loc_0045CE2C;
loc_0045CCD6:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) << ((uint8_t)((uint8_t)(local_rdi))));
    goto loc_0045CB84;
loc_0045CCE3:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(local_r15), (uint8_t)(result), Arg3, Arg4);
    local_r11 = 0;
    goto loc_0045CA41;
loc_0045CCF5:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(result)));
    result = (uint32_t)((1) << ((uint8_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) - 1);
    result = (uint32_t)((result) << ((uint8_t)(Arg4)));
    Arg2 = (local_rdi) - ((uint32_t)(Arg2));
    Arg3 = (Arg3) + (4);
    goto loc_0045CC2D;
loc_0045CD26:
    *(uint32_t *)(Arg3) = 0xFFFFFFFFULL;
    goto loc_0045C7DD;
loc_0045CD32:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB69D80)))) & (64)) == 0) goto loc_0045C9EF;
    result = KiCheckVpBackingLongSpinWaitHypercall(Arg4, Arg2, Arg3, Arg4);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_0045C9EF;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), Arg2, Arg3, Arg4);
    local_r11 = 0;
    goto loc_0045C9F1;
loc_0045CD5F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB69D53)))) & (64)) == 0) goto loc_0045CC5B;
    result = KiCheckVpBackingLongSpinWaitHypercall((uint32_t)((uint32_t)(local_rbp)), Arg2, Arg3, Arg4);
    local_r11 = 0;
    if ((uint8_t)(result) == 0) goto loc_0045CC5B;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_rbp)), Arg2, Arg3, Arg4);
    local_r11 = 0;
    goto loc_0045CC5D;
loc_0045CD8C:
    result = (*(uint64_t *)(local_r15)) & ((uint32_t)((uint32_t)(local_rbp)));
    *(uint64_t *)(local_r15) = result;
    result = MiAddLockedPageCharge(v_stack_p40, Arg2, Arg3, Arg4);
    local_r11 = 0;
    if ((uint32_t)(result) != 0) goto loc_0045CB48;
    result = MiPfnReferenceCountIsZero(v_stack_p40, (uint32_t)(v_stack_p38), Arg3, Arg4);
    goto loc_0045C986;
loc_0045CDD1:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p38)))) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) << ((uint8_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) - ((uint32_t)(local_rbp)));
    result = (uint32_t)((result) << ((uint8_t)(Arg4)));
    Arg3 = (Arg3) + (4);
    Arg2 = (local_rbp) - ((uint32_t)(Arg2));
    if (Arg2 < 32) goto loc_0045CE1E;
    Arg1 = (Arg2) >> (5);
    result = ((uint32_t)(Arg2)) * (Arg1);
    Arg2 = (Arg2) + (result);
loc_0045CE0E:
    *(uint32_t *)(Arg3) = 0xFFFFFFFFULL;
    Arg3 = (Arg3) + (4);
    Arg1 = (Arg1) - (local_rbp);
    if (condition_is_not_equal) goto loc_0045CE0E;
loc_0045CE1E:
    if (Arg2 == 0) goto loc_0045CB2E;
    goto loc_0045CCBF;
loc_0045CE2C:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p38)))) & (31));
    Arg2 = (uint32_t)((32) - ((uint32_t)(result)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbp))) << ((uint8_t)((uint32_t)(Arg2))));
    result = (uint32_t)((result) - ((uint32_t)(local_rbp)));
    result = (uint32_t)((result) << ((uint8_t)(Arg4)));
    result = (uint32_t)(~(result));
    Arg3 = (Arg3) + (4);
    v_stack_p20 = v_stack_p20;
    Arg2 = (local_rbp) - ((uint32_t)(Arg2));
    if (Arg2 < 32) goto loc_0045CE81;
    v_stack_p20 = v_stack_p20;
    Arg1 = (Arg2) >> (5);
    result = ((uint32_t)(Arg2)) * (Arg1);
    Arg2 = (Arg2) + (result);
loc_0045CE75:
    *(uint32_t *)(Arg3) = 0;
    Arg3 = (Arg3) + (4);
    Arg1 = (Arg1) - (local_rbp);
    if (condition_is_not_equal) goto loc_0045CE75;
loc_0045CE81:
    if (Arg2 == 0) goto loc_0045CB88;
    goto loc_0045CCD6;
loc_0045CE8F:
    goto loc_0045C621;
loc_0045CE97:
    goto loc_0045CB2E;
loc_0045CEA1:
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    goto loc_0045C7B3;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045C560&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
