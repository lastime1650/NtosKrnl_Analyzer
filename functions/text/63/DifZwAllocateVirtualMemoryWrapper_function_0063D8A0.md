# DifZwAllocateVirtualMemoryWrapper

- RVA: `0x0063D8A0`–`0x0063DA47` (길이 `423` bytes)
- VA: `0x000000014063D8A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `122`개 명령, `423/423` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063D8E6` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063D90E` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063D956` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063D97C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063D995` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063D9B5` → [ZwAllocateVirtualMemory](../6A/ZwAllocateVirtualMemory_function_006AD3D0.md) (function, `0x006AD3D0`)
- `0x0063D9E1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063DA07` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063DA20` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063D91E` → RVA `0x00F048B8` (`.data`; read)
- `0x0063D943` → RVA `0x00F04980` (`.data`; read)
- `0x0063D94F` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063D8A0  48 8B C4                        mov rax, rsp
0063D8A3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0063D8A7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0063D8AB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0063D8AF  48 89 48 08                     mov qword ptr [rax + 8], rcx
0063D8B3  55                              push rbp
0063D8B4  41 54                           push r12
0063D8B6  41 55                           push r13
0063D8B8  41 56                           push r14
0063D8BA  41 57                           push r15
0063D8BC  48 8B EC                        mov rbp, rsp
0063D8BF  48 83 EC 70                     sub rsp, 0x70
0063D8C3  0F 57 C0                        xorps xmm0, xmm0
0063D8C6  33 C0                           xor eax, eax
0063D8C8  B9 90 00 00 00                  mov ecx, 0x90
0063D8CD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063D8D1  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0063D8D5  4D 8B F9                        mov r15, r9
0063D8D8  4D 8B E0                        mov r12, r8
0063D8DB  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063D8DF  4C 8B EA                        mov r13, rdx
0063D8E2  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063D8E6  E8 49 81 E5 FF                  call 0x140495a34
0063D8EB  4C 8B F0                        mov r14, rax
0063D8EE  48 85 C0                        test rax, rax
0063D8F1  0F 84 A3 00 00 00               je 0x14063d99a
0063D8F7  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
0063D8FA  F6 C1 18                        test cl, 0x18
0063D8FD  74 0A                           je 0x14063d909
0063D8FF  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063D903  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
0063D907  EB 0E                           jmp 0x14063d917
0063D909  F6 C1 04                        test cl, 4
0063D90C  74 09                           je 0x14063d917
0063D90E  E8 F5 62 E9 FF                  call 0x1404d3c08
0063D913  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0063D917  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0063D91B  40 32 F6                        xor sil, sil
0063D91E  40 38 35 93 6F 8C 00            cmp byte ptr [rip + 0x8c6f93], sil
0063D925  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0063D929  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
0063D92C  89 45 CC                        mov dword ptr [rbp - 0x34], eax
0063D92F  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0063D932  89 45 C8                        mov dword ptr [rbp - 0x38], eax
0063D935  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
0063D939  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
0063D93D  4C 89 7D D0                     mov qword ptr [rbp - 0x30], r15
0063D941  75 0C                           jne 0x14063d94f
0063D943  F7 05 33 70 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7033], 0x800
0063D94D  74 13                           je 0x14063d962
0063D94F  48 8D 0D 2A 65 8C 00            lea rcx, [rip + 0x8c652a]
0063D956  E8 C5 8C BD FF                  call 0x140216620
0063D95B  40 8A F0                        mov sil, al
0063D95E  84 C0                           test al, al
0063D960  74 38                           je 0x14063d99a
0063D962  49 8D 7E 20                     lea rdi, [r14 + 0x20]
0063D966  48 8B 1F                        mov rbx, qword ptr [rdi]
0063D969  EB 19                           jmp 0x14063d984
0063D96B  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063D96F  48 85 C0                        test rax, rax
0063D972  74 0D                           je 0x14063d981
0063D974  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063D978  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0063D97C  E8 4F D1 07 00                  call 0x1406baad0
0063D981  48 8B 1B                        mov rbx, qword ptr [rbx]
0063D984  48 3B DF                        cmp rbx, rdi
0063D987  75 E2                           jne 0x14063d96b
0063D989  40 84 F6                        test sil, sil
0063D98C  74 0C                           je 0x14063d99a
0063D98E  48 8D 0D EB 64 8C 00            lea rcx, [rip + 0x8c64eb]
0063D995  E8 E6 C4 D0 FF                  call 0x140349e80
0063D99A  8B 45 58                        mov eax, dword ptr [rbp + 0x58]
0063D99D  4D 8B CF                        mov r9, r15
0063D9A0  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0063D9A4  4D 8B C4                        mov r8, r12
0063D9A7  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
0063D9AB  49 8B D5                        mov rdx, r13
0063D9AE  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
0063D9B1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0063D9B5  E8 16 FA 06 00                  call 0x1406ad3d0
0063D9BA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063D9BD  4D 85 F6                        test r14, r14
0063D9C0  74 63                           je 0x14063da25
0063D9C2  40 32 FF                        xor dil, dil
0063D9C5  40 38 3D EC 6E 8C 00            cmp byte ptr [rip + 0x8c6eec], dil
0063D9CC  75 0C                           jne 0x14063d9da
0063D9CE  F7 05 A8 6F 8C 00 00 08 00 00   test dword ptr [rip + 0x8c6fa8], 0x800
0063D9D8  74 13                           je 0x14063d9ed
0063D9DA  48 8D 0D 9F 64 8C 00            lea rcx, [rip + 0x8c649f]
0063D9E1  E8 3A 8C BD FF                  call 0x140216620
0063D9E6  40 8A F8                        mov dil, al
0063D9E9  84 C0                           test al, al
0063D9EB  74 38                           je 0x14063da25
0063D9ED  49 8D 76 30                     lea rsi, [r14 + 0x30]
0063D9F1  48 8B 1E                        mov rbx, qword ptr [rsi]
0063D9F4  EB 19                           jmp 0x14063da0f
0063D9F6  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063D9FA  48 85 C0                        test rax, rax
0063D9FD  74 0D                           je 0x14063da0c
0063D9FF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063DA03  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0063DA07  E8 C4 D0 07 00                  call 0x1406baad0
0063DA0C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063DA0F  48 3B DE                        cmp rbx, rsi
0063DA12  75 E2                           jne 0x14063d9f6
0063DA14  40 84 FF                        test dil, dil
0063DA17  74 0C                           je 0x14063da25
0063DA19  48 8D 0D 60 64 8C 00            lea rcx, [rip + 0x8c6460]
0063DA20  E8 5B C4 D0 FF                  call 0x140349e80
0063DA25  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063DA28  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0063DA2D  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0063DA31  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0063DA35  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0063DA39  49 8B E3                        mov rsp, r11
0063DA3C  41 5F                           pop r15
0063DA3E  41 5E                           pop r14
0063DA40  41 5D                           pop r13
0063DA42  41 5C                           pop r12
0063DA44  5D                              pop rbp
0063DA45  C3                              ret
0063DA46  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwAllocateVirtualMemoryWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(144, a2, a3, a4);
    if (result == 0) goto loc_0063D99A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063D909;
    v_stack_m68 = v_stack_p0;
    goto loc_0063D917;
loc_0063D909:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m5C = (unsigned int)((unsigned int)(a5));
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    v_stack_m58 = a4;
    if ((*(unsigned __int8 *)(v_rip + 9203603)) != 0) goto loc_0063D94F;
    if (((*(unsigned int *)(v_rip + 9203763)) & (0x800ULL)) == 0) goto loc_0063D962;
loc_0063D94F:
    result = ExAcquireRundownProtection(v_rip + 9200938, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063D99A;
loc_0063D962:
    goto loc_0063D984;
loc_0063D96B:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063D984:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063D96B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9200875;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m70 = (unsigned int)((unsigned int)(a6));
    v_stack_m78 = (unsigned int)((unsigned int)(a5));
    result = ZwAllocateVirtualMemory(v_stack_p8, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063DA25;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9203436)) != 0) goto loc_0063D9DA;
    if (((*(unsigned int *)(v_rip + 9203624)) & (0x800ULL)) == 0) goto loc_0063D9ED;
loc_0063D9DA:
    result = ExAcquireRundownProtection(v_rip + 9200799, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063DA25;
loc_0063D9ED:
    goto loc_0063DA0F;
loc_0063D9F6:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063DA0F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_0063D9F6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9200736;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwAllocateVirtualMemoryWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(144, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0063D99A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063D909;
    v_stack_m68 = v_stack_p0;
    goto loc_0063D917;
loc_0063D909:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m5C = (uint32_t)((uint32_t)(Arg5));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    v_stack_m58 = Arg4;
    if ((*(uint8_t *)(v_rip + 0x8C6F93)) != 0) goto loc_0063D94F;
    if (((*(uint32_t *)(v_rip + 0x8C7033)) & (0x800ULL)) == 0) goto loc_0063D962;
loc_0063D94F:
    result = ExAcquireRundownProtection(v_rip + 9200938, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063D99A;
loc_0063D962:
    goto loc_0063D984;
loc_0063D96B:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063D984:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063D96B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9200875;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m70 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m78 = (uint32_t)((uint32_t)(Arg5));
    result = ZwAllocateVirtualMemory(v_stack_p8, Arg2, Arg3, Arg4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063DA25;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C6EEC)) != 0) goto loc_0063D9DA;
    if (((*(uint32_t *)(v_rip + 0x8C6FA8)) & (0x800ULL)) == 0) goto loc_0063D9ED;
loc_0063D9DA:
    result = ExAcquireRundownProtection(v_rip + 9200799, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0063DA25;
loc_0063D9ED:
    goto loc_0063DA0F;
loc_0063D9F6:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0063DA0F:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_0063D9F6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9200736;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063D8A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063D8A0[BB_0063D8A0]
  bb_0063D8F7[BB_0063D8F7]
  bb_0063D8FF[BB_0063D8FF]
  bb_0063D909[BB_0063D909]
  bb_0063D90E[BB_0063D90E]
  bb_0063D917[BB_0063D917]
  bb_0063D943[BB_0063D943]
  bb_0063D94F[BB_0063D94F]
  bb_0063D962[BB_0063D962]
  bb_0063D96B[BB_0063D96B]
  bb_0063D974[BB_0063D974]
  bb_0063D981[BB_0063D981]
  bb_0063D984[BB_0063D984]
  bb_0063D989[BB_0063D989]
  bb_0063D98E[BB_0063D98E]
  bb_0063D99A[BB_0063D99A]
  bb_0063D9C2[BB_0063D9C2]
  bb_0063D9CE[BB_0063D9CE]
  bb_0063D9DA[BB_0063D9DA]
  bb_0063D9ED[BB_0063D9ED]
  bb_0063D9F6[BB_0063D9F6]
  bb_0063D9FF[BB_0063D9FF]
  bb_0063DA0C[BB_0063DA0C]
  bb_0063DA0F[BB_0063DA0F]
  bb_0063DA14[BB_0063DA14]
  bb_0063DA19[BB_0063DA19]
  bb_0063DA25[BB_0063DA25]
  bb_0063DA46[BB_0063DA46]
  bb_0063D8A0 -->|branch| bb_0063D99A
  bb_0063D8A0 -->|fallthrough| bb_0063D8F7
  bb_0063D8F7 -->|branch| bb_0063D909
  bb_0063D8F7 -->|fallthrough| bb_0063D8FF
  bb_0063D8FF -->|branch| bb_0063D917
  bb_0063D909 -->|branch| bb_0063D917
  bb_0063D909 -->|fallthrough| bb_0063D90E
  bb_0063D90E -->|flow| bb_0063D917
  bb_0063D917 -->|branch| bb_0063D94F
  bb_0063D917 -->|fallthrough| bb_0063D943
  bb_0063D943 -->|branch| bb_0063D962
  bb_0063D943 -->|fallthrough| bb_0063D94F
  bb_0063D94F -->|branch| bb_0063D99A
  bb_0063D94F -->|fallthrough| bb_0063D962
  bb_0063D962 -->|branch| bb_0063D984
  bb_0063D96B -->|branch| bb_0063D981
  bb_0063D96B -->|fallthrough| bb_0063D974
  bb_0063D974 -->|flow| bb_0063D981
  bb_0063D981 -->|flow| bb_0063D984
  bb_0063D984 -->|branch| bb_0063D96B
  bb_0063D984 -->|fallthrough| bb_0063D989
  bb_0063D989 -->|branch| bb_0063D99A
  bb_0063D989 -->|fallthrough| bb_0063D98E
  bb_0063D98E -->|flow| bb_0063D99A
  bb_0063D99A -->|branch| bb_0063DA25
  bb_0063D99A -->|fallthrough| bb_0063D9C2
  bb_0063D9C2 -->|branch| bb_0063D9DA
  bb_0063D9C2 -->|fallthrough| bb_0063D9CE
  bb_0063D9CE -->|branch| bb_0063D9ED
  bb_0063D9CE -->|fallthrough| bb_0063D9DA
  bb_0063D9DA -->|branch| bb_0063DA25
  bb_0063D9DA -->|fallthrough| bb_0063D9ED
  bb_0063D9ED -->|branch| bb_0063DA0F
  bb_0063D9F6 -->|branch| bb_0063DA0C
  bb_0063D9F6 -->|fallthrough| bb_0063D9FF
  bb_0063D9FF -->|flow| bb_0063DA0C
  bb_0063DA0C -->|flow| bb_0063DA0F
  bb_0063DA0F -->|branch| bb_0063D9F6
  bb_0063DA0F -->|fallthrough| bb_0063DA14
  bb_0063DA14 -->|branch| bb_0063DA25
  bb_0063DA14 -->|fallthrough| bb_0063DA19
  bb_0063DA19 -->|flow| bb_0063DA25
```
