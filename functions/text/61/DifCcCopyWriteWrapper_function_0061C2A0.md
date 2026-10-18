# DifCcCopyWriteWrapper

- RVA: `0x0061C2A0`–`0x0061C43C` (길이 `412` bytes)
- VA: `0x000000014061C2A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `117`개 명령, `412/412` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0061C2E0` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061C306` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061C34A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C370` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061C389` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061C3AA` → [CcCopyWriteEx](../3C/CcCopyWriteEx_function_003CA4F0.md) (function, `0x003CA4F0`)
- `0x0061C3D6` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061C3FC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061C415` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061C316` → RVA `0x00F048B8` (`.data`; read)
- `0x0061C337` → RVA `0x00F04980` (`.data`; read)
- `0x0061C343` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061C2A0  48 8B C4                        mov rax, rsp
0061C2A3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0061C2A7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0061C2AB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0061C2AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0061C2B3  55                              push rbp
0061C2B4  41 54                           push r12
0061C2B6  41 55                           push r13
0061C2B8  41 56                           push r14
0061C2BA  41 57                           push r15
0061C2BC  48 8B EC                        mov rbp, rsp
0061C2BF  48 83 EC 60                     sub rsp, 0x60
0061C2C3  0F 57 C0                        xorps xmm0, xmm0
0061C2C6  B9 B2 01 00 00                  mov ecx, 0x1b2
0061C2CB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0061C2CF  45 8A F9                        mov r15b, r9b
0061C2D2  45 8B E0                        mov r12d, r8d
0061C2D5  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0061C2D9  4C 8B EA                        mov r13, rdx
0061C2DC  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0061C2E0  E8 4F 97 E7 FF                  call 0x140495a34
0061C2E5  48 8B F0                        mov rsi, rax
0061C2E8  48 85 C0                        test rax, rax
0061C2EB  0F 84 9D 00 00 00               je 0x14061c38e
0061C2F1  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061C2F4  A8 18                           test al, 0x18
0061C2F6  74 0A                           je 0x14061c302
0061C2F8  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0061C2FC  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0061C300  EB 0D                           jmp 0x14061c30f
0061C302  A8 04                           test al, 4
0061C304  74 09                           je 0x14061c30f
0061C306  E8 FD 78 EB FF                  call 0x1404d3c08
0061C30B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0061C30F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0061C313  45 32 F6                        xor r14b, r14b
0061C316  44 38 35 9B 85 8E 00            cmp byte ptr [rip + 0x8e859b], r14b
0061C31D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0061C321  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0061C325  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0061C329  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0061C32D  44 89 65 E4                     mov dword ptr [rbp - 0x1c], r12d
0061C331  44 88 7D E0                     mov byte ptr [rbp - 0x20], r15b
0061C335  75 0C                           jne 0x14061c343
0061C337  F7 05 3F 86 8E 00 00 08 00 00   test dword ptr [rip + 0x8e863f], 0x800
0061C341  74 13                           je 0x14061c356
0061C343  48 8D 0D 36 7B 8E 00            lea rcx, [rip + 0x8e7b36]
0061C34A  E8 D1 A2 BF FF                  call 0x140216620
0061C34F  44 8A F0                        mov r14b, al
0061C352  84 C0                           test al, al
0061C354  74 38                           je 0x14061c38e
0061C356  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0061C35A  48 8B 1F                        mov rbx, qword ptr [rdi]
0061C35D  EB 19                           jmp 0x14061c378
0061C35F  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C363  48 85 C0                        test rax, rax
0061C366  74 0D                           je 0x14061c375
0061C368  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C36C  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061C370  E8 5B E7 09 00                  call 0x1406baad0
0061C375  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C378  48 3B DF                        cmp rbx, rdi
0061C37B  75 E2                           jne 0x14061c35f
0061C37D  45 84 F6                        test r14b, r14b
0061C380  74 0C                           je 0x14061c38e
0061C382  48 8D 0D F7 7A 8E 00            lea rcx, [rip + 0x8e7af7]
0061C389  E8 F2 DA D2 FF                  call 0x140349e80
0061C38E  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0061C392  45 8A CF                        mov r9b, r15b
0061C395  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
0061C39B  45 8B C4                        mov r8d, r12d
0061C39E  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0061C3A2  49 8B D5                        mov rdx, r13
0061C3A5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061C3AA  E8 41 E1 DA FF                  call 0x1403ca4f0
0061C3AF  88 45 F8                        mov byte ptr [rbp - 8], al
0061C3B2  48 85 F6                        test rsi, rsi
0061C3B5  74 63                           je 0x14061c41a
0061C3B7  40 32 FF                        xor dil, dil
0061C3BA  40 38 3D F7 84 8E 00            cmp byte ptr [rip + 0x8e84f7], dil
0061C3C1  75 0C                           jne 0x14061c3cf
0061C3C3  F7 05 B3 85 8E 00 00 08 00 00   test dword ptr [rip + 0x8e85b3], 0x800
0061C3CD  74 13                           je 0x14061c3e2
0061C3CF  48 8D 0D AA 7A 8E 00            lea rcx, [rip + 0x8e7aaa]
0061C3D6  E8 45 A2 BF FF                  call 0x140216620
0061C3DB  40 8A F8                        mov dil, al
0061C3DE  84 C0                           test al, al
0061C3E0  74 38                           je 0x14061c41a
0061C3E2  48 83 C6 30                     add rsi, 0x30
0061C3E6  48 8B 1E                        mov rbx, qword ptr [rsi]
0061C3E9  EB 19                           jmp 0x14061c404
0061C3EB  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061C3EF  48 85 C0                        test rax, rax
0061C3F2  74 0D                           je 0x14061c401
0061C3F4  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061C3F8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0061C3FC  E8 CF E6 09 00                  call 0x1406baad0
0061C401  48 8B 1B                        mov rbx, qword ptr [rbx]
0061C404  48 3B DE                        cmp rbx, rsi
0061C407  75 E2                           jne 0x14061c3eb
0061C409  40 84 FF                        test dil, dil
0061C40C  74 0C                           je 0x14061c41a
0061C40E  48 8D 0D 6B 7A 8E 00            lea rcx, [rip + 0x8e7a6b]
0061C415  E8 66 DA D2 FF                  call 0x140349e80
0061C41A  8A 45 F8                        mov al, byte ptr [rbp - 8]
0061C41D  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
0061C422  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0061C426  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0061C42A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0061C42E  49 8B E3                        mov rsp, r11
0061C431  41 5F                           pop r15
0061C433  41 5E                           pop r14
0061C435  41 5D                           pop r13
0061C437  41 5C                           pop r12
0061C439  5D                              pop rbp
0061C43A  C3                              ret
0061C43B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifCcCopyWriteWrapper(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int8 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m44;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(434, a2, a3, a4);
    if (result == 0) goto loc_0061C38E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061C302;
    v_stack_m58 = v_stack_p0;
    goto loc_0061C30F;
loc_0061C302:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = a5;
    v_stack_m40 = a2;
    v_stack_m44 = (unsigned int)((unsigned int)(a3));
    v_stack_m48 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9340315)) != 0) goto loc_0061C343;
    if (((*(unsigned int *)(v_rip + 9340479)) & (0x800ULL)) == 0) goto loc_0061C356;
loc_0061C343:
    result = ExAcquireRundownProtection(v_rip + 9337654, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061C38E;
loc_0061C356:
    goto loc_0061C378;
loc_0061C35F:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061C378:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061C35F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9337591;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = a5;
    result = CcCopyWriteEx(v_stack_p8, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m30 = (unsigned __int8)(result);
    if (result == 0) goto loc_0061C41A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9340151)) != 0) goto loc_0061C3CF;
    if (((*(unsigned int *)(v_rip + 9340339)) & (0x800ULL)) == 0) goto loc_0061C3E2;
loc_0061C3CF:
    result = ExAcquireRundownProtection(v_rip + 9337514, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061C41A;
loc_0061C3E2:
    v_rsi = (result) + (48);
    goto loc_0061C404;
loc_0061C3EB:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
loc_0061C404:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061C3EB;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9337451;
        result = ExReleaseRundownProtection(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    }
    return v_stack_m30;
}
```

## 5. (Beta) C Style

```c
int64_t DifCcCopyWriteWrapper(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint8_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m44;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(434, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0061C38E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061C302;
    v_stack_m58 = v_stack_p0;
    goto loc_0061C30F;
loc_0061C302:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = Arg5;
    v_stack_m40 = Arg2;
    v_stack_m44 = (uint32_t)((uint32_t)(Arg3));
    v_stack_m48 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8E859B)) != 0) goto loc_0061C343;
    if (((*(uint32_t *)(v_rip + 0x8E863F)) & (0x800ULL)) == 0) goto loc_0061C356;
loc_0061C343:
    result = ExAcquireRundownProtection(v_rip + 9337654, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061C38E;
loc_0061C356:
    goto loc_0061C378;
loc_0061C35F:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0061C378:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061C35F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9337591;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = Arg5;
    result = CcCopyWriteEx(v_stack_p8, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m30 = (uint8_t)(result);
    if (result == 0) goto loc_0061C41A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E84F7)) != 0) goto loc_0061C3CF;
    if (((*(uint32_t *)(v_rip + 0x8E85B3)) & (0x800ULL)) == 0) goto loc_0061C3E2;
loc_0061C3CF:
    result = ExAcquireRundownProtection(v_rip + 9337514, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0061C41A;
loc_0061C3E2:
    local_rsi = (result) + (48);
    goto loc_0061C404;
loc_0061C3EB:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
loc_0061C404:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061C3EB;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9337451;
        result = ExReleaseRundownProtection(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    }
    return v_stack_m30;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061C2A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061C2A0[BB_0061C2A0]
  bb_0061C2F1[BB_0061C2F1]
  bb_0061C2F8[BB_0061C2F8]
  bb_0061C302[BB_0061C302]
  bb_0061C306[BB_0061C306]
  bb_0061C30F[BB_0061C30F]
  bb_0061C337[BB_0061C337]
  bb_0061C343[BB_0061C343]
  bb_0061C356[BB_0061C356]
  bb_0061C35F[BB_0061C35F]
  bb_0061C368[BB_0061C368]
  bb_0061C375[BB_0061C375]
  bb_0061C378[BB_0061C378]
  bb_0061C37D[BB_0061C37D]
  bb_0061C382[BB_0061C382]
  bb_0061C38E[BB_0061C38E]
  bb_0061C3B7[BB_0061C3B7]
  bb_0061C3C3[BB_0061C3C3]
  bb_0061C3CF[BB_0061C3CF]
  bb_0061C3E2[BB_0061C3E2]
  bb_0061C3EB[BB_0061C3EB]
  bb_0061C3F4[BB_0061C3F4]
  bb_0061C401[BB_0061C401]
  bb_0061C404[BB_0061C404]
  bb_0061C409[BB_0061C409]
  bb_0061C40E[BB_0061C40E]
  bb_0061C41A[BB_0061C41A]
  bb_0061C43B[BB_0061C43B]
  bb_0061C2A0 -->|branch| bb_0061C38E
  bb_0061C2A0 -->|fallthrough| bb_0061C2F1
  bb_0061C2F1 -->|branch| bb_0061C302
  bb_0061C2F1 -->|fallthrough| bb_0061C2F8
  bb_0061C2F8 -->|branch| bb_0061C30F
  bb_0061C302 -->|branch| bb_0061C30F
  bb_0061C302 -->|fallthrough| bb_0061C306
  bb_0061C306 -->|flow| bb_0061C30F
  bb_0061C30F -->|branch| bb_0061C343
  bb_0061C30F -->|fallthrough| bb_0061C337
  bb_0061C337 -->|branch| bb_0061C356
  bb_0061C337 -->|fallthrough| bb_0061C343
  bb_0061C343 -->|branch| bb_0061C38E
  bb_0061C343 -->|fallthrough| bb_0061C356
  bb_0061C356 -->|branch| bb_0061C378
  bb_0061C35F -->|branch| bb_0061C375
  bb_0061C35F -->|fallthrough| bb_0061C368
  bb_0061C368 -->|flow| bb_0061C375
  bb_0061C375 -->|flow| bb_0061C378
  bb_0061C378 -->|branch| bb_0061C35F
  bb_0061C378 -->|fallthrough| bb_0061C37D
  bb_0061C37D -->|branch| bb_0061C38E
  bb_0061C37D -->|fallthrough| bb_0061C382
  bb_0061C382 -->|flow| bb_0061C38E
  bb_0061C38E -->|branch| bb_0061C41A
  bb_0061C38E -->|fallthrough| bb_0061C3B7
  bb_0061C3B7 -->|branch| bb_0061C3CF
  bb_0061C3B7 -->|fallthrough| bb_0061C3C3
  bb_0061C3C3 -->|branch| bb_0061C3E2
  bb_0061C3C3 -->|fallthrough| bb_0061C3CF
  bb_0061C3CF -->|branch| bb_0061C41A
  bb_0061C3CF -->|fallthrough| bb_0061C3E2
  bb_0061C3E2 -->|branch| bb_0061C404
  bb_0061C3EB -->|branch| bb_0061C401
  bb_0061C3EB -->|fallthrough| bb_0061C3F4
  bb_0061C3F4 -->|flow| bb_0061C401
  bb_0061C401 -->|flow| bb_0061C404
  bb_0061C404 -->|branch| bb_0061C3EB
  bb_0061C404 -->|fallthrough| bb_0061C409
  bb_0061C409 -->|branch| bb_0061C41A
  bb_0061C409 -->|fallthrough| bb_0061C40E
  bb_0061C40E -->|flow| bb_0061C41A
```
