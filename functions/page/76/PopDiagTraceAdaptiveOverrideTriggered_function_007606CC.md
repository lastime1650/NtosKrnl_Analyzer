# PopDiagTraceAdaptiveOverrideTriggered

- RVA: `0x007606CC`–`0x007607FD` (길이 `305` bytes)
- VA: `0x00000001407606CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCC84`
- 디코드: `69`개 명령, `305/305` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0076070C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x007607E2` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x007607EE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopAdaptiveConsoleSessionOverrideTrigger](PopAdaptiveConsoleSessionOverrideTrigger_function_0076B664.md) at `0x0076B68A`

### Static image references
- `0x007606DA` → RVA `0x00E0A740` (`.data`; read)
- `0x007606E8` → RVA `0x00E07748` (`.data`; read)
- `0x007607BD` → RVA `0x0004B4FC` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0076070C` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x007607E2` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x007607EE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007606CC  40 55                           push rbp
007606CE  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
007606D3  48 81 EC F0 00 00 00            sub rsp, 0xf0
007606DA  48 8B 05 5F A0 6A 00            mov rax, qword ptr [rip + 0x6aa05f]
007606E1  48 33 C4                        xor rax, rsp
007606E4  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
007606E8  83 3D 59 70 6A 00 05            cmp dword ptr [rip + 0x6a7059], 5
007606EF  44 8B D2                        mov r10d, edx
007606F2  4C 8B D9                        mov r11, rcx
007606F5  0F 86 EC 00 00 00               jbe 0x1407607e7
007606FB  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00760705  48 8D 0D 3C 70 6A 00            lea rcx, [rip + 0x6a703c]
0076070C  E8 8F E3 CC FF                  call 0x14042eaa0
00760711  84 C0                           test al, al
00760713  0F 84 CE 00 00 00               je 0x1407607e7
00760719  83 65 F3 00                     and dword ptr [rbp - 0xd], 0
0076071D  48 8D 45 A7                     lea rax, [rbp - 0x59]
00760721  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
00760725  48 B8 04 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000004
0076072F  4C 89 5D A7                     mov qword ptr [rbp - 0x59], r11
00760733  41 BB 08 00 00 00               mov r11d, 8
00760739  44 89 5D EF                     mov dword ptr [rbp - 0x11], r11d
0076073D  8B 08                           mov ecx, dword ptr [rax]
0076073F  48 B8 20 03 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000320
00760749  48 C1 E1 20                     shl rcx, 0x20
0076074D  48 8B 00                        mov rax, qword ptr [rax]
00760750  83 65 03 00                     and dword ptr [rbp + 3], 0
00760754  83 65 13 00                     and dword ptr [rbp + 0x13], 0
00760758  83 65 23 00                     and dword ptr [rbp + 0x23], 0
0076075C  83 65 33 00                     and dword ptr [rbp + 0x33], 0
00760760  83 65 43 00                     and dword ptr [rbp + 0x43], 0
00760764  48 C1 E0 08                     shl rax, 8
00760768  48 F7 E1                        mul rcx
0076076B  48 8D 45 AF                     lea rax, [rbp - 0x51]
0076076F  44 89 45 9B                     mov dword ptr [rbp - 0x65], r8d
00760773  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00760777  48 8D 0D CA 6F 6A 00            lea rcx, [rip + 0x6a6fca]
0076077E  48 89 55 AF                     mov qword ptr [rbp - 0x51], rdx
00760782  48 8D 45 97                     lea rax, [rbp - 0x69]
00760786  48 89 45 07                     mov qword ptr [rbp + 7], rax
0076078A  41 8D 53 FC                     lea edx, [r11 - 4]
0076078E  48 8D 45 9B                     lea rax, [rbp - 0x65]
00760792  89 55 0F                        mov dword ptr [rbp + 0xf], edx
00760795  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00760799  45 33 C0                        xor r8d, r8d
0076079C  48 8D 45 9F                     lea rax, [rbp - 0x61]
007607A0  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
007607A3  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007607A7  48 8D 45 B7                     lea rax, [rbp - 0x49]
007607AB  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
007607AF  48 8D 45 C7                     lea rax, [rbp - 0x39]
007607B3  44 89 4D 9F                     mov dword ptr [rbp - 0x61], r9d
007607B7  45 33 C9                        xor r9d, r9d
007607BA  89 55 2F                        mov dword ptr [rbp + 0x2f], edx
007607BD  48 8D 15 38 AD 8E FF            lea rdx, [rip - 0x7152c8]
007607C4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007607C9  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
007607CE  44 89 5D FF                     mov dword ptr [rbp - 1], r11d
007607D2  44 89 55 97                     mov dword ptr [rbp - 0x69], r10d
007607D6  48 C7 45 B7 00 00 00 01         mov qword ptr [rbp - 0x49], 0x1000000
007607DE  44 89 5D 3F                     mov dword ptr [rbp + 0x3f], r11d
007607E2  E8 F9 58 CC FF                  call 0x1404260e0
007607E7  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
007607EB  48 33 CC                        xor rcx, rsp
007607EE  E8 4D BE F4 FF                  call 0x1406ac640
007607F3  48 81 C4 F0 00 00 00            add rsp, 0xf0
007607FA  5D                              pop rbp
007607FB  C3                              ret
007607FC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceAdaptiveOverrideTriggered(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD8;

    v_rsp = (v_rsp) - (240);
    result = (*(unsigned __int64 *)(v_rip + 6987871)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned int *)(v_rip + 6975577)) <= 5) goto loc_007607E7;
    result = tlgKeywordOn(v_rip + 6975548, a2, a3, a4);
    v_r11 = a1;
    if ((unsigned __int8)(result) != 0) {
        result = v_stack_mB8;
        v_stack_m78 = result;
        v_stack_mB8 = a1;
        v_r11 = 8;
        v_stack_m70 = (unsigned int)(v_r11);
        a1 = *(unsigned int *)(result);
        a1 = (a1) << (32);
        result = *(unsigned __int64 *)(result);
        result = (result) << (8);
        result = v_stack_mB0;
        v_stack_mC4 = a3;
        v_stack_m68 = result;
        a1 = v_rip + 6975434;
        v_stack_mB0 = a2;
        result = v_stack_mC8;
        v_stack_m58 = result;
        a2 = v_r11 - 4;
        result = v_stack_mC4;
        v_stack_m50 = a2;
        v_stack_m48 = result;
        a3 = 0;
        result = v_stack_mC0;
        v_stack_m40 = a2;
        v_stack_m38 = result;
        result = v_stack_mA8;
        v_stack_m28 = result;
        result = v_stack_m98;
        v_stack_mC0 = a4;
        a4 = 0;
        v_stack_m30 = a2;
        a2 = v_rip - 7426760;
        v_stack_mD0 = result;
        v_stack_mD8 = (unsigned int)(v_r11);
        v_stack_m60 = (unsigned int)(v_r11);
        v_stack_mC8 = (unsigned int)((unsigned int)(a2));
        v_stack_mA8 = 0x1000000ULL;
        v_stack_m20 = (unsigned int)(v_r11);
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (240);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceAdaptiveOverrideTriggered(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD8;

    local_rsp = (local_rsp) - (240);
    result = (*(uint64_t *)(v_rip + 0x6AA05F)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint32_t *)(v_rip + 0x6A7059)) <= 5) goto loc_007607E7;
    result = tlgKeywordOn(v_rip + 6975548, Arg2, Arg3, Arg4);
    local_r11 = Arg1;
    if ((uint8_t)(result) != 0) {
        result = v_stack_mB8;
        v_stack_m78 = result;
        v_stack_mB8 = Arg1;
        local_r11 = 8;
        v_stack_m70 = (uint32_t)(local_r11);
        Arg1 = *(uint32_t *)(result);
        Arg1 = (Arg1) << (32);
        result = *(uint64_t *)(result);
        result = (result) << (8);
        result = v_stack_mB0;
        v_stack_mC4 = Arg3;
        v_stack_m68 = result;
        Arg1 = v_rip + 6975434;
        v_stack_mB0 = Arg2;
        result = v_stack_mC8;
        v_stack_m58 = result;
        Arg2 = local_r11 - 4;
        result = v_stack_mC4;
        v_stack_m50 = Arg2;
        v_stack_m48 = result;
        Arg3 = 0;
        result = v_stack_mC0;
        v_stack_m40 = Arg2;
        v_stack_m38 = result;
        result = v_stack_mA8;
        v_stack_m28 = result;
        result = v_stack_m98;
        v_stack_mC0 = Arg4;
        Arg4 = 0;
        v_stack_m30 = Arg2;
        Arg2 = v_rip - 7426760;
        v_stack_mD0 = result;
        v_stack_mD8 = (uint32_t)(local_r11);
        v_stack_m60 = (uint32_t)(local_r11);
        v_stack_mC8 = (uint32_t)((uint32_t)(Arg2));
        v_stack_mA8 = 0x1000000ULL;
        v_stack_m20 = (uint32_t)(local_r11);
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (240);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007606CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007606CC[BB_007606CC]
  bb_007606FB[BB_007606FB]
  bb_00760719[BB_00760719]
  bb_007607E7[BB_007607E7]
  bb_007607FC[BB_007607FC]
  bb_007606CC -->|branch| bb_007607E7
  bb_007606CC -->|fallthrough| bb_007606FB
  bb_007606FB -->|branch| bb_007607E7
  bb_007606FB -->|fallthrough| bb_00760719
  bb_00760719 -->|flow| bb_007607E7
```
