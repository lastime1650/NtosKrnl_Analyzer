# DifZwQueryInformationTransactionManagerWrapper

- RVA: `0x00647A00`–`0x00647B9C` (길이 `412` bytes)
- VA: `0x0000000140647A00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD780`
- 디코드: `118`개 명령, `412/412` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00647A44` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00647A6C` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00647AB0` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647AD6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647AEF` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00647B0A` → [ZwQueryInformationTransactionManager](../6A/ZwQueryInformationTransactionManager_function_006AFC30.md) (function, `0x006AFC30`)
- `0x00647B36` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00647B5C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00647B75` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00647A7C` → RVA `0x00F048B8` (`.data`; read)
- `0x00647A9D` → RVA `0x00F04980` (`.data`; read)
- `0x00647AA9` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00647A00  48 8B C4                        mov rax, rsp
00647A03  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00647A07  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00647A0B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00647A0F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00647A13  55                              push rbp
00647A14  41 54                           push r12
00647A16  41 55                           push r13
00647A18  41 56                           push r14
00647A1A  41 57                           push r15
00647A1C  48 8B EC                        mov rbp, rsp
00647A1F  48 83 EC 70                     sub rsp, 0x70
00647A23  33 C0                           xor eax, eax
00647A25  0F 57 C0                        xorps xmm0, xmm0
00647A28  45 8B F9                        mov r15d, r9d
00647A2B  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00647A2F  4D 8B E0                        mov r12, r8
00647A32  44 8B EA                        mov r13d, edx
00647A35  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00647A39  8D 48 2B                        lea ecx, [rax + 0x2b]
00647A3C  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00647A40  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00647A44  E8 EB DF E4 FF                  call 0x140495a34
00647A49  4C 8B F0                        mov r14, rax
00647A4C  48 85 C0                        test rax, rax
00647A4F  0F 84 9F 00 00 00               je 0x140647af4
00647A55  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00647A58  F6 C1 18                        test cl, 0x18
00647A5B  74 0A                           je 0x140647a67
00647A5D  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00647A61  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
00647A65  EB 0E                           jmp 0x140647a75
00647A67  F6 C1 04                        test cl, 4
00647A6A  74 09                           je 0x140647a75
00647A6C  E8 97 C1 E8 FF                  call 0x1404d3c08
00647A71  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00647A75  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00647A79  40 32 F6                        xor sil, sil
00647A7C  40 38 35 35 CE 8B 00            cmp byte ptr [rip + 0x8bce35], sil
00647A83  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00647A87  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00647A8B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00647A8F  44 89 6D E0                     mov dword ptr [rbp - 0x20], r13d
00647A93  4C 89 65 D8                     mov qword ptr [rbp - 0x28], r12
00647A97  44 89 7D D0                     mov dword ptr [rbp - 0x30], r15d
00647A9B  75 0C                           jne 0x140647aa9
00647A9D  F7 05 D9 CE 8B 00 00 08 00 00   test dword ptr [rip + 0x8bced9], 0x800
00647AA7  74 13                           je 0x140647abc
00647AA9  48 8D 0D D0 C3 8B 00            lea rcx, [rip + 0x8bc3d0]
00647AB0  E8 6B EB BC FF                  call 0x140216620
00647AB5  40 8A F0                        mov sil, al
00647AB8  84 C0                           test al, al
00647ABA  74 38                           je 0x140647af4
00647ABC  49 8D 7E 20                     lea rdi, [r14 + 0x20]
00647AC0  48 8B 1F                        mov rbx, qword ptr [rdi]
00647AC3  EB 19                           jmp 0x140647ade
00647AC5  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647AC9  48 85 C0                        test rax, rax
00647ACC  74 0D                           je 0x140647adb
00647ACE  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647AD2  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00647AD6  E8 F5 2F 07 00                  call 0x1406baad0
00647ADB  48 8B 1B                        mov rbx, qword ptr [rbx]
00647ADE  48 3B DF                        cmp rbx, rdi
00647AE1  75 E2                           jne 0x140647ac5
00647AE3  40 84 F6                        test sil, sil
00647AE6  74 0C                           je 0x140647af4
00647AE8  48 8D 0D 91 C3 8B 00            lea rcx, [rip + 0x8bc391]
00647AEF  E8 8C 23 D0 FF                  call 0x140349e80
00647AF4  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
00647AF8  45 8B CF                        mov r9d, r15d
00647AFB  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00647AFF  4D 8B C4                        mov r8, r12
00647B02  41 8B D5                        mov edx, r13d
00647B05  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00647B0A  E8 21 81 06 00                  call 0x1406afc30
00647B0F  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00647B12  4D 85 F6                        test r14, r14
00647B15  74 63                           je 0x140647b7a
00647B17  40 32 FF                        xor dil, dil
00647B1A  40 38 3D 97 CD 8B 00            cmp byte ptr [rip + 0x8bcd97], dil
00647B21  75 0C                           jne 0x140647b2f
00647B23  F7 05 53 CE 8B 00 00 08 00 00   test dword ptr [rip + 0x8bce53], 0x800
00647B2D  74 13                           je 0x140647b42
00647B2F  48 8D 0D 4A C3 8B 00            lea rcx, [rip + 0x8bc34a]
00647B36  E8 E5 EA BC FF                  call 0x140216620
00647B3B  40 8A F8                        mov dil, al
00647B3E  84 C0                           test al, al
00647B40  74 38                           je 0x140647b7a
00647B42  49 8D 76 30                     lea rsi, [r14 + 0x30]
00647B46  48 8B 1E                        mov rbx, qword ptr [rsi]
00647B49  EB 19                           jmp 0x140647b64
00647B4B  48 8D 43 F0                     lea rax, [rbx - 0x10]
00647B4F  48 85 C0                        test rax, rax
00647B52  74 0D                           je 0x140647b61
00647B54  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00647B58  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00647B5C  E8 6F 2F 07 00                  call 0x1406baad0
00647B61  48 8B 1B                        mov rbx, qword ptr [rbx]
00647B64  48 3B DE                        cmp rbx, rsi
00647B67  75 E2                           jne 0x140647b4b
00647B69  40 84 FF                        test dil, dil
00647B6C  74 0C                           je 0x140647b7a
00647B6E  48 8D 0D 0B C3 8B 00            lea rcx, [rip + 0x8bc30b]
00647B75  E8 06 23 D0 FF                  call 0x140349e80
00647B7A  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
00647B7D  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
00647B82  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00647B86  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00647B8A  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00647B8E  49 8B E3                        mov rsp, r11
00647B91  41 5F                           pop r15
00647B93  41 5E                           pop r14
00647B95  41 5D                           pop r13
00647B97  41 5C                           pop r12
00647B99  5D                              pop rbp
00647B9A  C3                              ret
00647B9B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryInformationTransactionManagerWrapper(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
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
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
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
    result = DifGetAPIThunkContextById(result + 43, a2, a3, a4);
    if (result == 0) goto loc_00647AF4;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00647A67;
    v_stack_m68 = v_stack_p0;
    goto loc_00647A75;
loc_00647A67:
    if ((((unsigned __int8)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m68 = result;
    }
    v_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = a5;
    v_stack_m48 = (unsigned int)((unsigned int)(a2));
    v_stack_m50 = a3;
    v_stack_m58 = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9162293)) != 0) goto loc_00647AA9;
    if (((*(unsigned int *)(v_rip + 9162457)) & (0x800ULL)) == 0) goto loc_00647ABC;
loc_00647AA9:
    result = ExAcquireRundownProtection(v_rip + 9159632, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00647AF4;
loc_00647ABC:
    goto loc_00647ADE;
loc_00647AC5:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00647ADE:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00647AC5;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9159569;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m78 = a5;
    result = ZwQueryInformationTransactionManager(v_stack_p8, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_00647B7A;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9162135)) != 0) goto loc_00647B2F;
    if (((*(unsigned int *)(v_rip + 9162323)) & (0x800ULL)) == 0) goto loc_00647B42;
loc_00647B2F:
    result = ExAcquireRundownProtection(v_rip + 9159498, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00647B7A;
loc_00647B42:
    goto loc_00647B64;
loc_00647B4B:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m68;
        result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00647B64:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00647B4B;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9159435;
        result = ExReleaseRundownProtection(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryInformationTransactionManagerWrapper(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5)
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
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
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
    result = DifGetAPIThunkContextById(result + 43, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00647AF4;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00647A67;
    v_stack_m68 = v_stack_p0;
    goto loc_00647A75;
loc_00647A67:
    if ((((uint8_t)(v_stack_p0)) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m68 = result;
    }
    local_rsi = 0;
    v_stack_m40 = v_stack_p8;
    v_stack_m60 = Arg5;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg2));
    v_stack_m50 = Arg3;
    v_stack_m58 = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8BCE35)) != 0) goto loc_00647AA9;
    if (((*(uint32_t *)(v_rip + 0x8BCED9)) & (0x800ULL)) == 0) goto loc_00647ABC;
loc_00647AA9:
    result = ExAcquireRundownProtection(v_rip + 9159632, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00647AF4;
loc_00647ABC:
    goto loc_00647ADE;
loc_00647AC5:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00647ADE:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00647AC5;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9159569;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m78 = Arg5;
    result = ZwQueryInformationTransactionManager(v_stack_p8, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_00647B7A;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BCD97)) != 0) goto loc_00647B2F;
    if (((*(uint32_t *)(v_rip + 0x8BCE53)) & (0x800ULL)) == 0) goto loc_00647B42;
loc_00647B2F:
    result = ExAcquireRundownProtection(v_rip + 9159498, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00647B7A;
loc_00647B42:
    goto loc_00647B64;
loc_00647B4B:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m68;
        result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00647B64:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00647B4B;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9159435;
        result = ExReleaseRundownProtection(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00647A00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00647A00[BB_00647A00]
  bb_00647A55[BB_00647A55]
  bb_00647A5D[BB_00647A5D]
  bb_00647A67[BB_00647A67]
  bb_00647A6C[BB_00647A6C]
  bb_00647A75[BB_00647A75]
  bb_00647A9D[BB_00647A9D]
  bb_00647AA9[BB_00647AA9]
  bb_00647ABC[BB_00647ABC]
  bb_00647AC5[BB_00647AC5]
  bb_00647ACE[BB_00647ACE]
  bb_00647ADB[BB_00647ADB]
  bb_00647ADE[BB_00647ADE]
  bb_00647AE3[BB_00647AE3]
  bb_00647AE8[BB_00647AE8]
  bb_00647AF4[BB_00647AF4]
  bb_00647B17[BB_00647B17]
  bb_00647B23[BB_00647B23]
  bb_00647B2F[BB_00647B2F]
  bb_00647B42[BB_00647B42]
  bb_00647B4B[BB_00647B4B]
  bb_00647B54[BB_00647B54]
  bb_00647B61[BB_00647B61]
  bb_00647B64[BB_00647B64]
  bb_00647B69[BB_00647B69]
  bb_00647B6E[BB_00647B6E]
  bb_00647B7A[BB_00647B7A]
  bb_00647B9B[BB_00647B9B]
  bb_00647A00 -->|branch| bb_00647AF4
  bb_00647A00 -->|fallthrough| bb_00647A55
  bb_00647A55 -->|branch| bb_00647A67
  bb_00647A55 -->|fallthrough| bb_00647A5D
  bb_00647A5D -->|branch| bb_00647A75
  bb_00647A67 -->|branch| bb_00647A75
  bb_00647A67 -->|fallthrough| bb_00647A6C
  bb_00647A6C -->|flow| bb_00647A75
  bb_00647A75 -->|branch| bb_00647AA9
  bb_00647A75 -->|fallthrough| bb_00647A9D
  bb_00647A9D -->|branch| bb_00647ABC
  bb_00647A9D -->|fallthrough| bb_00647AA9
  bb_00647AA9 -->|branch| bb_00647AF4
  bb_00647AA9 -->|fallthrough| bb_00647ABC
  bb_00647ABC -->|branch| bb_00647ADE
  bb_00647AC5 -->|branch| bb_00647ADB
  bb_00647AC5 -->|fallthrough| bb_00647ACE
  bb_00647ACE -->|flow| bb_00647ADB
  bb_00647ADB -->|flow| bb_00647ADE
  bb_00647ADE -->|branch| bb_00647AC5
  bb_00647ADE -->|fallthrough| bb_00647AE3
  bb_00647AE3 -->|branch| bb_00647AF4
  bb_00647AE3 -->|fallthrough| bb_00647AE8
  bb_00647AE8 -->|flow| bb_00647AF4
  bb_00647AF4 -->|branch| bb_00647B7A
  bb_00647AF4 -->|fallthrough| bb_00647B17
  bb_00647B17 -->|branch| bb_00647B2F
  bb_00647B17 -->|fallthrough| bb_00647B23
  bb_00647B23 -->|branch| bb_00647B42
  bb_00647B23 -->|fallthrough| bb_00647B2F
  bb_00647B2F -->|branch| bb_00647B7A
  bb_00647B2F -->|fallthrough| bb_00647B42
  bb_00647B42 -->|branch| bb_00647B64
  bb_00647B4B -->|branch| bb_00647B61
  bb_00647B4B -->|fallthrough| bb_00647B54
  bb_00647B54 -->|flow| bb_00647B61
  bb_00647B61 -->|flow| bb_00647B64
  bb_00647B64 -->|branch| bb_00647B4B
  bb_00647B64 -->|fallthrough| bb_00647B69
  bb_00647B69 -->|branch| bb_00647B7A
  bb_00647B69 -->|fallthrough| bb_00647B6E
  bb_00647B6E -->|flow| bb_00647B7A
```
