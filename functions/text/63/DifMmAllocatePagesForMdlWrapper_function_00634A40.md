# DifMmAllocatePagesForMdlWrapper

- RVA: `0x00634A40`–`0x00634BC7` (길이 `391` bytes)
- VA: `0x0000000140634A40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2C68`
- 디코드: `112`개 명령, `391/391` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00634A80` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00634AA6` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00634AE2` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00634B08` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00634B21` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00634B33` → [MmAllocatePagesForMdl](../3E/MmAllocatePagesForMdl_function_003EA840.md) (function, `0x003EA840`)
- `0x00634B60` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00634B86` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00634B9F` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00634AB6` → RVA `0x00F048B8` (`.data`; read)
- `0x00634ACF` → RVA `0x00F04980` (`.data`; read)
- `0x00634ADB` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00634A40  48 8B C4                        mov rax, rsp
00634A43  48 89 58 08                     mov qword ptr [rax + 8], rbx
00634A47  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
00634A4B  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00634A4F  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
00634A53  55                              push rbp
00634A54  41 54                           push r12
00634A56  41 55                           push r13
00634A58  41 56                           push r14
00634A5A  41 57                           push r15
00634A5C  48 8B EC                        mov rbp, rsp
00634A5F  48 83 EC 50                     sub rsp, 0x50
00634A63  0F 57 C0                        xorps xmm0, xmm0
00634A66  48 8B F1                        mov rsi, rcx
00634A69  B9 E6 00 00 00                  mov ecx, 0xe6
00634A6E  49 8B D8                        mov rbx, r8
00634A71  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00634A75  48 8B FA                        mov rdi, rdx
00634A78  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00634A7C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00634A80  E8 AF 0F E6 FF                  call 0x140495a34
00634A85  4C 8B E8                        mov r13, rax
00634A88  48 85 C0                        test rax, rax
00634A8B  0F 84 95 00 00 00               je 0x140634b26
00634A91  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00634A94  A8 18                           test al, 0x18
00634A96  74 0A                           je 0x140634aa2
00634A98  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00634A9C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00634AA0  EB 0D                           jmp 0x140634aaf
00634AA2  A8 04                           test al, 4
00634AA4  74 09                           je 0x140634aaf
00634AA6  E8 5D F1 E9 FF                  call 0x1404d3c08
00634AAB  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00634AAF  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
00634AB3  45 32 E4                        xor r12b, r12b
00634AB6  44 38 25 FB FD 8C 00            cmp byte ptr [rip + 0x8cfdfb], r12b
00634ABD  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
00634AC1  48 89 7D E8                     mov qword ptr [rbp - 0x18], rdi
00634AC5  48 89 5D E0                     mov qword ptr [rbp - 0x20], rbx
00634AC9  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00634ACD  75 0C                           jne 0x140634adb
00634ACF  F7 05 A7 FE 8C 00 00 08 00 00   test dword ptr [rip + 0x8cfea7], 0x800
00634AD9  74 13                           je 0x140634aee
00634ADB  48 8D 0D 9E F3 8C 00            lea rcx, [rip + 0x8cf39e]
00634AE2  E8 39 1B BE FF                  call 0x140216620
00634AE7  44 8A E0                        mov r12b, al
00634AEA  84 C0                           test al, al
00634AEC  74 38                           je 0x140634b26
00634AEE  4D 8D 7D 20                     lea r15, [r13 + 0x20]
00634AF2  4D 8B 37                        mov r14, qword ptr [r15]
00634AF5  EB 19                           jmp 0x140634b10
00634AF7  49 8D 46 F0                     lea rax, [r14 - 0x10]
00634AFB  48 85 C0                        test rax, rax
00634AFE  74 0D                           je 0x140634b0d
00634B00  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00634B04  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00634B08  E8 C3 5F 08 00                  call 0x1406baad0
00634B0D  4D 8B 36                        mov r14, qword ptr [r14]
00634B10  4D 3B F7                        cmp r14, r15
00634B13  75 E2                           jne 0x140634af7
00634B15  45 84 E4                        test r12b, r12b
00634B18  74 0C                           je 0x140634b26
00634B1A  48 8D 0D 5F F3 8C 00            lea rcx, [rip + 0x8cf35f]
00634B21  E8 5A 53 D1 FF                  call 0x140349e80
00634B26  4C 8B 4D 48                     mov r9, qword ptr [rbp + 0x48]
00634B2A  4C 8B C3                        mov r8, rbx
00634B2D  48 8B D7                        mov rdx, rdi
00634B30  48 8B CE                        mov rcx, rsi
00634B33  E8 08 5D DB FF                  call 0x1403ea840
00634B38  48 89 45 F8                     mov qword ptr [rbp - 8], rax
00634B3C  4D 85 ED                        test r13, r13
00634B3F  74 63                           je 0x140634ba4
00634B41  40 32 FF                        xor dil, dil
00634B44  40 38 3D 6D FD 8C 00            cmp byte ptr [rip + 0x8cfd6d], dil
00634B4B  75 0C                           jne 0x140634b59
00634B4D  F7 05 29 FE 8C 00 00 08 00 00   test dword ptr [rip + 0x8cfe29], 0x800
00634B57  74 13                           je 0x140634b6c
00634B59  48 8D 0D 20 F3 8C 00            lea rcx, [rip + 0x8cf320]
00634B60  E8 BB 1A BE FF                  call 0x140216620
00634B65  40 8A F8                        mov dil, al
00634B68  84 C0                           test al, al
00634B6A  74 38                           je 0x140634ba4
00634B6C  49 8D 75 30                     lea rsi, [r13 + 0x30]
00634B70  48 8B 1E                        mov rbx, qword ptr [rsi]
00634B73  EB 19                           jmp 0x140634b8e
00634B75  48 8D 43 F0                     lea rax, [rbx - 0x10]
00634B79  48 85 C0                        test rax, rax
00634B7C  74 0D                           je 0x140634b8b
00634B7E  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00634B82  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00634B86  E8 45 5F 08 00                  call 0x1406baad0
00634B8B  48 8B 1B                        mov rbx, qword ptr [rbx]
00634B8E  48 3B DE                        cmp rbx, rsi
00634B91  75 E2                           jne 0x140634b75
00634B93  40 84 FF                        test dil, dil
00634B96  74 0C                           je 0x140634ba4
00634B98  48 8D 0D E1 F2 8C 00            lea rcx, [rip + 0x8cf2e1]
00634B9F  E8 DC 52 D1 FF                  call 0x140349e80
00634BA4  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00634BA8  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
00634BAD  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
00634BB1  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
00634BB5  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
00634BB9  49 8B E3                        mov rsp, r11
00634BBC  41 5F                           pop r15
00634BBE  41 5E                           pop r14
00634BC0  41 5D                           pop r13
00634BC2  41 5C                           pop r12
00634BC4  5D                              pop rbp
00634BC5  C3                              ret
00634BC6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifMmAllocatePagesForMdlWrapper(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(230, a2, a3, a4);
    if (result == 0) goto loc_00634B26;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00634AA2;
    v_stack_m58 = v_stack_p0;
    goto loc_00634AAF;
loc_00634AA2:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r12 = 0;
    v_stack_m38 = a1;
    v_stack_m40 = a2;
    v_stack_m48 = a3;
    v_stack_m50 = v_stack_p20;
    if ((*(unsigned __int8 *)(v_rip + 9240059)) != 0) goto loc_00634ADB;
    if (((*(unsigned int *)(v_rip + 9240231)) & (0x800ULL)) == 0) goto loc_00634AEE;
loc_00634ADB:
    result = ExAcquireRundownProtection(v_rip + 9237406, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00634B26;
loc_00634AEE:
    goto loc_00634B10;
loc_00634AF7:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00634B10:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00634AF7;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9237343;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = MmAllocatePagesForMdl(a1, a2, a3, v_stack_p20);
    v_stack_m30 = result;
    if (result == 0) goto loc_00634BA4;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9239917)) != 0) goto loc_00634B59;
    if (((*(unsigned int *)(v_rip + 9240105)) & (0x800ULL)) == 0) goto loc_00634B6C;
loc_00634B59:
    result = ExAcquireRundownProtection(v_rip + 9237280, a2, a3, v_stack_p20);
    if ((unsigned __int8)(result) == 0) goto loc_00634BA4;
loc_00634B6C:
    goto loc_00634B8E;
loc_00634B75:
    result = *(unsigned __int64 *)(result + 48) - 16;
    if (*(unsigned __int64 *)(result + 48) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, v_stack_p20);
    }
loc_00634B8E:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48))) != (result + 48)) goto loc_00634B75;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9237217;
        result = ExReleaseRundownProtection(a1, a2, a3, v_stack_p20);
    }
    return v_stack_m30;
}
```

## 5. (Beta) C Style

```c
int64_t DifMmAllocatePagesForMdlWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (80);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(230, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00634B26;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00634AA2;
    v_stack_m58 = v_stack_p0;
    goto loc_00634AAF;
loc_00634AA2:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r12 = 0;
    v_stack_m38 = Arg1;
    v_stack_m40 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m50 = v_stack_p20;
    if ((*(uint8_t *)(v_rip + 0x8CFDFB)) != 0) goto loc_00634ADB;
    if (((*(uint32_t *)(v_rip + 0x8CFEA7)) & (0x800ULL)) == 0) goto loc_00634AEE;
loc_00634ADB:
    result = ExAcquireRundownProtection(v_rip + 9237406, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00634B26;
loc_00634AEE:
    goto loc_00634B10;
loc_00634AF7:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00634B10:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00634AF7;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9237343;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    result = MmAllocatePagesForMdl(Arg1, Arg2, Arg3, v_stack_p20);
    v_stack_m30 = result;
    if (result == 0) goto loc_00634BA4;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8CFD6D)) != 0) goto loc_00634B59;
    if (((*(uint32_t *)(v_rip + 0x8CFE29)) & (0x800ULL)) == 0) goto loc_00634B6C;
loc_00634B59:
    result = ExAcquireRundownProtection(v_rip + 9237280, Arg2, Arg3, v_stack_p20);
    if ((uint8_t)(result) == 0) goto loc_00634BA4;
loc_00634B6C:
    goto loc_00634B8E;
loc_00634B75:
    result = *(uint64_t *)(result + 0x30) - 16;
    if (*(uint64_t *)(result + 0x30) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x30) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, v_stack_p20);
    }
loc_00634B8E:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x30))) != (result + 48)) goto loc_00634B75;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9237217;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, v_stack_p20);
    }
    return v_stack_m30;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00634A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00634A40[BB_00634A40]
  bb_00634A91[BB_00634A91]
  bb_00634A98[BB_00634A98]
  bb_00634AA2[BB_00634AA2]
  bb_00634AA6[BB_00634AA6]
  bb_00634AAF[BB_00634AAF]
  bb_00634ACF[BB_00634ACF]
  bb_00634ADB[BB_00634ADB]
  bb_00634AEE[BB_00634AEE]
  bb_00634AF7[BB_00634AF7]
  bb_00634B00[BB_00634B00]
  bb_00634B0D[BB_00634B0D]
  bb_00634B10[BB_00634B10]
  bb_00634B15[BB_00634B15]
  bb_00634B1A[BB_00634B1A]
  bb_00634B26[BB_00634B26]
  bb_00634B41[BB_00634B41]
  bb_00634B4D[BB_00634B4D]
  bb_00634B59[BB_00634B59]
  bb_00634B6C[BB_00634B6C]
  bb_00634B75[BB_00634B75]
  bb_00634B7E[BB_00634B7E]
  bb_00634B8B[BB_00634B8B]
  bb_00634B8E[BB_00634B8E]
  bb_00634B93[BB_00634B93]
  bb_00634B98[BB_00634B98]
  bb_00634BA4[BB_00634BA4]
  bb_00634BC6[BB_00634BC6]
  bb_00634A40 -->|branch| bb_00634B26
  bb_00634A40 -->|fallthrough| bb_00634A91
  bb_00634A91 -->|branch| bb_00634AA2
  bb_00634A91 -->|fallthrough| bb_00634A98
  bb_00634A98 -->|branch| bb_00634AAF
  bb_00634AA2 -->|branch| bb_00634AAF
  bb_00634AA2 -->|fallthrough| bb_00634AA6
  bb_00634AA6 -->|flow| bb_00634AAF
  bb_00634AAF -->|branch| bb_00634ADB
  bb_00634AAF -->|fallthrough| bb_00634ACF
  bb_00634ACF -->|branch| bb_00634AEE
  bb_00634ACF -->|fallthrough| bb_00634ADB
  bb_00634ADB -->|branch| bb_00634B26
  bb_00634ADB -->|fallthrough| bb_00634AEE
  bb_00634AEE -->|branch| bb_00634B10
  bb_00634AF7 -->|branch| bb_00634B0D
  bb_00634AF7 -->|fallthrough| bb_00634B00
  bb_00634B00 -->|flow| bb_00634B0D
  bb_00634B0D -->|flow| bb_00634B10
  bb_00634B10 -->|branch| bb_00634AF7
  bb_00634B10 -->|fallthrough| bb_00634B15
  bb_00634B15 -->|branch| bb_00634B26
  bb_00634B15 -->|fallthrough| bb_00634B1A
  bb_00634B1A -->|flow| bb_00634B26
  bb_00634B26 -->|branch| bb_00634BA4
  bb_00634B26 -->|fallthrough| bb_00634B41
  bb_00634B41 -->|branch| bb_00634B59
  bb_00634B41 -->|fallthrough| bb_00634B4D
  bb_00634B4D -->|branch| bb_00634B6C
  bb_00634B4D -->|fallthrough| bb_00634B59
  bb_00634B59 -->|branch| bb_00634BA4
  bb_00634B59 -->|fallthrough| bb_00634B6C
  bb_00634B6C -->|branch| bb_00634B8E
  bb_00634B75 -->|branch| bb_00634B8B
  bb_00634B75 -->|fallthrough| bb_00634B7E
  bb_00634B7E -->|flow| bb_00634B8B
  bb_00634B8B -->|flow| bb_00634B8E
  bb_00634B8E -->|branch| bb_00634B75
  bb_00634B8E -->|fallthrough| bb_00634B93
  bb_00634B93 -->|branch| bb_00634BA4
  bb_00634B93 -->|fallthrough| bb_00634B98
  bb_00634B98 -->|flow| bb_00634BA4
```
