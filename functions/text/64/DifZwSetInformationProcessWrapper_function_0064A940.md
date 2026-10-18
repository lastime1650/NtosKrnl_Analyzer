# DifZwSetInformationProcessWrapper

- RVA: `0x0064A940`–`0x0064AAC5` (길이 `389` bytes)
- VA: `0x000000014064A940`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2B7C`
- 디코드: `112`개 명령, `389/389` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0064A980` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0064A9A6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0064A9E2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064AA08` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064AA21` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0064AA33` → [ZwSetInformationProcess](../6A/ZwSetInformationProcess_function_006AD450.md) (function, `0x006AD450`)
- `0x0064AA5F` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0064AA85` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0064AA9E` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0064A9B6` → RVA `0x00F048B8` (`.data`; read)
- `0x0064A9CF` → RVA `0x00F04980` (`.data`; read)
- `0x0064A9DB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064A940  48 8B C4                        mov rax, rsp
0064A943  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0064A947  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0064A94B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0064A94F  48 89 48 08                     mov qword ptr [rax + 8], rcx
0064A953  55                              push rbp
0064A954  41 54                           push r12
0064A956  41 55                           push r13
0064A958  41 56                           push r14
0064A95A  41 57                           push r15
0064A95C  48 8B EC                        mov rbp, rsp
0064A95F  48 83 EC 50                     sub rsp, 0x50
0064A963  0F 57 C0                        xorps xmm0, xmm0
0064A966  B9 0E 00 00 00                  mov ecx, 0xe
0064A96B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0064A96F  45 8B F9                        mov r15d, r9d
0064A972  4D 8B E0                        mov r12, r8
0064A975  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0064A979  44 8B EA                        mov r13d, edx
0064A97C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
0064A980  E8 AF B0 E4 FF                  call 0x140495a34
0064A985  48 8B F0                        mov rsi, rax
0064A988  48 85 C0                        test rax, rax
0064A98B  0F 84 95 00 00 00               je 0x14064aa26
0064A991  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0064A994  A8 18                           test al, 0x18
0064A996  74 0A                           je 0x14064a9a2
0064A998  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0064A99C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0064A9A0  EB 0D                           jmp 0x14064a9af
0064A9A2  A8 04                           test al, 4
0064A9A4  74 09                           je 0x14064a9af
0064A9A6  E8 5D 92 E8 FF                  call 0x1404d3c08
0064A9AB  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0064A9AF  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0064A9B3  45 32 F6                        xor r14b, r14b
0064A9B6  44 38 35 FB 9E 8B 00            cmp byte ptr [rip + 0x8b9efb], r14b
0064A9BD  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0064A9C1  44 89 6D E8                     mov dword ptr [rbp - 0x18], r13d
0064A9C5  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0064A9C9  44 89 7D D8                     mov dword ptr [rbp - 0x28], r15d
0064A9CD  75 0C                           jne 0x14064a9db
0064A9CF  F7 05 A7 9F 8B 00 00 08 00 00   test dword ptr [rip + 0x8b9fa7], 0x800
0064A9D9  74 13                           je 0x14064a9ee
0064A9DB  48 8D 0D 9E 94 8B 00            lea rcx, [rip + 0x8b949e]
0064A9E2  E8 39 BC BC FF                  call 0x140216620
0064A9E7  44 8A F0                        mov r14b, al
0064A9EA  84 C0                           test al, al
0064A9EC  74 38                           je 0x14064aa26
0064A9EE  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0064A9F2  48 8B 1F                        mov rbx, qword ptr [rdi]
0064A9F5  EB 19                           jmp 0x14064aa10
0064A9F7  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064A9FB  48 85 C0                        test rax, rax
0064A9FE  74 0D                           je 0x14064aa0d
0064AA00  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064AA04  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064AA08  E8 C3 00 07 00                  call 0x1406baad0
0064AA0D  48 8B 1B                        mov rbx, qword ptr [rbx]
0064AA10  48 3B DF                        cmp rbx, rdi
0064AA13  75 E2                           jne 0x14064a9f7
0064AA15  45 84 F6                        test r14b, r14b
0064AA18  74 0C                           je 0x14064aa26
0064AA1A  48 8D 0D 5F 94 8B 00            lea rcx, [rip + 0x8b945f]
0064AA21  E8 5A F4 CF FF                  call 0x140349e80
0064AA26  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
0064AA2A  45 8B CF                        mov r9d, r15d
0064AA2D  4D 8B C4                        mov r8, r12
0064AA30  41 8B D5                        mov edx, r13d
0064AA33  E8 18 2A 06 00                  call 0x1406ad450
0064AA38  89 45 F8                        mov dword ptr [rbp - 8], eax
0064AA3B  48 85 F6                        test rsi, rsi
0064AA3E  74 63                           je 0x14064aaa3
0064AA40  40 32 FF                        xor dil, dil
0064AA43  40 38 3D 6E 9E 8B 00            cmp byte ptr [rip + 0x8b9e6e], dil
0064AA4A  75 0C                           jne 0x14064aa58
0064AA4C  F7 05 2A 9F 8B 00 00 08 00 00   test dword ptr [rip + 0x8b9f2a], 0x800
0064AA56  74 13                           je 0x14064aa6b
0064AA58  48 8D 0D 21 94 8B 00            lea rcx, [rip + 0x8b9421]
0064AA5F  E8 BC BB BC FF                  call 0x140216620
0064AA64  40 8A F8                        mov dil, al
0064AA67  84 C0                           test al, al
0064AA69  74 38                           je 0x14064aaa3
0064AA6B  48 83 C6 30                     add rsi, 0x30
0064AA6F  48 8B 1E                        mov rbx, qword ptr [rsi]
0064AA72  EB 19                           jmp 0x14064aa8d
0064AA74  48 8D 43 F0                     lea rax, [rbx - 0x10]
0064AA78  48 85 C0                        test rax, rax
0064AA7B  74 0D                           je 0x14064aa8a
0064AA7D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0064AA81  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0064AA85  E8 46 00 07 00                  call 0x1406baad0
0064AA8A  48 8B 1B                        mov rbx, qword ptr [rbx]
0064AA8D  48 3B DE                        cmp rbx, rsi
0064AA90  75 E2                           jne 0x14064aa74
0064AA92  40 84 FF                        test dil, dil
0064AA95  74 0C                           je 0x14064aaa3
0064AA97  48 8D 0D E2 93 8B 00            lea rcx, [rip + 0x8b93e2]
0064AA9E  E8 DD F3 CF FF                  call 0x140349e80
0064AAA3  8B 45 F8                        mov eax, dword ptr [rbp - 8]
0064AAA6  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0064AAAB  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0064AAAF  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0064AAB3  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0064AAB7  49 8B E3                        mov rsp, r11
0064AABA  41 5F                           pop r15
0064AABC  41 5E                           pop r14
0064AABE  41 5D                           pop r13
0064AAC0  41 5C                           pop r12
0064AAC2  5D                              pop rbp
0064AAC3  C3                              ret
0064AAC4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwSetInformationProcessWrapper(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(14, a2, a3, a4);
    if (result == 0) goto loc_0064AA26;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0064A9A2;
    v_stack_m58 = v_stack_p0;
    goto loc_0064A9AF;
loc_0064A9A2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (unsigned int)((unsigned int)(a2));
    v_stack_m48 = a3;
    v_stack_m50 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9150203)) != 0) goto loc_0064A9DB;
    if (((*(unsigned int *)(v_rip + 9150375)) & (0x800ULL)) == 0) goto loc_0064A9EE;
loc_0064A9DB:
    result = ExAcquireRundownProtection(v_rip + 9147550, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0064AA26;
loc_0064A9EE:
    goto loc_0064AA10;
loc_0064A9F7:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0064AA10:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0064A9F7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9147487;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = ZwSetInformationProcess(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_0064AAA3;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9150062)) != 0) goto loc_0064AA58;
    if (((*(unsigned int *)(v_rip + 9150250)) & (0x800ULL)) == 0) goto loc_0064AA6B;
loc_0064AA58:
    result = ExAcquireRundownProtection(v_rip + 9147425, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_0064AAA3;
loc_0064AA6B:
    v_rsi = (result) + (48);
    goto loc_0064AA8D;
loc_0064AA74:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_0064AA8D:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0064AA74;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9147362;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwSetInformationProcessWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(14, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_0064AA26;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0064A9A2;
    v_stack_m58 = v_stack_p0;
    goto loc_0064A9AF;
loc_0064A9A2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m48 = Arg3;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8B9EFB)) != 0) goto loc_0064A9DB;
    if (((*(uint32_t *)(v_rip + 0x8B9FA7)) & (0x800ULL)) == 0) goto loc_0064A9EE;
loc_0064A9DB:
    result = ExAcquireRundownProtection(v_rip + 9147550, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_0064AA26;
loc_0064A9EE:
    goto loc_0064AA10;
loc_0064A9F7:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_0064AA10:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0064A9F7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9147487;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = ZwSetInformationProcess(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_0064AAA3;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8B9E6E)) != 0) goto loc_0064AA58;
    if (((*(uint32_t *)(v_rip + 0x8B9F2A)) & (0x800ULL)) == 0) goto loc_0064AA6B;
loc_0064AA58:
    result = ExAcquireRundownProtection(v_rip + 9147425, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_0064AAA3;
loc_0064AA6B:
    local_rsi = (result) + (48);
    goto loc_0064AA8D;
loc_0064AA74:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_0064AA8D:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0064AA74;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9147362;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064A940&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064A940[BB_0064A940]
  bb_0064A991[BB_0064A991]
  bb_0064A998[BB_0064A998]
  bb_0064A9A2[BB_0064A9A2]
  bb_0064A9A6[BB_0064A9A6]
  bb_0064A9AF[BB_0064A9AF]
  bb_0064A9CF[BB_0064A9CF]
  bb_0064A9DB[BB_0064A9DB]
  bb_0064A9EE[BB_0064A9EE]
  bb_0064A9F7[BB_0064A9F7]
  bb_0064AA00[BB_0064AA00]
  bb_0064AA0D[BB_0064AA0D]
  bb_0064AA10[BB_0064AA10]
  bb_0064AA15[BB_0064AA15]
  bb_0064AA1A[BB_0064AA1A]
  bb_0064AA26[BB_0064AA26]
  bb_0064AA40[BB_0064AA40]
  bb_0064AA4C[BB_0064AA4C]
  bb_0064AA58[BB_0064AA58]
  bb_0064AA6B[BB_0064AA6B]
  bb_0064AA74[BB_0064AA74]
  bb_0064AA7D[BB_0064AA7D]
  bb_0064AA8A[BB_0064AA8A]
  bb_0064AA8D[BB_0064AA8D]
  bb_0064AA92[BB_0064AA92]
  bb_0064AA97[BB_0064AA97]
  bb_0064AAA3[BB_0064AAA3]
  bb_0064AAC4[BB_0064AAC4]
  bb_0064A940 -->|branch| bb_0064AA26
  bb_0064A940 -->|fallthrough| bb_0064A991
  bb_0064A991 -->|branch| bb_0064A9A2
  bb_0064A991 -->|fallthrough| bb_0064A998
  bb_0064A998 -->|branch| bb_0064A9AF
  bb_0064A9A2 -->|branch| bb_0064A9AF
  bb_0064A9A2 -->|fallthrough| bb_0064A9A6
  bb_0064A9A6 -->|flow| bb_0064A9AF
  bb_0064A9AF -->|branch| bb_0064A9DB
  bb_0064A9AF -->|fallthrough| bb_0064A9CF
  bb_0064A9CF -->|branch| bb_0064A9EE
  bb_0064A9CF -->|fallthrough| bb_0064A9DB
  bb_0064A9DB -->|branch| bb_0064AA26
  bb_0064A9DB -->|fallthrough| bb_0064A9EE
  bb_0064A9EE -->|branch| bb_0064AA10
  bb_0064A9F7 -->|branch| bb_0064AA0D
  bb_0064A9F7 -->|fallthrough| bb_0064AA00
  bb_0064AA00 -->|flow| bb_0064AA0D
  bb_0064AA0D -->|flow| bb_0064AA10
  bb_0064AA10 -->|branch| bb_0064A9F7
  bb_0064AA10 -->|fallthrough| bb_0064AA15
  bb_0064AA15 -->|branch| bb_0064AA26
  bb_0064AA15 -->|fallthrough| bb_0064AA1A
  bb_0064AA1A -->|flow| bb_0064AA26
  bb_0064AA26 -->|branch| bb_0064AAA3
  bb_0064AA26 -->|fallthrough| bb_0064AA40
  bb_0064AA40 -->|branch| bb_0064AA58
  bb_0064AA40 -->|fallthrough| bb_0064AA4C
  bb_0064AA4C -->|branch| bb_0064AA6B
  bb_0064AA4C -->|fallthrough| bb_0064AA58
  bb_0064AA58 -->|branch| bb_0064AAA3
  bb_0064AA58 -->|fallthrough| bb_0064AA6B
  bb_0064AA6B -->|branch| bb_0064AA8D
  bb_0064AA74 -->|branch| bb_0064AA8A
  bb_0064AA74 -->|fallthrough| bb_0064AA7D
  bb_0064AA7D -->|flow| bb_0064AA8A
  bb_0064AA8A -->|flow| bb_0064AA8D
  bb_0064AA8D -->|branch| bb_0064AA74
  bb_0064AA8D -->|fallthrough| bb_0064AA92
  bb_0064AA92 -->|branch| bb_0064AAA3
  bb_0064AA92 -->|fallthrough| bb_0064AA97
  bb_0064AA97 -->|flow| bb_0064AAA3
```
